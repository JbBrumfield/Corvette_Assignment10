# File Name : main.py
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

from censusAPIPackage.census_api import CensusAPI

def main():
    # Define the URL for the API request
    url = "https://api.census.gov/data/2021/pep/population?get=DENSITY_2021,POP_2021,NAME,STATE&for=region:*"
    
    # Instantiate the CensusAPI class
    api = CensusAPI(url)

    # Fetch the data from the API
    data = api.fetch_data()

    if data:
        # Save the fetched data to a CSV file
        api.save_to_csv(data, "population_data.csv")

    insights = api.get_population_insights(data)

        # Check if error occurred
    if "error" in insights:
            print(insights["error"])
    else:
            print("\n--- California County Population Statistics ---")
            print(f"Total counties: {insights['total_counties']}")
            print(f"Total population: {insights['total_population']:,}")
            print(f"Average population: {insights['average_population']:,}")

            most = insights['most_populous']
            least = insights['least_populous']
            print(f"Most populous county: {most[0]} ({most[1]:,})")
            print(f"Least populous county: {least[0]} ({least[1]:,})")

            print("\nTop 5 Most Populous Counties:")
            for i, (name, pop) in enumerate(insights['top_5'], start=1):
                print(f"{i}. {name}: {pop:,}")


if __name__ == "__main__":
    main()
