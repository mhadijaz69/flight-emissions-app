import streamlit as st
import altair as alt
import pandas as pd
from geopy.distance import geodesic

# Dictionary of sample airports (lat, lon)
airports = {
    "LHR (London Heathrow)": (51.4700, -0.4543),
    "JFK (New York)": (40.6413, -73.7781),
    "DXB (Dubai)": (25.2532, 55.3657),
    "LHE (Lahore)": (31.5216, 74.4036),
    "IST (Istanbul Airport)": (41.2753, 28.7519),  
    "YYZ (Toronto Pearson)": (43.6777, -79.6248), 
    "SYD (Sydney Airport)": (-33.9399, 151.1753), 
    "SIN (Singapore Changi)": (1.3644, 103.9915),  

}

# Aircraft fuel burn (liters per 100 km per seat) - rough estimates
aircraft_data = {
    "Boeing 737": 3.1,
    "Airbus A320": 3.3,
    "Boeing 787": 2.5,
    "Airbus A350": 2.4,
    "Boeing 747": 3.1,
    "Airbus A380": 3.3,
}

st.title("✈️ Flight Fuel & Emission Calculator")

# Input form
origin = st.selectbox("Select origin airport", list(airports.keys()))
destination = st.selectbox("Select destination airport", list(airports.keys()))
aircraft1 = st.selectbox("✈️ Select First Aircraft", list(aircraft_data.keys()), key="ac1")
aircraft2 = st.selectbox("✈️ Select Second Aircraft", list(aircraft_data.keys()), key="ac2")
passengers = st.slider("Number of passengers", 1, 350, 150)

fuel_price_per_liter = st.number_input(
    "💵 Enter fuel price per liter (USD):",
    min_value=0.1,
    max_value=5.0,
    value=0.8,
    step=0.1
)

if st.button("Calculate"):
    # Calculate distance
    distance_km = geodesic(airports[origin], airports[destination]).km
    st.write(f"🌍 Flight distance: {distance_km:.1f} km")

    # Automatic passenger estimation
    if distance_km < 1500:
        passengers = 150
    elif distance_km < 4000:
        passengers = 220
    else:
        passengers = 300



    # Store results for both aircraft
    results = {}

    for ac in [aircraft1, aircraft2]:
        burn_rate = aircraft_data[ac]
        total_fuel = (distance_km / 100) * burn_rate * passengers
        emissions = total_fuel * 2.5  
        fuel_cost = total_fuel * fuel_price_per_liter
        cost_per_passenger = fuel_cost / passengers

        results[ac] = {
            "fuel": total_fuel,
            "emissions": emissions,
            "fuel_cost": fuel_cost,
            "cost_per_passenger": cost_per_passenger
        }

        st.subheader(f"Results for {ac}")
        st.write(f"⛽ Fuel use: {total_fuel:,.0f} liters")
        st.write(f"💨 CO₂ emissions: {emissions:,.0f} kg")
        st.write(f"💰 Fuel cost: ${fuel_cost:,.2f}")
        st.success(f"Cost per passenger: ${cost_per_passenger:,.2f}")

    # 📊 Chart for comparison
    chart_data = pd.DataFrame({
        "Aircraft": [aircraft1, aircraft2],
        "CO2 Emissions (kg)": [results[aircraft1]["emissions"], results[aircraft2]["emissions"]],
        "Fuel Cost (USD)": [results[aircraft1]["fuel_cost"], results[aircraft2]["fuel_cost"]]
    })

    chart = alt.Chart(chart_data).transform_fold(
        ["CO2 Emissions (kg)", "Fuel Cost (USD)"],
        as_=["Metric", "Value"]
    ).mark_bar().encode(
        x="Aircraft:N",
        y="Value:Q",
        color="Metric:N",
        column="Metric:N"
    ).properties(title="Aircraft Comparison")

    st.altair_chart(chart, use_container_width=True)

    # 📌 Conclusion message
    cheaper = min(results, key=lambda x: results[x]["fuel_cost"])
    expensive = max(results, key=lambda x: results[x]["fuel_cost"])
    diff = results[expensive]["fuel_cost"] - results[cheaper]["fuel_cost"]
    percent = (diff / results[expensive]["fuel_cost"]) * 100

    st.subheader("📢 Conclusion")
    st.success(f"{cheaper} is more economical, saving about ${diff:,.2f} ({percent:.1f}%) compared to {expensive}.")


