import requests
import json

class GraphAPI:
    def __init__(self, ad_acc, fb_api):
        self.base_url = "https://graph.facebook.com/v20.0/"
        self.api_fields = ["spend","cpc","cpm","objective","adset_name","adset_id","clicks","campaign_name","campaign_id","frequency"]
        self.token = "&access_token=" + fb_api

    def get_insights(self, ad_acc, level="adset"):
        url = self.base_url + "act_" + str(ad_acc)
        url += "/insights?level=" + level
        url += "&fields=" + ",".join(self.api_fields)

        data = requests.get(url + self.token)
        data = json.loads(data._content.decode("utf-8"))
        return data

# act_956757482423549/insights?level=adset&fields=spend,cpc,cpm,objective,adset_name,adset_id,clicks,campaign_name,campaign_id,conversions,frequency,conversion_values,ad_name,ad_id,ad_impression_actions

    def get_campaigns_status(self, ad_acc):
        url = self.base_url + "act_" + str(ad_acc)
        url += "/campaigns?fields=name,status{name, id}"
        data = requests.get(url + self.token)
        return json.loads(data._content.decode("utf-8"))

    def get_adset_status(self, ad_acc):
        url = self.base_url + "act_" + str(ad_acc)
        url += "/adsets?fields=name,status,id"
        data = requests.get(url + self.token)
        return json.loads(data._content.decode("utf-8"))

if __name__ == "__main__":
    fb_api = open("tokens/token").read()
    ad_acc = "956757482423549"

    self = GraphAPI(ad_acc, fb_api)

    self.get_insights(ad_acc)
    self.get_campaigns_status(ad_acc)

