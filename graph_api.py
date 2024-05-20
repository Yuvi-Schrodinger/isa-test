import pandas as pd
import plotly.express as px
import requests
import streamlit as st
import json
import plotly.express as px
#tentar criar classe da api por aqui mesmo

class GraphAPI:
    def __init__(self, ad_acc, fb_api):
        self.base_url = "https://graph.facebook.com/v19.0/"
        self.api_fields = ["spend", "cpc", "cpm", "objective", "adset_name", 
                "adset_id", "clicks", "campaign_name", "campaign_id", 
                "conversions", "frequency", "conversion_values", "ad_name", "ad_id"]
        self.token = "&access_token=" + fb_api
        self.ad_acc = ad_acc

    def get_insights(self, ad_acc, level="campaign"):
        url = self.base_url + "act_" + str(ad_acc)
        url += "/insights?level=" + level
        url += "&fields=" + ",".join(self.api_fields)

        data = requests.get(url + self.token)
        data = json.loads(data._content.decode("utf-8"))
        for i in data["data"]:
            if "conversions" in i:
                i["conversion"] = float(i["conversions"][0]["value"])
        return data

# act_3120164588217844/insights?level=adset&fields=spend,cpc,cpm,objective,adset_name,adset_id,clicks,campaign_name,campaign_id,conversions,frequency,conversion_values,ad_name,ad_id,ad_impression_actions

    def get_campaigns_status(self, ad_acc):
        url = self.base_url + "act_" + str(ad_acc)
        url += "/campaigns?fields=name,status,adsets{name, id}"
        data = requests.get(url + self.token)
        return json.loads(data._content.decode("utf-8"))

    def get_adset_status(self, ad_acc):
        url = self.base_url + "act_" + str(ad_acc)
        url += "/adsets?fields=name,status,id"
        data = requests.get(url + self.token)
        return json.loads(data._content.decode("utf-8"))

    def get_data_over_time(self, campaign):
        url = self.base_url + str(campaign)
        url += "/insights?fields="+ ",".join(self.api_fields)
        url += "&date_preset=last_30d&time_increment=1"

        data = requests.get(url + self.token)
        data = json.loads(data._content.decode("utf-8"))
        for i in data["data"]:
            if "conversions" in i:
                i["conversion"] = float(i["conversions"][0]["value"])
        return data


# act_3120164588217844/campaigns?fields=name,status, adsets
if __name__ == "__main__":
    fb_api = open("tokens/token").read()
    ad_acc = "956757482423549"

    self = GraphAPI(ad_acc, fb_api)

    self.get_insights(ad_acc)
    self.get_campaigns_status(ad_acc)["data"]

    self.get_data_over_time(120208363974670077)
    self.get_data_over_time(120208363974670077)

