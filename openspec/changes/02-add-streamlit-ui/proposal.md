# Change Proposal: Add Streamlit Web Interface

## Summary
Develop a Streamlit web application (`app.py`) to visualize the weather forecast data stored in the SQLite database. The app will feature a dropdown menu for location selection and display the relevant weather information in a table.

## Motivation
The current CLI output is functional but not user-friendly for browsing data. A web interface allows for better visualization, filtering, and interaction with the weather data.

## Proposed Changes
- Create `app.py` using the Streamlit library.
- Connect `app.py` to `sqlitedata.db` to read weather records.
- Implement a "Refresh Data" button in the UI to trigger the crawler (reusing logic from `weather_crawler.py`).
- Add a sidebar or main area dropdown to filter by "Location".
- Display the data in an interactive dataframe.
