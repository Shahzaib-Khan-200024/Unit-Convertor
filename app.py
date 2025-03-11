import streamlit as st
from forex_python.converter import CurrencyRates
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
        if from_unit == "celsius" and to_unit == "fahrenheit":
            result = (value * 9/5) + 32
        elif from_unit == "fahrenheit" and to_unit == "celsius":
            result = (value - 32) * 5/9
        elif from_unit == "celsius" and to_unit == "kelvin":
            result = value + 273.15
        elif from_unit == "kelvin" and to_unit == "celsius":
            result = value - 273.15
        elif from_unit == "fahrenheit" and to_unit == "kelvin":
            result = (value - 32) * 5/9 + 273.15
        elif from_unit == "kelvin" and to_unit == "fahrenheit":
            result = (value - 273.15) * 9/5 + 32
        else:
            result = value
        
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

# Currency Conversion
elif conversion_type == "Currency":
    c = CurrencyRates()
    currency_codes = ["USD", "EUR", "PKR", "INR", "GBP", "AUD", "CAD", "JPY", "CNY"]
    value = st.number_input("Enter amount:", value=1.0)
    from_currency = st.selectbox("From:", currency_codes)
    to_currency = st.selectbox("To:", currency_codes)
    
    if st.button("Convert"):
        try:
            result = c.convert(from_currency, to_currency, value)
            st.success(f"{value} {from_currency} = {result:.2f} {to_currency}")
        except Exception as e:
            st.error("Error fetching currency rates. Check your internet connection.")

# Area Conversion
elif conversion_type == "Area":
    area_units = ["square meter", "square kilometer", "square mile", "square foot", "square inch", "hectare", "acre"]
    value = st.number_input("Enter value:", value=1.0)
    from_unit = st.selectbox("From:", area_units)
    to_unit = st.selectbox("To:", area_units)
    
    if st.button("Convert"):
        result = (value * ureg(from_unit)).to(to_unit)
        st.success(f"{value} {from_unit} = {result.magnitude:.4f} {to_unit}")

# Time Conversion
elif conversion_type == "Time":
    time_units = ["second", "minute", "hour", "day", "week", "month", "year"]
    value = st.number_input("Enter value:", value=1.0)
    from_unit = st.selectbox("From:", time_units)
    to_unit = st.selectbox("To:", time_units)
    
    if st.button("Convert"):
        result = (value * ureg(from_unit)).to(to_unit)
        st.success(f"{value} {from_unit} = {result.magnitude:.4f} {to_unit}")

# Speed Conversion
elif conversion_type == "Speed":
    speed_units = ["meter per second", "kilometer per hour", "mile per hour", "knot"]
    value = st.number_input("Enter value:", value=1.0)
    from_unit = st.selectbox("From:", speed_units)
    to_unit = st.selectbox("To:", speed_units)
    
    if st.button("Convert"):
        result = (value * ureg(from_unit)).to(to_unit)
        st.success(f"{value} {from_unit} = {result.magnitude:.4f} {to_unit}")

st.caption("Built with ❤️ using Streamlit")


# streamlit run app.py