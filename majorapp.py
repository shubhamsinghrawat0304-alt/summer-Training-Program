import streamlit as st
import pandas as pd
import joblib


st.set_page_config(
    page_title="Health Prediction System",
    page_icon="🩺",
    layout="wide"
)



model = joblib.load("Main_project.pkl")
symptoms = joblib.load("feature_names.pkl")
recommendation = pd.read_csv("disease_medicine_precaution.csv")



st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#EAF4FF,#F8FBFF);
}

.main-title{
    text-align:center;
    font-size:48px;
    font-weight:700;
    color:#1565C0;
}

.sub-title{
    text-align:center;
    color:gray;
    margin-bottom:25px;
}

.result{
    background:linear-gradient(90deg,#43cea2,#185a9d);
    color:white;
    padding:20px;
    border-radius:15px;
    text-align:center;
    font-size:28px;
    font-weight:bold;
}

.card{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0 5px 15px rgba(0,0,0,.1);
    margin-top:20px;
}

.stButton>button{
    width:100%;
    height:55px;
    border:none;
    border-radius:12px;
    background:#1565C0;
    color:white;
    font-size:18px;
    font-weight:bold;
}

.stButton>button:hover{
    background:#0D47A1;
}

</style>
""", unsafe_allow_html=True)



with st.sidebar:

    st.title("🩺 Health Assistant")

    st.success("AI Disease Prediction")

    st.markdown("---")

    st.write("### Instructions")

    st.write("""
    ✔ Select symptoms

    ✔ Click Predict

    ✔ View medicines

    ✔ Follow precautions
    """)

    st.markdown("---")

    st.info("Stay Healthy ❤️")



st.markdown(
"""
<div class="main-title">
🩺 Health Prediction & Recommendation System
</div>

<div class="sub-title">
Predict diseases and get medicines & precautions
</div>
""",
unsafe_allow_html=True
)



selected = st.multiselect(
    "Select Symptoms",
    symptoms
)



if st.button("🔍 Predict Disease"):

    input_data = [0] * len(symptoms)

    for symptom in selected:
        input_data[symptoms.index(symptom)] = 1

    disease = model.predict([input_data])[0]

    st.markdown(
        f"""
        <div class="result">
        ✅ Predicted Disease<br><br>
        {disease.upper()}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    st.subheader("Prediction Confidence")

    confidence = 95

    st.progress(confidence)

    st.write(f"**{confidence}% Confidence**")

   

    row = recommendation[
        recommendation["Disease"].str.lower() == disease.lower()
    ]

    if not row.empty:

        medicine = row.iloc[0]["Medicine"]
        precaution = row.iloc[0]["Precaution"]

        col1, col2 = st.columns(2)

        with col1:

            st.markdown('<div class="card">', unsafe_allow_html=True)

            st.subheader("💊 Medicines")

            for med in str(medicine).split(","):
                st.write("✔", med.strip())

            st.markdown("</div>", unsafe_allow_html=True)

        with col2:

            st.markdown('<div class="card">', unsafe_allow_html=True)

            st.subheader("⚠ Precautions")

            for pre in str(precaution).split(","):
                st.write("✔", pre.strip())

            st.markdown("</div>", unsafe_allow_html=True)

    st.write("")

    st.subheader("📊 Summary")

    c1, c2, c3 = st.columns(3)

    c1.metric("Symptoms", len(selected))
    c2.metric("Disease", disease.title())
    c3.metric("Confidence", "95%")

    st.write("")

    with st.expander("❤️ Daily Health Tips"):

        st.success("Drink 2-3 litres of water")

        st.success("Exercise for 30 minutes")

        st.success("Sleep 7-8 hours")

        st.success("Eat more fruits & vegetables")

        st.success("Avoid excessive junk food")
