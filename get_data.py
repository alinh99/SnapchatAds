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


access_token = "eyJpc3MiOiJodHRwczpcL1wvYWNjb3VudHMuc25hcGNoYXQuY29tXC9hY2NvdW50c1wvb2F1dGgyXC90b2tlbiIsInR5cCI6IkpXVCIsImVuYyI6IkExMjhDQkMtSFMyNTYiLCJhbGciOiJkaXIiLCJraWQiOiJhY2Nlc3MtdG9rZW4tYTEyOGNiYy1oczI1Ni4wIn0..Cl45CiFNrCeDR3ZGqCNCLQ.FHkD060LqD-eFIDKO0-LEe9ZCGt6lnahBpi3pf9Jx1w_KELctmIwgGJYQbyuZlju7cF2vblZy4Ss6mram-1JdR_JuFCn0ZSWjLUPmAwymq5JQ8EsbCI27qBcJyv35Q1uqwnVyZTripNOx1ZaeNeqPVLNL9UCyFwHtn8ulFBDHS_KbVpHG4mcNkwb-8hNxB5LHIYADtg_FqfJryU--s96NhsR5rZoF555h8OfXDKnGXcSaVDXord_S5HpD1LRiE3UQ36Bi_fMKglc3LDzcz6tdV6oU-W8j_V60FgxHPCf_-jKQ8oVNezIsEq4sqhIqeSYXVtNMrsjNoO8QQ-avVJPkAOtAOttrq-l5Ye7wPFxwYVesT73dzin4qdl9sArjBqL5ynpAJAl0IOAznAviKQaS-CaCtxYmbbOYefrqyE4V49HItThHrKpuapSIU9Kelw1eYh2UQeBgAL_3j8JGyJ2vOjo6XD87K1xQZxBTFUe7P8RLJEdsAcpUa60JTnwo_6ouLiIdKco1hNkpVBgqhNyKdveaMPeLW4Vy5YjBsq_r2EhW3bi4OvxNx4mGXfbzdnBKAzYxJTz-Wc8wR3YWnaPaIB9vLDZ7ccknRHalxMfhqVf5DlWWdYH6i6aY0SuZKqgQC8SNX4-4gpSx7aBb3ZqsqBXXTh6dkeJlnSG6pnStVweGrQWPifevCzrVtLK13IVdKBMupqm6yXpxF5Hr0xNkn8mjytJliqB2s8dgJtznyc.56OoXDMZI_3_mi1twcZuLA"
adAccount_id = "c4d11bf0-981f-4365-a07b-90bc3c9c900e"

# adsquad_metrics = get_adsquads(adAccount_id, access_token)
# adsquads = adsquad_metrics["adsquads"]

# campaign_metrics = get_campaigns(adAccount_id, access_token)
# campaigns = campaign_metrics["campaigns"]

# data = []
# for cam in campaigns:
#     campaign_id = cam["campaign"]["id"]
#     campaign_name = cam["campaign"]["name"]
#     time = cam["campaign"]["start_time"]
#     matching_adsquads = [
#         adsquad
#         for adsquad in adsquads
#         if adsquad["adsquad"]["campaign_id"] == campaign_id
#     ]
#     for adsquad in matching_adsquads:
#         adsquad_name = adsquad["adsquad"]["name"]
#         if not "total_stats" in cam:
#             cam["total_stats"] = [
#                 {
#                     "total_stat": {
#                         "stats": {
#                             "impressions": 0,
#                             "swipes": 0,
#                             "spend": 0,
#                             "paid_impressions": 0,
#                             "video_views": 0,
#                             "conversion_ad_click": 0,
#                             "conversion_rate": 0,
#                         }
#                     }
#                 }
#             ]
#         total_stat = cam["total_stats"][0]["total_stat"]["stats"]

#         # Append data to list
#         data.append(
#             {
#                 "Campaign ID": campaign_id,
#                 "Campaign Name": campaign_name,
#                 "Date": time,
#                 "Impressions": total_stat["impressions"],
#                 "Swipes": total_stat["swipes"],
#                 "Amount Spent": total_stat["spend"],
#                 "Paid Impressions": total_stat["paid_impressions"],
#                 "Click Rate": total_stat["conversion_rate"],
#                 "Adset Name": adsquad_name,
#             }
#         )

