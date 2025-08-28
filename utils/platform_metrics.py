import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Define the Hamiltonian for the Azure Metrics model
# H = 0.5*p1**2 + 0.5*p2**2 + 0.5*q1**2 + q2**2 + 0.25*q1*q2
def hamiltonian_azure(state, t):
    q1, q2, p1, p2 = state
    # Hamilton's equations
    q1_dot = p1
    q2_dot = p2
    p1_dot = -q1 - 0.25 * q2
    p2_dot = -2 * q2 - 0.25 * q1
    return [q1_dot, q2_dot, p1_dot, p2_dot]

# Initial conditions from the example
q1_initial = 50
q2_initial = 100
p1_initial = 5
p2_initial = 20
initial_state = [q1_initial, q2_initial, p1_initial, p2_initial]

# Time points for the simulation
t = np.linspace(0, 1, 100) # Simulating for 1 week

# Solve the differential equations
solution = odeint(hamiltonian_azure, initial_state, t)
q1_solution, q2_solution, p1_solution, p2_solution = solution.T

# Create the plots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Plot the trajectory in (q1, q2) space
ax1.plot(q1_solution, q2_solution, label='Platform Trajectory')
ax1.plot(q1_solution[0], q2_solution[0], 'go', label='Start (t=0)') # Start point
ax1.plot(q1_solution[-1], q2_solution[-1], 'ro', label=f'End (t={t[-1]})') # End point
ax1.set_title('Platform Trajectory in (Deployments, MTTR) Space')
ax1.set_xlabel('Cumulative Deployments ($q_1$)')
ax1.set_ylabel('Cumulative Resolution Time ($q_2$)')
ax1.grid(True)
ax1.legend()

# Plot the trajectory in (p1, p2) space (momentum)
ax2.plot(p1_solution, p2_solution, label='Momentum Trajectory')
ax2.plot(p1_solution[0], p2_solution[0], 'go', label='Start (t=0)') # Start point
ax2.plot(p1_solution[-1], p2_solution[-1], 'ro', label=f'End (t={t[-1]})') # End point
ax2.set_title('Platform Momentum in (p1, p2) Space')
ax2.set_xlabel('Deployment Momentum ($p_1$)')
ax2.set_ylabel('Resolution Momentum ($p_2$)')
ax2.grid(True)
ax2.legend()

plt.tight_layout()
plt.show()