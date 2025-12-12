# AIoT 天氣爬蟲與儀表板 ??

本專案是 AIoT 課程的一部分，是一個針對台灣的天氣資料爬蟲與視覺化儀表板。它從台灣中央氣象署 (CWA) 開放資料 API 擷取天氣預報資料，並透過互動式的 Streamlit 網頁應用程式呈現。

## 功能

- **資料爬蟲**：擷取台灣各地的最新天氣預報。
- **資料庫**：使用 SQLite (`sqlitedata.db`) 在地端儲存天氣資料。
- **互動式儀表板**：使用 Streamlit 建置，方便探索資料。
- **視覺化**：
    - 使用 Plotly 繪製溫度趨勢 (最低/最高溫)。
    - 關鍵指標 (平均溫度、地點總數)。
    - 詳細資料表。
- **資料管理**：介面上有「重新整理資料」按鈕，可直接觸發爬蟲更新資料。

## 安裝

1. **複製專案 (Clone)**：
   ```bash
   git clone https://github.com/Joxanne/AIoT_Weather_Crawler.git
   cd AIoT_Weather_Crawler
   ```

2. **安裝依賴套件**：
   ```bash
   pip install -r requirements.txt
   ```

## 使用方式

1. **執行 Streamlit 應用程式**：
   ```bash
   streamlit run app.py
   ```

2. **初始化資料**：
   - 首次開啟應用程式時，資料庫可能是空的。
   - 請點擊側邊欄的 **"? Refresh Data"** 按鈕，從 CWA API 擷取最新的天氣資料。

## 專案結構

- `app.py`: 主要的 Streamlit 應用程式檔案，包含 UI 邏輯與視覺化。
- `weather_crawler.py`: 包含從 API 擷取資料並與 SQLite 資料庫互動的邏輯。
- `requirements.txt`: Python 依賴套件列表。
- `sqlitedata.db`: SQLite 資料庫檔案 (自動產生)。

## 資料來源

- [台灣中央氣象署 (CWA) 開放資料平台](https://opendata.cwa.gov.tw/)
