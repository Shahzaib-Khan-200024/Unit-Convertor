import streamlit as st
import requests
from pint import UnitRegistry

# Initialize unit registry
ureg = UnitRegistry()

# Streamlit UI
st.title("Google Unit Converter")

# Conversion Type Selection
conversion_type = st.selectbox(
    "Select Conversion Type:",
    ["Length", "Weight", "Temperature", "Currency", "Area", "Time", "Speed", "Volume", "Energy", "Pressure", "Power", "Data Storage"]
)

# Length Conversion
if conversion_type == "Length":
    length_units = ["meter", "kilometer", "mile", "foot", "inch", "yard", "centimeter", "millimeter", "nanometer"]
    value = st.number_input("Enter value:", value=1.0)
    from_unit = st.selectbox("From:", length_units)
    to_unit = st.selectbox("To:", length_units)
    if st.button("Convert"):
        result = (value * ureg(from_unit)).to(to_unit)
        st.success(f"{value} {from_unit} = {result.magnitude:.4f} {to_unit}")

# Weight Conversion
elif conversion_type == "Weight":
    weight_units = ["gram", "kilogram", "pound", "ounce", "ton"]
    value = st.number_input("Enter value:", value=1.0)
    from_unit = st.selectbox("From:", weight_units)
    to_unit = st.selectbox("To:", weight_units)
    if st.button("Convert"):
        result = (value * ureg(from_unit)).to(to_unit)
        st.success(f"{value} {from_unit} = {result.magnitude:.4f} {to_unit}")

# Temperature Conversion
elif conversion_type == "Temperature":
    temp_units = ["celsius", "fahrenheit", "kelvin"]
    value = st.number_input("Enter temperature:", value=0.0)
    from_unit = st.selectbox("From:", temp_units)
    to_unit = st.selectbox("To:", temp_units)
    if st.button("Convert"):
        conversions = {
            ("celsius", "fahrenheit"): lambda v: (v * 9/5) + 32,
            ("fahrenheit", "celsius"): lambda v: (v - 32) * 5/9,
            ("celsius", "kelvin"): lambda v: v + 273.15,
            ("kelvin", "celsius"): lambda v: v - 273.15,
            ("fahrenheit", "kelvin"): lambda v: (v - 32) * 5/9 + 273.15,
            ("kelvin", "fahrenheit"): lambda v: (v - 273.15) * 9/5 + 32
        }
        result = conversions.get((from_unit, to_unit), lambda v: v)(value)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

# Currency Conversion
elif conversion_type == "Currency":
    api_key = "7d8c8ce68b5f96933c5a9f8690b719f9"  # Replace with your actual API key from exchangeratesapi.io
    url = f"https://api.exchangeratesapi.io/latest?access_key={api_key}"
    currency_codes = ["USD", "EUR", "PKR", "INR", "GBP", "AUD", "CAD", "JPY", "CNY"]
    value = st.number_input("Enter amount:", value=1.0)
    from_currency = st.selectbox("From:", currency_codes)
    to_currency = st.selectbox("To:", currency_codes)
    if st.button("Convert"):
        try:
            response = requests.get(url).json()
            rate = response['rates'][to_currency] / response['rates'][from_currency]
            result = value * rate
            st.success(f"{value} {from_currency} = {result:.2f} {to_currency}")
        except Exception:
            st.error("Failed to fetch exchange rates. Try again later.")

# General Unit Conversion (Area, Time, Speed, Volume, Energy, Pressure, Power, Data Storage)
elif conversion_type in ["Area", "Time", "Speed", "Volume", "Energy", "Pressure", "Power", "Data Storage"]:
    unit_categories = {
        "Area": ["square meter", "square kilometer", "square mile", "square foot", "square inch", "hectare", "acre"],
        "Time": ["second", "minute", "hour", "day", "week", "month", "year"],
        "Speed": ["meter per second", "kilometer per hour", "mile per hour", "knot"],
        "Volume": ["liter", "milliliter", "cubic meter", "gallon", "quart", "pint", "cup", "fluid ounce"],
        "Energy": ["joule", "kilojoule", "calorie", "kilocalorie", "watt hour", "kilowatt hour"],
        "Pressure": ["pascal", "bar", "psi", "atmosphere", "torr"],
        "Power": ["watt", "kilowatt", "horsepower", "megawatt"],
        "Data Storage": ["byte", "kilobyte", "megabyte", "gigabyte", "terabyte", "petabyte"]
    }
    
    units = unit_categories[conversion_type]
    value = st.number_input("Enter value:", value=1.0)
    from_unit = st.selectbox("From:", units)
    to_unit = st.selectbox("To:", units)
    if st.button("Convert"):
        result = (value * ureg(from_unit)).to(to_unit)
        st.success(f"{value} {from_unit} = {result.magnitude:.4f} {to_unit}")

st.caption("Built with ❤️ using Streamlit")

# streamlit run app.py