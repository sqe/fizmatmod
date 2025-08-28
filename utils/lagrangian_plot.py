import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# hamiltonian_model.py (Included for self-containment)
def hamiltonian(state, t):
    """
    Defines the system of ordinary differential equations (ODEs) based on
    Hamilton's equations. This function is used by scipy.integrate.odeint
    to solve for the system's evolution over time.

    Args:
        state (list): The current state vector [q1..q5, p1..p5].
        t (float): The current time point.

    Returns:
        list: The derivative of the state vector [q_dot, p_dot].
    """
    q1, q2, q3, q4, q5, p1, p2, p3, p4, p5 = state

    # Hamilton's equations for generalized coordinates (q_dot = p)
    # This shows that the rate of change of each metric is equal to its momentum.
    q1_dot = p1
    q2_dot = p2
    q3_dot = p3
    q4_dot = p4
    q5_dot = p5

    # Hamilton's equations for canonical momenta (p_dot = -dH/dq)
    # The rate of change of momentum is determined by the "force" from potential energy.
    p1_dot = -q1 - 0.5 * q2 - 0.75 * q3
    p2_dot = -2 * q2 - 0.5 * q1
    p3_dot = -4 * q3 - 0.75 * q1 - 0.25 * q5
    p4_dot = -q4
    p5_dot = -10 * q5 - 0.25 * q3

    return [q1_dot, q2_dot, q3_dot, q4_dot, q5_dot, p1_dot, p2_dot, p3_dot, p4_dot, p5_dot]

# --- Example 8: Positive Outcome Scenario ---
# We use the same initial conditions as the positive outcome example
# to ensure the Lagrangian plot corresponds to a healthy project.
q1_initial_pos = 50
q2_initial_pos = 100
q3_initial_pos = 2
q4_initial_pos = 80
q5_initial_pos = 5

p1_initial_pos = 7    # Higher deployment velocity
p2_initial_pos = -5   # Negative toil momentum (automation)
p3_initial_pos = -0.2 # Negative incident momentum (proactive fixes)
p4_initial_pos = 8    # Slower resource cost increase
p5_initial_pos = 0    # No new downtime

initial_state_pos = [q1_initial_pos, q2_initial_pos, q3_initial_pos, q4_initial_pos, q5_initial_pos,
                     p1_initial_pos, p2_initial_pos, p3_initial_pos, p4_initial_pos, p5_initial_pos]

# Time points for the simulation
t = np.linspace(0, 5, 100) # Simulating for 5 weeks

# Solve the Hamiltonian differential equations.
# This gives us the values for all q's (coordinates) and p's (momenta) over time.
solution_pos = odeint(hamiltonian, initial_state_pos, t)
q_sol_pos, p_sol_pos = solution_pos[:, :5], solution_pos[:, 5:]

# Calculate the generalized velocities (q_dot) from the momenta.
# For this specific model, momentum is equal to velocity (p = q_dot).
q_dot_sol_pos = p_sol_pos

# --- Calculate Kinetic Energy (T) ---
# T = 0.5 * sum(q_dot_i^2)
kinetic_energy = 0.5 * (q_dot_sol_pos[:, 0]**2 + q_dot_sol_pos[:, 1]**2 + 
                        q_dot_sol_pos[:, 2]**2 + q_dot_sol_pos[:, 3]**2 + 
                        q_dot_sol_pos[:, 4]**2)

# --- Calculate Potential Energy (V) ---
# V = 0.5*q1^2 + q2^2 + 2*q3^2 + 0.5*q4^2 + 5*q5^2 + 0.5*q1*q2 + 0.75*q1*q3 + 0.25*q3*q5
potential_energy = (0.5 * q_sol_pos[:, 0]**2 + q_sol_pos[:, 1]**2 + 
                    2 * q_sol_pos[:, 2]**2 + 0.5 * q_sol_pos[:, 3]**2 + 
                    5 * q_sol_pos[:, 4]**2 + 0.5 * q_sol_pos[:, 0] * q_sol_pos[:, 1] + 
                    0.75 * q_sol_pos[:, 0] * q_sol_pos[:, 2] + 
                    0.25 * q_sol_pos[:, 2] * q_sol_pos[:, 4])

# --- Calculate the Lagrangian (L) ---
# L = T - V
lagrangian = kinetic_energy - potential_energy

# Create the figure for the Lagrangian, Kinetic Energy, and Potential Energy plots
fig = plt.figure(figsize=(12, 8))

ax = fig.add_subplot(1, 1, 1)
ax.plot(t, kinetic_energy, label='Kinetic Energy ($T$)')
ax.plot(t, potential_energy, label='Potential Energy ($V$)')
ax.plot(t, lagrangian, label='Lagrangian ($L = T - V$)')
ax.set_title('Energy and Lagrangian over Time (Positive Outcome)')
ax.set_xlabel('Time (weeks)')
ax.set_ylabel('Value')
ax.grid(True)
ax.legend()

plt.tight_layout()
plt.show()
