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

    st.header("1. What is Reaction Rate?")

    st.write(
        "Reaction rate tells us how quickly the concentration of a "
        "reactant or product changes as a reaction proceeds."
    )

    st.write(
        "For a reactant, the concentration generally decreases as "
        "the reaction proceeds. For a product, the concentration "
        "generally increases."
    )

    st.info(
        "Reaction rate is commonly expressed in units of "
        "mol L⁻¹ s⁻¹."
    )

    # -----------------------------------------------------
    # SECTION 2
    # -----------------------------------------------------

    st.header("2. Change in Concentration and Time")

    st.write(
        "To calculate a reaction rate, we need to consider how much "
        "the concentration changes over a period of time."
    )

    st.subheader("The Δ symbol")

    st.write(
        "The Greek letter delta, Δ, is used to represent a "
        "**change in a quantity**."
    )

    st.latex(r"\Delta = \text{change in}")

    st.write(
        "Therefore:"
    )

    st.latex(r"\Delta[\text{Reactant}] = \text{change in reactant concentration}")

    st.latex(r"\Delta t = \text{change in time}")

    st.write(
        "A change is calculated by subtracting the initial value "
        "from the final value:"
    )

    st.latex(r"\Delta X = X_2 - X_1")

    st.write(
        "For concentration and time, this becomes:"
    )

    st.latex(
        r"\Delta[\text{Reactant}] "
        r"= [\text{Reactant}]_{t_2} - [\text{Reactant}]_{t_1}"
    )

    st.latex(
        r"\Delta t = t_2 - t_1"
    )

    st.write(
        "Here, the subscripts indicate the values at the two "
        "different times:"
    )

    st.markdown("""
    - \(t_1\) = the initial time
    - \(t_2\) = the later time
    - \([\text{Reactant}]_{t_1}\) = reactant concentration at \(t_1\)
    - \([\text{Reactant}]_{t_2}\) = reactant concentration at \(t_2\)
    """)

    # -----------------------------------------------------
    # SECTION 3
    # -----------------------------------------------------

    st.header("3. Average Reaction Rate")

    st.write(
        "The average reaction rate describes the average change in "
        "concentration over a particular time interval."
    )

    st.subheader("For a reactant")

    st.write(
        "Because the concentration of a reactant decreases as the "
        "reaction proceeds, the change in concentration is normally "
        "negative. A negative sign is therefore included so that "
        "the reaction rate is expressed as a positive quantity."
    )

    st.latex(
        r"\text{Average rate}"
        r" = -\frac{\Delta[\text{Reactant}]}{\Delta t}"
    )

    st.write(
        "Using the definitions of Δ concentration and Δ time, "
        "the equation can also be written as:"
    )

    st.latex(
        r"\text{Average rate}"
        r" = -\frac{[\text{Reactant}]_{t_2}"
        r" - [\text{Reactant}]_{t_1}}"
        r"{t_2 - t_1}"
    )

    st.info(
        "The Δ symbol means 'change in'. It does not mean a single "
        "value; it represents the difference between two values."
    )

    # -----------------------------------------------------
    # SECTION 4
    # -----------------------------------------------------

    st.header("4. Worked Example")

    st.write(
        "The concentration of a reactant changes from "
        "0.80 mol L⁻¹ at 10 s to 0.50 mol L⁻¹ at 30 s."
    )

    st.markdown("""
    **Given:**

    \[
    [\text{Reactant}]_{t_1} = 0.80\ \text{mol L}^{-1}
    \]

    \[
    [\text{Reactant}]_{t_2} = 0.50\ \text{mol L}^{-1}
    \]

    \[
    t_1 = 10\ \text{s}
    \]

    \[
    t_2 = 30\ \text{s}
    \]
    """)

    st.write("### Step 1: Calculate the change in concentration")

    st.latex(
        r"\Delta[\text{Reactant}]"
        r" = 0.50 - 0.80"
        r" = -0.30\ \text{mol L}^{-1}"
    )

    st.write("### Step 2: Calculate the change in time")

    st.latex(
        r"\Delta t = 30 - 10 = 20\ \text{s}"
    )

    st.write("### Step 3: Calculate the average rate")

    st.latex(
        r"\text{Average rate}"
        r" = -\frac{-0.30}{20}"
        r" = 0.015\ \text{mol L}^{-1}\text{s}^{-1}"
    )

    st.success(
        "Average reaction rate = 0.015 mol L⁻¹ s⁻¹"
    )

    # -----------------------------------------------------
    # SECTION 5
    # -----------------------------------------------------

    st.header("5. Concentration–Time Graph")

    st.write(
        "The change in concentration can also be represented "
        "graphically."
    )

    time_data = np.array([0, 10, 20, 30])
    concentration_data = np.array([1.00, 0.80, 0.65, 0.50])

    fig, ax = plt.subplots()

    ax.plot(
        time_data,
        concentration_data,
        marker="o"
    )

    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Reactant concentration (mol L⁻¹)")
    ax.set_title("Reactant Concentration vs Time")

    ax.grid(True)

    st.pyplot(fig)

    st.write(
        "The concentration decreases as time increases because "
        "the reactant is being consumed."
    )

    # -----------------------------------------------------
    # SECTION 6
    # -----------------------------------------------------

    st.header("6. Interactive Average Rate")

    st.write(
        "Use the controls below to investigate how changes in "
        "concentration and time affect the calculated average rate."
    )

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Initial point")

        t1 = st.number_input(
            "Initial time, t₁ (s)",
            min_value=0.0,
            max_value=1000.0,
            value=10.0,
            step=1.0
        )

        concentration_t1 = st.number_input(
            "Reactant concentration at t₁ (mol L⁻¹)",
            min_value=0.01,
            max_value=10.0,
            value=0.80,
            step=0.05
        )

    with col2:

        st.subheader("Later point")

        t2 = st.number_input(
            "Later time, t₂ (s)",
            min_value=0.1,
            max_value=1000.0,
            value=30.0,
            step=1.0
        )

        concentration_t2 = st.number_input(
            "Reactant concentration at t₂ (mol L⁻¹)",
            min_value=0.0,
            max_value=10.0,
            value=0.50,
            step=0.05
        )

    if t2 <= t1:

        st.error(
            "The later time, t₂, must be greater than the initial "
            "time, t₁."
        )

    else:

        delta_concentration = concentration_t2 - concentration_t1
        delta_time = t2 - t1

        average_rate = -delta_concentration / delta_time

        st.subheader("Your calculated values")

        result_col1, result_col2, result_col3 = st.columns(3)

        with result_col1:
            st.metric(
                "Δ concentration",
                f"{delta_concentration:.3f} mol L⁻¹"
            )

        with result_col2:
            st.metric(
                "Δ time",
                f"{delta_time:.1f} s"
            )

        with result_col3:
            st.metric(
                "Average rate",
                f"{average_rate:.4f} mol L⁻¹ s⁻¹"
            )

        st.latex(
            r"\text{Average rate}"
            r" = -\frac{[\text{Reactant}]_{t_2}"
            r" - [\text{Reactant}]_{t_1}}"
            r"{t_2-t_1}"
        )

        # -------------------------------------------------
        # INTERACTIVE GRAPH
        # -------------------------------------------------

        graph_time = np.array([t1, t2])
        graph_concentration = np.array(
            [concentration_t1, concentration_t2]
        )

        fig2, ax2 = plt.subplots()

        ax2.plot(
            graph_time,
            graph_concentration,
            marker="o"
        )

        ax2.set_xlabel("Time (s)")
        ax2.set_ylabel("Reactant concentration (mol L⁻¹)")
        ax2.set_title("Change in Reactant Concentration")

        ax2.grid(True)

        st.pyplot(fig2)

        st.write(
            "The two selected points define the time interval over "
            "which the average reaction rate is calculated."
        )

    # -----------------------------------------------------
    # SECTION 7
    # -----------------------------------------------------

    st.header("7. Instantaneous Reaction Rate")

    st.write(
        "The average reaction rate describes the rate over a "
        "particular time interval. However, the reaction rate may "
        "change as the reaction proceeds."
    )

    st.write(
        "The **instantaneous reaction rate** is the reaction rate "
        "at a particular instant in time."
    )

    st.write(
        "On a concentration–time graph, the instantaneous rate "
        "is related to the slope of the tangent to the curve "
        "at that point."
    )

    st.info(
        "Average rate considers a time interval. Instantaneous "
        "rate considers the rate at a particular moment."
    )

    # -----------------------------------------------------
    # SECTION 8
    # -----------------------------------------------------

    st.header("8. Check Your Understanding")

    question1 = st.radio(
        "What does the symbol Δ represent?",
        [
            "A final value",
            "A change in a quantity",
            "A reaction rate",
            "A concentration"
        ],
        key="delta_question"
    )

    if st.button("Check Δ Answer"):

        if question1 == "A change in a quantity":

            st.success(
                "Correct! Δ (delta) is used to represent a change "
                "in a quantity."
            )

        else:

            st.error(
                "Not quite. Δ (delta) represents a change in a quantity."
            )

    question2 = st.radio(
        "Which statement correctly describes average reaction rate?",
        [
            "It describes the change in concentration over a time interval.",
            "It is always the same throughout a reaction.",
            "It only applies to products.",
            "It has no units."
        ],
        key="rate_question"
    )

    if st.button("Check Rate Answer"):

        if question2 == (
            "It describes the change in concentration over a time interval."
        ):

            st.success(
                "Correct! Average reaction rate describes the change "
                "in concentration over a particular time interval."
            )

        else:

            st.error(
                "Not quite. Average reaction rate describes the "
                "change in concentration over a time interval."
            )

    # -----------------------------------------------------
    # SUMMARY
    # -----------------------------------------------------

    st.header("Key Points")

    st.markdown("""
    **Reaction rate tells us how quickly a reaction occurs.**

    Remember:

    1. Reaction rate describes how concentration changes with time.
    2. **Δ means 'change in'.**
    3. A change is calculated as final value − initial value.
    4. \(\Delta t = t_2 - t_1\)
    5. For a reactant, concentration generally decreases with time.
    6. The negative sign in the reactant rate equation makes the rate positive.
    7. Average rate describes the rate over a time interval.
    8. Instantaneous rate describes the rate at a particular instant.
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
