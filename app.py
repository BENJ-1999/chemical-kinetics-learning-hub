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
        "Chemical kinetics is the study of how quickly chemical "
        "reactions occur and the factors that influence reaction rates."
    )

    st.markdown("""
    Chemical kinetics helps us understand:

    - how fast chemical reactions occur
    - how reaction rates are measured
    - how concentration changes during a reaction
    - how temperature affects reaction rates
    - how catalysts affect reaction rates
    - how reaction mechanisms can be investigated
    """)

    st.info(
        "Use the Topics menu on the left to explore Chemical Kinetics."
    )


# =========================================================
# REACTION RATE
# =========================================================

elif topic == "Reaction Rate":

    st.title("Reaction Rate")

    st.write(
        "Reaction rate describes how quickly the concentration of "
        "reactants or products changes as a chemical reaction occurs."
    )

    # =====================================================
    # SECTION 1 — COLLISION THEORY
    # =====================================================

    st.header("1. Collision Theory")

    st.write(
        "Collision theory provides a molecular explanation for why "
        "chemical reactions occur at different rates."
    )

    st.subheader("What is a particle?")

    st.write(
        "In collision theory, the term **particle** refers to the "
        "individual chemical species involved in a reaction. Depending "
        "on the reaction, these particles may be atoms, molecules, or ions."
    )

    st.write(
        "For a molecular reaction, it is often useful to refer to these "
        "particles specifically as **reactant molecules**."
    )

    st.subheader("Collisions between reactant molecules")

    st.write(
        "For a chemical reaction to occur, reactant particles must collide. "
        "However, not every collision results in a reaction."
    )

    st.markdown("""
    For a collision to result in a reaction, the reactant particles must:

    1. collide with **sufficient energy**
    2. have the **correct orientation**
    """)

    st.subheader("Activation Energy")

    st.write(
        "For a chemical reaction to occur, reactant particles must collide "
        "with sufficient energy. The **minimum energy required for a "
        "collision to result in a reaction is called the activation energy**, "
        "represented by \(E_a\)."
    )

    st.latex(r"E_a = \text{activation energy}")

    st.write(
        "A collision must have energy equal to or greater than \(E_a\) "
        "for the particles to have enough energy to react."
    )

    st.subheader("Correct orientation")

    st.write(
        "The reactant particles must also collide with an orientation that "
        "allows the appropriate bonds to break and form."
    )

    st.write(
        "Therefore, a collision with sufficient energy will not necessarily "
        "produce a reaction if the particles have the wrong orientation."
    )

    st.subheader("Effective collisions")

    st.write(
        "A collision that has sufficient energy to overcome \(E_a\) and "
        "occurs with the correct orientation is called an **effective collision**."
    )

    st.success(
        "Effective collision = sufficient energy + correct orientation"
    )

    # -----------------------------------------------------
    # COLLISION THEORY SIMULATION
    # -----------------------------------------------------

    st.subheader("Interactive Collision Simulation")

    st.write(
        "Adjust the controls to explore how collision energy and "
        "orientation affect whether a collision is effective."
    )

    col1, col2 = st.columns(2)

    with col1:

        collision_energy = st.slider(
            "Collision energy",
            min_value=20,
            max_value=120,
            value=70,
            step=5
        )

    with col2:

        orientation = st.slider(
            "Orientation suitability",
            min_value=0,
            max_value=100,
            value=70,
            step=5
        )

    activation_energy = 60

    if collision_energy >= activation_energy and orientation >= 60:
        collision_result = "Effective collision"
        result_message = (
            "The collision has sufficient energy to overcome "
            "the activation energy and a suitable orientation."
        )
    elif collision_energy < activation_energy:
        collision_result = "Insufficient energy"
        result_message = (
            "The collision does not have enough energy to overcome "
            "the activation energy."
        )
    else:
        collision_result = "Incorrect orientation"
        result_message = (
            "The particles have sufficient energy, but their orientation "
            "is not suitable for the reaction."
        )

    sim_col1, sim_col2 = st.columns([1, 1])

    with sim_col1:

        fig_collision, ax_collision = plt.subplots(figsize=(5, 4))

        # Reactant molecules
        molecule_positions = np.array([
            [0.25, 0.70],
            [0.38, 0.70],
            [0.62, 0.30],
            [0.75, 0.30]
        ])

        for x, y in molecule_positions:
            circle = plt.Circle(
                (x, y),
                0.045,
                fill=False,
                linewidth=2
            )
            ax_collision.add_patch(circle)

        # Motion arrows
        ax_collision.arrow(
            0.25, 0.70,
            0.09, 0,
            head_width=0.025,
            head_length=0.025,
            length_includes_head=True
        )

        ax_collision.arrow(
            0.75, 0.30,
            -0.09, 0,
            head_width=0.025,
            head_length=0.025,
            length_includes_head=True
        )

        ax_collision.set_xlim(0, 1)
        ax_collision.set_ylim(0, 1)
        ax_collision.set_aspect("equal")
        ax_collision.set_xticks([])
        ax_collision.set_yticks([])
        ax_collision.set_title("Reactant molecules approaching")

        st.pyplot(fig_collision)

    with sim_col2:

        st.metric(
            "Activation energy, Ea",
            f"{activation_energy} energy units"
        )

        st.metric(
            "Collision energy",
            f"{collision_energy} energy units"
        )

        st.metric(
            "Orientation suitability",
            f"{orientation}%"
        )

        if collision_result == "Effective collision":
            st.success(collision_result)
        elif collision_result == "Insufficient energy":
            st.warning(collision_result)
        else:
            st.warning(collision_result)

        st.write(result_message)

    st.info(
        "The simulation is a conceptual model. In a real reaction, "
        "molecules have a distribution of energies and orientations."
    )

    # =====================================================
    # SECTION 2 — WHAT IS THE RATE OF A REACTION?
    # =====================================================

    st.header("2. What Is the Rate of a Reaction?")

    st.write(
        "Reaction rate describes how quickly the concentration of a "
        "reactant decreases or the concentration of a product increases "
        "as a reaction proceeds."
    )

    st.subheader("A simple reaction")

    st.latex(r"\mathrm{A \rightarrow B}")

    st.write(
        "As the reaction proceeds, reactant A is consumed and product B "
        "is formed."
    )

    st.write(
        "Therefore, the concentration of A decreases with time, while "
        "the concentration of B increases with time."
    )

    st.info(
        "Reaction rate is commonly expressed in units of "
        "mol L⁻¹ s⁻¹."
    )

    # -----------------------------------------------------
    # CONCENTRATION-TIME GRAPH
    # -----------------------------------------------------

    st.subheader("Concentration changes with time")

    time_data = np.array([0, 10, 20, 30, 40, 50, 60])
    reactant_data = np.array([
        1.00, 0.80, 0.65, 0.50, 0.38, 0.28, 0.20
    ])
    product_data = np.array([
        0.00, 0.20, 0.35, 0.50, 0.62, 0.72, 0.80
    ])

    fig_conc, ax_conc = plt.subplots(figsize=(8, 5))

    ax_conc.plot(
        time_data,
        reactant_data,
        marker="o",
        label="Reactant A"
    )

    ax_conc.plot(
        time_data,
        product_data,
        marker="o",
        label="Product B"
    )

    ax_conc.set_xlabel("Time (s)")
    ax_conc.set_ylabel("Concentration (mol L⁻¹)")
    ax_conc.set_title("Concentration of Reactant and Product vs Time")
    ax_conc.legend()
    ax_conc.grid(True)

    st.pyplot(fig_conc)

    st.write(
        "The decreasing curve represents the reactant being consumed. "
        "The increasing curve represents the product being formed."
    )

    # =====================================================
    # AVERAGE RATE
    # =====================================================

    st.subheader("Average Reaction Rate")

    st.write(
        "The average reaction rate describes the change in concentration "
        "over a particular time interval."
    )

    st.write(
        "For a reactant, the rate is based on the **absolute value of the "
        "change in concentration** over the time interval. Because the "
        "reactant concentration decreases, the conventional rate equation "
        "includes a negative sign."
    )

    st.latex(
        r"\text{Average rate}"
        r"=-\frac{\Delta[\mathrm{A}]}{\Delta t}"
    )

    st.write(
        "The change in concentration between two times can be written using "
        "the concentrations at \(t_1\) and \(t_2\):"
    )

    st.latex(
        r"\Delta[\mathrm{A}]"
        r"=[\mathrm{A}]_{t_2}-[\mathrm{A}]_{t_1}"
    )

    st.latex(
        r"\Delta t=t_2-t_1"
    )

    st.write(
        "Therefore, the average rate can be written directly in terms of "
        "the concentrations at \(t_1\) and \(t_2\):"
    )

    st.latex(
        r"\boxed{"
        r"\text{Average rate}"
        r"=-\frac{[\mathrm{A}]_{t_2}-[\mathrm{A}]_{t_1}}"
        r"{t_2-t_1}"
        r"}"
    )

    st.write(
        "For a product, whose concentration increases as the reaction "
        "proceeds, the average rate is:"
    )

    st.latex(
        r"\boxed{"
        r"\text{Average rate}"
        r"=\frac{\Delta[\mathrm{B}]}{\Delta t}"
        r"}"
    )

    # =====================================================
    # WORKED EXAMPLE
    # =====================================================

    st.subheader("Worked Example")

    st.write(
        "The concentration of reactant A changes from "
        "0.80 mol L⁻¹ at 10 s to 0.50 mol L⁻¹ at 30 s."
    )

    st.markdown("**Given:**")

    st.latex(
        r"[\mathrm{A}]_{t_1}=0.80\ \mathrm{mol\,L^{-1}}"
    )

    st.latex(
        r"[\mathrm{A}]_{t_2}=0.50\ \mathrm{mol\,L^{-1}}"
    )

    st.latex(r"t_1=10\ \mathrm{s}")

    st.latex(r"t_2=30\ \mathrm{s}")

    st.write("**Step 1: Calculate the change in concentration**")

    st.latex(
        r"\Delta[\mathrm{A}]"
        r"=0.50-0.80"
        r"=-0.30\ \mathrm{mol\,L^{-1}}"
    )

    st.write("**Step 2: Calculate the change in time**")

    st.latex(
        r"\Delta t=30-10=20\ \mathrm{s}"
    )

    st.write("**Step 3: Calculate the average rate**")

    st.latex(
        r"\text{Average rate}"
        r"=-\frac{-0.30}{20}"
        r"=0.015\ \mathrm{mol\,L^{-1}\,s^{-1}}"
    )

    st.success(
        "Average reaction rate = 0.015 mol L⁻¹ s⁻¹"
    )

    # =====================================================
    # INTERACTIVE AVERAGE RATE
    # =====================================================

    st.subheader("Interactive Average Rate")

    st.write(
        "Select two points to investigate how the average reaction rate "
        "changes when the concentration interval or time interval changes."
    )

    col1, col2 = st.columns(2)

    with col1:

        st.write("**Initial point**")

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

        st.write("**Later point**")

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

        st.write("### Your calculated values")

        result_col1, result_col2, result_col3 = st.columns(3)

        with result_col1:

            st.metric(
                "Change in concentration",
                f"{delta_concentration:.3f} mol L⁻¹"
            )

        with result_col2:

            st.metric(
                "Change in time",
                f"{delta_time:.1f} s"
            )

        with result_col3:

            st.metric(
                "Average rate",
                f"{average_rate:.4f} mol L⁻¹ s⁻¹"
            )

        st.latex(
            r"\text{Average rate}"
            r"=-\frac{[\mathrm{A}]_{t_2}-[\mathrm{A}]_{t_1}}"
            r"{t_2-t_1}"
        )

        # -------------------------------------------------
        # INTERACTIVE GRAPH
        # -------------------------------------------------

        graph_time = np.array([t1, t2])
        graph_concentration = np.array(
            [concentration_t1, concentration_t2]
        )

        fig_rate, ax_rate = plt.subplots(figsize=(8, 5))

        ax_rate.plot(
            graph_time,
            graph_concentration,
            marker="o"
        )

        ax_rate.plot(
            graph_time,
            graph_concentration,
            linestyle="--"
        )

        ax_rate.set_xlabel("Time (s)")
        ax_rate.set_ylabel("Reactant concentration (mol L⁻¹)")
        ax_rate.set_title("Average Rate Between Two Selected Points")
        ax_rate.grid(True)

        st.pyplot(fig_rate)

        st.write(
            "The two selected points define the time interval over which "
            "the average reaction rate is calculated."
        )

    # =====================================================
    # INSTANTANEOUS RATE
    # =====================================================

    st.subheader("Instantaneous Reaction Rate")

    st.write(
        "The average reaction rate describes the rate over a particular "
        "time interval. However, the reaction rate usually changes as "
        "the reaction proceeds."
    )

    st.write(
        "The **instantaneous reaction rate** is the reaction rate at "
        "a particular instant in time."
    )

    st.write(
        "On a concentration–time graph, the instantaneous rate is "
        "determined from the **slope of the tangent to the curve** "
        "at that particular time."
    )

    st.latex(
        r"\boxed{"
        r"\text{rate}=-\frac{d[\mathrm{A}]}{dt}"
        r"}"
    )

    st.write(
        "For a product:"
    )

    st.latex(
        r"\boxed{"
        r"\text{rate}=\frac{d[\mathrm{B}]}{dt}"
        r"}"
    )

    # -----------------------------------------------------
    # TANGENT SIMULATION
    # -----------------------------------------------------

    st.subheader("Interactive Tangent to the Curve")

    tangent_time = st.slider(
        "Choose a time to examine the instantaneous rate (s)",
        min_value=0.0,
        max_value=60.0,
        value=30.0,
        step=1.0
    )

    # Smooth model for demonstration
    smooth_time = np.linspace(0, 60, 300)

    # Exponential-like reactant decay
    smooth_reactant = np.exp(-smooth_time / 35)

    # Numerical derivative
    derivative = np.gradient(
        smooth_reactant,
        smooth_time
    )

    tangent_index = np.argmin(
        np.abs(smooth_time - tangent_time)
    )

    tangent_concentration = smooth_reactant[tangent_index]
    tangent_slope = derivative[tangent_index]

    # Tangent line
    tangent_line = (
        tangent_concentration
        + tangent_slope * (smooth_time - tangent_time)
    )

    fig_tangent, ax_tangent = plt.subplots(figsize=(8, 5))

    ax_tangent.plot(
        smooth_time,
        smooth_reactant,
        label="Reactant concentration"
    )

    ax_tangent.plot(
        smooth_time,
        tangent_line,
        linestyle="--",
        label="Tangent"
    )

    ax_tangent.plot(
        tangent_time,
        tangent_concentration,
        marker="o",
        markersize=8
    )

    ax_tangent.set_xlabel("Time (s)")
    ax_tangent.set_ylabel("Reactant concentration (relative units)")
    ax_tangent.set_title(
        "Instantaneous Rate from the Tangent"
    )
    ax_tangent.legend()
    ax_tangent.grid(True)

    st.pyplot(fig_tangent)

    st.info(
        f"At t = {tangent_time:.0f} s, the tangent represents the "
        "instantaneous rate at that particular moment."
    )

    # =====================================================
    # INITIAL RATE
    # =====================================================

    st.subheader("Initial Reaction Rate")

    st.write(
        "The **initial rate** is the instantaneous reaction rate "
        "at the beginning of the reaction, when \(t=0\)."
    )

    st.latex(
        r"\boxed{"
        r"\text{Initial rate}"
        r"=-\left.\frac{d[\mathrm{A}]}{dt}\right|_{t=0}"
        r"}"
    )

    st.write(
        "Initial rates are particularly useful when comparing the "
        "effect of changing experimental conditions on a reaction."
    )

    # =====================================================
    # STOICHIOMETRIC RATE
    # =====================================================

    st.subheader("Reaction Rate and Stoichiometric Coefficients")

    st.write(
        "For a reaction involving several reactants and products, "
        "the rate can be expressed in terms of the concentration "
        "change of each species."
    )

    st.latex(
        r"\mathrm{aA+bB\rightarrow cC+dD}"
    )

    st.write(
        "The stoichiometric coefficients are used to ensure that the "
        "same reaction rate is obtained regardless of which species "
        "is used to describe the rate."
    )

    st.latex(
        r"\boxed{"
        r"\text{rate}"
        r"="
        r"-\frac{1}{a}\frac{d[\mathrm{A}]}{dt}"
        r"="
        r"-\frac{1}{b}\frac{d[\mathrm{B}]}{dt}"
        r"="
        r"\frac{1}{c}\frac{d[\mathrm{C}]}{dt}"
        r"="
        r"\frac{1}{d}\frac{d[\mathrm{D}]}{dt}"
        r"}"
    )

    st.write(
        "The negative signs are used for reactants because their "
        "concentrations decrease with time. Products have positive "
        "signs because their concentrations increase with time."
    )

    st.subheader("Example")

    st.latex(
        r"\mathrm{2A+B\rightarrow3C}"
    )

    st.latex(
        r"\text{rate}"
        r"=-\frac{1}{2}\frac{d[\mathrm{A}]}{dt}"
        r"=-\frac{d[\mathrm{B}]}{dt}"
        r"=\frac{1}{3}\frac{d[\mathrm{C}]}{dt}"
    )

    st.info(
        "The stoichiometric coefficients connect the rates of "
        "consumption of reactants with the rate of formation of products."
    )

    # =====================================================
    # CHECK YOUR UNDERSTANDING
    # =====================================================

    st.header("Check Your Understanding")

    question1 = st.radio(
        "1. Which collision is most likely to result in a reaction?",
        [
            "A collision with low energy and the correct orientation",
            "A collision with sufficient energy but the wrong orientation",
            "A collision with sufficient energy and the correct orientation",
            "Any collision between reactant molecules"
        ],
        key="collision_question"
    )

    if st.button("Check Collision Answer"):

        if question1 == (
            "A collision with sufficient energy and the correct orientation"
        ):

            st.success(
                "Correct! An effective collision requires sufficient "
                "energy to overcome Ea and the correct orientation."
            )

        else:

            st.error(
                "Not quite. An effective collision requires both "
                "sufficient energy and the correct orientation."
            )

    question2 = st.radio(
        "2. What does average reaction rate describe?",
        [
            "The rate at exactly one instant",
            "The change in concentration over a time interval",
            "Only the concentration of products",
            "The activation energy of the reaction"
        ],
        key="average_rate_question"
    )

    if st.button("Check Average Rate Answer"):

        if question2 == (
            "The change in concentration over a time interval"
        ):

            st.success(
                "Correct! Average rate describes the change in "
                "concentration over a particular time interval."
            )

        else:

            st.error(
                "Not quite. Average rate describes the change in "
                "concentration over a time interval."
            )

    question3 = st.radio(
        "3. What does the slope of a concentration–time curve represent?",
        [
            "The concentration",
            "The activation energy",
            "The reaction rate",
            "The stoichiometric coefficient"
        ],
        key="slope_question"
    )

    if st.button("Check Slope Answer"):

        if question3 == "The reaction rate":

            st.success(
                "Correct! The slope of a concentration–time curve "
                "is related to the reaction rate."
            )

        else:

            st.error(
                "Not quite. The slope of a concentration–time curve "
                "represents the rate of concentration change."
            )

    # =====================================================
    # KEY POINTS
    # =====================================================

    st.header("Key Points")

    st.markdown("""
    **Reaction rate tells us how quickly a reaction occurs.**

    Remember:

    1. Reactant particles must collide for a reaction to occur.
    2. An effective collision requires sufficient energy and the correct orientation.
    3. **Activation energy, \(E_a\), is the minimum energy required for a collision to result in a reaction.**
    4. Reaction rate describes how concentration changes with time.
    5. Reactant concentrations generally decrease as a reaction proceeds.
    6. Product concentrations generally increase as a reaction proceeds.
    7. Average rate describes concentration change over a time interval.
    8. Instantaneous rate describes the rate at a particular instant.
    9. Initial rate is the instantaneous rate at \(t=0\).
    10. Stoichiometric coefficients relate the rates of consumption and formation of different species.
    """)


# =========================================================
# FACTORS AFFECTING REACTION RATE
# =========================================================

elif topic == "Factors Affecting Reaction Rate":

    st.title("Factors Affecting Reaction Rate")

    st.write(
        "Several factors can affect how quickly a chemical reaction occurs. "
        "These factors influence the frequency of collisions and/or the "
        "fraction of collisions that are effective."
    )

    # -----------------------------------------------------
    # CONCENTRATION
    # -----------------------------------------------------

    st.header("1. Concentration")

    st.write(
        "Increasing the concentration of reactants increases the number "
        "of reactant particles in a given volume."
    )

    st.write(
        "With more particles present in the same volume, collisions occur "
        "more frequently. This increases the number of effective collisions "
        "per unit time and generally increases the reaction rate."
    )

    concentration_level = st.slider(
        "Reactant concentration",
        min_value=1,
        max_value=10,
        value=5,
        key="concentration_factor"
    )

    st.metric(
        "Relative particle concentration",
        concentration_level
    )

    # -----------------------------------------------------
    # TEMPERATURE
    # -----------------------------------------------------

    st.header("2. Temperature")

    st.write(
        "Increasing temperature increases the average kinetic energy of "
        "the particles."
    )

    st.write(
        "As temperature increases, particles move faster and collisions "
        "occur more frequently. More importantly, a greater fraction of "
        "particles have enough energy to overcome the activation energy, "
        "\(E_a\). Therefore, the number of effective collisions increases."
    )

    temperature = st.slider(
        "Temperature (°C)",
        min_value=10,
        max_value=100,
        value=25,
        step=5,
        key="temperature_factor"
    )

    fraction_above_ea = min(
        95,
        max(
            5,
            int(
                10
                + (temperature - 10) * 0.9
            )
        )
    )

    st.metric(
        "Conceptual fraction with energy ≥ Ea",
        f"{fraction_above_ea}%"
    )

    # -----------------------------------------------------
    # SURFACE AREA
    # -----------------------------------------------------

    st.header("3. Surface Area")

    st.write(
        "For reactions involving a solid, increasing the surface area "
        "exposes more particles at the surface where collisions can occur."
    )

    surface_area = st.slider(
        "Relative surface area",
        min_value=1,
        max_value=10,
        value=5,
        key="surface_factor"
    )

    st.metric(
        "Relative exposed surface",
        surface_area
    )

    st.info(
        "A powdered solid generally has a greater exposed surface area "
        "than the same amount of solid in a single large piece."
    )

    # -----------------------------------------------------
    # CATALYST
    # -----------------------------------------------------

    st.header("4. Catalyst")

    st.write(
        "A catalyst increases the reaction rate by providing an "
        "alternative reaction pathway with a lower activation energy."
    )

    st.latex(
        r"E_{a,\mathrm{catalysed}} < E_{a,\mathrm{uncatalysed}}"
    )

    st.write(
        "Because the activation energy is lower, a greater fraction of "
        "collisions can have sufficient energy to result in reaction."
    )

    st.write(
        "A catalyst is not consumed overall in the reaction and does not "
        "change the overall enthalpy change of the reaction."
    )

    catalyst = st.checkbox(
        "Add catalyst",
        value=False,
        key="catalyst_factor"
    )

    if catalyst:

        st.success(
            "Catalyst present: the alternative pathway has a lower activation energy."
        )

    else:

        st.info(
            "No catalyst: the reaction follows the uncatalysed pathway."
        )

    # -----------------------------------------------------
    # SUMMARY
    # -----------------------------------------------------

    st.header("Summary")

    st.markdown("""
    | Factor | Effect on reaction rate |
    |---|---|
    | **Concentration** | More frequent collisions |
    | **Temperature** | More particles have energy ≥ \(E_a\) |
    | **Surface area** | More exposed particles available for collisions |
    | **Catalyst** | Provides an alternative pathway with lower \(E_a\) |
    """)


# =========================================================
# OTHER TOPICS — TEMPORARY PLACEHOLDERS
# =========================================================

else:

    st.title(topic)

    st.info(
        "This section is currently being developed. "
        "More interactive activities will be added soon."
    )
