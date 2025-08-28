# hamiltonian_model.py
import numpy as np
from scipy.integrate import odeint

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
