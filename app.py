import streamlit as st

st.set_page_config(
    page_title="Chemical Kinetics Learning Hub",
    page_icon="🧪",
    layout="wide"
)

st.title("🧪 Chemical Kinetics Learning Hub")

st.write(
    "An interactive learning app for understanding the principles "
    "of chemical kinetics."
)

st.header("Welcome!")

st.markdown("""
### What is Chemical Kinetics?

Chemical kinetics is the study of:

- how fast chemical reactions occur
- the factors that affect reaction rates
- how reaction rates can be measured
- how temperature affects reaction rates
- how catalysts affect reactions
- how reaction mechanisms can be investigated
""")

st.info("More interactive chemistry activities will be added soon.")

st.sidebar.title("Topics")

topic = st.sidebar.selectbox(
    "Choose a topic:",
    [
        "Home",
        "Reaction Rate",
        "Collision Theory",
        "Factors Affecting Rate",
        "Activation Energy",
        "Arrhenius Equation",
        "Catalysts",
        "Enzyme Kinetics",
        "Michaelis-Menten Kinetics"
    ]
)

if topic != "Home":
    st.subheader(topic)
    st.write("This section is currently being developed.")
