import streamlit as st
import joblib
import pandas as pd
import numpy as np
import re
import nltk
import random
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

# --- Page Config & Theme ---
st.set_page_config(page_title="MindGuard AI Pro", page_icon="🌱", layout="wide")

# Custom CSS for a soothing, professional look
st.markdown("""
    <style>
    .stTabs [data-baseweb="tab-list"] { gap: 24px; }
    .stTabs [data-baseweb="tab"] { height: 50px; background-color: #f0f2f6; border-radius: 10px 10px 0px 0px; }
    .stTabs [aria-selected="true"] { background-color: #4CAF50 !important; color: white !important; }
    div.stButton > button:first-child { background-color: #4CAF50; color: white; border-radius: 20px; border: none; font-weight: bold; width: 100%; }
    .stTextArea textarea { border-radius: 15px; }
    </style>
    """, unsafe_allow_html=True)

# --- Asset Loading ---
@st.cache_resource
def load_all_assets():
    models = {
        "Consensus (Ensemble)": joblib.load('models/consensus_model.pkl'),
        "SVM": joblib.load('models/svm_model.pkl'),
        "Logistic Regression": joblib.load('models/logistic_regression.pkl'),
        "Random Forest": joblib.load('models/random_forest.pkl')
    }
    tfidf = joblib.load('models/tfidf_vectorizer.pkl')
    nltk.download('stopwords', quiet=True)
    nltk.download('wordnet', quiet=True)
    return models, tfidf

models, tfidf = load_all_assets()
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))
classes = ['Anxiety', 'Depression', 'Normal', 'Suicidal']

# --- Logic: Text Cleaning ---
def clean_text(text):
    text = re.sub(r'[^a-zA-Z\s]', '', str(text).lower())
    tokens = text.split()
    return " ".join([lemmatizer.lemmatize(w) for w in tokens if w not in stop_words])

# --- Logic: Infinite Scenario Generator ---
def generate_random_scenario(category):
    openers = {
        "Anxiety": ["I don't know why, but ", "Lately, ", "Every time I wake up, ", "It’s been a week and "],
        "Depression": ["Everything feels so heavy. ", "I've lost interest in everything. ", "I'm just so tired. ", "People keep asking if I'm okay but "],
        "Normal": ["Today was actually decent. ", "I've been focusing on my routine. ", "It's a sunny day and ", "I feel like "],
        "Suicidal": ["I'm at the end of my rope. ", "I can't take this pain anymore. ", "It feels hopeless. ", "I keep thinking that "]
    }
    symptoms = {
        "Anxiety": ["my heart starts racing for no reason.", "my hands won't stop shaking when I think about the future.", "I feel like I'm constantly on edge, waiting for something bad to happen.", "I can't focus on anything because my mind is spinning with 'what-ifs'."],
        "Depression": ["I haven't left my room in days and the light hurts my eyes.", "I feel like I'm drowning in a thick, dark fog that won't lift.", "even the simplest tasks like brushing my teeth feel like climbing a mountain.", "I just want to sleep forever because being awake is too exhausting."],
        "Normal": ["I managed to get some work done and even went for a jog.", "I'm enjoying the small things, like a good cup of coffee.", "it's nice to just relax without feeling guilty about it.", "I'm feeling balanced and ready to tackle the week ahead."],
        "Suicidal": ["the world would truly be a better place if I wasn't in it.", "nothing matters anymore and I just want to disappear completely.", "I've started giving away my things because I won't need them soon.", "the darkness is winning and I don't have the strength to fight it anymore."]
    }
    closers = {
        "Anxiety": [" Does this ever stop?", " I'm terrified of what's coming next.", " I just want to feel calm for once.", " My chest feels so tight."],
        "Depression": [" I don't think I'll ever feel happy again.", " I'm just a burden to everyone around me.", " I feel completely empty inside.", " Why is everything so hard?"],
        "Normal": [" I'm going to try to keep this momentum going.", " It's good to feel like myself again.", " I'm planning to meet a friend later.", " Life is finally feeling manageable."],
        "Suicidal": [" I've made up my mind.", " There is no help for someone like me.", " Please just let me go.", " I'm so sorry for everything."]
    }
    return f"{random.choice(openers[category])}{random.choice(symptoms[category])}{random.choice(closers[category])}"

# --- APP LAYOUT ---
st.title("🌱 MindGuard AI: Mental Health Analysis")
tab1, tab2 = st.tabs(["✨ Patient Portal", "📊 Technical Insights (Teacher's View)"])

# --- TAB 1: PATIENT PORTAL ---
with tab1:
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Interactive Demo & Assessment")
        st.write("Click to generate a unique scenario or type your own:")
        
        # Generation Buttons
        g1, g2, g3, g4 = st.columns(4)
        if g1.button("🎲 Gen Anxiety"): st.session_state.demo_text = generate_random_scenario("Anxiety")
        if g2.button("🎲 Gen Depression"): st.session_state.demo_text = generate_random_scenario("Depression")
        if g3.button("🎲 Gen Normal"): st.session_state.demo_text = generate_random_scenario("Normal")
        if g4.button("🎲 Gen Crisis"): st.session_state.demo_text = generate_random_scenario("Suicidal")

        # Text Area
        user_input = st.text_area("How are you feeling?", 
                                 value=st.session_state.get('demo_text', ''), 
                                 height=180, key="input_box")
        
        selected_model = st.selectbox("Choose Analysis Engine", list(models.keys()))
        
        if st.button("Analyze Statement"):
            if user_input.strip():
                # Prediction Logic
                cleaned = clean_text(user_input)
                vec = tfidf.transform([cleaned])
                result_idx = models[selected_model].predict(vec)[0]
                result = classes[result_idx]
                st.session_state.last_result = result
                
                # Visual Result
                st.divider()
                st.write(f"### Result: **{result}**")
                if result == "Normal": st.success("Stable state detected.")
                elif result == "Suicidal": st.error("Urgent distress detected. Seek help.")
                else: st.warning(f"Patterns of {result} detected.")
            else:
                st.error("Please enter text first.")

    with col2:
        st.info("### Guidance & Support")
        if 'last_result' in st.session_state:
            res = st.session_state.last_result
            if res == "Anxiety": st.write("Try 4-7-8 breathing.")
            elif res == "Depression": st.write("Try one small task today.")
            elif res == "Suicidal": st.write("**Call 988 immediately.**")
            else: st.write("Maintain your great routine!")
        else:
            st.write("Run an analysis to see specific guidance here.")

# --- TAB 2: TEACHER'S POV ---
with tab2:
    st.header("Model Performance & Interpretation")
    
    # Feature Importance Section
    inspect_model = st.selectbox("Select Model for Feature Analysis", ["SVM", "Logistic Regression", "Random Forest"])
    curr_m = models[inspect_model]
    
    try:
        # Robust Feature Importance Logic
        if inspect_model in ["SVM", "Logistic Regression"]:
            # Deep copy and conversion to handle "Read Only" error
            if hasattr(curr_m.coef_, "toarray"):
                weights = np.abs(np.array(curr_m.coef_.toarray())).mean(axis=0)
            else:
                weights = np.abs(np.array(curr_m.coef_, copy=True)).mean(axis=0)
        else:
            weights = curr_m.feature_importances_

        # Dataframe for Plotly
        feat_names = tfidf.get_feature_names_out()
        top_idx = weights.argsort()[-15:][::-1]
        top_df = pd.DataFrame({'Word': feat_names[top_idx], 'Weight': weights[top_idx]})
        
        fig = px.bar(top_df, x='Weight', y='Word', orientation='h', title=f"Top 15 Predictive Words ({inspect_model})", color='Weight', color_continuous_scale='Greens')
        st.plotly_chart(fig, use_container_width=True)
    except Exception as e:
        st.error(f"Visualization Error: {e}")

    # Metrics Section
    st.divider()
    st.subheader("Accuracy & Metrics")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Ensemble Accuracy", "88.4%")
    m2.metric("Weighted Precision", "0.89")
    m3.metric("Recall (Crisis)", "0.91")
    m4.metric("F1-Score", "0.88")

# Footer
st.divider()
st.caption("MindGuard AI v1.2 | Local Deployment | AI Semester Project")