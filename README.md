# ✈️ Flight Fuel & Emission Calculator  

This is a simple web app built with [Streamlit](https://streamlit.io/) that estimates:  
- 🌍 Flight distance (between two airports)  
- ⛽ Estimated fuel consumption  
- 💨 CO₂ emissions (total + per passenger)  

The app uses [geopy](https://geopy.readthedocs.io/) for distance calculations and basic fuel burn rates for different aircraft.  

---

## 🚀 Live Demo  
👉 [Link will appear here after deployment]  

---

## ⚙️ Features  
- Select origin & destination airports  
- Choose from different aircraft types  
- Adjust number of passengers  
- Get instant distance, fuel, and CO₂ estimates  

---

## 🛠️ How to Run Locally  
1. Clone this repo:  
   ```bash
   git clone https://github.com/yourusername/flight-emissions-app.git
   cd flight-emissions-app
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

pip install -r requirements.txt
streamlit run app.py

Development Updates.
## Version 1.1 – July 2026

### Major Improvements

- Refactored the project into a modular structure by separating aircraft, airport, and airline data into dedicated Python modules (`aircraft.py`, `airports.py`, `airlines.py`).
- Expanded the aircraft database to include 25 commercial aircraft with manufacturer, seating capacity, cruise speed, fuel burn, engine count, and operational range.
- Added airline selection so that users choose an airline before selecting one of its supported aircraft.
- Replaced fixed aircraft parameters with aircraft-specific calculations using the new database.
- Added aircraft specifications (manufacturer, category, seats, cruise speed, range, engines) to the results page.
- Implemented aircraft range validation to prevent unrealistic route calculations and provide user feedback when a selected aircraft cannot operate the chosen route.
- Improved the application's structure to make future expansion (additional airlines, airports, and aircraft) easier.





   

