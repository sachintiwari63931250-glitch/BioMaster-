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
    st.header("📝 Unlimited MCQs Practice")

    if "mcqs" not in st.session_state:
        st.session_state.mcqs = []

    st.subheader("➕ Add New MCQ")

    q = st.text_input("Question")
    opt1 = st.text_input("Option A")
    opt2 = st.text_input("Option B")
    opt3 = st.text_input("Option C")
    opt4 = st.text_input("Option D")
    correct = st.selectbox(
        "Correct Answer",
        ["Option A", "Option B", "Option C", "Option D"]
    )

    if st.button("Add MCQ"):
        if q and opt1 and opt2 and opt3 and opt4:
            st.session_state.mcqs.append({
                "question": q,
                "options": [opt1, opt2, opt3, opt4],
                "answer": {
                    "Option A": opt1,
                    "Option B": opt2,
                    "Option C": opt3,
                    "Option D": opt4
                }[correct]
            })
            st.success("MCQ Added Successfully ✅")
        else:
            st.error("Please fill all fields ❌")

    st.markdown("---")
    st.subheader("📘 Practice MCQs")

    score = 0

    for i, mcq in enumerate(st.session_state.mcqs):
        user_ans = st.radio(
            f"Q{i+1}. {mcq['question']}",
            mcq["options"],
            key=f"mcq_{i}"
        )
        if user_ans == mcq["answer"]:
            score += 1

    if st.session_state.mcqs:
        st.success(f"Score: {score} / {len(st.session_state.mcqs)}")
    else:
        st.info("No MCQs added yet")


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
