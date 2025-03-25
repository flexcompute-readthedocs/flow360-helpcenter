# Time Stepping

Time stepping controls how your Flow360 simulation advances in time. Proper configuration is crucial for both solution accuracy and computational efficiency.

## Overview

You can configure:
- Whether your simulation is steady or unsteady
- How time advances in unsteady simulations
- How pseudo-time iterations are controlled for convergence

## Steady vs. Unsteady Simulations

### Steady Simulation

Steady simulations assume flow conditions do not change with time. These are appropriate for:
- Flows that have reached an equilibrium state
- Cases where time-dependent phenomena are not of interest
- Most external aerodynamics cases (aircraft in cruise, steady wind conditions)

**Key Settings**:
- **Maximum Steps**: Number of pseudo-time steps to run (default: 2000)
- **CFL Settings**: Controls convergence speed and stability (default: Adaptive CFL)

### Unsteady Simulation

Unsteady simulations model time-dependent flow phenomena. These are necessary for:
- Vortex shedding and wake dynamics
- Time-varying boundary conditions
- Moving or rotating geometries
- Transient flows

**Key Settings**:
- **Step Size**: Physical time between solution snapshots
- **Steps**: Total number of physical time steps
- **Maximum Pseudo Steps**: Maximum iterations within each physical step (default: 20)
- **CFL Settings**: Controls convergence within each physical step (default: Adaptive CFL)
- **Order of Accuracy**: Temporal accuracy (1st or 2nd order, default: 2)

## Time Step Size Selection

For unsteady simulations, choosing an appropriate physical time step size is critical:

### Based on Vortex Shedding

For flows with vortex shedding (e.g., bluff bodies, airfoils at high angles):
1. Estimate the vortex shedding frequency using: f = (St × U)/D
   - St is the Strouhal number (typically ~0.2)
   - U is the freestream velocity
   - D is the characteristic length
2. Set time step to capture ~100 steps per shedding cycle: Δt = 0.01/f

### Based on Rotation

For rotating geometries (propellers, turbomachinery):
- Use 3-6° of rotation per step for initial flow development
- Use 1-3° per step for accurate data collection
- Use 0.5-1° per step for detailed flow visualization

## CFL Settings

The Courant-Friedrichs-Lewy (CFL) number controls the time step size in pseudo-time iterations and affects convergence speed and stability.

### Adaptive CFL (Recommended)

Adaptive CFL automatically adjusts the CFL number based on solution convergence, providing an optimal balance between speed and stability. This is the recommended and default approach in Flow360.

**Key Parameters**:
- **Minimum**: Lower bound for CFL (default: 0.1)
- **Maximum**: Upper bound for CFL
  - For steady simulations: 10,000 (default)
  - For unsteady simulations: 1,000,000 (default)
- **Maximum Relative Change**: How quickly CFL can increase
  - For steady simulations: 1% per step (default)
  - For unsteady simulations: 50% per step (default)
- **Convergence Limiting Factor**: Controls the aggressiveness of the adaptation
  - For steady simulations: 0.25 (default, more conservative)
  - For unsteady simulations: 1.0 (default, more aggressive)

**Benefits**:
- Automatically reduces CFL when residuals increase, preventing divergence
- Increases CFL when residuals decrease, accelerating convergence
- Requires minimal user intervention
- Works well for a wide range of flow conditions

### Ramp CFL (Alternative)

Ramp CFL linearly increases the CFL number over a specified number of iterations.

**Key Parameters**:
- **Initial**: Starting CFL number
  - For steady simulations: 5 (default)
  - For unsteady simulations: 1 (default)
- **Final**: Maximum CFL number
  - For steady simulations: 200 (default)
  - For unsteady simulations: 1,000,000 (default)
- **Ramp Steps**: Number of steps to reach the final CFL
  - For steady simulations: 40 (default)
  - For unsteady simulations: 30 (default)

## Best Practices

### For Steady Simulations
- Start with the default Adaptive CFL settings
- If convergence is slow, increase the Convergence Limiting Factor (up to 0.5)
- For complex cases with convergence difficulties, reduce the Maximum Relative Change to 0.5

### For Unsteady Simulations
- Choose physical time step based on the phenomenon of interest
- Use Adaptive CFL with default settings
- Ensure sufficient pseudo-steps for convergence within each physical step
- Monitor residual convergence within each physical step

### When to Adjust Parameters
- **Increase Maximum Relative Change**: When convergence is too slow
- **Decrease Convergence Limiting Factor**: When simulation diverges
- **Reduce Maximum CFL**: When turbulence equations become unstable

## UI Configuration

In the Flow360 UI, you can configure time stepping settings in the dedicated Time Stepping section:

1. Navigate to the Time Stepping section in the simulation setup
2. Choose between Steady and Unsteady
3. Configure CFL settings (Adaptive is recommended and set as default)
4. Set additional parameters based on your simulation requirements

## Example Configurations

### Steady External Aerodynamics
- **Type**: Steady
- **Maximum Steps**: 2000
- **CFL Type**: Adaptive
- **CFL Min**: 0.1
- **CFL Max**: 10000
- **Maximum Relative Change**: 1.0
- **Convergence Limiting Factor**: 0.25

### Unsteady Vortex Shedding
- **Type**: Unsteady
- **Step Size**: Based on vortex shedding frequency
- **Steps**: Enough to capture several shedding cycles
- **Maximum Pseudo Steps**: 30
- **CFL Type**: Adaptive
- **CFL Min**: 0.1
- **CFL Max**: 1000000
- **Maximum Relative Change**: 50
- **Convergence Limiting Factor**: 1.0
- **Order of Accuracy**: 2 