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


    st.header("Collision Theory")

    st.markdown("""
    Collision theory provides a molecular explanation for why chemical reactions
    occur at different rates.

    For a chemical reaction to occur, **reactant particles must collide**.
    In collision theory, the term *particle* refers to an individual chemical
    species involved in a reaction. Depending on the reaction, these particles
    may be **atoms, molecules, or ions**.

    However, not every collision results in a reaction.

    For a collision to result in a reaction, the reactant particles must:

    1. collide with **sufficient energy**
    2. have the **correct orientation**
    """)

    st.markdown("---")

    st.markdown("### Sufficient Energy")

    st.markdown("""
    The colliding particles must have enough energy for the reaction to occur.
    The minimum energy required for a collision to result in a reaction is called
    the **activation energy, \(E_a\)**.
    """)

    st.image(
    "collision_theory_Ea_diagram.png",
    width=525
)

    st.markdown("""
    In the energy profile above, \(E_a\) represents the energy barrier that the
    reactant particles must overcome for the reaction to occur.
    """)

    st.markdown("---")

    st.markdown("### Correct Orientation")

    st.markdown("""
    Having sufficient energy is not enough. The reactant molecules must also
    collide with the **correct orientation**.

    This means that the appropriate parts of the molecules must be positioned
    correctly during the collision so that the necessary bonds can form or break.
    """)

    
    st.image(
        "collision_theory_orientation_diagram.png",
        use_container_width=True
    )

    st.markdown("""
    A collision with the correct orientation can result in a reaction, whereas
    a collision with an incorrect orientation may not result in a reaction,
    even when the particles have sufficient energy.
    """)

    st.markdown("---")

    st.markdown("### Effective Collisions")

    st.markdown("""
    A collision that has both **sufficient energy** and the **correct orientation**
    is called an **effective collision**.

    Therefore:
    """)

    st.latex(
        r"\boxed{\text{Effective collision}=\text{sufficient energy}+\text{correct orientation}}"
    )

    st.info(
        "Only collisions that satisfy both conditions can result in a chemical reaction."
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


# ============================================================
# THREE WAYS TO DESCRIBE REACTION RATE
# ============================================================
st.subheader(
    "Average, Instantaneous and Initial Rates"
)

st.write(
    "Reaction rate can be described over a time interval "
    "or at a particular instant during a reaction."
)

fig = plot_three_rates()

st.pyplot(
    fig,
    use_container_width=True
)

plt.close(fig)

"""Compact concentration-time diagram showing
average, instantaneous and initial rates.
"""

t = np.linspace(0, 10, 300)

# Simple exponential decrease in reactant concentration
A0 = 1.00
k = 0.20
A = A0 * np.exp(-k * t)

fig, ax = plt.subplots(figsize=(9, 4.8))

# --------------------------------------------------------
# Concentration-time curve
# --------------------------------------------------------

    ax.plot(
        t,
        A,
        linewidth=2.5
    )

    # --------------------------------------------------------
    # Average rate: secant between t₁ and t₂
    # --------------------------------------------------------

    t1_graph = 2.5
    t2_graph = 6.5

    A1 = A0 * np.exp(-k * t1_graph)
    A2 = A0 * np.exp(-k * t2_graph)

    average_slope = (A2 - A1) / (t2_graph - t1_graph)

    t_average = np.array([
        t1_graph,
        t2_graph
    ])

    A_average = (
        A1
        + average_slope * (t_average - t1_graph)
    )

    ax.plot(
        t_average,
        A_average,
        linestyle="--",
        linewidth=2
    )

    ax.scatter(
        [t1_graph, t2_graph],
        [A1, A2],
        s=45,
        zorder=5
    )

    # --------------------------------------------------------
    # Instantaneous rate: tangent at t
    # --------------------------------------------------------

    ti = 4.5
    Ai = A0 * np.exp(-k * ti)

    instantaneous_slope = -k * Ai

    tangent_width = 1.8

    t_tangent = np.array([
        ti - tangent_width,
        ti + tangent_width
    ])

    A_tangent = (
        Ai
        + instantaneous_slope * (t_tangent - ti)
    )

    ax.plot(
        t_tangent,
        A_tangent,
        linestyle=":",
        linewidth=2.5
    )

    ax.scatter(
        [ti],
        [Ai],
        s=50,
        zorder=5
    )

    # --------------------------------------------------------
    # Initial rate: tangent at t = 0
    # --------------------------------------------------------

    initial_slope = -k * A0

    t_initial = np.array([
        0,
        2.0
    ])

    A_initial = (
        A0
        + initial_slope * t_initial
    )

    ax.plot(
        t_initial,
        A_initial,
        linestyle="-.",
        linewidth=2
    )

    ax.scatter(
        [0],
        [A0],
        s=50,
        zorder=5
    )

    # --------------------------------------------------------
    # Graph labels
    # --------------------------------------------------------

    ax.annotate(
        "Initial rate\n(t = 0)",
        xy=(
            0.3,
            A0 + initial_slope * 0.3
        ),
        xytext=(
            1.0,
            1.04
        ),
        arrowprops=dict(
            arrowstyle="->",
            lw=1.2
        ),
        fontsize=10
    )

    ax.annotate(
        "Instantaneous rate\nat time t",
        xy=(
            ti + 0.2,
            Ai + instantaneous_slope * 0.2
        ),
        xytext=(
            5.5,
            0.72
        ),
        arrowprops=dict(
            arrowstyle="->",
            lw=1.2
        ),
        fontsize=10
    )

    ax.annotate(
        "Average rate\nbetween $t_1$ and $t_2$",
        xy=(
            4.5,
            (A1 + A2) / 2
        ),
        xytext=(
            6.0,
            0.40
        ),
        arrowprops=dict(
            arrowstyle="->",
            lw=1.2
        ),
        fontsize=10
    )

    # --------------------------------------------------------
    # Time labels
    # --------------------------------------------------------

    ax.text(
        t1_graph,
        -0.07,
        r"$t_1$",
        ha="center",
        fontsize=11
    )

    ax.text(
        t2_graph,
        -0.07,
        r"$t_2$",
        ha="center",
        fontsize=11
    )

    ax.text(
        ti,
        -0.07,
        r"$t$",
        ha="center",
        fontsize=11
    )

    # --------------------------------------------------------
    # Formatting
    # --------------------------------------------------------

    ax.set_xlabel(
        "Time",
        fontsize=11
    )

    ax.set_ylabel(
        "Concentration of A",
        fontsize=11
    )

    ax.set_title(
        "Three ways to describe reaction rate",
        fontsize=13,
        pad=10
    )

    ax.set_xlim(
        -0.3,
        10
    )

    ax.set_ylim(
        -0.12,
        1.15
    )

    ax.grid(
        alpha=0.2
    )

    plt.tight_layout()

    return fig


# ============================================================
# DISPLAY THREE RATES
# ============================================================

st.subheader(
    "Average, Instantaneous and Initial Rates"
)

st.write(
    "Reaction rate can be described over a time interval "
    "or at a particular instant during a reaction."
)

fig = plot_three_rates()

st.pyplot(
    fig,
    use_container_width=True
)

plt.close(fig)


# ============================================================
# THREE CONCISE EXPLANATIONS
# ============================================================

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown("**Average rate**")

    st.write(
        "The rate of reaction over a specified time interval."
    )

    st.latex(
        r"\text{Average rate} = "
        r"-\frac{\Delta[A]}{\Delta t}"
    )


with col2:

    st.markdown("**Instantaneous rate**")

    st.write(
        "The rate of reaction at a particular instant. "
        "It is the slope of the tangent to the curve."
    )

    st.latex(
        r"\text{Instantaneous rate} = "
        r"-\frac{d[A]}{dt}"
    )


with col3:

    st.markdown("**Initial rate**")

    st.write(
        "The instantaneous rate at the start of the reaction, "
        "when t = 0."
    )

    st.latex(
        r"\text{Initial rate} = "
        r"\left.-\frac{d[A]}{dt}\right|_{t=0}"
    )


# ============================================================
# CALCULATING AN AVERAGE RATE
# ============================================================

st.subheader(
    "Calculating an Average Rate"
)

st.write(
    "For an average rate, the change in concentration is "
    "considered between two times, t₁ and t₂."
)

col1, col2 = st.columns(2)

with col1:

    st.latex(
        r"\Delta[A] = [A]_{t_2} - [A]_{t_1}"
    )

with col2:

    st.latex(
        r"\Delta t = t_2 - t_1"
    )

st.write(
    "Here, Δ means change in. For a reactant, the concentration "
    "decreases as the reaction proceeds, so the negative sign "
    "in the rate equation gives a positive reaction rate."
)


# =====================================================
# WORKED EXAMPLE
# =====================================================

st.subheader(
    "Worked Example"
)

st.write(
    "The concentration of reactant A changes from "
    "0.80 mol L⁻¹ at 10 s to 0.50 mol L⁻¹ at 30 s."
)

st.markdown(
    "**Given:**"
)

st.latex(
    r"[\mathrm{A}]_{t_1}=0.80\ \mathrm{mol\,L^{-1}}"
)

st.latex(
    r"[\mathrm{A}]_{t_2}=0.50\ \mathrm{mol\,L^{-1}}"
)

st.latex(
    r"t_1=10\ \mathrm{s}"
)

st.latex(
    r"t_2=30\ \mathrm{s}"
)

st.write(
    "**Step 1: Calculate the change in concentration**"
)

st.latex(
    r"\Delta[\mathrm{A}]"
    r"=0.50-0.80"
    r"=-0.30\ \mathrm{mol\,L^{-1}}"
)

st.write(
    "**Step 2: Calculate the change in time**"
)

st.latex(
    r"\Delta t=30-10=20\ \mathrm{s}"
)

st.write(
    "**Step 3: Calculate the average rate**"
)

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

st.subheader(
    "Interactive Average Rate"
)

st.write(
    "Select two points to investigate how the average reaction "
    "rate changes when the concentration interval or time "
    "interval changes."
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
        "The later time, t₂, must be greater than the "
        "initial time, t₁."
    )

else:

    delta_concentration = (
        concentration_t2 - concentration_t1
    )

    delta_time = t2 - t1

    average_rate = (
        -delta_concentration / delta_time
    )

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
            "represents the rate of concentration change with time."
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
        "The rate of a chemical reaction depends on how often reactant "
        "particles collide and how many of those collisions are effective."
    )

    st.info(
        "Remember: an effective collision requires sufficient energy to "
        "overcome the activation energy, Ea, and the correct orientation."
    )

    # =====================================================
    # 1. CONCENTRATION
    # =====================================================

    st.header("1. Concentration")

    st.write(
        "Increasing the concentration of reactants increases the number "
        "of reactant particles in a given volume."
    )

    st.write(
        "This increases the frequency of collisions between reactant "
        "particles. If the temperature and other conditions remain "
        "constant, more effective collisions can occur per unit time."
    )

    st.subheader("Interactive particle model")

    concentration_level = st.slider(
        "Reactant concentration",
        min_value=2,
        max_value=10,
        value=5,
        step=1,
        key="concentration_visual"
    )

    # Create a reproducible set of molecule positions
    rng = np.random.default_rng(10)

    max_molecules = 40

    positions = rng.uniform(
        low=0.08,
        high=0.92,
        size=(max_molecules, 2)
    )

    visible_molecules = concentration_level * 4

    fig_concentration, ax_concentration = plt.subplots(
        figsize=(7, 4.5)
    )

    for i in range(visible_molecules):

        x, y = positions[i]

        circle = plt.Circle(
            (x, y),
            0.025,
            fill=False,
            linewidth=1.8
        )

        ax_concentration.add_patch(circle)

    ax_concentration.set_xlim(0, 1)
    ax_concentration.set_ylim(0, 1)
    ax_concentration.set_aspect("equal")
    ax_concentration.set_xticks([])
    ax_concentration.set_yticks([])

    ax_concentration.set_title(
        f"Reactant molecules at relative concentration {concentration_level}"
    )

    st.pyplot(fig_concentration)

    if concentration_level <= 3:

        st.info(
            "Lower concentration: fewer reactant molecules occupy the "
            "same volume, so collisions occur less frequently."
        )

    elif concentration_level <= 6:

        st.info(
            "Moderate concentration: reactant molecules are more closely "
            "packed, increasing the frequency of collisions."
        )

    else:

        st.success(
            "Higher concentration: more reactant molecules occupy the "
            "same volume, so collisions occur more frequently."
        )

    st.markdown("""
    **Key idea**

    Higher concentration → more frequent collisions → more effective
    collisions per unit time → generally faster reaction.
    """)

    # =====================================================
    # 2. TEMPERATURE
    # =====================================================

    st.header("2. Temperature")

    st.write(
        "Increasing temperature increases the average kinetic energy of "
        "the particles. The particles therefore move faster."
    )

    st.write(
        "More importantly, increasing temperature increases the fraction "
        "of particles with enough energy to overcome the activation energy, "
        "Ea."
    )

    st.subheader("Interactive temperature model")

    temperature_level = st.slider(
        "Temperature",
        min_value=1,
        max_value=3,
        value=2,
        step=1,
        key="temperature_visual"
    )

    temperature_labels = {
        1: "Lower temperature",
        2: "Moderate temperature",
        3: "Higher temperature"
    }

    temperature_speeds = {
        1: 0.035,
        2: 0.065,
        3: 0.10
    }

    speed = temperature_speeds[temperature_level]

    st.write(
        f"**{temperature_labels[temperature_level]}**"
    )

    rng_temperature = np.random.default_rng(20)

    temperature_positions = rng_temperature.uniform(
        low=0.10,
        high=0.90,
        size=(12, 2)
    )

    fig_temperature, ax_temperature = plt.subplots(
        figsize=(7, 4.5)
    )

    for x, y in temperature_positions:

        # Different directions make the diagram look more like
        # a collection of moving molecules.
        angle = rng_temperature.uniform(0, 2 * np.pi)

        dx = np.cos(angle) * speed
        dy = np.sin(angle) * speed

        circle = plt.Circle(
            (x, y),
            0.025,
            fill=False,
            linewidth=1.8
        )

        ax_temperature.add_patch(circle)

        ax_temperature.arrow(
            x,
            y,
            dx,
            dy,
            head_width=0.012,
            head_length=0.018,
            length_includes_head=True
        )

    ax_temperature.set_xlim(0, 1)
    ax_temperature.set_ylim(0, 1)
    ax_temperature.set_aspect("equal")
    ax_temperature.set_xticks([])
    ax_temperature.set_yticks([])

    ax_temperature.set_title(
        "Conceptual model of particle motion"
    )

    st.pyplot(fig_temperature)

    if temperature_level == 1:

        st.info(
            "At lower temperature, particles have lower average kinetic "
            "energy and move more slowly."
        )

    elif temperature_level == 2:

        st.info(
            "At moderate temperature, particles have a higher average "
            "kinetic energy than at lower temperature."
        )

    else:

        st.success(
            "At higher temperature, particles move faster and a greater "
            "fraction have energy equal to or greater than Ea."
        )

    # -----------------------------------------------------
    # ENERGY DISTRIBUTION CONCEPT
    # -----------------------------------------------------

    st.subheader("Why does temperature have such a strong effect?")

    st.write(
        "Particles in a sample do not all have exactly the same kinetic "
        "energy. They have a distribution of energies."
    )

    st.write(
        "When the temperature increases, the energy distribution shifts "
        "so that a greater fraction of particles have energy at or above "
        "the activation energy."
    )

    energy = np.linspace(0, 10, 400)

    # Two conceptual Maxwell-Boltzmann-like curves.
    # These are deliberately normalised illustrative curves,
    # not quantitative experimental distributions.

    low_temperature = (
        energy ** 1.2
        * np.exp(-energy / 1.35)
    )

    high_temperature = (
        energy ** 1.2
        * np.exp(-energy / 2.2)
    )

    # Normalise only for visual comparison
    low_temperature = (
        low_temperature / np.max(low_temperature)
    )

    high_temperature = (
        high_temperature / np.max(high_temperature)
    )

    activation_energy_position = 5.5

    fig_energy, ax_energy = plt.subplots(
        figsize=(8, 5)
    )

    ax_energy.plot(
        energy,
        low_temperature,
        label="Lower temperature"
    )

    ax_energy.plot(
        energy,
        high_temperature,
        label="Higher temperature"
    )

    ax_energy.axvline(
        activation_energy_position,
        linestyle="--",
        label=r"$E_a$"
    )

    ax_energy.set_xlabel("Kinetic energy")
    ax_energy.set_ylabel("Relative number of particles")
    ax_energy.set_title(
        "Conceptual energy distributions at different temperatures"
    )

    ax_energy.legend()
    ax_energy.grid(True)

    st.pyplot(fig_energy)

    st.info(
        "The shaded region is not shown quantitatively here. The key idea "
        "is that at higher temperature, a greater fraction of particles "
        "have energy ≥ Ea."
    )

    st.markdown("""
    **Key idea**

    Higher temperature → greater average kinetic energy → greater fraction
    of particles with energy ≥ Ea → more effective collisions → faster reaction.
    """)

    # =====================================================
    # 3. SURFACE AREA
    # =====================================================

    st.header("3. Surface Area")

    st.write(
        "Surface area is important when a reaction involves a solid."
    )

    st.write(
        "Only particles at the exposed surface of a solid are directly "
        "available to collide with particles in another phase, such as "
        "a gas or solution."
    )

    surface_choice = st.radio(
        "Choose a solid arrangement:",
        [
            "One large piece",
            "Same amount divided into smaller pieces"
        ],
        horizontal=True,
        key="surface_area_choice"
    )

    fig_surface, ax_surface = plt.subplots(
        figsize=(7, 4.5)
    )

    if surface_choice == "One large piece":

        large_piece = plt.Rectangle(
            (0.30, 0.25),
            0.40,
            0.50,
            fill=False,
            linewidth=2.5
        )

        ax_surface.add_patch(large_piece)

        # Surface particles
        surface_points = [
            (0.30, 0.25),
            (0.50, 0.25),
            (0.70, 0.25),
            (0.30, 0.50),
            (0.30, 0.75),
            (0.50, 0.75),
            (0.70, 0.75),
            (0.70, 0.50)
        ]

        for x, y in surface_points:

            ax_surface.plot(
                x,
                y,
                marker="o",
                markersize=7
            )

        ax_surface.set_title(
            "One large piece: smaller exposed surface area"
        )

    else:

        small_pieces = [
            (0.18, 0.58),
            (0.40, 0.58),
            (0.62, 0.58),
            (0.29, 0.32),
            (0.51, 0.32),
            (0.73, 0.32)
        ]

        for x, y in small_pieces:

            piece = plt.Rectangle(
                (x, y),
                0.15,
                0.15,
                fill=False,
                linewidth=2
            )

            ax_surface.add_patch(piece)

        ax_surface.set_title(
            "Smaller pieces: greater total exposed surface area"
        )

    ax_surface.set_xlim(0, 1)
    ax_surface.set_ylim(0, 1)
    ax_surface.set_aspect("equal")
    ax_surface.set_xticks([])
    ax_surface.set_yticks([])

    st.pyplot(fig_surface)

    if surface_choice == "One large piece":

        st.info(
            "A smaller fraction of the solid's particles are exposed at "
            "the surface."
        )

    else:

        st.success(
            "Breaking the same amount of solid into smaller pieces increases "
            "the total exposed surface area."
        )

    st.markdown("""
    **Key idea**

    Greater surface area → more exposed particles → more opportunities
    for collisions → generally faster reaction.
    """)

    # =====================================================
    # 4. CATALYST
    # =====================================================

    st.header("4. Catalyst")

    st.write(
        "A catalyst increases reaction rate by providing an alternative "
        "reaction pathway with a lower activation energy."
    )

    st.write(
        "The catalyst does not change the identities or energies of the "
        "reactants and products, so the overall enthalpy change, ΔH, "
        "remains the same."
    )

    catalyst_present = st.radio(
        "Reaction pathway:",
        [
            "Without catalyst",
            "With catalyst"
        ],
        horizontal=True,
        key="catalyst_pathway"
    )

    reaction_coordinate = np.linspace(0, 10, 300)

    reactant_energy = 2.0
    product_energy = 4.0

    # Uncatalysed pathway
    uncatalysed_peak = 8.0
    uncatalysed_curve = (
        reactant_energy
        + (
            uncatalysed_peak - reactant_energy
        )
        * np.exp(
            -((reaction_coordinate - 5.0) ** 2) / 1.6
        )
    )

    # Catalysed pathway
    catalysed_peak = 5.8
    catalysed_curve = (
        reactant_energy
        + (
            catalysed_peak - reactant_energy
        )
        * np.exp(
            -((reaction_coordinate - 5.0) ** 2) / 1.6
        )
    )

    # Correct the product end of both curves
    product_transition = (
        1 / (
            1 + np.exp(
                -(reaction_coordinate - 7.0) * 4
            )
        )
    )

    uncatalysed_curve = (
        uncatalysed_curve
        * (1 - product_transition)
        + product_energy * product_transition
    )

    catalysed_curve = (
        catalysed_curve
        * (1 - product_transition)
        + product_energy * product_transition
    )

    fig_catalyst, ax_catalyst = plt.subplots(
        figsize=(8, 5)
    )

    ax_catalyst.plot(
        reaction_coordinate,
        uncatalysed_curve,
        linestyle="--",
        label="Uncatalysed pathway"
    )

    ax_catalyst.plot(
        reaction_coordinate,
        catalysed_curve,
        label="Catalysed pathway"
    )

    ax_catalyst.axhline(
        reactant_energy,
        linestyle=":",
        label="Reactants"
    )

    ax_catalyst.axhline(
        product_energy,
        linestyle="-.",
        label="Products"
    )

    ax_catalyst.set_xlabel("Reaction progress")
    ax_catalyst.set_ylabel("Potential energy")
    ax_catalyst.set_title(
        "Energy Profile: Catalysed and Uncatalysed Pathways"
    )

    ax_catalyst.legend()
    ax_catalyst.grid(True)

    st.pyplot(fig_catalyst)

    if catalyst_present == "With catalyst":

        st.success(
            "With a catalyst, the reaction follows a pathway with a lower "
            "activation energy."
        )

        st.latex(
            r"E_{a,\mathrm{catalysed}}"
            r"<"
            r"E_{a,\mathrm{uncatalysed}}"
        )

    else:

        st.info(
            "Without a catalyst, the reaction follows the pathway with "
            "the higher activation energy."
        )

    st.write(
        "Notice that the reactant and product energy levels remain the "
        "same. Therefore, the overall ΔH of the reaction is unchanged."
    )

    st.markdown("""
    **Key idea**

    Catalyst → alternative pathway → lower \(E_a\) → greater fraction of
    collisions can overcome \(E_a\) → faster reaction.
    """)

    # =====================================================
    # COMPARING THE FOUR FACTORS
    # =====================================================

    st.header("Compare the Factors")

    st.write(
        "Use the activity below to identify the main reason each factor "
        "changes the reaction rate."
    )

    comparison_factor = st.selectbox(
        "Choose a factor:",
        [
            "Concentration",
            "Temperature",
            "Surface area",
            "Catalyst"
        ],
        key="factor_comparison"
    )

    if comparison_factor == "Concentration":

        st.write(
            "**Question:** Why does increasing concentration generally "
            "increase reaction rate?"
        )

        answer = st.radio(
            "Choose the best explanation:",
            [
                "Particles become larger",
                "There are more frequent collisions between reactant particles",
                "The activation energy always increases",
                "The products become more stable"
            ],
            key="compare_concentration"
        )

        if st.button(
            "Check concentration answer",
            key="check_concentration"
        ):

            if answer == (
                "There are more frequent collisions between reactant particles"
            ):

                st.success(
                    "Correct. More reactant particles in the same volume "
                    "lead to more frequent collisions."
                )

            else:

                st.error(
                    "Not quite. Increasing concentration mainly increases "
                    "the frequency of collisions."
                )

    elif comparison_factor == "Temperature":

        st.write(
            "**Question:** Why does increasing temperature generally "
            "increase reaction rate?"
        )

        answer = st.radio(
            "Choose the best explanation:",
            [
                "All particles suddenly have the same energy",
                "The activation energy becomes zero",
                "A greater fraction of particles have energy ≥ Ea",
                "The concentration automatically doubles"
            ],
            key="compare_temperature"
        )

        if st.button(
            "Check temperature answer",
            key="check_temperature"
        ):

            if answer == (
                "A greater fraction of particles have energy ≥ Ea"
            ):

                st.success(
                    "Correct. Increasing temperature increases the fraction "
                    "of particles energetic enough to overcome Ea."
                )

            else:

                st.error(
                    "Not quite. The important idea is that a greater fraction "
                    "of particles have energy ≥ Ea."
                )

    elif comparison_factor == "Surface area":

        st.write(
            "**Question:** Why does increasing the surface area of a solid "
            "generally increase reaction rate?"
        )

        answer = st.radio(
            "Choose the best explanation:",
            [
                "The solid becomes chemically different",
                "More particles are exposed at the surface",
                "The activation energy becomes zero",
                "The mass of the solid automatically increases"
            ],
            key="compare_surface"
        )

        if st.button(
            "Check surface-area answer",
            key="check_surface"
        ):

            if answer == (
                "More particles are exposed at the surface"
            ):

                st.success(
                    "Correct. A greater exposed surface provides more "
                    "opportunities for collisions."
                )

            else:

                st.error(
                    "Not quite. Increasing surface area exposes more "
                    "particles to potential collisions."
                )

    else:

        st.write(
            "**Question:** How does a catalyst increase reaction rate?"
        )

        answer = st.radio(
            "Choose the best explanation:",
            [
                "It increases the overall ΔH",
                "It increases the concentration of products",
                "It provides an alternative pathway with lower Ea",
                "It permanently changes the reactants"
            ],
            key="compare_catalyst"
        )

        if st.button(
            "Check catalyst answer",
            key="check_catalyst"
        ):

            if answer == (
                "It provides an alternative pathway with lower Ea"
            ):

                st.success(
                    "Correct. A catalyst provides an alternative pathway "
                    "with a lower activation energy."
                )

            else:

                st.error(
                    "Not quite. A catalyst increases reaction rate by "
                    "providing an alternative pathway with lower Ea."
                )

    # =====================================================
    # SUMMARY TABLE
    # =====================================================

    st.header("Summary")

    st.markdown("""
    | Factor | Main effect | Why the rate changes |
    |---|---|---|
    | **Concentration** | More frequent collisions | More reactant particles are present in the same volume |
    | **Temperature** | More particles have energy ≥ \(E_a\) | A greater fraction of collisions can be effective |
    | **Surface area** | More exposed particles | More opportunities for collisions at a solid surface |
    | **Catalyst** | Lower \(E_a\) pathway | A greater fraction of collisions can overcome \(E_a\) |
    """)

    # =====================================================
    # CHECK YOUR UNDERSTANDING
    # =====================================================

    st.header("Check Your Understanding")

    st.write(
        "Test whether you can explain the factors using collision theory."
    )

    q1 = st.radio(
        "1. A reaction is carried out at a higher concentration, "
        "with temperature unchanged. What is the main effect?",
        [
            "The particles have greater average kinetic energy",
            "There are more frequent collisions",
            "The activation energy increases",
            "The products disappear"
        ],
        key="factor_q1"
    )

    if st.button("Check Question 1", key="factor_check1"):

        if q1 == "There are more frequent collisions":

            st.success("Correct!")

        else:

            st.error(
                "Not quite. Increasing concentration increases the "
                "frequency of collisions."
            )

    q2 = st.radio(
        "2. Why does increasing temperature increase the number of "
        "effective collisions?",
        [
            "All collisions become effective",
            "The activation energy becomes zero",
            "A greater fraction of particles have energy ≥ Ea",
            "The particles stop moving"
        ],
        key="factor_q2"
    )

    if st.button("Check Question 2", key="factor_check2"):

        if q2 == "A greater fraction of particles have energy ≥ Ea":

            st.success("Correct!")

        else:

            st.error(
                "Not quite. Higher temperature increases the fraction "
                "of particles with energy ≥ Ea."
            )

    q3 = st.radio(
        "3. Which statement about a catalyst is correct?",
        [
            "A catalyst increases the overall ΔH",
            "A catalyst is always consumed completely",
            "A catalyst provides an alternative pathway with lower Ea",
            "A catalyst changes the products into different substances"
        ],
        key="factor_q3"
    )

    if st.button("Check Question 3", key="factor_check3"):

        if q3 == (
            "A catalyst provides an alternative pathway with lower Ea"
        ):

            st.success("Correct!")

        else:

            st.error(
                "Not quite. A catalyst provides an alternative pathway "
                "with a lower activation energy."
            )

    st.success(
        "Excellent. The key connection is: reaction conditions affect "
        "the frequency of collisions and/or the fraction of collisions "
        "that are effective."
    )
    # =========================================================
# RATE LAWS
# =========================================================

elif topic == "Rate Laws":

    st.title("Rate Laws")

    st.write(
        "A rate law describes how the rate of a reaction depends on the "
        "concentrations of the reactants."
    )

    st.info(
        "A rate law is determined experimentally. The exponents in a "
        "rate law are not automatically taken from the stoichiometric "
        "coefficients of the balanced chemical equation."
    )

    # =====================================================
    # 1. INTRODUCTION
    # =====================================================

    st.header("1. What Is a Rate Law?")

    st.write(
        "For many reactions, changing the concentration of a reactant "
        "changes the reaction rate. A rate law gives the mathematical "
        "relationship between reactant concentration and reaction rate."
    )

    st.subheader("General form")

    st.latex(
        r"\boxed{\text{rate}=k[\mathrm{A}]^m[\mathrm{B}]^n}"
    )

    st.write(
        "For this rate law:"
    )

    st.markdown("""
    - **rate** = reaction rate
    - **k** = rate constant
    - **[A] and [B]** = concentrations of reactants A and B
    - **m and n** = reaction orders with respect to A and B
    """)

    st.write(
        "The values of \(m\) and \(n\) determine how strongly the reaction "
        "rate depends on the concentration of each reactant."
    )

    # =====================================================
    # 2. RATE CONSTANT
    # =====================================================

    st.header("2. The Rate Constant, k")

    st.write(
        "The constant \(k\) is called the **rate constant**. For a given "
        "reaction under specified conditions, \(k\) has a constant value."
    )

    st.write(
        "The value of \(k\) depends on conditions such as temperature and "
        "the nature of the reaction."
    )

    st.write(
        "A larger value of \(k\) generally corresponds to a faster reaction "
        "when the reactant concentrations and reaction orders are the same."
    )

    st.warning(
        "The units of \(k\) depend on the overall reaction order."
    )

    # =====================================================
    # 3. REACTION ORDER
    # =====================================================

    st.header("3. Reaction Order")

    st.write(
        "The exponent of a reactant concentration in the rate law tells "
        "us the order of the reaction with respect to that reactant."
    )

    st.subheader("Order with respect to A")

    st.latex(
        r"\text{rate}=k[\mathrm{A}]^m"
    )

    st.write(
        "The reaction is said to be **\(m\)th order with respect to A**."
    )

    st.subheader("Overall reaction order")

    st.write(
        "The overall reaction order is the sum of the individual reaction "
        "orders."
    )

    st.latex(
        r"\boxed{\text{Overall order}=m+n}"
    )

    st.write(
        "For example, if a rate law is:"
    )

    st.latex(
        r"\text{rate}=k[\mathrm{A}]^2[\mathrm{B}]"
    )

    st.write(
        "then the reaction is:"
    )

    st.markdown("""
    - second order with respect to A
    - first order with respect to B
    - third order overall
    """)

    st.latex(
        r"\text{Overall order}=2+1=3"
    )

    # =====================================================
    # 4. WHAT DO THE EXPONENTS MEAN?
    # =====================================================

    st.header("4. What Do the Exponents Mean?")

    st.write(
        "The exponent tells us how the reaction rate changes when the "
        "concentration of that reactant changes."
    )

    st.subheader("Zero order")

    st.latex(
        r"\text{rate}=k[\mathrm{A}]^0"
    )

    st.write(
        "Because any non-zero quantity raised to the power of zero is 1:"
    )

    st.latex(
        r"[\mathrm{A}]^0=1"
    )

    st.latex(
        r"\boxed{\text{rate}=k}"
    )

    st.write(
        "The rate does not depend on the concentration of A."
    )

    st.subheader("First order")

    st.latex(
        r"\text{rate}=k[\mathrm{A}]"
    )

    st.write(
        "The rate is directly proportional to the concentration of A."
    )

    st.markdown("""
    If [A] doubles:

    **rate doubles**
    """)

    st.subheader("Second order")

    st.latex(
        r"\text{rate}=k[\mathrm{A}]^2"
    )

    st.write(
        "The rate is proportional to the square of the concentration of A."
    )

    st.markdown("""
    If [A] doubles:

    **rate increases by a factor of 4**
    """)

    # =====================================================
    # 5. INTERACTIVE EXPONENT EXPLORER
    # =====================================================

    st.header("5. Interactive Rate-Law Explorer")

    st.write(
        "Change the concentration of A and the reaction order to see "
        "how the reaction rate changes."
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        concentration_A = st.slider(
            "Concentration of A (mol L⁻¹)",
            min_value=0.1,
            max_value=2.0,
            value=1.0,
            step=0.1,
            key="rate_law_concentration"
        )

    with col2:

        reaction_order_A = st.selectbox(
            "Order with respect to A",
            [0, 1, 2, 3],
            index=1,
            key="rate_law_order"
        )

    with col3:

        rate_constant = st.number_input(
            "Rate constant, k",
            min_value=0.01,
            max_value=10.0,
            value=1.0,
            step=0.1,
            key="rate_law_k"
        )

    calculated_rate = (
        rate_constant
        * concentration_A ** reaction_order_A
    )

    st.latex(
        rf"\text{{rate}}=k[\mathrm{{A}}]^{{{reaction_order_A}}}"
    )

    st.metric(
        "Calculated rate",
        f"{calculated_rate:.3f}"
    )

    if reaction_order_A == 0:

        st.info(
            "Zero order: changing [A] does not change the rate."
        )

    elif reaction_order_A == 1:

        st.info(
            "First order: doubling [A] doubles the rate."
        )

    elif reaction_order_A == 2:

        st.info(
            "Second order: doubling [A] increases the rate by a factor of 4."
        )

    else:

        st.info(
            f"Third order: doubling [A] increases the rate by a factor of 8."
        )

    # =====================================================
    # 6. HOW CONCENTRATION AFFECTS RATE
    # =====================================================

    st.header("6. How Does Concentration Affect Rate?")

    st.write(
        "The effect of changing concentration depends on the reaction order."
    )

    selected_order = st.slider(
        "Select the reaction order",
        min_value=0,
        max_value=3,
        value=1,
        step=1,
        key="order_comparison"
    )

    initial_concentration = 1.0
    doubled_concentration = 2.0

    initial_rate_relative = (
        initial_concentration ** selected_order
    )

    doubled_rate_relative = (
        doubled_concentration ** selected_order
    )

    if initial_rate_relative != 0:

        rate_factor = (
            doubled_rate_relative
            / initial_rate_relative
        )

    else:

        rate_factor = 1

    st.write(
        f"Consider a reaction with order **{selected_order}** with respect "
        "to A."
    )

    st.latex(
        rf"\text{{rate}}\propto[\mathrm{{A}}]^{{{selected_order}}}"
    )

    result_col1, result_col2, result_col3 = st.columns(3)

    with result_col1:

        st.metric(
            "[A] before",
            "1.0 mol L⁻¹"
        )

    with result_col2:

        st.metric(
            "[A] after",
            "2.0 mol L⁻¹"
        )

    with result_col3:

        st.metric(
            "Rate change",
            f"{rate_factor:.0f} ×"
        )

    if selected_order == 0:

        st.success(
            "Zero order: doubling the concentration does not change the rate."
        )

    elif selected_order == 1:

        st.success(
            "First order: doubling the concentration doubles the rate."
        )

    elif selected_order == 2:

        st.success(
            "Second order: doubling the concentration makes the rate "
            "four times larger."
        )

    else:

        st.success(
            "Third order: doubling the concentration makes the rate "
            "eight times larger."
        )

    # =====================================================
    # 7. TWO-REACTANT RATE LAW
    # =====================================================

    st.header("7. Rate Laws with More Than One Reactant")

    st.write(
        "A rate law can contain more than one reactant concentration."
    )

    st.latex(
        r"\boxed{\text{rate}=k[\mathrm{A}]^m[\mathrm{B}]^n}"
    )

    st.write(
        "For example:"
    )

    st.latex(
        r"\text{rate}=k[\mathrm{A}]^2[\mathrm{B}]"
    )

    st.write(
        "This tells us that:"
    )

    st.markdown("""
    - the reaction is second order with respect to A
    - the reaction is first order with respect to B
    - the reaction is third order overall
    """)

    st.latex(
        r"\text{Overall order}=2+1=3"
    )

    # =====================================================
    # 8. INTERACTIVE TWO-REACTANT RATE LAW
    # =====================================================

    st.header("8. Interactive Two-Reactant Rate Law")

    st.write(
        "Explore how changing the concentrations of A and B affects "
        "the reaction rate."
    )

    col1, col2 = st.columns(2)

    with col1:

        concentration_A_two = st.slider(
            "Concentration of A (mol L⁻¹)",
            min_value=0.1,
            max_value=2.0,
            value=1.0,
            step=0.1,
            key="two_reactant_A"
        )

        order_A_two = st.selectbox(
            "Order with respect to A",
            [0, 1, 2],
            index=1,
            key="two_reactant_order_A"
        )

    with col2:

        concentration_B_two = st.slider(
            "Concentration of B (mol L⁻¹)",
            min_value=0.1,
            max_value=2.0,
            value=1.0,
            step=0.1,
            key="two_reactant_B"
        )

        order_B_two = st.selectbox(
            "Order with respect to B",
            [0, 1, 2],
            index=1,
            key="two_reactant_order_B"
        )

    k_two = 1.0

    two_reactant_rate = (
        k_two
        * concentration_A_two ** order_A_two
        * concentration_B_two ** order_B_two
    )

    st.latex(
        rf"\text{{rate}}="
        rf"k[\mathrm{{A}}]^{{{order_A_two}}}"
        rf"[\mathrm{{B}}]^{{{order_B_two}}}"
    )

    st.metric(
        "Calculated relative rate",
        f"{two_reactant_rate:.3f}"
    )

    overall_order_two = (
        order_A_two + order_B_two
    )

    st.info(
        f"Overall reaction order = "
        f"{order_A_two} + {order_B_two} = "
        f"{overall_order_two}"
    )

    # =====================================================
    # 9. IMPORTANT NOTE ABOUT STOICHIOMETRY
    # =====================================================

    st.header("9. Rate Law vs Balanced Equation")

    st.write(
        "It is important not to assume that the exponents in a rate law "
        "are the same as the stoichiometric coefficients in the balanced "
        "chemical equation."
    )

    st.latex(
        r"\mathrm{A+2B\rightarrow products}"
    )

    st.write(
        "For a general reaction, the experimentally determined rate law "
        "could, for example, be:"
    )

    st.latex(
        r"\text{rate}=k[\mathrm{A}]^2[\mathrm{B}]"
    )

    st.warning(
        "The exponents in an experimentally determined rate law must be "
        "determined from experimental data. They cannot generally be "
        "obtained simply by looking at the balanced equation."
    )

    # =====================================================
    # 10. CHECK YOUR UNDERSTANDING
    # =====================================================

    st.header("Check Your Understanding")

    question1 = st.radio(
        "1. What does the exponent of a reactant concentration in a "
        "rate law tell us?",
        [
            "The molar mass of the reactant",
            "The reaction order with respect to that reactant",
            "The activation energy",
            "The temperature of the reaction"
        ],
        key="rate_law_question1"
    )

    if st.button(
        "Check Question 1",
        key="rate_law_check1"
    ):

        if question1 == (
            "The reaction order with respect to that reactant"
        ):

            st.success(
                "Correct! The exponent gives the reaction order "
                "with respect to that reactant."
            )

        else:

            st.error(
                "Not quite. The exponent tells us the reaction order "
                "with respect to that reactant."
            )

    question2 = st.radio(
        "2. For rate = k[A]², what happens to the rate if [A] doubles?",
        [
            "The rate stays the same",
            "The rate doubles",
            "The rate becomes four times larger",
            "The rate becomes eight times larger"
        ],
        key="rate_law_question2"
    )

    if st.button(
        "Check Question 2",
        key="rate_law_check2"
    ):

        if question2 == (
            "The rate becomes four times larger"
        ):

            st.success(
                "Correct! For a second-order dependence, "
                "2² = 4."
            )

        else:

            st.error(
                "Not quite. If [A] doubles, the rate changes by "
                "2² = 4."
            )

    question3 = st.radio(
        "3. How are the exponents in a rate law usually determined?",
        [
            "From the molar masses of the reactants",
            "From the balanced equation in every case",
            "Experimentally",
            "From the colour of the reaction"
        ],
        key="rate_law_question3"
    )

    if st.button(
        "Check Question 3",
        key="rate_law_check3"
    ):

        if question3 == "Experimentally":

            st.success(
                "Correct! Reaction orders are generally determined "
                "experimentally."
            )

        else:

            st.error(
                "Not quite. Reaction orders are generally determined "
                "from experimental measurements."
            )

    # =====================================================
    # KEY POINTS
    # =====================================================

    st.header("Key Points")

    st.markdown("""
    **Remember:**

    1. A rate law describes how reaction rate depends on reactant concentrations.
    2. The general form is \( \text{rate}=k[A]^m[B]^n \).
    3. \(k\) is the rate constant.
    4. The exponent gives the order with respect to that reactant.
    5. The overall order is the sum of the individual orders.
    6. Zero-order reactions do not depend on that reactant concentration.
    7. First-order dependence means doubling concentration doubles the rate.
    8. Second-order dependence means doubling concentration makes the rate four times larger.
    9. Reaction orders are generally determined experimentally.
    10. The exponents in a rate law cannot generally be obtained from the balanced equation.
    """) 

elif topic == "Order of Reaction":

    st.header("Order of Reaction")

    st.markdown("""
    The **order of a reaction** describes how the reaction rate depends on the
    concentration of one or more reactants.
    """)

    # ---------------------------------------------------------
    # 1. What does reaction order mean?
    # ---------------------------------------------------------

    st.subheader("1. What does reaction order mean?")

    st.markdown("""
    From the rate-law section, we saw that a reaction may have a rate law such as:
    """)

    st.latex(r"\text{rate}=k[A]^m[B]^n")

    st.markdown("""
    The exponents **m** and **n** tell us how the rate depends on the
    concentrations of A and B.

    - **m** = order with respect to A
    - **n** = order with respect to B
    - **m + n** = overall reaction order

    These exponents are generally determined **experimentally**. They cannot
    usually be obtained simply by looking at the coefficients in the balanced
    chemical equation.
    """)

    st.latex(r"\boxed{\text{Overall order}=m+n}")

    st.divider()

    # ---------------------------------------------------------
    # 2. Simple examples
    # ---------------------------------------------------------

    st.subheader("2. How concentration affects rate")

    st.markdown("""
    Consider a rate law containing only reactant A:
    """)

    st.latex(r"\text{rate}=k[A]^m")

    st.markdown("""
    The value of **m** determines how the rate changes when the concentration
    of A changes.
    """)

    order_choice = st.selectbox(
        "Choose the order with respect to A:",
        ["Zero order", "First order", "Second order"],
        key="order_example"
    )

    if order_choice == "Zero order":

        st.latex(r"\text{rate}=k[A]^0=k")

        st.info("""
        **Zero order:** The rate does not depend on the concentration of A.

        If [A] doubles, the rate remains unchanged.
        """)

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Change in [A]", "×2")

        with col2:
            st.metric("Change in rate", "×1")

    elif order_choice == "First order":

        st.latex(r"\text{rate}=k[A]")

        st.info("""
        **First order:** The rate is directly proportional to the concentration
        of A.

        If [A] doubles, the rate doubles.
        """)

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Change in [A]", "×2")

        with col2:
            st.metric("Change in rate", "×2")

    else:

        st.latex(r"\text{rate}=k[A]^2")

        st.info("""
        **Second order:** The rate is proportional to the square of the
        concentration of A.

        If [A] doubles, the rate increases by a factor of four.
        """)

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Change in [A]", "×2")

        with col2:
            st.metric("Change in rate", "×4")

    st.divider()

    # ---------------------------------------------------------
    # 3. Determining reaction order experimentally
    # ---------------------------------------------------------

    st.subheader("3. Determining reaction order from experimental data")

    st.markdown("""
    Reaction orders are commonly determined using **initial-rate experiments**.

    In these experiments, the initial concentrations of the reactants are
    changed systematically and the corresponding initial reaction rates are
    measured.
    """)

    st.markdown("""
    For example, suppose the rate law is:
    """)

    st.latex(r"\text{rate}=k[A]^m[B]^n")

    st.markdown("""
    To determine the order with respect to **A**, compare two experiments in
    which **[B] is kept constant**.

    To determine the order with respect to **B**, compare two experiments in
    which **[A] is kept constant**.
    """)

    st.divider()

    # ---------------------------------------------------------
    # 4. Experimental data
    # ---------------------------------------------------------

    st.subheader("4. Example: initial-rate data")

    data = {
        "Experiment": [1, 2, 3],
        "[A] (mol L⁻¹)": [0.10, 0.20, 0.10],
        "[B] (mol L⁻¹)": [0.10, 0.10, 0.20],
        "Initial rate (mol L⁻¹ s⁻¹)": [0.020, 0.040, 0.080]
    }

    st.dataframe(
        data,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("""
    Notice that the experiments have been designed so that we can compare
    one reactant at a time.
    """)

    st.divider()

    # ---------------------------------------------------------
    # 5. Determine order with respect to A
    # ---------------------------------------------------------

    st.subheader("5. Determining the order with respect to A")

    st.markdown("""
    Compare **Experiments 1 and 2**.

    The concentration of B remains constant:
    """)

    st.latex(r"[B]_1=[B]_2=0.10\ \text{mol L}^{-1}")

    st.markdown("""
    Therefore, any change in rate is associated with the change in [A].
    """)

    st.latex(
        r"\frac{\text{rate}_2}{\text{rate}_1}"
        r"="
        r"\left(\frac{[A]_2}{[A]_1}\right)^m"
    )

    st.markdown("Substituting the experimental values:")

    st.latex(
        r"\frac{0.040}{0.020}"
        r"="
        r"\left(\frac{0.20}{0.10}\right)^m"
    )

    st.latex(r"2=2^m")

    st.markdown("Therefore:")

    st.latex(r"\boxed{m=1}")

    st.success("The reaction is **first order with respect to A**.")

    st.divider()

    # ---------------------------------------------------------
    # 6. Determine order with respect to B
    # ---------------------------------------------------------

    st.subheader("6. Determining the order with respect to B")

    st.markdown("""
    Now compare **Experiments 1 and 3**.

    The concentration of A remains constant:
    """)

    st.latex(r"[A]_1=[A]_3=0.10\ \text{mol L}^{-1}")

    st.markdown("""
    Therefore, the change in rate is associated with the change in [B].
    """)

    st.latex(
        r"\frac{\text{rate}_3}{\text{rate}_1}"
        r"="
        r"\left(\frac{[B]_3}{[B]_1}\right)^n"
    )

    st.markdown("Substituting the experimental values:")

    st.latex(
        r"\frac{0.080}{0.020}"
        r"="
        r"\left(\frac{0.20}{0.10}\right)^n"
    )

    st.latex(r"4=2^n")

    st.markdown("Therefore:")

    st.latex(r"\boxed{n=2}")

    st.success("The reaction is **second order with respect to B**.")

    st.divider()

    # ---------------------------------------------------------
    # 7. Overall order
    # ---------------------------------------------------------

    st.subheader("7. Determining the overall reaction order")

    st.markdown("""
    We have determined:
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Order with respect to A", "1")

    with col2:
        st.metric("Order with respect to B", "2")

    with col3:
        st.metric("Overall order", "3")

    st.latex(
        r"\boxed{\text{Overall order}=m+n=1+2=3}"
    )

    st.markdown("""
    Therefore, the rate law is:
    """)

    st.latex(
        r"\boxed{\text{rate}=k[A][B]^2}"
    )

    st.divider()

    # ---------------------------------------------------------
    # 8. Determining rate constant k
    # ---------------------------------------------------------

    st.subheader("8. Determining the rate constant, k")

    st.markdown("""
    Once the reaction orders are known, the rate constant can be calculated
    using the rate law.
    """)

    st.latex(r"\text{rate}=k[A][B]^2")

    st.markdown("Rearranging:")

    st.latex(
        r"\boxed{k=\frac{\text{rate}}{[A][B]^2}}"
    )

    st.markdown("Using Experiment 1:")

    st.latex(
        r"k=\frac{0.020}{(0.10)(0.10)^2}"
    )

    st.latex(r"k=20")

    st.success(
        "For this example, **k = 20 L² mol⁻² s⁻¹**."
    )

    st.markdown("""
    The units of the rate constant depend on the overall reaction order.
    """)

    st.divider()

    # ---------------------------------------------------------
    # 9. Interactive experiment comparison
    # ---------------------------------------------------------

    st.subheader("9. Interactive: compare two experiments")

    st.markdown("""
    Choose two experiments to compare. The app will determine which reactant
    changed and calculate the corresponding reaction order.
    """)

    exp1 = st.selectbox(
        "First experiment:",
        [1, 2, 3],
        index=0,
        key="order_exp1"
    )

    exp2 = st.selectbox(
        "Second experiment:",
        [1, 2, 3],
        index=1,
        key="order_exp2"
    )

    experiments = {
        1: {"A": 0.10, "B": 0.10, "rate": 0.020},
        2: {"A": 0.20, "B": 0.10, "rate": 0.040},
        3: {"A": 0.10, "B": 0.20, "rate": 0.080}
    }

    e1 = experiments[exp1]
    e2 = experiments[exp2]

    st.markdown("### Selected data")

    comparison_data = {
        "Experiment": [
            f"Experiment {exp1}",
            f"Experiment {exp2}"
        ],
        "[A] (mol L⁻¹)": [
            e1["A"],
            e2["A"]
        ],
        "[B] (mol L⁻¹)": [
            e1["B"],
            e2["B"]
        ],
        "Initial rate (mol L⁻¹ s⁻¹)": [
            e1["rate"],
            e2["rate"]
        ]
    }

    st.dataframe(
        comparison_data,
        use_container_width=True,
        hide_index=True
    )

    if exp1 == exp2:

        st.warning("Please choose two different experiments.")

    else:

        A_changed = not np.isclose(e1["A"], e2["A"])
        B_changed = not np.isclose(e1["B"], e2["B"])

        # -----------------------------------------------------
        # A changed, B constant
        # -----------------------------------------------------

        if A_changed and not B_changed:

            concentration_ratio = e2["A"] / e1["A"]
            rate_ratio = e2["rate"] / e1["rate"]

            st.markdown("### A changed while B remained constant")

            st.latex(
                rf"\frac{{[A]_2}}{{[A]_1}}={concentration_ratio:.2f}"
            )

            st.latex(
                rf"\frac{{\text{{rate}}_2}}{{\text{{rate}}_1}}={rate_ratio:.2f}"
            )

            if (
                concentration_ratio > 0
                and concentration_ratio != 1
                and rate_ratio > 0
            ):

                calculated_order = (
                    np.log(rate_ratio)
                    / np.log(concentration_ratio)
                )

                st.latex(
                    rf"m="
                    rf"\frac{{\ln(\text{{rate}}_2/\text{{rate}}_1)}}"
                    rf"{{\ln([A]_2/[A]_1)}}"
                    rf"={calculated_order:.2f}"
                )

                if np.isclose(
                    calculated_order,
                    round(calculated_order),
                    atol=0.05
                ):

                    order_display = int(round(calculated_order))

                    st.success(
                        f"The reaction is approximately "
                        f"**{order_display} order with respect to A**."
                    )

                else:

                    st.info(
                        f"The calculated order with respect to A is "
                        f"approximately **{calculated_order:.2f}**."
                    )

        # -----------------------------------------------------
        # B changed, A constant
        # -----------------------------------------------------

        elif B_changed and not A_changed:

            concentration_ratio = e2["B"] / e1["B"]
            rate_ratio = e2["rate"] / e1["rate"]

            st.markdown("### B changed while A remained constant")

            st.latex(
                rf"\frac{{[B]_2}}{{[B]_1}}={concentration_ratio:.2f}"
            )

            st.latex(
                rf"\frac{{\text{{rate}}_2}}{{\text{{rate}}_1}}={rate_ratio:.2f}"
            )

            if (
                concentration_ratio > 0
                and concentration_ratio != 1
                and rate_ratio > 0
            ):

                calculated_order = (
                    np.log(rate_ratio)
                    / np.log(concentration_ratio)
                )

                st.latex(
                    rf"n="
                    rf"\frac{{\ln(\text{{rate}}_2/\text{{rate}}_1)}}"
                    rf"{{\ln([B]_2/[B]_1)}}"
                    rf"={calculated_order:.2f}"
                )

                if np.isclose(
                    calculated_order,
                    round(calculated_order),
                    atol=0.05
                ):

                    order_display = int(round(calculated_order))

                    st.success(
                        f"The reaction is approximately "
                        f"**{order_display} order with respect to B**."
                    )

                else:

                    st.info(
                        f"The calculated order with respect to B is "
                        f"approximately **{calculated_order:.2f}**."
                    )

        # -----------------------------------------------------
        # Both concentrations changed
        # -----------------------------------------------------

        else:

            st.warning("""
            Both reactant concentrations changed between these experiments.

            These experiments cannot be used directly to determine the order
            with respect to a single reactant because more than one concentration
            changed.
            """)

    st.divider()

    # ---------------------------------------------------------
    # 10. Complete worked example
    # ---------------------------------------------------------

    st.subheader("10. Worked example: complete rate law")

    st.markdown("""
    From the experimental data:

    **Step 1 — Determine the order with respect to A**

    Compare Experiments 1 and 2:

    - [A] doubles
    - [B] remains constant
    - rate doubles

    Therefore:
    """)

    st.latex(r"m=1")

    st.markdown("""
    **Step 2 — Determine the order with respect to B**

    Compare Experiments 1 and 3:

    - [B] doubles
    - [A] remains constant
    - rate increases by a factor of four

    Therefore:
    """)

    st.latex(r"n=2")

    st.markdown("""
    **Step 3 — Write the rate law**
    """)

    st.latex(
        r"\boxed{\text{rate}=k[A][B]^2}"
    )

    st.markdown("""
    **Step 4 — Determine the overall order**
    """)

    st.latex(
        r"\boxed{\text{Overall order}=1+2=3}"
    )

    st.markdown("""
    **Step 5 — Calculate k**
    """)

    st.latex(
        r"\boxed{k=20\ \text{L}^2\text{mol}^{-2}\text{s}^{-1}}"
    )

    st.divider()

    # ---------------------------------------------------------
    # 11. Check your understanding
    # ---------------------------------------------------------

    st.subheader("11. Check your understanding")

    st.markdown("""
    Consider the following experimental results:
    """)

    practice_data = {
        "Experiment": [1, 2, 3],
        "[A] (mol L⁻¹)": [0.10, 0.20, 0.10],
        "[B] (mol L⁻¹)": [0.10, 0.10, 0.20],
        "Initial rate (mol L⁻¹ s⁻¹)": [0.030, 0.060, 0.120]
    }

    st.dataframe(
        practice_data,
        use_container_width=True,
        hide_index=True
    )

    question = st.selectbox(
        "What is the order with respect to A?",
        [
            "Select an answer",
            "Zero order",
            "First order",
            "Second order",
            "Third order"
        ],
        key="order_practice"
    )

    if question != "Select an answer":

        if question == "First order":

            st.success("""
            Correct. Comparing Experiments 1 and 2, [A] doubles while [B]
            remains constant. The rate also doubles, so the reaction is
            first order with respect to A.
            """)

        else:

            st.error("""
            Not quite. Compare Experiments 1 and 2: [A] doubles while [B]
            remains constant, and the rate also doubles. What does this tell
            you about the order with respect to A?
            """)

    st.divider()

    # ---------------------------------------------------------
    # 12. Key points
    # ---------------------------------------------------------

    st.subheader("Key points")

    st.markdown("""
    - Reaction order describes how the rate depends on reactant concentration.
    - The exponents in a rate law are determined experimentally.
    - To determine the order with respect to one reactant, keep the other reactant concentrations constant.
    - If doubling a concentration doubles the rate → **first order**.
    - If doubling a concentration leaves the rate unchanged → **zero order**.
    - If doubling a concentration makes the rate four times larger → **second order**.
    - Overall order is the sum of the individual orders.
    - Once the rate law is known, the rate constant \(k\) can be calculated.
    """)


elif topic == "Integrated Rate Laws":

    st.header("Integrated Rate Laws")

    st.markdown("""
    In the previous section, we used experimental data to determine the
    **order of a reaction**.

    We can now use the reaction order to describe how the concentration of a
    reactant changes with time.
    """)

    st.divider()

    # ---------------------------------------------------------
    # 1. From rate laws to integrated rate laws
    # ---------------------------------------------------------

    st.subheader("1. From rate laws to concentration vs time")

    st.markdown("""
    Consider a reaction involving one reactant:

    """)

    st.latex(r"A \rightarrow \text{products}")

    st.markdown("""
    For a reaction involving A, the rate can be written as:
    """)

    st.latex(r"\text{rate}=-\frac{d[A]}{dt}")

    st.markdown("""
    The rate law tells us how the rate depends on the concentration of A:

    """)

    st.latex(r"\text{rate}=k[A]^n")

    st.markdown("""
    Combining these gives:
    """)

    st.latex(r"-\frac{d[A]}{dt}=k[A]^n")

    st.markdown("""
    **Integrated rate laws** are obtained by integrating this rate equation.
    They allow us to calculate the concentration of a reactant at a given
    time, or determine how concentration changes with time.
    """)

    st.info("""
    The integrated rate law that applies depends on the **order of the reaction**.
    """)

    st.divider()

    # ---------------------------------------------------------
    # 2. Zero-order reactions
    # ---------------------------------------------------------

    st.subheader("2. Zero-order reactions")

    st.markdown("""
    For a zero-order reaction:
    """)

    st.latex(r"\text{rate}=k[A]^0=k")

    st.markdown("""
    Therefore:
    """)

    st.latex(r"-\frac{d[A]}{dt}=k")

    st.markdown("""
    Integrating gives the zero-order integrated rate law:
    """)

    st.latex(
        r"\boxed{[A]_t=[A]_0-kt}"
    )

    st.markdown("""
    where:

    - \([A]_0\) = initial concentration of A
    - \([A]_t\) = concentration of A at time \(t\)
    - \(k\) = rate constant
    - \(t\) = time
    """)

    st.markdown("""
    A plot of **[A] against time** is therefore a straight line for a
    zero-order reaction.
    """)

    # Interactive zero order graph
    st.markdown("### Zero-order concentration–time graph")

    zero_k = st.slider(
        "Rate constant, k (mol L⁻¹ s⁻¹)",
        min_value=0.005,
        max_value=0.050,
        value=0.020,
        step=0.005,
        key="zero_order_k"
    )

    zero_A0 = st.slider(
        "Initial concentration, [A]₀ (mol L⁻¹)",
        min_value=0.20,
        max_value=1.00,
        value=0.80,
        step=0.10,
        key="zero_order_A0"
    )

    zero_time = np.linspace(0, zero_A0 / zero_k, 100)

    zero_concentration = zero_A0 - zero_k * zero_time

    fig, ax = plt.subplots()

    ax.plot(
        zero_time,
        zero_concentration
    )

    ax.set_xlabel("Time (s)")
    ax.set_ylabel("[A] (mol L⁻¹)")
    ax.set_title("Zero-order reaction")
    ax.set_ylim(bottom=0)
    ax.grid(True, alpha=0.3)

    st.pyplot(fig)

    st.latex(
        rf"[A]_t={zero_A0:.2f}-{zero_k:.3f}t"
    )

    st.divider()

    # ---------------------------------------------------------
    # 3. First-order reactions
    # ---------------------------------------------------------

    st.subheader("3. First-order reactions")

    st.markdown("""
    For a first-order reaction:
    """)

    st.latex(r"\text{rate}=k[A]")

    st.markdown("""
    Therefore:
    """)

    st.latex(r"-\frac{d[A]}{dt}=k[A]")

    st.markdown("""
    Integrating gives:
    """)

    st.latex(
        r"\boxed{\ln[A]_t=\ln[A]_0-kt}"
    )

    st.markdown("""
    An equivalent form is:
    """)

    st.latex(
        r"\boxed{[A]_t=[A]_0e^{-kt}}"
    )

    st.markdown("""
    For a first-order reaction, a plot of **ln[A] against time** is a
    straight line.

    The gradient of this line is:
    """)

    st.latex(r"\boxed{\text{gradient}=-k}")

    # Interactive first order graph
    st.markdown("### First-order concentration–time graph")

    first_k = st.slider(
        "Rate constant, k (s⁻¹)",
        min_value=0.005,
        max_value=0.100,
        value=0.020,
        step=0.005,
        key="first_order_k"
    )

    first_A0 = st.slider(
        "Initial concentration, [A]₀ (mol L⁻¹)",
        min_value=0.20,
        max_value=1.00,
        value=0.80,
        step=0.10,
        key="first_order_A0"
    )

    first_time = np.linspace(
        0,
        5 / first_k,
        150
    )

    first_concentration = first_A0 * np.exp(-first_k * first_time)

    fig, ax = plt.subplots()

    ax.plot(
        first_time,
        first_concentration
    )

    ax.set_xlabel("Time (s)")
    ax.set_ylabel("[A] (mol L⁻¹)")
    ax.set_title("First-order reaction")
    ax.set_ylim(bottom=0)
    ax.grid(True, alpha=0.3)

    st.pyplot(fig)

    st.latex(
        rf"[A]_t={first_A0:.2f}e^{{-{first_k:.3f}t}}"
    )

    st.divider()

    # ---------------------------------------------------------
    # 4. Second-order reactions
    # ---------------------------------------------------------

    st.subheader("4. Second-order reactions")

    st.markdown("""
    For a second-order reaction involving A:
    """)

    st.latex(r"\text{rate}=k[A]^2")

    st.markdown("""
    Therefore:
    """)

    st.latex(r"-\frac{d[A]}{dt}=k[A]^2")

    st.markdown("""
    Integrating gives:
    """)

    st.latex(
        r"\boxed{\frac{1}{[A]_t}=\frac{1}{[A]_0}+kt}"
    )

    st.markdown("""
    For a second-order reaction, a plot of **1/[A] against time** is a
    straight line.

    The gradient of this line is:
    """)

    st.latex(r"\boxed{\text{gradient}=k}")

    # Interactive second order graph
    st.markdown("### Second-order concentration–time graph")

    second_k = st.slider(
        "Rate constant, k (L mol⁻¹ s⁻¹)",
        min_value=0.005,
        max_value=0.100,
        value=0.020,
        step=0.005,
        key="second_order_k"
    )

    second_A0 = st.slider(
        "Initial concentration, [A]₀ (mol L⁻¹)",
        min_value=0.20,
        max_value=1.00,
        value=0.80,
        step=0.10,
        key="second_order_A0"
    )

    second_time = np.linspace(
        0,
        1 / (second_k * second_A0) * 5,
        150
    )

    second_concentration = (
        1 /
        (
            1 / second_A0
            + second_k * second_time
        )
    )

    fig, ax = plt.subplots()

    ax.plot(
        second_time,
        second_concentration
    )

    ax.set_xlabel("Time (s)")
    ax.set_ylabel("[A] (mol L⁻¹)")
    ax.set_title("Second-order reaction")
    ax.set_ylim(bottom=0)
    ax.grid(True, alpha=0.3)

    st.pyplot(fig)

    st.latex(
        rf"\frac{{1}}{{[A]_t}}="
        rf"\frac{{1}}{{{second_A0:.2f}}}"
        rf"+{second_k:.3f}t"
    )

    st.divider()

    # ---------------------------------------------------------
    # 5. Comparing the three integrated rate laws
    # ---------------------------------------------------------

    st.subheader("5. Comparing the integrated rate laws")

    comparison_data = {
        "Reaction order": [
            "Zero order",
            "First order",
            "Second order"
        ],
        "Integrated rate law": [
            "[A]ₜ = [A]₀ − kt",
            "ln[A]ₜ = ln[A]₀ − kt",
            "1/[A]ₜ = 1/[A]₀ + kt"
        ],
        "Linear plot": [
            "[A] vs time",
            "ln[A] vs time",
            "1/[A] vs time"
        ],
        "Gradient": [
            "−k",
            "−k",
            "+k"
        ]
    }

    st.table(comparison_data)

    st.markdown("""
    This gives us a useful way to identify reaction order from concentration–
    time data: determine which transformed concentration gives a straight line.
    """)

    st.divider()

    # ---------------------------------------------------------
    # 6. Half-life
    # ---------------------------------------------------------

    st.subheader("6. Half-life")

    st.markdown("""
    The **half-life**, \(t_{1/2}\), is the time required for the concentration
    of a reactant to decrease to half of its initial value.
    """)

    st.latex(
        r"[A]_t=\frac{[A]_0}{2}"
    )

    st.markdown("""
    The half-life behaves differently for different reaction orders.
    """)

    half_life_choice = st.selectbox(
        "Choose a reaction order:",
        ["Zero order", "First order", "Second order"],
        key="half_life_order"
    )

    if half_life_choice == "Zero order":

        st.latex(
            r"\boxed{t_{1/2}=\frac{[A]_0}{2k}}"
        )

        st.markdown("""
        For a zero-order reaction, the half-life **depends on the initial
        concentration**.

        A larger initial concentration gives a longer half-life.
        """)

    elif half_life_choice == "First order":

        st.latex(
            r"\boxed{t_{1/2}=\frac{\ln 2}{k}}"
        )

        st.markdown("""
        For a first-order reaction, the half-life **does not depend on the
        initial concentration**.

        As long as the temperature and conditions remain constant, the
        half-life remains constant.
        """)

    else:

        st.latex(
            r"\boxed{t_{1/2}=\frac{1}{k[A]_0}}"
        )

        st.markdown("""
        For a second-order reaction, the half-life **depends on the initial
        concentration**.
        """)

    st.divider()

    # ---------------------------------------------------------
    # 7. Interactive half-life calculator
    # ---------------------------------------------------------

    st.subheader("7. Interactive half-life calculator")

    half_order = st.selectbox(
        "Reaction order:",
        ["Zero order", "First order", "Second order"],
        key="half_order_calc"
    )

    half_A0 = st.number_input(
        "Initial concentration, [A]₀ (mol L⁻¹)",
        min_value=0.01,
        max_value=5.00,
        value=1.00,
        step=0.10,
        key="half_A0_calc"
    )

    if half_order == "Zero order":

        half_k = st.number_input(
            "Rate constant, k (mol L⁻¹ s⁻¹)",
            min_value=0.001,
            max_value=10.0,
            value=0.050,
            step=0.001,
            format="%.3f",
            key="half_zero_k"
        )

        half_life = half_A0 / (2 * half_k)

        st.latex(
            r"t_{1/2}=\frac{[A]_0}{2k}"
        )

        st.metric(
            "Half-life",
            f"{half_life:.2f} s"
        )

    elif half_order == "First order":

        half_k = st.number_input(
            "Rate constant, k (s⁻¹)",
            min_value=0.001,
            max_value=10.0,
            value=0.050,
            step=0.001,
            format="%.3f",
            key="half_first_k"
        )

        half_life = np.log(2) / half_k

        st.latex(
            r"t_{1/2}=\frac{\ln 2}{k}"
        )

        st.metric(
            "Half-life",
            f"{half_life:.2f} s"
        )

    else:

        half_k = st.number_input(
            "Rate constant, k (L mol⁻¹ s⁻¹)",
            min_value=0.001,
            max_value=10.0,
            value=0.050,
            step=0.001,
            format="%.3f",
            key="half_second_k"
        )

        half_life = 1 / (half_k * half_A0)

        st.latex(
            r"t_{1/2}=\frac{1}{k[A]_0}"
        )

        st.metric(
            "Half-life",
            f"{half_life:.2f} s"
        )

    st.divider()

    # ---------------------------------------------------------
    # 8. Important comparison
    # ---------------------------------------------------------

    st.subheader("8. An important difference between reaction orders")

    st.markdown("""
    Half-life provides a particularly useful way to distinguish a
    first-order reaction from zero- and second-order reactions.
    """)

    st.info("""
    **First-order reaction**

    The half-life is constant and does not depend on the initial concentration.

    **Zero- and second-order reactions**

    The half-life depends on the initial concentration.
    """)

    st.divider()

    # ---------------------------------------------------------
    # 9. Check your understanding
    # ---------------------------------------------------------

    st.subheader("9. Check your understanding")

    question = st.selectbox(
        "Which integrated rate law applies to a first-order reaction?",
        [
            "Select an answer",
            "[A]ₜ = [A]₀ − kt",
            "ln[A]ₜ = ln[A]₀ − kt",
            "1/[A]ₜ = 1/[A]₀ + kt"
        ],
        key="integrated_rate_question"
    )

    if question != "Select an answer":

        if question == "ln[A]ₜ = ln[A]₀ − kt":

            st.success("""
            Correct. For a first-order reaction:

            ln[A]ₜ = ln[A]₀ − kt
            """)

        else:

            st.error("""
            Not quite. Recall that each reaction order has its own integrated
            rate law. For a first-order reaction, the logarithm of concentration
            appears in the equation.
            """)

    st.divider()

    # ---------------------------------------------------------
    # 10. Key points
    # ---------------------------------------------------------

    st.subheader("Key points")

    st.markdown("""
    - Integrated rate laws describe how concentration changes with time.
    - The integrated rate law depends on the reaction order.
    - Zero order: \([A]_t=[A]_0-kt\)
    - First order: \(\ln[A]_t=\ln[A]_0-kt\)
    - Second order: \(1/[A]_t=1/[A]_0+kt\)
    - The gradient of the appropriate linear plot can be used to determine \(k\).
    - Half-life is the time required for a reactant concentration to decrease to half its initial value.
    - First-order reactions have a constant half-life that is independent of initial concentration.
    """)


elif topic == "Arrhenius Equation":

    st.header("Arrhenius Equation")

    st.markdown("""
    ### Why does temperature affect reaction rate?

    Temperature affects the rate constant, **k**, and therefore affects the rate of a chemical reaction.

    The Arrhenius equation describes how the rate constant depends on temperature and activation energy.
    """)

    st.markdown("### Activation Energy")

    st.markdown("""
    The **activation energy**, \(E_a\), is the minimum energy required for reactant particles
    to reach the activated state needed for a reaction to occur.

    From the Arrhenius equation:
    """)

    st.latex(
        r"k=Ae^{-E_a/(RT)}"
    )

    st.markdown("""
    The exponential term is:
    """)

    st.latex(
        r"e^{-E_a/(RT)}"
    )

    st.markdown("""
    When temperature increases, the magnitude of the negative exponent decreases.
    Therefore, the value of the exponential term increases.

    As a result, **k increases**.
    """)

    st.latex(
        r"\boxed{T\uparrow\quad\Rightarrow\quad k\uparrow\quad\Rightarrow\quad \text{reaction rate generally increases}}"
    )

    st.markdown("---")

    st.markdown("### Understanding the effect of temperature")

    st.markdown("""
    At a higher temperature, particles have a wider range of energies and a greater
    fraction of particles have energy equal to or greater than the activation energy, \(E_a\).

    This increases the number of effective collisions and therefore generally increases
    the reaction rate.
    """)

    # Conceptual energy distribution graph
    energy = np.linspace(0, 200, 500)

    T1 = 1.0
    T2 = 1.35

    distribution_low = energy * np.exp(-energy / (40 * T1))
    distribution_high = energy * np.exp(-energy / (40 * T2))

    Ea_visual = 80

    fig, ax = plt.subplots(figsize=(9, 4.5))

    ax.plot(
        energy,
        distribution_low,
        label="Lower temperature"
    )

    ax.plot(
        energy,
        distribution_high,
        label="Higher temperature"
    )

    ax.axvline(
        Ea_visual,
        linestyle="--",
        label=r"$E_a$"
    )

    ax.set_xlabel("Energy")
    ax.set_ylabel("Relative number of particles")
    ax.set_title("Effect of Temperature on the Energy Distribution")
    ax.legend()
    ax.grid(alpha=0.25)

    st.pyplot(fig)

    st.info(
        "At higher temperature, a greater fraction of particles has energy equal to or greater than Ea."
    )

    st.markdown("---")

    st.markdown("### The Arrhenius Equation")

    st.markdown("""
    The Arrhenius equation is:
    """)

    st.latex(
        r"\boxed{k=Ae^{-E_a/(RT)}}"
    )

    st.markdown("""
    where:

    - **k** = rate constant
    - **A** = frequency factor
    - **\(E_a\)** = activation energy
    - **R** = gas constant = \(8.314\ \mathrm{J\,mol^{-1}\,K^{-1}}\)
    - **T** = absolute temperature in kelvin (K)

    The activation energy must be expressed in units consistent with the value of \(R\).
    Therefore, when using \(R=8.314\ \mathrm{J\,mol^{-1}\,K^{-1}}\), \(E_a\) must be in J mol⁻¹.
    """)

    st.markdown("---")

    st.markdown("### Interactive Arrhenius Explorer")

    Ea_kJ = st.slider(
        "Activation energy, Ea (kJ mol⁻¹)",
        min_value=10.0,
        max_value=150.0,
        value=50.0,
        step=5.0
    )

    temperature_C = st.slider(
        "Temperature (°C)",
        min_value=0.0,
        max_value=150.0,
        value=25.0,
        step=5.0
    )

    R = 8.314
    A_factor = 1.0e10

    temperature_K = temperature_C + 273.15
    Ea_J = Ea_kJ * 1000

    k_value = A_factor * np.exp(
        -Ea_J / (R * temperature_K)
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Temperature",
            f"{temperature_K:.2f} K"
        )

    with col2:
        st.metric(
            "Activation energy",
            f"{Ea_kJ:.1f} kJ mol⁻¹"
        )

    with col3:
        st.metric(
            "Rate constant, k",
            f"{k_value:.3e}"
        )

    temperatures_C = np.linspace(0, 150, 300)
    temperatures_K = temperatures_C + 273.15

    k_values = A_factor * np.exp(
        -Ea_J / (R * temperatures_K)
    )

    fig, ax = plt.subplots(figsize=(9, 4.5))

    ax.plot(
        temperatures_C,
        k_values
    )

    ax.scatter(
        [temperature_C],
        [k_value],
        s=80,
        zorder=5
    )

    ax.set_xlabel("Temperature (°C)")
    ax.set_ylabel("Rate constant, k")
    ax.set_title("Arrhenius Relationship")
    ax.grid(alpha=0.25)

    st.pyplot(fig)

    st.markdown("""
    **Observation:** As temperature increases, the rate constant increases.
    The effect becomes particularly important when the activation energy is large.
    """)

    st.markdown("---")

    st.markdown("### Two-Temperature Form of the Arrhenius Equation")

    st.markdown("""
    Sometimes the rate constant is known at two different temperatures.
    In this case, the Arrhenius equation can be written in a form that allows the
    activation energy to be calculated without knowing the frequency factor, \(A\).
    """)

    st.latex(
        r"\boxed{\ln\left(\frac{k_2}{k_1}\right)=-\frac{E_a}{R}\left(\frac{1}{T_2}-\frac{1}{T_1}\right)}"
    )

    st.markdown("""
    Rearranging gives:
    """)

    st.latex(
        r"\boxed{E_a=-R\frac{\ln(k_2/k_1)}{(1/T_2)-(1/T_1)}}"
    )

    st.markdown("""
    Remember that the temperatures must be expressed in **kelvin**, not degrees Celsius.
    """)

    st.markdown("---")

    st.markdown("### Worked Example: Calculating Activation Energy")

    st.markdown("""
    A reaction has a rate constant of \(0.0020\ \mathrm{s^{-1}}\) at 298.15 K
    and \(0.0100\ \mathrm{s^{-1}}\) at 318.15 K.

    Calculate the activation energy.
    """)

    k1 = 0.0020
    k2 = 0.0100
    T1 = 298.15
    T2 = 318.15

    Ea_example = (
        -R
        * np.log(k2 / k1)
        / ((1 / T2) - (1 / T1))
    )

    Ea_example_kJ = Ea_example / 1000

    st.latex(
        r"E_a=-R\frac{\ln(k_2/k_1)}{(1/T_2)-(1/T_1)}"
    )

    st.markdown(f"""
    Substituting the values:
    """)

    st.latex(
        rf"E_a={Ea_example_kJ:.1f}\ \mathrm{{kJ\,mol^{{-1}}}}"
    )

    st.success(
        f"The activation energy is approximately {Ea_example_kJ:.1f} kJ mol⁻¹."
    )

    st.markdown("---")

    st.markdown("### Linear Form of the Arrhenius Equation")

    st.markdown("""
    The Arrhenius equation can also be rearranged into a linear form.
    """)

    st.latex(
        r"\boxed{\ln k=\ln A-\frac{E_a}{R}\frac{1}{T}}"
    )

    st.markdown("""
    This has the same form as the equation of a straight line:

    \[
    y=mx+c
    \]

    Therefore:

    - \(y=\ln k\)
    - \(x=1/T\)
    - gradient \(=-E_a/R\)
    - intercept \(=\ln A\)
    """)

    st.latex(
        r"\boxed{\text{gradient}=-\frac{E_a}{R}}"
    )

    st.markdown("""
    Therefore, if a graph of **ln k against 1/T** is a straight line,
    the activation energy can be obtained from the gradient.
    """)

    st.markdown("---")

    st.markdown("### Interactive Arrhenius Plot")

    Ea_plot_kJ = st.slider(
        "Choose activation energy for the Arrhenius plot (kJ mol⁻¹)",
        min_value=20.0,
        max_value=120.0,
        value=60.0,
        step=5.0
    )

    Ea_plot_J = Ea_plot_kJ * 1000

    T_plot = np.linspace(280, 380, 100)

    ln_k_plot = (
        np.log(A_factor)
        - Ea_plot_J / (R * T_plot)
    )

    inverse_T = 1 / T_plot

    fig, ax = plt.subplots(figsize=(9, 4.5))

    ax.plot(
        inverse_T,
        ln_k_plot
    )

    ax.set_xlabel("1/T (K⁻¹)")
    ax.set_ylabel("ln k")
    ax.set_title("Linear Arrhenius Plot")
    ax.grid(alpha=0.25)

    st.pyplot(fig)

    gradient = -Ea_plot_J / R

    st.write(
        f"Gradient = {gradient:.3e} K"
    )

    st.markdown("""
    The gradient is negative because \(k\) increases as temperature increases,
    while \(1/T\) decreases.
    """)

    st.markdown("---")

    st.markdown("### Check Your Understanding")

    q1 = st.radio(
        "1. What happens to the rate constant when temperature increases?",
        [
            "It generally increases",
            "It always decreases",
            "It remains unchanged",
            "It becomes zero"
        ],
        key="arrhenius_q1"
    )

    if q1 == "It generally increases":
        st.success("Correct. Increasing temperature generally increases k.")
    else:
        st.error("Not quite. According to the Arrhenius equation, increasing temperature generally increases k.")

    q2 = st.radio(
        "2. Which temperature unit should be used in the Arrhenius equation?",
        [
            "°C",
            "K",
            "°F",
            "Any temperature scale"
        ],
        key="arrhenius_q2"
    )

    if q2 == "K":
        st.success("Correct. Temperature must be expressed in kelvin.")
    else:
        st.error("Not quite. Temperature must be expressed in kelvin.")

    q3 = st.radio(
        "3. What does the gradient of a plot of ln k against 1/T represent?",
        [
            r"$-E_a/R$",
            r"$E_a/R$",
            r"$-R/E_a$",
            r"$E_a$"
        ],
        key="arrhenius_q3"
    )

    if q3 == r"$-E_a/R$":
        st.success("Correct. The gradient is −Ea/R.")
    else:
        st.error("Not quite. The gradient of an ln k versus 1/T plot is −Ea/R.")

    st.markdown("---")

    st.markdown("### Key Points")

    st.markdown("""
    - The **Arrhenius equation** relates the rate constant to temperature and activation energy.
    - Increasing temperature generally increases the **rate constant, k**.
    - \(E_a\) is the activation energy.
    - Temperature must be expressed in **kelvin**.
    - When \(R=8.314\ \mathrm{J\,mol^{-1}\,K^{-1}}\), \(E_a\) must be in **J mol⁻¹**.
    - The two-temperature form allows \(E_a\) to be calculated from two values of \(k\).
    - A plot of **ln k against 1/T** has gradient \(-E_a/R\).
    """)
    
elif topic == "Catalysts":

    st.header("Catalysts")

    st.markdown("""
    ### What is a catalyst?

    A **catalyst** is a substance that increases the rate of a chemical reaction
    without being consumed overall in the reaction.

    A catalyst works by providing an **alternative reaction pathway with a lower
    activation energy, \(E_a\)**.
    """)

    st.latex(
        r"\boxed{\text{Catalyst}\quad\Rightarrow\quad E_a\downarrow\quad\Rightarrow\quad k\uparrow\quad\Rightarrow\quad \text{reaction rate}\uparrow}"
    )

    st.markdown("""
    The catalyst does **not** provide extra energy to the reactant particles.
    Instead, it changes the pathway by which the reaction occurs.
    """)

    st.markdown("---")

    st.markdown("### How does a catalyst work?")

    st.markdown("""
    For a reaction to occur, reactant particles must pass through a high-energy
    transition state.

    Without a catalyst, the reaction follows one pathway with a particular
    activation energy.

    A catalyst provides an alternative pathway with a **lower activation energy**.
    """)

    st.markdown("""
    The diagram below compares the energy profile of a reaction with and without
    a catalyst.
    """)

    # Energy profile
    reaction_coordinate = np.linspace(0, 1, 400)

    reactant_energy = 1.0
    product_energy = 0.35

    # Uncatalysed pathway
    uncatalysed = (
        reactant_energy
        + (1.75 - reactant_energy)
        * np.exp(-((reaction_coordinate - 0.48) / 0.18) ** 2)
        - (reactant_energy - product_energy) * reaction_coordinate
    )

    # Catalysed pathway
    catalysed = (
        reactant_energy
        + (1.38 - reactant_energy)
        * np.exp(-((reaction_coordinate - 0.48) / 0.18) ** 2)
        - (reactant_energy - product_energy) * reaction_coordinate
    )

    fig, ax = plt.subplots(figsize=(9, 5))

    ax.plot(
        reaction_coordinate,
        uncatalysed,
        label="Uncatalysed pathway"
    )

    ax.plot(
        reaction_coordinate,
        catalysed,
        label="Catalysed pathway"
    )

    ax.axhline(
        reactant_energy,
        linestyle="--",
        alpha=0.5
    )

    ax.axhline(
        product_energy,
        linestyle="--",
        alpha=0.5
    )

    ax.set_xlabel("Reaction coordinate")
    ax.set_ylabel("Potential energy")
    ax.set_title("Catalysed and Uncatalysed Reaction Pathways")
    ax.legend()
    ax.grid(alpha=0.25)

    st.pyplot(fig)

    st.markdown("""
    Notice that the **reactant and product energy levels are the same** for both
    pathways.

    The catalyst changes the height of the energy barrier, but it does not change
    the energy difference between reactants and products.
    """)

    st.markdown("---")

    st.markdown("### Activation Energy and a Catalyst")

    st.markdown("""
    Activation energy is measured from the reactant energy level to the highest
    point of the reaction pathway.
    """)

    st.latex(
        r"\boxed{E_a=E_{\text{transition state}}-E_{\text{reactants}}}"
    )

    st.markdown("""
    Because the catalysed pathway has a lower maximum energy, its activation energy
    is smaller.
    """)

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Uncatalysed activation energy",
            "Higher"
        )

    with col2:
        st.metric(
            "Catalysed activation energy",
            "Lower"
        )

    st.markdown("---")

    st.markdown("### Connection to the Arrhenius Equation")

    st.markdown("""
    The Arrhenius equation shows why lowering the activation energy increases the
    rate constant:
    """)

    st.latex(
        r"\boxed{k=Ae^{-E_a/(RT)}}"
    )

    st.markdown("""
    At the same temperature, lowering \(E_a\) makes the negative exponent less
    negative.

    Therefore, the exponential term becomes larger and the rate constant increases.
    """)

    st.latex(
        r"\boxed{E_a\downarrow\quad\Rightarrow\quad k\uparrow}"
    )

    st.markdown("""
    Therefore, a catalyst can increase the reaction rate by lowering the activation
    energy of the reaction pathway.
    """)

    st.markdown("---")

    st.markdown("### Interactive Catalyst Explorer")

    Ea_uncatalysed = st.slider(
        "Uncatalysed activation energy (kJ mol⁻¹)",
        min_value=20.0,
        max_value=150.0,
        value=80.0,
        step=5.0
    )

    catalyst_reduction = st.slider(
        "Reduction in activation energy provided by catalyst (kJ mol⁻¹)",
        min_value=5.0,
        max_value=70.0,
        value=30.0,
        step=5.0
    )

    Ea_catalysed = max(
        Ea_uncatalysed - catalyst_reduction,
        5.0
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Uncatalysed Ea",
            f"{Ea_uncatalysed:.0f} kJ mol⁻¹"
        )

    with col2:
        st.metric(
            "Catalysed Ea",
            f"{Ea_catalysed:.0f} kJ mol⁻¹"
        )

    st.latex(
        rf"\boxed{{\Delta E_a={Ea_uncatalysed:.0f}-{Ea_catalysed:.0f}={Ea_uncatalysed-Ea_catalysed:.0f}\ \mathrm{{kJ\,mol^{{-1}}}}}}"
    )

    st.markdown("---")

    st.markdown("### What a Catalyst Does NOT Change")

    st.markdown("""
    A catalyst changes the **reaction pathway**, but it does not change the
    overall energy difference between reactants and products.
    """)

    comparison_data = {
        "Property": [
            "Activation energy, Ea",
            "Reaction pathway",
            "Overall ΔH",
            "Reactant energy",
            "Product energy",
            "Equilibrium constant, K",
            "Equilibrium position"
        ],
        "Effect of catalyst": [
            "Decreases",
            "Changes",
            "No change",
            "No change",
            "No change",
            "No change",
            "No change"
        ]
    }

    st.table(comparison_data)

    st.markdown("""
    **Important:** A catalyst speeds up both the forward and reverse reactions.
    Therefore, it does not change the equilibrium position or the equilibrium
    constant. It simply allows equilibrium to be reached more quickly.
    """)

    st.markdown("---")

    st.markdown("### Catalysts and Collision Theory")

    st.markdown("""
    Collision theory states that a successful reaction requires particles to collide
    with sufficient energy and appropriate orientation.

    A catalyst provides an alternative pathway with a lower activation energy.

    Therefore, at the same temperature, a greater fraction of collisions can have
    sufficient energy to overcome the activation-energy barrier.
    """)

    st.latex(
        r"\boxed{\text{Catalyst}\quad\Rightarrow\quad E_a\downarrow\quad\Rightarrow\quad \text{more effective collisions}}"
    )

    st.markdown("""
    The catalyst does not make the particles move faster and does not increase the
    temperature. Instead, it makes it easier for collisions to lead to reaction.
    """)

    st.markdown("---")

    st.markdown("### Examples of Catalysts")

    catalyst_examples = {
        "Catalyst": [
            "Iron (Fe)",
            "Nickel (Ni)",
            "Platinum (Pt)",
            "Enzymes"
        ],
        "Example application": [
            "Ammonia production",
            "Hydrogenation reactions",
            "Catalytic converters",
            "Biological reactions"
        ]
    }

    st.table(catalyst_examples)

    st.markdown("""
    **Enzymes** are biological catalysts. They increase the rates of biochemical
    reactions by providing reaction pathways with lower activation energies.
    """)

    st.markdown("---")

    st.markdown("### Check Your Understanding")

    catalyst_q1 = st.radio(
        "1. What is the main effect of a catalyst?",
        [
            "It lowers the activation energy",
            "It increases the temperature",
            "It increases the ΔH of the reaction",
            "It increases the energy of every reactant particle"
        ],
        key="catalyst_q1"
    )

    if catalyst_q1 == "It lowers the activation energy":
        st.success("Correct. A catalyst provides an alternative pathway with a lower activation energy.")
    else:
        st.error("Not quite. A catalyst works by providing an alternative pathway with a lower activation energy.")

    catalyst_q2 = st.radio(
        "2. What happens to the overall ΔH of a reaction when a catalyst is added?",
        [
            "It increases",
            "It decreases",
            "It does not change",
            "It becomes zero"
        ],
        key="catalyst_q2"
    )

    if catalyst_q2 == "It does not change":
        st.success("Correct. A catalyst changes the pathway, not the overall energy difference between reactants and products.")
    else:
        st.error("Not quite. A catalyst does not change the overall ΔH of the reaction.")

    catalyst_q3 = st.radio(
        "3. Does a catalyst change the equilibrium constant?",
        [
            "Yes, it increases K",
            "Yes, it decreases K",
            "No, it does not change K",
            "It makes K equal to zero"
        ],
        key="catalyst_q3"
    )

    if catalyst_q3 == "No, it does not change K":
        st.success("Correct. A catalyst speeds up both the forward and reverse reactions and does not change K.")
    else:
        st.error("Not quite. A catalyst does not change the equilibrium constant.")

    catalyst_q4 = st.radio(
        "4. Why does a catalyst increase the reaction rate?",
        [
            "It provides an alternative pathway with lower Ea",
            "It increases the concentration of reactants",
            "It increases the temperature",
            "It changes the products into reactants"
        ],
        key="catalyst_q4"
    )

    if catalyst_q4 == "It provides an alternative pathway with lower Ea":
        st.success("Correct. The lower activation energy means a greater fraction of collisions can result in reaction.")
    else:
        st.error("Not quite. The catalyst provides an alternative pathway with a lower activation energy.")

    st.markdown("---")

    st.markdown("### Key Points")

    st.markdown("""
    - A **catalyst increases the rate of a reaction**.
    - A catalyst provides an **alternative reaction pathway**.
    - The alternative pathway has a **lower activation energy, Ea**.
    - A catalyst does **not** change the overall **ΔH** of the reaction.
    - A catalyst does **not** change the reactant or product energy levels.
    - A catalyst does **not** change the **equilibrium constant, K**.
    - A catalyst allows equilibrium to be reached **more quickly**.
    - Catalysts increase reaction rate without being consumed overall.
    """)

elif topic == "Reaction Mechanisms":

    st.header("Reaction Mechanisms")

    st.markdown("""
    ### What is a reaction mechanism?

    A **reaction mechanism** describes the individual steps by which a chemical
    reaction occurs.

    A chemical reaction that appears to occur in one step in the overall equation
    may actually occur through several smaller steps called **elementary steps**.
    """)

    st.markdown("### Overall Reaction vs Reaction Mechanism")

    st.markdown("""
    Consider the overall reaction:
    """)

    st.latex(
        r"\boxed{A+B\rightarrow C}"
    )

    st.markdown("""
    This equation tells us the overall change in reactants and products.

    It does **not necessarily tell us how the reaction occurs at the molecular level**.
    """)

    st.markdown("""
    For example, the reaction could occur through two elementary steps:
    """)

    st.latex(
        r"A+B\rightarrow I"
    )

    st.latex(
        r"I\rightarrow C"
    )

    st.markdown("""
    Here, **I** is a reaction intermediate.
    """)

    st.markdown("---")

    st.markdown("### Elementary Steps")

    st.markdown("""
    An **elementary step** represents a single molecular event in a reaction
    mechanism.

    For an elementary step, the rate law can be related directly to the reacting
    species in that step.
    """)

    st.markdown("For example:")

    st.latex(
        r"A+B\rightarrow C"
    )

    st.markdown("""
    For this elementary step, the rate law is:
    """)

    st.latex(
        r"\boxed{\text{rate}=k[A][B]}"
    )

    st.markdown("""
    This is different from an overall reaction, where the experimentally determined
    rate law may not be directly related to the coefficients in the overall balanced
    equation.
    """)

    st.info(
        "The coefficients in an overall chemical equation cannot generally be used directly as exponents in the rate law."
    )

    st.markdown("---")

    st.markdown("### Reaction Intermediates")

    st.markdown("""
    A **reaction intermediate** is a species that is produced in one elementary step
    and consumed in a later step.

    It appears in the mechanism but does **not appear in the overall reaction**.
    """)

    st.markdown("Consider the mechanism:")

    st.latex(
        r"A+B\rightarrow I"
    )

    st.latex(
        r"I+D\rightarrow C"
    )

    st.markdown("""
    Adding the two elementary steps gives:
    """)

    st.latex(
        r"A+B+I+D\rightarrow I+C"
    )

    st.markdown("""
    The intermediate \(I\) appears on both sides and cancels:
    """)

    st.latex(
        r"\boxed{A+B+D\rightarrow C}"
    )

    st.markdown("""
    Therefore, \(I\) is an **intermediate**.
    """)

    st.markdown("---")

    st.markdown("### Identifying an Intermediate")

    st.markdown("""
    An intermediate:

    - is **formed** in one step,
    - is **consumed** in a later step,
    - does not appear in the overall reaction.
    """)

    mechanism_data = {
        "Species": [
            "A",
            "B",
            "I",
            "D",
            "C"
        ],
        "Role": [
            "Reactant",
            "Reactant",
            "Intermediate",
            "Reactant",
            "Product"
        ]
    }

    st.table(mechanism_data)

    st.markdown("---")

    st.markdown("### Slow and Fast Elementary Steps")

    st.markdown("""
    Different elementary steps can occur at different rates.

    A reaction mechanism may contain:

    - a **fast step**, which occurs relatively quickly
    - a **slow step**, which occurs relatively slowly
    """)

    st.markdown("""
    Consider the mechanism:
    """)

    st.latex(
        r"A+B\rightarrow I\qquad\text{fast}"
    )

    st.latex(
        r"I+D\rightarrow C\qquad\text{slow}"
    )

    st.markdown("""
    The slow step is often important in determining the overall reaction rate.
    """)

    st.markdown("---")

    st.markdown("### Rate-Determining Step")

    st.markdown("""
    The **rate-determining step** is the slow step in a simplified mechanism that
    limits the overall rate of the reaction.

    Because this step is slow, the reaction cannot proceed overall much faster than
    this step allows.
    """)

    st.latex(
        r"\boxed{\text{Slow step}\quad\Rightarrow\quad\text{rate-determining step}}"
    )

    st.warning(
        "For more complicated mechanisms, determining the rate law from a mechanism can require additional kinetic analysis. The slow-step approximation is a useful introductory model."
    )

    st.markdown("---")

    st.markdown("### Worked Example")

    st.markdown("""
    Consider the mechanism:
    """)

    st.latex(
        r"A+B\rightarrow I\qquad\text{slow}"
    )

    st.latex(
        r"I\rightarrow C\qquad\text{fast}"
    )

    st.markdown("""
    The slow step is the first step, so it is the rate-determining step.

    For this elementary slow step:
    """)

    st.latex(
        r"\boxed{\text{rate}=k[A][B]}"
    )

    st.markdown("""
    Notice that the intermediate \(I\) does not appear in the rate law because it is
    formed in the first step and consumed in the second step.
    """)

    st.markdown("---")

    st.markdown("### Interactive Mechanism Explorer")

    mechanism_choice = st.selectbox(
        "Choose a mechanism:",
        [
            "One-step reaction",
            "Two-step reaction with an intermediate",
            "Two-step reaction with a slow first step"
        ],
        key="mechanism_choice"
    )

    if mechanism_choice == "One-step reaction":

        st.markdown("#### Mechanism")

        st.latex(
            r"A+B\rightarrow C"
        )

        st.markdown("""
        This mechanism contains one elementary step.
        """)

        st.latex(
            r"\boxed{\text{rate}=k[A][B]}"
        )

        st.success(
            "There is no intermediate because the reaction occurs in a single elementary step."
        )

    elif mechanism_choice == "Two-step reaction with an intermediate":

        st.markdown("#### Mechanism")

        st.latex(
            r"A+B\rightarrow I"
        )

        st.latex(
            r"I\rightarrow C"
        )

        st.markdown("""
        \(I\) is formed in the first step and consumed in the second step.
        Therefore, \(I\) is an intermediate.
        """)

        st.latex(
            r"\boxed{A+B+I\rightarrow I+C}"
        )

        st.markdown("After cancelling the intermediate:")

        st.latex(
            r"\boxed{A+B\rightarrow C}"
        )

        st.success(
            "Correct: I is an intermediate because it is produced and then consumed."
        )

    else:

        st.markdown("#### Mechanism")

        st.latex(
            r"A+B\rightarrow I\qquad\text{slow}"
        )

        st.latex(
            r"I\rightarrow C\qquad\text{fast}"
        )

        st.markdown("""
        The first step is slow, so it is the rate-determining step.
        """)

        st.latex(
            r"\boxed{\text{rate}=k[A][B]}"
        )

        st.success(
            "The rate law follows the reactants involved in the slow elementary step in this simplified mechanism."
        )

    st.markdown("---")

    st.markdown("### Mechanisms and Rate Laws")

    st.markdown("""
    This is an important connection between reaction mechanisms and kinetics.

    The **overall balanced equation** tells us the overall stoichiometric change.

    The **experimentally determined rate law** tells us how the reaction rate depends
    on reactant concentrations.

    A proposed mechanism must be consistent with the experimentally observed rate law.
    """)

    st.latex(
        r"\boxed{\text{Proposed mechanism}\quad\Longleftrightarrow\quad\text{experimentally observed rate law}}"
    )

    st.markdown("""
    If a proposed mechanism predicts a rate law that is inconsistent with experiment,
    the mechanism is not an appropriate explanation for the observed reaction.
    """)

    st.markdown("---")

    st.markdown("### Catalysts in Reaction Mechanisms")

    st.markdown("""
    Catalysts can participate in reaction mechanisms.

    A catalyst may react with a reactant in one elementary step and then be regenerated
    in a later step.

    Because it is regenerated, the catalyst is not consumed overall.
    """)

    st.markdown("For example:")

    st.latex(
        r"A+\mathrm{Cat}\rightarrow I"
    )

    st.latex(
        r"I+B\rightarrow C+\mathrm{Cat}"
    )

    st.markdown("""
    Adding the two steps gives:
    """)

    st.latex(
        r"A+B+\mathrm{Cat}\rightarrow C+\mathrm{Cat}"
    )

    st.markdown("""
    The catalyst appears on both sides and cancels:
    """)

    st.latex(
        r"\boxed{A+B\rightarrow C}"
    )

    st.success(
        "The catalyst participates in the mechanism but is regenerated and therefore does not appear in the overall reaction."
    )

    st.markdown("---")

    st.markdown("### Energy Profiles and Reaction Mechanisms")

    st.markdown("""
    A multi-step reaction mechanism can have more than one energy barrier.

    Each elementary step can have its own activation energy.
    """)

    reaction_coordinate = np.linspace(0, 1, 500)

    baseline = 0.15

    energy_profile = (
        baseline
        + 0.95 * np.exp(-((reaction_coordinate - 0.28) / 0.10) ** 2)
        + 0.65 * np.exp(-((reaction_coordinate - 0.72) / 0.12) ** 2)
        - 0.10 * reaction_coordinate
    )

    fig, ax = plt.subplots(figsize=(9, 4.5))

    ax.plot(
        reaction_coordinate,
        energy_profile
    )

    ax.set_xlabel("Reaction coordinate")
    ax.set_ylabel("Potential energy")
    ax.set_title("Example Energy Profile for a Two-Step Mechanism")
    ax.grid(alpha=0.25)

    st.pyplot(fig)

    st.markdown("""
    Each maximum represents a transition state for an elementary step.

    The minimum between the two maxima represents an **intermediate**.
    """)

    st.markdown("---")

    st.markdown("### Check Your Understanding")

    mechanism_q1 = st.radio(
        "1. What is a reaction mechanism?",
        [
            "The individual steps by which a reaction occurs",
            "The balanced equation only",
            "The energy released by a reaction",
            "The concentration of the products"
        ],
        key="mechanism_q1"
    )

    if mechanism_q1 == "The individual steps by which a reaction occurs":
        st.success("Correct. A reaction mechanism describes the elementary steps of a reaction.")
    else:
        st.error("Not quite. A reaction mechanism describes the individual steps by which a reaction occurs.")

    mechanism_q2 = st.radio(
        "2. What is a reaction intermediate?",
        [
            "A species produced in one step and consumed in a later step",
            "A reactant that is never consumed",
            "A catalyst that changes the rate",
            "The final product"
        ],
        key="mechanism_q2"
    )

    if mechanism_q2 == "A species produced in one step and consumed in a later step":
        st.success("Correct. An intermediate is formed and then consumed during the mechanism.")
    else:
        st.error("Not quite. An intermediate is formed in one step and consumed in a later step.")

    mechanism_q3 = st.radio(
        "3. What is the rate-determining step?",
        [
            "The slow step in a simplified mechanism",
            "The fastest step",
            "The final step in every mechanism",
            "The step with the smallest activation energy"
        ],
        key="mechanism_q3"
    )

    if mechanism_q3 == "The slow step in a simplified mechanism":
        st.success("Correct. The slow step is commonly treated as the rate-determining step in an introductory mechanism.")
    else:
        st.error("Not quite. In the simplified treatment, the slow step is the rate-determining step.")

    mechanism_q4 = st.radio(
        "4. Can the coefficients in an overall balanced equation generally be used as rate-law exponents?",
        [
            "Yes, always",
            "No, not generally",
            "Only for products",
            "Only when a catalyst is present"
        ],
        key="mechanism_q4"
    )

    if mechanism_q4 == "No, not generally":
        st.success("Correct. Rate-law exponents must generally be determined experimentally.")
    else:
        st.error("Not quite. The exponents in an experimentally determined rate law cannot generally be obtained from the overall equation.")

    st.markdown("---")

    st.markdown("### Key Points")

    st.markdown("""
    - A **reaction mechanism** describes the individual steps of a chemical reaction.
    - Individual steps are called **elementary steps**.
    - A **reaction intermediate** is produced in one step and consumed in another.
    - Intermediates do not appear in the overall reaction.
    - The **slow step** is commonly treated as the rate-determining step in a simplified mechanism.
    - The overall balanced equation does not necessarily show the actual molecular pathway.
    - Rate laws must generally be supported by **experimental evidence**.
    - Catalysts can participate in mechanisms and are regenerated rather than consumed overall.
    - A proposed mechanism should be consistent with the experimentally observed rate law.
    """)
