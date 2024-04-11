import requests

def post_campaigns(
    adAccount_id,
    access_token,
    granularity,
    breakdown,
    report_dimension,
    fields,
    test=True,
):
    url = "https://adsapi.snapchat.com/v1/adaccounts/{}/campaigns".format(adAccount_id)
    params = {
        "granularity": granularity,
        "breakdown": breakdown,
        "report_dimension": report_dimension,
        "fields": fields,
        "limit": 100,
        "test": test,
    }
    headers = {"Authorization": f"Bearer {access_token}"}
    # response = requests.request("GET", url, headers=headers, params=params)
    response = requests.get(url, headers=headers, params=params)
    return response


def get_campaigns(adAccount_id, access_token):
    response = post_campaigns(
        adAccount_id=adAccount_id,
        access_token=access_token,
        granularity="TOTAL",
        breakdown="campaign",
        report_dimension=["country,os"],
        fields=[
            """impressions,spend,swipes,video_views,
               paid_impressions,conversion_ad_click
            """
        ],
    )

    return response.json()


def get_adsquads(
    adAccount_id,
    access_token,
):
    url = "https://adsapi.snapchat.com/v1/adaccounts/{}/adsquads".format(adAccount_id)
    params = {
        "return_placement_v2": True,
        "read_deleted_entities": True
    }
    headers = {"Authorization": f"Bearer {access_token}"}
    # response = requests.request("GET", url, headers=headers, params=params)
    response = requests.get(url, headers=headers, params=params)
    return response.json()