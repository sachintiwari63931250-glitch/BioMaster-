import streamlit as st

st.set_page_config(page_title="DoubtBuster NEET", layout="centered")

lang = st.selectbox(
    "🌐 Language / भाषा चुनें",
    ["English", "Hinglish"]
)

if lang == "English":
    st.title("DoubtBuster NEET")
    st.caption("NEET Biology | Notes • MCQs • PDF • Photo Doubt Solver")
    notes = "Biology Notes"
else:
    st.title("DoubtBuster NEET")
    st.caption("NEET Biology | Notes • MCQs • PDF • Photo Doubt Solver")
    notes = "Biology Notes (Hindi + English)"

menu = st.radio(
    "Select Feature",
    ["📘 Notes", "📝 MCQs", "📄 PDF Viewer", "📷 Photo Doubt Solver"]
)

if menu == "📘 Notes":
    st.header(notes)
    st.write("• Cell Biology")
    st.write("• Plant Physiology")
    st.write("• Human Physiology")

elif menu == "📝 MCQs":
    st.header("MCQs Section")
    st.info("MCQs yahan add honge")

elif menu == "📄 PDF Viewer":
    st.header("PDF Viewer")
    st.info("PDF upload option yahan aayega")

elif menu == "📷 Photo Doubt Solver":
    st.header("Photo Doubt Solver")
    st.info("Image upload karke doubt pooch sakte ho")
