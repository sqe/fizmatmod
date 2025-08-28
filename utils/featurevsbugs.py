import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Define the Hamiltonian for the Features vs. Bugs model
# H = 0.5*p1**2 + (1/3)*p2**2 + 0.5*q1**2 + q2**2 + 0.5*q1*q2
def hamiltonian(state, t):
    q1, q2, p1, p2 = state
    # Hamilton's equations
    q1_dot = p1
    q2_dot = (2/3) * p2
    p1_dot = -q1 - 0.5 * q2
    p2_dot = -2 * q2 - 0.5 * q1
    return [q1_dot, q2_dot, p1_dot, p2_dot]

# Initial conditions from the example
q1_initial = 5
q2_initial = 2
p1_initial = 1
p2_initial = 0.75
initial_state = [q1_initial, q2_initial, p1_initial, p2_initial]

# Time points for the simulation
t = np.linspace(0, 10, 100) # Simulating for 10 weeks

# Solve the differential equations
solution = odeint(hamiltonian, initial_state, t)
q1_solution, q2_solution, p1_solution, p2_solution = solution.T

# Create a figure with three subplots
fig = plt.figure(figsize=(18, 6))

# Subplot 1: Trajectory in (q1, q2) space with time as color
ax1 = fig.add_subplot(1, 3, 1)
sc1 = ax1.scatter(q1_solution, q2_solution, c=t, cmap='viridis', label='Project Trajectory')
ax1.plot(q1_solution, q2_solution, color='gray', linestyle='--', alpha=0.5)
ax1.plot(q1_solution[0], q2_solution[0], 'go', label='Start (t=0)')
ax1.plot(q1_solution[-1], q2_solution[-1], 'ro', label=f'End (t={t[-1]})')
ax1.set_title('Trajectory in (Features, Bugs) Space')
ax1.set_xlabel('Number of Features ($q_1$)')
ax1.set_ylabel('Number of Bugs ($q_2$)')
ax1.grid(True)
ax1.legend()
plt.colorbar(sc1, ax=ax1, label='Time (weeks)')

# Subplot 2: Trajectory in (p1, p2) space with time as color
ax2 = fig.add_subplot(1, 3, 2)
sc2 = ax2.scatter(p1_solution, p2_solution, c=t, cmap='plasma', label='Momentum Trajectory')
ax2.plot(p1_solution, p2_solution, color='gray', linestyle='--', alpha=0.5)
ax2.plot(p1_solution[0], p2_solution[0], 'go', label='Start (t=0)')
ax2.plot(p1_solution[-1], p2_solution[-1], 'ro', label=f'End (t={t[-1]})')
ax2.set_title('Momentum in (p1, p2) Space')
ax2.set_xlabel('Feature Momentum ($p_1$)')
ax2.set_ylabel('Bug Momentum ($p_2$)')
ax2.grid(True)
ax2.legend()
plt.colorbar(sc2, ax=ax2, label='Time (weeks)')

# Subplot 3: All variables vs. Time
ax3 = fig.add_subplot(1, 3, 3)
ax3.plot(t, q1_solution, label='Features ($q_1$)')
ax3.plot(t, q2_solution, label='Bugs ($q_2$)')
ax3.plot(t, p1_solution, label='Feature Momentum ($p_1$)')
ax3.plot(t, p2_solution, label='Bug Momentum ($p_2$)')
ax3.set_title('Variables over Time')
ax3.set_xlabel('Time (weeks)')
ax3.set_ylabel('Value')
ax3.grid(True)
ax3.legend()

plt.tight_layout()
plt.show()