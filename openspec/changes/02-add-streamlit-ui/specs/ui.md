# Spec: Streamlit UI

## ADDED Requirements

### UI-001: Location Selection
The user interface MUST provide a dropdown menu to select a specific location or "All Locations".

#### Scenario: Filter by Location
Given the user selects "Taipei" from the dropdown
When the data is displayed
Then only records where `location` is "Taipei" should be shown

### UI-002: Data Visualization
The system MUST display weather forecast data (Date, Weather, Temp) in a tabular format.

#### Scenario: View Data
Given the database has weather records
When the app loads
Then a table containing the forecast data should be visible

### UI-003: Data Refresh
The user interface SHOULD provide a mechanism to trigger a new data fetch from the API.

#### Scenario: Refresh Data
Given the user clicks "Update Data"
Then the system should fetch the latest data from the CWA API
And update the database
And refresh the displayed table
