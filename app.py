import streamlit as st
import altair as alt
import pandas as pd
from geopy.distance import geodesic
from aircraft import aircraft
from airports import airports
from airlines import airlines

st.title("✈️ Flight Fuel & Emission Calculator")

# Input form
origin = st.selectbox("Select origin airport", list(airports.keys()))
destination = st.selectbox("Select destination airport", list(airports.keys()))
airline1 = st.selectbox(
    "🏢 Select First Airline",
    list(airlines.keys()),
    key="air1"
)

aircraft1 = st.selectbox(
    "✈️ Aircraft",
    airlines[airline1],
    key="ac1"
)

airline2 = st.selectbox(
    "🏢 Select Second Airline",
    list(airlines.keys()),
    key="air2"
)

aircraft2 = st.selectbox(
    "✈️ Aircraft",
    airlines[airline2],
    key="ac2"
)
passengers = st.slider("Number of passengers", 1, 350, 150)

# Automatically adjusted aviation fuel price (global average estimate)
fuel_price_per_liter = 0.92
st.write(f"💵 Fuel price: ${fuel_price_per_liter:.2f}/L (adjusted automatically)")

if st.button("Calculate"):

    # Calculate distance
    distance_km = geodesic(airports[origin], airports[destination]).km
    st.write(f"🌍 Flight distance: {distance_km:.1f} km")

    results = {}

    for ac in [aircraft1, aircraft2]:

        burn_rate = aircraft[ac]["fuel_burn"]
        speed = aircraft[ac]["cruise_speed"]
        max_range = aircraft[ac]["range"]
        capacity = aircraft[ac]["seats"]

        # Check aircraft range
        if distance_km > max_range:
            st.error(
                f"❌ {ac} cannot operate this route.\nMaximum range: {max_range:,} km"
            )
            continue

        st.write(f"👥 Aircraft Capacity: {capacity}")

        # Flight calculations
        flight_time = distance_km / speed
        total_fuel = burn_rate * flight_time
        emissions = total_fuel * 3.149
        fuel_cost = total_fuel * fuel_price_per_liter
        cost_per_passenger = fuel_cost / passengers

        results[ac] = {
            "fuel": total_fuel,
            "emissions": emissions,
            "fuel_cost": fuel_cost,
            "cost_per_passenger": cost_per_passenger
        }

        st.subheader(f"Results for {ac}")
        st.write(f"⛽ Fuel use: {total_fuel:,.0f} kg")
        st.write(f"💨 CO₂ emissions: {emissions:,.0f} kg")
        st.write(f"💰 Fuel cost: ${fuel_cost:,.2f}")
        st.success(f"💺 Cost per passenger: ${cost_per_passenger:,.2f}")

        with st.expander(f"📋 {ac} Specifications"):
            st.write(f"**Manufacturer:** {aircraft[ac]['manufacturer']}")
            st.write(f"**Category:** {aircraft[ac]['category']}")
            st.write(f"**Seats:** {aircraft[ac]['seats']}")
            st.write(f"**Cruise Speed:** {aircraft[ac]['cruise_speed']} km/h")
            st.write(f"**Range:** {aircraft[ac]['range']} km")
            st.write(f"**Engines:** {aircraft[ac]['engines']}")

    if len(results) == 2:

        chart_data = pd.DataFrame({
            "Aircraft": [aircraft1, aircraft2],
            "CO2 Emissions (kg)": [
                results[aircraft1]["emissions"],
                results[aircraft2]["emissions"]
            ],
            "Fuel Cost (USD)": [
                results[aircraft1]["fuel_cost"],
                results[aircraft2]["fuel_cost"]
            ]
        })

        chart = alt.Chart(chart_data).transform_fold(
            ["CO2 Emissions (kg)", "Fuel Cost (USD)"],
            as_=["Metric", "Value"]
        ).mark_bar().encode(
            x="Aircraft:N",
            y="Value:Q",
            color="Metric:N",
            column="Metric:N"
        )

        st.altair_chart(chart, use_container_width=True)

        cheaper = min(results, key=lambda x: results[x]["fuel_cost"])
        expensive = max(results, key=lambda x: results[x]["fuel_cost"])

        diff = results[expensive]["fuel_cost"] - results[cheaper]["fuel_cost"]
        percent = diff / results[expensive]["fuel_cost"] * 100

        st.subheader("📢 Conclusion")
        st.success(
            f"{cheaper} is more economical, saving ${diff:,.2f} ({percent:.1f}%) compared to {expensive}."
        )

