"""
aircraft.py

Commercial aircraft database for the Flight Emissions Calculator.

Each aircraft stores:
- manufacturer
- category
- typical seating capacity
- average cruise fuel burn (kg/hour)
- number of engines
- average cruise speed (km/h)
- maximum range (km)

Fuel burn values are approximate averages compiled from
manufacturer specifications and published aviation references.
"""

aircraft = {

    # ---------------- Airbus ---------------- #

    "Airbus A220-100": {
        "manufacturer": "Airbus",
        "category": "Regional",
        "seats": 120,
        "fuel_burn": 2100,
        "engines": 2,
        "cruise_speed": 870,
        "range": 6300
    },

    "Airbus A220-300": {
        "manufacturer": "Airbus",
        "category": "Regional",
        "seats": 145,
        "fuel_burn": 2250,
        "engines": 2,
        "cruise_speed": 870,
        "range": 6300
    },

    "Airbus A319": {
        "manufacturer": "Airbus",
        "category": "Short Haul",
        "seats": 140,
        "fuel_burn": 2350,
        "engines": 2,
        "cruise_speed": 828,
        "range": 6900
    },

    "Airbus A320": {
        "manufacturer": "Airbus",
        "category": "Short Haul",
        "seats": 180,
        "fuel_burn": 2500,
        "engines": 2,
        "cruise_speed": 840,
        "range": 6150
    },

    "Airbus A321": {
        "manufacturer": "Airbus",
        "category": "Short Haul",
        "seats": 220,
        "fuel_burn": 2800,
        "engines": 2,
        "cruise_speed": 840,
        "range": 7400
    },

    "Airbus A330-200": {
        "manufacturer": "Airbus",
        "category": "Long Haul",
        "seats": 250,
        "fuel_burn": 5400,
        "engines": 2,
        "cruise_speed": 880,
        "range": 13450
    },

    "Airbus A330-300": {
        "manufacturer": "Airbus",
        "category": "Long Haul",
        "seats": 300,
        "fuel_burn": 5800,
        "engines": 2,
        "cruise_speed": 880,
        "range": 11750
    },

    "Airbus A350-900": {
        "manufacturer": "Airbus",
        "category": "Long Haul",
        "seats": 325,
        "fuel_burn": 5600,
        "engines": 2,
        "cruise_speed": 903,
        "range": 15000
    },

    "Airbus A350-1000": {
        "manufacturer": "Airbus",
        "category": "Long Haul",
        "seats": 370,
        "fuel_burn": 6200,
        "engines": 2,
        "cruise_speed": 903,
        "range": 16100
    },

    "Airbus A380-800": {
        "manufacturer": "Airbus",
        "category": "Ultra Long Haul",
        "seats": 555,
        "fuel_burn": 11500,
        "engines": 4,
        "cruise_speed": 903,
        "range": 15200
    },

    # ---------------- Boeing ---------------- #

    "Boeing 737-700": {
        "manufacturer": "Boeing",
        "category": "Short Haul",
        "seats": 140,
        "fuel_burn": 2350,
        "engines": 2,
        "cruise_speed": 842,
        "range": 6230
    },

    "Boeing 737-800": {
        "manufacturer": "Boeing",
        "category": "Short Haul",
        "seats": 189,
        "fuel_burn": 2600,
        "engines": 2,
        "cruise_speed": 842,
        "range": 5436
    },

    "Boeing 737 MAX 8": {
        "manufacturer": "Boeing",
        "category": "Short Haul",
        "seats": 210,
        "fuel_burn": 2350,
        "engines": 2,
        "cruise_speed": 839,
        "range": 6570
    },

    "Boeing 757-200": {
        "manufacturer": "Boeing",
        "category": "Medium Haul",
        "seats": 200,
        "fuel_burn": 3900,
        "engines": 2,
        "cruise_speed": 850,
        "range": 7222
    },

    "Boeing 767-300ER": {
        "manufacturer": "Boeing",
        "category": "Long Haul",
        "seats": 269,
        "fuel_burn": 5200,
        "engines": 2,
        "cruise_speed": 851,
        "range": 11065
    },

    "Boeing 777-200ER": {
        "manufacturer": "Boeing",
        "category": "Long Haul",
        "seats": 314,
        "fuel_burn": 6800,
        "engines": 2,
        "cruise_speed": 905,
        "range": 14300
    },

    "Boeing 777-300ER": {
        "manufacturer": "Boeing",
        "category": "Long Haul",
        "seats": 396,
        "fuel_burn": 7200,
        "engines": 2,
        "cruise_speed": 905,
        "range": 13650
    },

    "Boeing 787-8 Dreamliner": {
        "manufacturer": "Boeing",
        "category": "Long Haul",
        "seats": 242,
        "fuel_burn": 4900,
        "engines": 2,
        "cruise_speed": 903,
        "range": 13620
    },

    "Boeing 787-9 Dreamliner": {
        "manufacturer": "Boeing",
        "category": "Long Haul",
        "seats": 290,
        "fuel_burn": 5300,
        "engines": 2,
        "cruise_speed": 903,
        "range": 14140
    },

    "Boeing 787-10 Dreamliner": {
        "manufacturer": "Boeing",
        "category": "Long Haul",
        "seats": 330,
        "fuel_burn": 5700,
        "engines": 2,
        "cruise_speed": 903,
        "range": 11910
    },

    # ---------------- Embraer ---------------- #

    "Embraer E170": {
        "manufacturer": "Embraer",
        "category": "Regional",
        "seats": 76,
        "fuel_burn": 1700,
        "engines": 2,
        "cruise_speed": 829,
        "range": 3900
    },

    "Embraer E175": {
        "manufacturer": "Embraer",
        "category": "Regional",
        "seats": 88,
        "fuel_burn": 1850,
        "engines": 2,
        "cruise_speed": 829,
        "range": 4000
    },

    "Embraer E190": {
        "manufacturer": "Embraer",
        "category": "Regional",
        "seats": 106,
        "fuel_burn": 2050,
        "engines": 2,
        "cruise_speed": 829,
        "range": 4500
    },

    "Embraer E195-E2": {
        "manufacturer": "Embraer",
        "category": "Regional",
        "seats": 132,
        "fuel_burn": 2200,
        "engines": 2,
        "cruise_speed": 870,
        "range": 4815
    },

    # ---------------- ATR ---------------- #

    "ATR 72-600": {
        "manufacturer": "ATR",
        "category": "Turboprop",
        "seats": 72,
        "fuel_burn": 900,
        "engines": 2,
        "cruise_speed": 510,
        "range": 1528
    }

}
