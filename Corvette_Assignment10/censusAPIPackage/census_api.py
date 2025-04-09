

import requests
import csv
 
class CensusAPI:
    def __init__(self, url):
        """
        Intializes the code
        """
        self.url = url
 
    def fetch_data(self):
        """
        Fetches data from the API
        Returns JSON file
        """
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise exception for HTTP errors
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return None
