
# File Name : census_api.py
# Student Name: Jacob Brumfield, Sharvari Patil, Rithu Aynampudi, Saivamsi Amireddy
# email:  brumfijb@mail.uc.edu, patilsg@mail.uc.edu, aynampru@mail.uc.edu, amiredsr@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date:   4/10/2025
# Course #/Section:   IS 4010 001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  Integrates an API that has data on the population of cities around the United States. Then it prints interesting information from this API.

# Brief Description of what this module does: This module prints the interesting information from the API and CSV file.
# Citations: https://realpython.com/, https://www.w3schools.com/python/, https://pythongeeks.org/

# Anything else that's relevant:

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
        def save_to_csv(self, data, filename):
        """
        Saves the fetched data to a CSV file
        Returns CSV file
        """

        if data is None:
            print("No data to write to CSV.")
            return
        try:
            with open(filename, mode="w", newline='') as file:
                writer = csv.writer(file)
                writer.writerow(data[0])  # Write header
                for row in data[1:]:
                    writer.writerow(row)  # Write data rows
            print(f"Data has been successfully saved to {filename}.")
        except Exception as e:
            print(f"Error saving data to CSV: {e}")
 
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