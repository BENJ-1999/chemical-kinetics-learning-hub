import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# PAGE SETUP
# ---------------------------------------------------------

st.set_page_config(
    page_title="Chemical Kinetics Learning App",
    page_icon="⚗️",
    layout="wide"
)

# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

st.sidebar.title("Topics")

topic = st.sidebar.radio(
    "Choose a topic:",
    [
        "Welcome",
        "Reaction Rate",
        "Factors Affecting Reaction Rate",
        "Rate Laws",
        "Order of Reaction",
        "Integrated Rate Laws",
        "Arrhenius Equation",
        "Collision Theory",
        "Catalysts",
        "Reaction Mechanisms"
    ]
)

# ---------------------------------------------------------
# WELCOME
# ---------------------------------------------------------

if topic == "Welcome":

    st.title("Welcome")

    st.header("What is Chemical Kinetics?")

    st.write(
        "Chemical kinetics is the study of:"
    )

    st.markdown("""
    - how fast chemical reactions occur
    - the factors that affect reaction rates
    - how reaction rates can be measured
    - how temperature affects reaction rates
    - how catalysts affect reactions
    - how reaction mechanisms can be investigated
    """)

    st.info(
        "Use the Topics menu on the left to explore Chemical Kinetics."
    )


# ---------------------------------------------------------
# REACTION RATE
# ---------------------------------------------------------

elif topic == "Reaction Rate":

    st.title("Reaction Rate")

    st.write(
        "Reaction rate describes how quickly the concentration of a "
        "reactant or product changes during a chemical reaction."
    )

    # -----------------------------------------------------
    # SECTION 1
    # -----------------------------------------------------

    st.header("1. What is reaction rate?")

    st.write(
        "For a reactant, the concentration decreases as the reaction "
        "proceeds. For a product, the concentration increases."
    )

    st.latex(
        r"\text{Rate} = -\frac{\Delta[\text{Reactant}]}{\Delta t}"
    )

    st.write(
        "The negative sign is used for a reactant because its "
        "concentration decreases with time."
    )

    st.latex(
        r"\text{Rate} = \frac{\Delta[\text{Product}]}{\Delta t}"
    )

    st.write(
        "For a product, the concentration increases, so no negative "
        "sign is required."
    )

    st.info(
        "Typical units for reaction rate are mol L⁻¹ s⁻¹."
    )

    # -----------------------------------------------------
    # SECTION 2
    # -----------------------------------------------------

    st.header("2. Average Reaction Rate")

    st.write(
        "Average reaction rate measures the change in concentration "
        "over a particular time interval."
    )

    st.latex(
        r"\text{Average rate} =
        -\frac{[\text{Reactant}]_2-[\text{Reactant}]_1}
        {t_2-t_1}"
    )

    st.write("### Example")

    st.write(
        "Suppose the concentration of a reactant decreases from "
        "0.80 mol L⁻¹ to 0.50 mol L⁻¹ over 30 seconds."
    )

    initial_conc = 0.80
    final_conc = 0.50
    time = 30

    rate = -(final_conc - initial_conc) / time

    st.success(
        f"Average reaction rate = {rate:.3f} mol L⁻¹ s⁻¹"
    )

    # -----------------------------------------------------
    # SECTION 3
    # -----------------------------------------------------

    st.header("3. Interactive Reaction Rate")

    st.write(
        "Use the controls below to investigate how the concentration "
        "of a reactant changes with time."
    )

    col1, col2 = st.columns(2)

    with col1:
        initial_concentration = st.slider(
            "Initial concentration (mol L⁻¹)",
            min_value=0.10,
            max_value=2.00,
            value=1.00,
            step=0.10
        )

    with col2:
        rate_constant = st.slider(
            "Reaction rate constant (s⁻¹)",
            min_value=0.01,
            max_value=0.20,
            value=0.05,
            step=0.01
        )

    # Time values
    t = np.linspace(0, 60, 200)

    # Simple first-order concentration model
    concentration = initial_concentration * np.exp(
        -rate_constant * t
    )

    # -----------------------------------------------------
    # GRAPH
    # -----------------------------------------------------

    fig, ax = plt.subplots()

    ax.plot(t, concentration)

    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Reactant concentration (mol L⁻¹)")
    ax.set_title("Reactant Concentration vs Time")

    ax.grid(True)

    st.pyplot(fig)

    st.write(
        "Notice how increasing the rate constant causes the reactant "
        "concentration to decrease more rapidly."
    )

    # -----------------------------------------------------
    # SECTION 4
    # -----------------------------------------------------

    st.header("4. What does the graph tell us?")

    st.markdown("""
    As the reaction proceeds:

    - the reactant concentration decreases
    - the reaction is initially faster
    - the rate becomes slower as the reaction proceeds
    - the slope of the concentration–time graph represents the rate
    """)

    st.info(
        "The steeper the concentration–time curve, the greater the "
        "reaction rate at that point."
    )

    # -----------------------------------------------------
    # SECTION 5
    # -----------------------------------------------------

    st.header("5. Check Your Understanding")

    question = st.radio(
        "A reaction consumes a reactant. Which statement is correct?",
        [
            "The reactant concentration increases with time.",
            "The reactant concentration decreases with time.",
            "The reactant concentration always remains constant.",
            "The reactant concentration immediately becomes zero."
        ]
    )

    if st.button("Check Answer"):

        if question == "The reactant concentration decreases with time.":

            st.success(
                "Correct! As the reactant is consumed, its concentration "
                "decreases as the reaction proceeds."
            )

        else:

            st.error(
                "Not quite. A reactant is consumed during a reaction, "
                "so its concentration generally decreases with time."
            )

    # -----------------------------------------------------
    # SUMMARY
    # -----------------------------------------------------

    st.header("Key Points")

    st.markdown("""
    **Reaction rate tells us how quickly a reaction occurs.**

    Remember:

    1. Reactants are consumed, so their concentrations decrease.
    2. Products are formed, so their concentrations increase.
    3. Reaction rate can be calculated from concentration changes.
    4. The slope of a concentration–time graph represents reaction rate.
    5. Reaction rate generally changes as a reaction proceeds.
    """)


# ---------------------------------------------------------
# OTHER TOPICS — TEMPORARY PLACEHOLDERS
# ---------------------------------------------------------

else:

    st.title(topic)

    st.info(
        "This section is currently being developed. "
        "More interactive activities will be added soon."
    )
