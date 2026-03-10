# Biscayne Bay Water Quality Dashboard

An interactive data dashboard built with Streamlit for exploring water quality measurements collected from Biscayne Bay, Florida. Developed as part of an internship-ready software development course with Prof. Gregory Reis.

## Features

- **Descriptive Statistics** — raw data table and summary stats for all measurements
- **2D Plots** — temperature over time (line chart) and dissolved oxygen vs. temperature colored by pH (scatter)
- **3D Plot** — geospatial scatter plot of latitude/longitude/water column depth colored by temperature
- **NASA APOD** — fetches and displays NASA's Astronomy Picture of the Day via their public API

## Tech Stack

- [Streamlit](https://streamlit.io/) — web dashboard framework
- [Pandas](https://pandas.pydata.org/) — data loading and analysis
- [Plotly Express](https://plotly.com/python/plotly-express/) — interactive 2D and 3D charts
- [NASA APOD API](https://api.nasa.gov/) — astronomy image of the day

## Setup

1. Clone the repo and create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install streamlit pandas plotly requests python-dotenv
   ```

3. Create a `.env` file in the project root with your NASA API key:
   ```
   NASA_API_KEY=your_api_key_here
   ```
   Get a free key at [https://api.nasa.gov/](https://api.nasa.gov/).

4. Run the dashboard:
   ```bash
   streamlit run dashboard.py
   ```

## Data

`biscayneBay_waterquality.csv` contains field measurements from Biscayne Bay including:
- Temperature (°C)
- pH
- Dissolved Oxygen (ODO mg/L)
- Latitude / Longitude
- Total Water Column (m)
- Time
