

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
        def get_population_insights(self, data):
             """
            Analyzes the population data and returns insights.
            Returns a dictionary containing:
            - total_counties
            - total_population
            - average_population
            - most_populous
            - least_populous
            - top_5
            """
        if not data or len(data) < 2:
            return {"error": "No data available for analysis."}
 
        header = data[0]
        try:
            name_index = header.index("NAME")
            pop_index = header.index("POP_2021")
        except ValueError:
            return {"error": "Expected columns 'NAME' and 'POP' not found in data."}
 
        counties = []
        total_population = 0

        for row in data[1:]:
            try:
                name = row[name_index]
                population = int(row[pop_index])
                counties.append((name, population))
                total_population += population
            except (ValueError, IndexError):
                continue  # Skip rows with invalid data
 
        if not counties:
            return {"error": "No valid population data found."}
 
        counties.sort(key=lambda x: x[1], reverse=True)
        average_population = total_population // len(counties)
 
        return {
            "total_counties": len(counties),
            "total_population": total_population,
            "average_population": average_population,
            "most_populous": counties[0],
            "least_populous": counties[-1],
            "top_5": counties[:5]
        }