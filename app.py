import streamlit as st

def calculate_bmi(weight, height_feet):
    """Calculates BMI and determines the health category."""
    # Convert height from feet to meters
    height_meters = height_feet * 0.3048
    
    # Calculate BMI
    bmi = weight / (height_meters ** 2)

    # Determine category and provide instructions
    if bmi < 18.5:
        category = "Underweight"
        color = "blue"
        instructions = """
        It is important to eat a balanced diet and ensure you're getting enough calories to support your body.
        Consider consulting a healthcare provider to determine if you have an underlying medical condition.
        """
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
        color = "green"
        instructions = """
        You're in a healthy weight range! Keep up with a balanced diet and regular physical activity to maintain your health.
        """
    elif 25 <= bmi < 29.9:
        category = "Overweight"
        color = "orange"
        instructions = """
        It's a good idea to focus on maintaining a balanced diet and incorporating regular exercise.
        You may want to consult a healthcare professional for personalized advice.
        """
    else:
        category = "Obese"
        color = "red"
        instructions = """
        Consider speaking with a healthcare provider about your weight and lifestyle changes to improve your overall health.
        A combination of diet, exercise, and possibly medical intervention may help you achieve a healthier weight.
        """

    return bmi, category, color, instructions

# Streamlit App Title
st.title("💪 BMI Calculator")

# User Inputs for weight and height
weight = st.number_input("Enter Your Weight (kg):", min_value=1.0, format="%.2f")
height_feet = st.number_input("Enter Your Height (feet):", min_value=1.0, format="%.2f")

# Button to calculate BMI
if st.button("Calculate BMI"):
    if weight > 0 and height_feet > 0:
        bmi, category, color, instructions = calculate_bmi(weight, height_feet)
        st.write(f"### Your BMI: **{bmi:.2f}**")
        st.markdown(f"### **Category: <span style='color:{color};'>{category}</span>**", unsafe_allow_html=True)
        st.write(f"### Instructions:")
        st.write(instructions)
    else:
        st.warning("Please enter valid values for weight and height.")
