import streamlit as st
import numpy as np
import pickle

# Load the trained Naive Bayes model
model_filename = "NBClassifier.pkl"
with open(model_filename, "rb") as file:
    model = pickle.load(file)

# Crop Emojis Dictionary
crop_emojis = {
    "Rice": "🌾", "Maize": "🌽", "Chickpea": "🫘", "Kidney Beans": "🥣", "Pigeon Peas": "🌱",
    "Moth Beans": "🥜", "Mung Bean": "🌿", "Black Gram": "🍛", "Lentil": "🍲", "Pomegranate": "🍎",
    "Banana": "🍌", "Mango": "🥭", "Grapes": "🍇", "Watermelon": "🍉", "Muskmelon": "🍈",
    "Apple": "🍏", "Orange": "🍊", "Papaya": "🥭", "Coconut": "🥥", "Cotton": "👕", "Jute": "🧵", "Coffee": "☕"
}

# Streamlit UI
st.set_page_config(page_title="Crop Recommendation System", layout="wide")

# Custom CSS for Styling
st.markdown("""
    <style>
        .main {
            background-color: #f5f5f5;
        }
        h1 {
            color: #2E86C1;
        }
        .stButton>button {
            background-color: #2E86C1;
            color: white;
            font-size: 18px;
            border-radius: 10px;
            padding: 8px;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #1F618D;
        }
        .output-text {
            font-size: 28px;
            font-weight: bold;
            color: #28a745;
            text-align: center;
            padding: 10px;
            border-radius: 10px;
            background-color: #eafbea;
        }
        .input-box {
            height: 40px;
            width: 100%;
            font-size: 16px;
            padding: 5px;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("🔍 Navigation")
choice = st.sidebar.radio("Go to", ["Home", "Crop Prediction"])

if choice == "Home":
    st.title("🌾 Welcome to the Crop Recommendation System")
    st.write("""
        **What is the Crop Recommendation System?**  
        The **AI-powered Crop Recommendation System** helps farmers **select the best crops** 
        based on **soil nutrients, weather conditions, and environmental factors**.  

        **🔹 How It Works?**  
        1️⃣ **Enter Soil and Weather Data** (Nitrogen, Phosphorus, Potassium, pH, Temperature, Humidity, Rainfall)  
        2️⃣ **Machine Learning Model Processes the Data**  
        3️⃣ **System Predicts the Best Crop** ✅  
        4️⃣ **Grow Crops Efficiently with Higher Yield** 🚜  

        🔥 **Start by selecting 'Crop Prediction' from the sidebar!**
    """)

    # Additional Features
    st.markdown("### 🌱 Features & Benefits")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("✔ **Smart Crop Suggestions** 🌾")
        st.markdown("✔ **Accurate Weather-Based Recommendations** ☁️")
        st.markdown("✔ **Soil Nutrient Analysis** 🧪")
    
    with col2:
        st.markdown("✔ **Supports Multiple Soil Types** 🌎")
        st.markdown("✔ **Easy-to-Use Interface** 🎨")
        st.markdown("✔ **Optimized for All Devices** 📱💻")

# Crop Prediction Section
elif choice == "Crop Prediction":
    st.title("🌱 Crop Recommendation System")
    st.write("Enter soil and weather details to get the best crop recommendation.")

    # Min & Max Values for Inputs
    min_max_values = {
        "Nitrogen (N)": (0, 140), "Phosphorus (P)": (5, 145), "Potassium (K)": (5, 205),
        "Temperature (°C)": (8, 45), "Humidity (%)": (10, 100), "pH Level": (3.5, 9.5), "Rainfall (mm)": (20, 300)
    }

    # Creating columns for better UI
    col1, col2 = st.columns(2)

    input_data = {}
    error_flag = False

    with col1:
        for key in ["Nitrogen (N)", "Phosphorus (P)", "Potassium (K)"]:
            min_val, max_val = min_max_values[key]
            value = st.text_input(f"🌿 {key} (Min: {min_val}, Max: {max_val})", value="50", key=key)
            try:
                float_value = float(value)
                if float_value < min_val or float_value > max_val:
                    st.error(f"❌ {key} must be between {min_val} and {max_val}!")
                    error_flag = True
                else:
                    input_data[key] = float_value
            except ValueError:
                st.error(f"❌ {key} must be a number!")
                error_flag = True

    with col2:
        for key in ["Temperature (°C)", "Humidity (%)", "pH Level", "Rainfall (mm)"]:
            min_val, max_val = min_max_values[key]
            value = st.text_input(f"🌡 {key} (Min: {min_val}, Max: {max_val})", value="25", key=key)
            try:
                float_value = float(value)
                if float_value < min_val or float_value > max_val:
                    st.error(f"❌ {key} must be between {min_val} and {max_val}!")
                    error_flag = True
                else:
                    input_data[key] = float_value
            except ValueError:
                st.error(f"❌ {key} must be a number!")
                error_flag = True

    # Prediction Button
    if st.button("🚜 Predict Crop"):
        if error_flag:
            st.error("❌ Please fix the errors above before predicting.")
        else:
            # Convert to NumPy array
            input_array = np.array([[input_data["Nitrogen (N)"], input_data["Phosphorus (P)"], input_data["Potassium (K)"], 
                                     input_data["Temperature (°C)"], input_data["Humidity (%)"], input_data["pH Level"], 
                                     input_data["Rainfall (mm)"]]])

            # Predict crop
            prediction = model.predict(input_array)[0]

            # Get Emoji for the predicted crop
            emoji = crop_emojis.get(prediction, "🌾")  

            # Display Result with Bigger Font
            st.markdown(f"<div class='output-text'>🎉 Recommended Crop: {prediction} {emoji}</div>", unsafe_allow_html=True)
