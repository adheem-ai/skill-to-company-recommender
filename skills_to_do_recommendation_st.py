import pandas as pd
import joblib
import streamlit as st

st.title("Welcome to Skill_to_Company Recommender")
name = st.text_input("Enter your name:")
if name:
    st.success(f"Hello {name}! let help you find the best company for you")

Menu = st.sidebar.selectbox(
    "navigate",
    ["Home", "Predict", "About", "Contact"]
)
model = joblib.load("C:/users/lenovo/Desktop/skill.py/skills_model.pkl")
encoder = ("C:/users/lenovo/Desktop/skill.py/skills_encoder.pkl")

age = st.number_input("Age: ")
skill = st.text_input("Skill_Acquired: ")
location = st.text_input("LGA: ")
skill_level = st.selectbox("skills level: ", ['Beginner', 'Intermediate', 'Advance'])
device = st.selectbox("Deviced used, e.g laptop or smartphone: ", ['smartphone', 'laptop'])
year_of_experience = st.number_input("Years of experience e.g 0.5 for 6 months, 3 for three years: ")
project_done = st.number_input("Number of projects done: ")
work_type = st.selectbox("Work type: ", ['hybrid', 'onsite', 'remote'])
target_sector = st.text_input("State your target sector: ")

if st.button("Recommended company"):
    sample_input = pd.DataFrame([{
    "age": age,
    "skill": "skill",
    "location": "location",
    "skill_level": "skill_level",
    "device": "device",
    "year_of_experience": year_of_experience,
    "project_done": project_done,
    "work_type": "work_type",
    "target_sector": "target_sector"
    }])
    sample_input['age'] = sample_input['age'].st.lower()
    sample_input['skill'] = sample_input['skill'].st.lower()
    sample_input['location'] = sample_input['location'].st.lower()
    sample_input['skill_level'] = sample_input['skill_level'].st.lower()
    sample_input['device'] = sample_input['device'].st.lower()
    sample_input['year_of_experience'] = sample_input['year_of_experience'].st.lower()
    sample_input['project_done'] = sample_input['project_done'].st.lower()
    sample_input['work_type'] = sample_input['work_type'].st.lower()
    sample_input['target_sector'] = sample_input['target_sector'].st.lower()

    converted = encoder.transform(sample_input)
    make_recommendation = model.predict(converted)
    st.success(f"\nRecommended Company:", make_recommendation[0])

