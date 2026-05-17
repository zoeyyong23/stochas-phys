# Langevin Dynamics & Ornstein-Uhlenbeck Process Simulator

This repository contains a Python implementation for simulating stochastic paths using **Langevin Dynamics** (analogous to the **Ornstein-Uhlenbeck process** in financial mathematics).

The simulation uses an Euler method to model systems characterized by a friction/mean-reverting force and random stochastic fluctuations (diffusion/volatility). It includes a Monte Carlo simulation script that visualizes multiple potential trajectories over time.

---

## 💡 Mathematical Background

The simulation models the stochastic differential equation (SDE):

$$dv_t = -\gamma v_t dt + \sigma dW_t$$

Where:

* **$v_t$**: The state variable at time $t$ (e.g., stellar velocity in physics, or interest rate/asset deviation in finance).
* **$\gamma$ (Gamma)**: The friction coefficient or the speed of mean reversion. It pulls the process back toward the mean ($0$).
* **$\sigma$ (Sigma)**: The diffusion coefficient or volatility, scaling the random shocks.
* **$dW_t$**: A Wiener process increment (Brownian motion), where $dW_t \sim \mathcal{N}(0, dt)$.

---

## 🚀 Features

* **Stochastic Simulation:** Models continuous-time random processes using discrete time steps ($dt$).
* **Monte Carlo Visualizer:** Generates and plots multiple paths simultaneously to observe statistical behavior and convergence.
* **Dual-Domain Comments:** Code documentation bridging both statistical physics (stellar dynamics/viscosity) and quantitative finance (Ornstein-Uhlenbeck interest rate modeling).

---

## 🛠️ Requirements & Installation

To run this simulation, you need Python 3.x along with `numpy` and `matplotlib`.

You can install the dependencies via pip:

```bash
pip install numpy matplotlib

```

---

## 💻 Usage

1. Copy the Python script into a file named `langevin_simulation.py`.
2. Run the script from your terminal:

```bash
python langevin_simulation.py

```

### Configuration Parameters

You can easily tweak the physical/financial properties inside the script:

```python
initial_velocity = 0.5  # Starting value (v0)
viscosity_gamma = 0.3   # Friction / Mean reversion strength
diffusion_sigma = 0.1   # Volatility / Noise magnitude
total_time = 100        # Total duration of the simulation (T)
time_step = 0.01        # Time increment (dt)
n_simulations = 5       # Number of Monte Carlo trajectories to plot

```

---

## 📊 Expected Output

Upon running the script, a `matplotlib` window will display the simulated paths.

Because $\gamma > 0$, you will observe the trajectories fluctuate randomly due to the $\sigma dW$ term, but they will consistently be pulled back toward the $0$ baseline (mean reversion).

* **Higher $\gamma$** results in tighter clustering around zero.
* **Higher $\sigma$** results in wider, more violent oscillations.
