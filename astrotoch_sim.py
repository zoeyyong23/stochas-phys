import numpy as np
import matplotlib.pyplot as plt

def simulate_langevin_path(v0, gamma, sigma, T, dt):
    """
    simulates a velocity path using the Langevin Eqn:
    dv = -gamma * v *dt + sigma *dW

    similar to the Ornstein-Uhlenbeck process in finance
    """

    n_steps = int(T/dt)
    t = np.linspace(0, T, n_steps)
    v = np.zeros(n_steps)
    v[0] = v0

    # standard normal increments (Wiener process)
    dw = np.random.normal(0, np.sqrt(dt), n_steps)

    for i in range(1, n_steps):
        # gamma term is drag/friction from moving through a cluster, or mean reversion in finance
        # sigma is diffucsion coefficient or volatility
        # dw is the Wiener process or stochastic component
        v[i] = v[i-1] - gamma * v[i-1] * dt + sigma * dw[i]

    return t, v

# stellar velocity / interest rate deviation
initial_velocity = 0.5
viscosity_gamma = 0.3 # friction coefficient (mean reversion strength)
diffusion_sigma = 0.1 # magnitude of random fluctuations (volatility)
total_time = 100
time_step = 0.01

# Monte Carlo Simulation
plt.figure(figsize=(10,6))
n_simulations = 5

for _ in range(n_simulations):
    time, velocity = simulate_langevin_path(initial_velocity, viscosity_gamma, diffusion_sigma, total_time, time_step)
    plt.plot(time, velocity, lw=1, alpha=0.8)

plt.title("Langevin Dynamics: Stellar Velocity Fluctuations (Monte Carlo)")
plt.xlabel("Time (Arbitrary Units)")
plt.ylabel("Velocity / Asset Value")
plt.axhline(0, color='black', linestyle='--', alpha=0.5) # Mean reversion level
plt.grid(True, alpha=0.3)
plt.show()
