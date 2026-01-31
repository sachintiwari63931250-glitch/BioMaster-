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
elif menu == "📷 Photo Doubt Solver":
    st.header("Photo Doubt Solver")
    img = st.file_uploader(
        "Upload image (JPG / PNG)",
        type=["jpg", "png", "jpeg"]
    )
    if img:
        st.image(img, caption="Uploaded Image", use_column_width=True)
        st.success("Image uploaded successfully ✅")
elif menu == "📝 MCQs":
    st.header("MCQs Practice")

    q1 = st.radio(
        "Q1. Powerhouse of the cell is?",
        ["Nucleus", "Mitochondria", "Ribosome", "Golgi body"]
    )

    if st.button("Check Answer"):
        if q1 == "Mitochondria":
            st.success("Correct ✅")
        else:
            st.error("Wrong ❌ Correct answer: Mitochondria")
