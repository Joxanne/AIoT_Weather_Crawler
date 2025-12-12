# Project Context

## Purpose
This project is a weather data crawler designed to fetch forecast data from the Taiwan Central Weather Administration (CWA) Open Data API. It extracts key weather metrics (temperature, weather description) for various locations, stores them in a local SQLite database for historical tracking, and displays the forecast in a readable table format.

## Tech Stack
- **Language:** Python 3.x
- **Libraries:**
  - `requests`: For making HTTP requests to the CWA API.
  - `pandas`: For data manipulation and tabular display.
  - `sqlite3`: For local data persistence.
  - `json`: For parsing API responses.

## Project Conventions

### Code Style
- Follow PEP 8 guidelines for Python code.
- Use 4 spaces for indentation.
- Ensure source files are UTF-8 encoded (`# -*- coding: utf-8 -*-`).
- Use descriptive variable and function names.

### Architecture Patterns
- **Script-based:** Currently a single script (`weather_crawler.py`) handling fetching, processing, storage, and display.
- **ETL Flow:** Extract (API), Transform (Parse & Clean), Load (SQLite & Display).

### Testing Strategy
- Manual testing by running the script and verifying output.
- Future: Unit tests for data parsing logic.

### Git Workflow
- Direct commits to main for now.
- Feature branches for major changes.

### OpenSpec Conventions
- **Change Naming:** All change proposals in `openspec/changes/` must be prefixed with a 2-digit incrementing number starting from 01 (e.g., `01-add-cli-support`, `02-add-streamlit-ui`). Check existing folders to determine the next number.

## Domain Context
- **Source:** Taiwan CWA Open Data API (Dataset ID: F-A0010-001).
- **Data Points:**
  - Location Name
  - Date
  - Weather Description (Wx)
  - Min/Max Temperature (MinT, MaxT)
  - (Rain Probability was removed in previous iterations).

## Important Constraints
- API requires an Authorization key.
- Data structure is deeply nested JSON.
- Encoding handling is critical for Traditional Chinese characters.

## External Dependencies
- CWA Open Data API Endpoint: `https://opendata.cwa.gov.tw/fileapi/v1/opendataapi/F-A0010-001`
