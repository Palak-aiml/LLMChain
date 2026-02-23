"""
llmchain/integrations/requests_tool.py

Integration for external API calls using requests.
"""
import requests

class RequestsTool:
    def get(self, url, params=None):
        response = requests.get(url, params=params)
        return response.json()

    def post(self, url, data=None, json=None):
        response = requests.post(url, data=data, json=json)
        return response.json()
