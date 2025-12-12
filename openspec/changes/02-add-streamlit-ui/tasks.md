# Implementation Tasks

- [x] Install `streamlit` (if not installed)
- [x] Refactor `weather_crawler.py` to ensure `get_weather_data` and `save_to_db` can be imported without running `main()`
- [x] Create `app.py`
- [x] Implement database connection in `app.py`
- [x] Add "Fetch/Refresh Data" button that calls `weather_crawler` functions
- [x] Create location dropdown selector (including an "All" option)
- [x] Display filtered data using `st.dataframe` or `st.table`
- [x] Verify the app runs with `streamlit run app.py`
