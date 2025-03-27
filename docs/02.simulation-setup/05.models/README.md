# Models

The Models section is a critical part of Flow360 simulation setup, where you define the physical behaviors and boundary conditions that govern your simulation. Proper configuration of these models ensures accurate representation of the real-world physics you're trying to simulate.

## Why Models Matter

Setting up appropriate models is crucial because:

1. **Physical Accuracy**: The models you select determine how closely your simulation represents real-world physics
2. **Computational Efficiency**: Different models have varying computational costs; choosing the right ones balances accuracy with performance
3. **Solution Stability**: Properly configured boundary conditions and physical models improve convergence and stability

## Key Components

The Models section consists of two main components:

### 1. Boundary Conditions

Boundary conditions define how flow behaves at the edges of your computational domain. Each boundary in your mesh must be assigned a specific type of boundary condition.

Flow360 supports various boundary condition types, including:
- Wall (no-slip and adiabatic/thermal)
- Freestream
- Inflow/Outflow
- Periodic
- Symmetry
- Slip wall

[Learn more about Boundary Conditions](./01.boundary-conditions.md)

### 2. 3D Models

The 3D Models section allows you to configure:

- **[Fluid Properties](./02.3d-models/01.fluid.md)**: Specify the working fluid and its physical properties
- **Solver Settings**: Configure the Navier-Stokes solver and turbulence modeling approach
- **Specialized Models**: Enable and configure additional physics models:
  - [Rotation](./02.3d-models/02.rotation.md) models for rotating machinery
  - [Blade Element Theory (BET) Disk](./02.3d-models/03.bet-disk.md) for propellers and rotors
  - [Actuator Disk](./02.3d-models/04.actuator-disk.md) for simplified propulsion modeling
  - [Porous Medium](./02.3d-models/05.porous-medium.md) for flow through porous regions

[Learn more about 3D Models](./02.3d-models/README.md)

## Best Practices

When configuring your models:

1. **Start Simple**: Begin with basic models before adding complexity
2. **Validate Incrementally**: Verify basic configurations before adding advanced models
3. **Consider Physics**: Choose models based on the dominant physical phenomena in your simulation
4. **Balance Detail**: More detailed models increase accuracy but also computational cost

## Next Steps

After configuring your models, you'll typically move on to:
- Setting up time stepping parameters
- Configuring output settings
- Defining user dynamics (if applicable) 