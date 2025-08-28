import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Import the core Hamiltonian function
import hamiltonian_model as hm

# --- Example 7: Negative Outcome Scenario ---
print("Plotting Example 7: Negative Outcome")

# Initial conditions for the negative outcome
# High initial toil, incidents, and downtime with low automation.
q1_initial_neg = 50
q2_initial_neg = 200
q3_initial_neg = 5
q4_initial_neg = 100
q5_initial_neg = 10

p1_initial_neg = 5    # Deployments/week
p2_initial_neg = 20   # Toil hours/week
p3_initial_neg = 0.5  # Incidents/week
p4_initial_neg = 10   # Resource cost/week
p5_initial_neg = 1    # Downtime minutes/week

initial_state_neg = [q1_initial_neg, q2_initial_neg, q3_initial_neg, q4_initial_neg, q5_initial_neg,
                     p1_initial_neg, p2_initial_neg, p3_initial_neg, p4_initial_neg, p5_initial_neg]

# Time points for the simulation
t = np.linspace(0, 5, 100) # Simulating for 5 weeks

# Solve the differential equations using the imported function
solution_neg = odeint(hm.hamiltonian, initial_state_neg, t)
# Separate the solution into q (coordinates) and p (momenta)
q_sol_neg, p_sol_neg = solution_neg[:, :5], solution_neg[:, 5:]

# Create a figure for the negative outcome plots
fig_neg = plt.figure(figsize=(18, 6))

# Subplot 1 (Left): Trajectory in (Deployments, Toil) Space
# Shows how deployments increase while toil also spirals upwards.
ax1_neg = fig_neg.add_subplot(1, 2, 1)
sc1_neg = ax1_neg.scatter(q_sol_neg[:, 0], q_sol_neg[:, 1], c=t, cmap='plasma')
ax1_neg.plot(q_sol_neg[:, 0], q_sol_neg[:, 1], color='gray', linestyle='--', alpha=0.5)
ax1_neg.set_title('Negative Outcome: Trajectory in (Deployments, Toil) Space')
ax1_neg.set_xlabel('Cumulative Deployments ($q_1$)')
ax1_neg.set_ylabel('Cumulative Toil ($q_2$)')
ax1_neg.grid(True)
plt.colorbar(sc1_neg, ax=ax1_neg, label='Time (weeks)')

# Subplot 2 (Right): All variables vs. Time
# This plot shows the compounding effect of negative trends over time.
ax2_neg = fig_neg.add_subplot(1, 2, 2)
ax2_neg.plot(t, q_sol_neg[:, 0], label='Deployments ($q_1$)')
ax2_neg.plot(t, q_sol_neg[:, 1], label='Toil ($q_2$)')
ax2_neg.plot(t, q_sol_neg[:, 2], label='Incidents ($q_3$)')
ax2_neg.plot(t, q_sol_neg[:, 3], label='Resource Price ($q_4$)')
ax2_neg.plot(t, q_sol_neg[:, 4], label='Downtime ($q_5$)')
ax2_neg.set_title('Negative Outcome: Metrics vs. Time')
ax2_neg.set_xlabel('Time (weeks)')
ax2_neg.set_ylabel('Cumulative Value')
ax2_neg.grid(True)
ax2_neg.legend()

plt.tight_layout()
plt.show()
