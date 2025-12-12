# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
import plotly.graph_objects as go
from weather_crawler import crawl_and_save, DB_NAME

# 1. Page Configuration
st.set_page_config(
    page_title="Taiwan Weather Dashboard",
    page_icon="🌤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Custom CSS
st.markdown("""
<style>
    .main {
        background-color: #f0f2f6;
    }
    .stApp {
        max-width: 100%;
    }
    div[data-testid="stMetric"] {
        background: linear-gradient(to bottom right, #0072ff, #00c6ff);
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.2);
        border: none;
    }
    /* Force text colors to ensure visibility in Dark Mode */
    [data-testid="stMetricLabel"] {
        font-size: 30px !important;
        font-weight: 900 !important;
        color: #ffffff !important;
    }
    [data-testid="stMetricValue"] {
        color: #ffffff !important;
    }
    h1, h2, h3 {
        color: #1f2937;
    }
</style>
""", unsafe_allow_html=True)

# 3. Sidebar
with st.sidebar:
    st.title("🌤️ Weather App")
    st.markdown("---")
    
    st.subheader("Data Management")
    if st.button("🔄 Refresh Data", use_container_width=True):
        with st.spinner("Fetching latest data from CWA API..."):
            success = crawl_and_save()
            if success:
                st.success("Updated successfully!")
                st.rerun()
            else:
                st.error("Update failed.")
    
    st.markdown("---")
    st.caption("Data Source: Taiwan CWA Open Data")

# 4. Main Content
st.title("Taiwan Weather Forecast Dashboard")

try:
    conn = sqlite3.connect(DB_NAME)
    
    # Load Data
    df = pd.read_sql("SELECT * FROM weather_forecasts", conn)
    conn.close()

    if df.empty:
        st.warning("No data found. Please click 'Refresh Data' in the sidebar.")
    else:
        # Preprocessing
        df['date'] = pd.to_datetime(df['date'])
        df['created_at'] = pd.to_datetime(df['created_at'])
        
        # Top Metrics Row
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Locations", df['location'].nunique())
        with col2:
            st.metric("Forecast Days", df['date'].nunique())
        with col3:
            avg_max_temp = df['max_temp'].mean()
            st.metric("Avg Max Temp", f"{avg_max_temp:.1f} °C")
        with col4:
            last_update = df['created_at'].max().strftime("%Y-%m-%d %H:%M")
            st.metric("Last Updated", last_update)

        st.markdown("---")

        # Filters
        col_filter, col_chart = st.columns([1, 3])
        
        with col_filter:
            st.subheader("📍 Location Filter")
            locations = sorted(df['location'].unique())
            selected_location = st.selectbox("Select Region", locations)
            
            # Filter data
            filtered_df = df[df['location'] == selected_location].sort_values('date')
            
            # Current Weather Card (First record of selected location)
            if not filtered_df.empty:
                current = filtered_df.iloc[0]
                st.info(f"""
                **{selected_location}**  
                📅 {current['date'].strftime('%Y-%m-%d')}  
                🌡️ {current['min_temp']} - {current['max_temp']} °C  
                ☁️ {current['weather_desc']}
                """)

        with col_chart:
            st.subheader("📈 Temperature Trend")
            if not filtered_df.empty:
                fig = go.Figure()
                
                # Max Temp Line
                fig.add_trace(go.Scatter(
                    x=filtered_df['date'], 
                    y=filtered_df['max_temp'],
                    mode='lines+markers',
                    name='Max Temp',
                    line=dict(color='#FF4B4B', width=3)
                ))
                
                # Min Temp Line
                fig.add_trace(go.Scatter(
                    x=filtered_df['date'], 
                    y=filtered_df['min_temp'],
                    mode='lines+markers',
                    name='Min Temp',
                    line=dict(color='#4B9CFF', width=3)
                ))
                
                fig.update_layout(
                    title=f"{selected_location} - 7 Day Forecast",
                    xaxis_title="Date",
                    yaxis_title="Temperature (°C)",
                    hovermode="x unified",
                    template="plotly_white",
                    height=400
                )
                st.plotly_chart(fig, use_container_width=True)

        # Detailed Data Table
        st.subheader("📊 Detailed Forecast Data")
        
        # Formatting for display
        display_df = filtered_df[['date', 'weather_desc', 'min_temp', 'max_temp']].copy()
        display_df['date'] = display_df['date'].dt.strftime('%Y-%m-%d')
        display_df.columns = ['Date', 'Weather Condition', 'Min Temp (°C)', 'Max Temp (°C)']
        
        st.dataframe(
            display_df,
            use_container_width=True,
            hide_index=True,
            column_config={
                "Min Temp (°C)": st.column_config.NumberColumn(format="%.1f °C"),
                "Max Temp (°C)": st.column_config.NumberColumn(format="%.1f °C"),
            }
        )

except Exception as e:
    st.error(f"Database Error: {e}")
    st.info("Please ensure the database is initialized by clicking 'Refresh Data'.")
