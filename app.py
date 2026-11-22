import streamlit as st
from data_handler import load_medicine_data, search_medicine
from llm_handler import explain_medicine

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(page_title="MediGuide AI", page_icon="💊", layout="wide")

# --------------------------------------------------
# CUSTOM STYLING
# --------------------------------------------------

st.markdown(
    """
<style>
    .main-title {
        font-size: 38px;
        font-weight: 750;
        color: #16856B;
    }

    .subtitle {
        color: #777777;
        font-size: 17px;
    }

    .medicine-card {
        background-color: rgba(128,128,128,0.08);
        padding: 18px;
        border-radius: 12px;
        margin-bottom: 12px;
    }

    .disclaimer {
        background-color: rgba(255,165,0,0.10);
        padding: 15px;
        border-radius: 10px;
        font-size: 14px;
    }
</style>
""",
    unsafe_allow_html=True,
)

# --------------------------------------------------
# LOAD DATASET
# --------------------------------------------------


@st.cache_data
def get_dataset():
    return load_medicine_data()


try:
    df = get_dataset()
except Exception as e:
    st.error(f"Unable to load medicine dataset: {e}")
    st.stop()

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown('<div class="main-title">💊 MediGuide AI</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="subtitle">'
    "Understand medicines through AI-powered explanations."
    "</div>",
    unsafe_allow_html=True,
)

st.write("")

st.info(
    "Search for a medicine to understand its composition, "
    "listed uses and commonly reported side effects."
)

# --------------------------------------------------
# SEARCH FORM
# --------------------------------------------------

with st.form("medicine_search_form"):

    medicine_name = st.text_input(
        "Enter medicine name", placeholder="Example: Augmentin 625 Duo Tablet"
    )

    search_button = st.form_submit_button(
        "🔍 Search Medicine", use_container_width=True
    )

# --------------------------------------------------
# SEARCH PROCESSING
# --------------------------------------------------

if search_button:

    if not medicine_name.strip():

        st.warning("Please enter a medicine name.")

        st.session_state.pop("medicine_result", None)
        st.session_state.pop("medicine_suggestions", None)

    else:

        result, suggestions = search_medicine(medicine_name, df)

        st.session_state.pop("medicine_result", None)
        st.session_state.pop("medicine_suggestions", None)

        if result is not None:

            st.session_state["medicine_result"] = result

        elif suggestions:

            st.session_state["medicine_suggestions"] = suggestions

        else:

            st.error(
                "Medicine not found in the dataset. "
                "Please check the spelling or try another name."
            )

# --------------------------------------------------
# HANDLE MULTIPLE MATCHES
# --------------------------------------------------

if "medicine_suggestions" in st.session_state:

    st.subheader("Multiple matches found")

    selected_medicine = st.selectbox(
        "Select the correct medicine:", st.session_state["medicine_suggestions"]
    )

    if st.button("Get Medicine Information"):

        result, _ = search_medicine(selected_medicine, df)

        if result is not None:
            st.session_state["medicine_result"] = result

            del st.session_state["medicine_suggestions"]

            st.rerun()

# --------------------------------------------------
# DISPLAY MEDICINE INFORMATION
# --------------------------------------------------

if "medicine_result" in st.session_state:

    medicine = st.session_state["medicine_result"]

    st.markdown("---")

    st.subheader("💊 Medicine Information")

    st.markdown(f"### {medicine['Medicine Name']}")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("**Composition**")
        st.write(medicine["Composition"])

        st.markdown("**Manufacturer**")
        st.write(medicine["Manufacturer"])

    with col2:

        st.markdown("**Uses (from dataset)**")
        st.write(medicine["Uses"])

        st.markdown("**Listed Side Effects (from dataset)**")
        st.write(medicine["Side_effects"])

    # --------------------------------------------------
    # AI EXPLANATION
    # --------------------------------------------------

    st.markdown("---")

    st.subheader("🤖 AI Medicine Explanation")

    if st.button(
        "Generate Simple Explanation", type="primary", use_container_width=True
    ):

        with st.spinner("MediGuide AI is preparing your explanation..."):

            explanation = explain_medicine(medicine)

        if explanation.startswith("Gemini API Error:"):
            st.error(explanation)

        else:
            st.session_state["ai_explanation"] = explanation
            st.session_state["ai_medicine_name"] = medicine["Medicine Name"]

    if st.session_state.get("ai_medicine_name") == medicine[
        "Medicine Name"
    ] and st.session_state.get("ai_explanation"):

        st.markdown(st.session_state["ai_explanation"])

    # --------------------------------------------------
    # MEDICAL DISCLAIMER
    # --------------------------------------------------

    st.markdown("---")

    st.markdown(
        """
    <div class="disclaimer">
        <strong>Medical Disclaimer</strong><br><br>
        This application provides educational information
        based on a public medicine dataset. The information
        may be incomplete or outdated and does not replace
        professional medical advice. Do not use it to make
        treatment or dosage decisions. Consult a qualified
        healthcare professional.
    </div>
    """,
        unsafe_allow_html=True,
    )

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("---")

st.caption("MediGuide AI | GenAI Mini Project | Problem Statement 58")
