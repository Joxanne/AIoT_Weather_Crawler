# -*- coding: utf-8 -*-
import requests
import pandas as pd
import sqlite3
import os
import sys
from datetime import datetime

# Ensure stdout handles utf-8
sys.stdout.reconfigure(encoding='utf-8')

# API URL
url = "https://opendata.cwa.gov.tw/fileapi/v1/opendataapi/F-A0010-001?Authorization=CWA-098BE5E3-2529-46C2-A82E-F996D8BA9D98&downloadType=WEB&format=JSON"
DB_NAME = 'sqlitedata.db'

def init_db():
    """Initialize database and table"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather_forecasts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            location TEXT,
            date TEXT,
            weather_desc TEXT,
            min_temp REAL,
            max_temp REAL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()
    print(f"Database {DB_NAME} initialized.")

def save_to_db(records):
    """Save data to SQLite"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Clear previous data
    cursor.execute("DELETE FROM weather_forecasts")
    
    insert_query = '''
        INSERT INTO weather_forecasts (location, date, weather_desc, min_temp, max_temp)
        VALUES (?, ?, ?, ?, ?)
    '''
    
    # Convert records for execute_many
    db_data = []
    for r in records:
        db_data.append((
            r['location'],
            r['date'],
            r['weather_desc'],
            r['min_temp'],
            r['max_temp']
        ))
        
    cursor.executemany(insert_query, db_data)
    conn.commit()
    print(f"Saved {len(db_data)} records to database.")
    conn.close()

def crawl_and_save():
    print("Connecting to CWA API...")

    try:
        response = requests.get(url)
        response.encoding = 'utf-8'
        
        if response.status_code == 200:
            data = response.json()
            
            try:
                # 1. Navigate to 'data' level
                # Path: cwaopendata -> resources -> resource -> data
                root = data.get('cwaopendata', {})
                
                # resource can be list or dict
                resources_node = root.get('resources', {})
                resource_node = resources_node.get('resource', {})
                
                if isinstance(resource_node, list):
                    resource_node = resource_node[0]
                    
                data_node = resource_node.get('data', {})
                
                # 2. Navigate to 'location' level
                agr_forecasts = data_node.get('agrWeatherForecasts', {}).get('weatherForecasts', {})
                locations = agr_forecasts.get('location', [])

                if not locations:
                    print("Warning: No location data found. Check API structure.")
                    return False
                else:
                    print(f"Successfully retrieved data for {len(locations)} locations. Processing...")
                    
                    # Initialize DB
                    init_db()
                    
                    all_records_for_df = []
                    all_records_for_db = []
                    
                    for loc in locations:
                        loc_name = loc['locationName']
                        
                        # Get weather elements
                        weather_elements = loc.get('weatherElements', {})
                        
                        daily_wx = weather_elements.get('Wx', {}).get('daily', [])
                        daily_maxT = weather_elements.get('MaxT', {}).get('daily', [])
                        daily_minT = weather_elements.get('MinT', {}).get('daily', [])
                        
                        # Get today's date
                        today = datetime.now().strftime('%Y-%m-%d')

                        # Loop based on Wx length
                        for i in range(len(daily_wx)):
                            date_str = daily_wx[i]['dataDate']
                            # Normalize date string to YYYY-MM-DD if necessary
                            if 'T' in date_str:
                                date_str = date_str.split('T')[0]
                            
                            # Skip past dates
                            if date_str < today:
                                continue

                            weather_desc = daily_wx[i]['weather']
                            
                            # Safely get values
                            max_t = daily_maxT[i]['temperature'] if i < len(daily_maxT) else None
                            min_t = daily_minT[i]['temperature'] if i < len(daily_minT) else None


                            # Prepare DB record (Raw Data)
                            all_records_for_db.append({
                                'location': loc_name,
                                'date': date_str,
                                'weather_desc': weather_desc,
                                'min_temp': min_t,
                                'max_temp': max_t
                            })
                            
                            # Prepare Display record (Formatted)
                            temp_str = f"{min_t} - {max_t}" if (min_t is not None and max_t is not None) else "-"
                            
                            all_records_for_df.append({
                                "Location": loc_name,
                                "Date": date_str,
                                "Weather": weather_desc,
                                "Temp": temp_str
                            })

                    # 3. Save to DB
                    save_to_db(all_records_for_db)

                    # 4. Display Table
                    df = pd.DataFrame(all_records_for_df)
                    print("\n=== Weather Forecast (First 20 rows) ===")
                    pd.set_option('display.max_rows', 20)
                    pd.set_option('display.unicode.east_asian_width', True)
                    print(df.head(20).to_markdown(index=False))
                    print(f"\nTotal {len(df)} records.")
                    return True

            except Exception as e:
                print(f"Data parsing failed: {e}")
                import traceback
                traceback.print_exc()
                return False
                
        else:
            print(f"Connection failed, status code: {response.status_code}")
            return False

    except Exception as e:
        print(f"Program error: {e}")
        return False

if __name__ == "__main__":
    crawl_and_save()
