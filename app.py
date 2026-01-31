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
import streamlit as st

st.set_page_config(page_title="DoubtBuster NEET", layout="centered")

st.title("📘 DoubtBuster NEET")
st.caption("NEET Biology | Notes • MCQs • PDF • Photo Doubt Solver")

menu = st.radio(
    "Select Feature",
    ["Notes", "MCQs", "PDF Viewer", "Photo Doubt Solver"]
)

if menu == "Notes":
    st.header("Biology Notes")
    st.write("• Cell Biology")
    st.write("• Plant Physiology")
    st.write("• Human Physiology")
elif menu == "MCQs":
    st.header("🧠 Auto MCQ Answer (Class 9–12)")

    q = st.text_area("Enter MCQ Question (English)")

    if st.button("Get Answer"):
        q_lower = q.lower()

        # --- Biology ---
        if "powerhouse" in q_lower:
            st.success("Answer: Mitochondria")
        elif "chlorophyll" in q_lower:
            st.success("Answer: Chloroplast")
        elif "heart" in q_lower and "chambers" in q_lower:
            st.success("Answer: 4")
        elif "photosynthesis" in q_lower:
            st.success("Answer: Chloroplast")
        elif "dna" in q_lower:
            st.success("Answer: Nucleus")

        # --- Physics ---
        elif "unit of force" in q_lower:
            st.success("Answer: Newton")
        elif "speed of light" in q_lower:
            st.success("Answer: 3 × 10⁸ m/s")
        elif "ohm" in q_lower:
            st.success("Answer: Resistance")

        # --- Chemistry ---
        elif "atomic number" in q_lower:
            st.success("Answer: Number of protons")
        elif "ph" in q_lower and "acid" in q_lower:
            st.success("Answer: Less than 7")
        elif "h2o" in q_lower:
            st.success("Answer: Water")

        else:
            st.warning(
                "Answer not found in offline logic.\n"
                "AI integration required for full coverage."
            )
   

elif menu == "PDF Viewer":
    st.header("PDF Viewer")
    st.info("PDF upload feature coming soon")

elif menu == "Photo Doubt Solver":
    st.header("Photo Doubt Solver")
    img = st.file_uploader(
        "Upload image (JPG / PNG)",
        type=["jpg", "png", "jpeg"]
    )
    if img:
        st.image(img, caption="Uploaded Image", use_column_width=True)
        st.success("Image uploaded successfully ✅")       
