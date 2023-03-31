import numpy as np
from qutip import *

"""
File containing lots of random useful functions for this project
"""

def TiltedLiouvillain(H, c_ops, nu_k, chi):
    """
    Returns the tilted Liouvillain for the system.
    """
    # Use the qutip function to get the Liouvillian given a Hamiltonian and collapse operators
    L = liouvillian(H, c_ops)

    # Add the tilted collapse operators
    Lk = sum([(np.exp(-1j*nu_k[k]*chi)-1) * to_super(c_ops[k]) for k in range(len(c_ops))])

    # Add the tilted collapse operators and turn them into a numpy array using .full()
    Lchi = (L + Lk).full()
    return Lchi

def SCGF(H, c_ops, nu_k, chi):
    """
    Returns the scaled cumulant generating function for the tilted Liouvillain
    """
    # Get the tilted Liouvillain numpy array
    Lchi = TiltedLiouvillain(H, c_ops, nu_k, chi)

    # Compute eigenvalues of Lchi
    eigs = np.linalg.eigvals(Lchi)

    # Return the maximum eigenvalue with the maximum real part
    return eigs[np.argmax(np.real(eigs))]

def BoseEinsteinDistribution(omega, beta):
    """
    Returns the Bose-Einstein distribution for the given frequency and temperature
    """
    return 1/(np.exp(omega*beta)-1)

def rates(a, omega, beta, kind='down'):
    """
    Returns the rates for the given frequency and temperature for an Ohmic bath
    """
    if kind=='down':
        return a * omega * (BoseEinsteinDistribution(omega, beta) + 1)
    elif kind=='up':
        return a * omega * BoseEinsteinDistribution(omega, beta)
    
def V_model_1bath(nu : float, a : float, delta : float, beta : float, kind : str = 'unified'):
    """
    Returns the V-model for the given parameters with an ohmic bath
    """
    # Define the Hamiltonian
    g1 = fock(3, 0)
    g2 = fock(3, 1)
    g3 = fock(3, 2)

    # Define Hamiltonian
    H =(nu - delta) * g2 * g2.dag() + nu * g3 * g3.dag()

    # Define collapse operators
    c_ops = []
    if kind == 'unified':
        c_ops.append(np.sqrt(rates(a, nu, beta, kind='down')) * (g1*g2.dag() + g1*g3.dag()))
        c_ops.append(np.sqrt(rates(a, nu, beta, kind='up')) * (g2 * g1.dag() + g3 * g1.dag()))
    elif kind == "secular":
        c_ops.append(np.sqrt(rates(a, nu, beta, kind='down')) * (g1*g2.dag()))
        c_ops.append(np.sqrt(rates(a, nu, beta, kind='down')) * (g1*g3.dag()))
        c_ops.append(np.sqrt(rates(a, nu, beta, kind='up')) * (g2 * g1.dag()))
        c_ops.append(np.sqrt(rates(a, nu, beta, kind='up')) * (g3 * g1.dag()))

    return [g1, g2, g3], H, c_ops

def V_model_2bath(nu : float, a : float, delta : float, beta : list, alpha: float, kind : str = 'unified'):
    """
    Returns the V-model for the given parameters with an ohmic bath
    """
    # Define the Hamiltonian
    g1 = fock(3, 0)
    g2 = fock(3, 1)
    g3 = fock(3, 2)

    # Define Hamiltonian
    H =(nu - delta) * g2 * g2.dag() + nu * g3 * g3.dag()

    # Define collapse operators
    c_ops = []
    if kind == 'unified':
        c_ops.append(np.sqrt(rates(a, nu, beta[0], kind='down')) * (g1*g2.dag() + g1*g3.dag()))
        c_ops.append(np.sqrt(rates(a, nu, beta[0], kind='up')) * (g2 * g1.dag() + g3 * g1.dag()))
        c_ops.append(np.sqrt(rates(a, nu, beta[1], kind='down')) * (g1*g2.dag() + alpha*g1*g3.dag()))
        c_ops.append(np.sqrt(rates(a, nu, beta[1], kind='up')) * (g2 * g1.dag() + alpha*g3 * g1.dag()))
    elif kind == "secular":
        c_ops.append(np.sqrt(rates(a, nu, beta[0], kind='down')) * (g1*g2.dag()))
        c_ops.append(np.sqrt(rates(a, nu, beta[0], kind='down')) * (g1*g3.dag()))
        c_ops.append(np.sqrt(rates(a, nu, beta[0], kind='up')) * (g2 * g1.dag()))
        c_ops.append(np.sqrt(rates(a, nu, beta[0], kind='up')) * (g3 * g1.dag()))
        c_ops.append(np.sqrt(rates(a, nu, beta[1], kind='down')) * (g1*g2.dag()))
        c_ops.append(np.sqrt(rates(a, nu, beta[1], kind='down')) * (alpha*g1*g3.dag()))
        c_ops.append(np.sqrt(rates(a, nu, beta[1], kind='up')) * (g2 * g1.dag()))
        c_ops.append(np.sqrt(rates(a, nu, beta[1], kind='up')) * (alpha*g3 * g1.dag()))


    return [g1, g2, g3], H, c_ops