# AIoT Weather Crawler & Dashboard ??

This project is a weather data crawler and visualization dashboard for Taiwan, built as part of the AIoT course. It fetches weather forecast data from the Taiwan Central Weather Administration (CWA) Open Data API and presents it in an interactive Streamlit web application.

## Features

- **Data Crawler**: Fetches the latest weather forecast for various locations in Taiwan.
- **Database**: Stores weather data locally using SQLite (`sqlitedata.db`).
- **Interactive Dashboard**: Built with Streamlit for easy data exploration.
- **Visualizations**:
    - Temperature trends (Min/Max) using Plotly.
    - Key metrics (Avg Temp, Total Locations).
    - Detailed data tables.
- **Data Management**: "Refresh Data" button to trigger the crawler directly from the UI.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Joxanne/AIoT_Weather_Crawler.git
   cd AIoT_Weather_Crawler
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

2. **Initialize Data**:
   - When you first open the app, the database might be empty.
   - Click the **"? Refresh Data"** button in the sidebar to fetch the latest weather data from the CWA API.

## Project Structure

- `app.py`: The main Streamlit application file containing the UI logic and visualizations.
- `weather_crawler.py`: Contains the logic for fetching data from the API and interacting with the SQLite database.
- `requirements.txt`: List of Python dependencies.
- `sqlitedata.db`: SQLite database file (generated automatically).

## Data Source

- [Taiwan Central Weather Administration (CWA) Open Data Platform](https://opendata.cwa.gov.tw/)
