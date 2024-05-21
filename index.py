import pandas as pd
import plotly.express as px
import requests
import streamlit as st
import json

import requests

class GraphAPI:
    def __init__(self, ad_acc, fb_api):
        self.base_url = "https://graph.facebook.com/v19.0/"
        self.api_fields = [
            "spend", "cpc", "cpm", "objective", "adset_name", 
            "adset_id", "clicks", "campaign_name", "campaign_id", 
            "conversions", "frequency", "conversion_values", "ad_name", "ad_id"
        ]
        self.token = fb_api
        self.ad_acc = ad_acc

    def make_request(self, endpoint, params=None):
        url = self.base_url + endpoint
        if params is None:
            params = {}
        params["access_token"] = self.token

        response = requests.get(url, params=params)
        try:
            response.raise_for_status()
            return response.json()
        except requests.HTTPError as e:
            print(f"Error fetching data: {e}")
            return None

    def get_insights(self, level="campaign"):
        endpoint = f"act_{self.ad_acc}/insights"
        params = {
            "fields": ",".join(self.api_fields),
            "level": level
        }
        return self.make_request(endpoint, params)

    def get_campaigns_status(self):
        endpoint = f"act_{self.ad_acc}/campaigns"
        params = {
            "fields": "name,status,id"
        }
        return self.make_request(endpoint, params)

    def get_adset_status(self):
        endpoint = f"act_{self.ad_acc}/adsets"
        params = {
            "fields": "name,status,id"
        }
        return self.make_request(endpoint, params)

    def get_data_over_time(self, campaign_id):
        endpoint = f"{campaign_id}/insights"
        params = {
            "fields": ",".join(self.api_fields),
            "date_preset": "last_30d",
            "time_increment": "1"
        }
        return self.make_request(endpoint, params)



if __name__ == "__main__":
    fb_api = open("tokens/token").read()
    ad_acc = "956757482423549"

    fb_graph_api = GraphAPI(ad_acc, fb_api)

    st.title("Dashboard da Isa")

    st.header("Campaign status")
    campaign_status = fb_graph_api.get_campaigns_status()
    st.write(campaign_status)

    st.header("Adset Status")
    adset_status = fb_graph_api.get_adset_status()
    st.write(adset_status)

    st.header("Insights")
    insights = fb_graph_api.get_insights()
    st.write(insights)

    st.header("Data Over Time for Campaign")
    campaign_id = 120208363974670077
    data_over_time = fb_graph_api.get_data_over_time(campaign_id)
    st.write(data_over_time)
