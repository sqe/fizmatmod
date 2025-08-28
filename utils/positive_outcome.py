# positive_outcome.py
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Import the core Hamiltonian function
import hamiltonian_model as hm

# --- Example 8: Positive Outcome Scenario ---
print("\nPlotting Example 8: Positive Outcome")

# Initial conditions for the positive outcome
# Lower initial toil and incidents, with active toil reduction.
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

# Solve the differential equations for the positive outcome
solution_pos = odeint(hm.hamiltonian, initial_state_pos, t)
# Separate the solution into q (coordinates) and p (momenta)
q_sol_pos, p_sol_pos = solution_pos[:, :5], solution_pos[:, 5:]

# Create a figure for the positive outcome plots
fig_pos = plt.figure(figsize=(18, 6))

# Subplot 1 (Left): Trajectory in (Deployments, Toil) Space
# Shows a healthy trend where deployments increase but toil decreases.
ax1_pos = fig_pos.add_subplot(1, 2, 1)
sc1_pos = ax1_pos.scatter(q_sol_pos[:, 0], q_sol_pos[:, 1], c=t, cmap='plasma')
ax1_pos.plot(q_sol_pos[:, 0], q_sol_pos[:, 1], color='gray', linestyle='--', alpha=0.5)
ax1_pos.set_title('Positive Outcome: Trajectory in (Deployments, Toil) Space')
ax1_pos.set_xlabel('Cumulative Deployments ($q_1$)')
ax1_pos.set_ylabel('Cumulative Toil ($q_2$)')
ax1_pos.grid(True)
plt.colorbar(sc1_pos, ax=ax1_pos, label='Time (weeks)')

# Subplot 2 (Right): All variables vs. Time
# This shows how a well-managed system keeps toil, incidents, and downtime low.
ax2_pos = fig_pos.add_subplot(1, 2, 2)
ax2_pos.plot(t, q_sol_pos[:, 0], label='Deployments ($q_1$)')
ax2_pos.plot(t, q_sol_pos[:, 1], label='Toil ($q_2$)')
ax2_pos.plot(t, q_sol_pos[:, 2], label='Incidents ($q_3$)')
ax2_pos.plot(t, q_sol_pos[:, 3], label='Resource Price ($q_4$)')
ax2_pos.plot(t, q_sol_pos[:, 4], label='Downtime ($q_5$)')
ax2_pos.set_title('Positive Outcome: Metrics vs. Time')
ax2_pos.set_xlabel('Time (weeks)')
ax2_pos.set_ylabel('Cumulative Value')
ax2_pos.grid(True)
ax2_pos.legend()

plt.tight_layout()
plt.show()
