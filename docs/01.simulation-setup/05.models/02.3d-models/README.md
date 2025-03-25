# 3D Models

The 3D Models section in Flow360 allows you to configure the fluid properties, solver settings, and specialized physical models for your simulation.

## Overview

In the Models section of the UI, after configuring boundary conditions, you'll set up the 3D model parameters that define the fluid behavior and any additional physical models needed for your specific application.

## Available Models

Flow360 offers several specialized models for different simulation requirements:

- [Fluid](./01.fluid.md) - Configure basic fluid properties and solver settings
- [Rotation](./02.rotation.md) - For simulating rotating reference frames
- [BET Disk](./03.bet-disk.md) - Blade Element Theory for propellers and rotors
- [Actuator Disk](./04.actuator-disk.md) - Simplified propulsor representation
- [Porous Medium](./05.porous-medium.md) - For modeling flow through porous regions

## Combining Specialized Models

Flow360 allows you to combine different specialized models for complex simulations:

**Example Combinations**:
- Rotation + BET Disk: For advanced rotorcraft simulations
- Multiple BET Disks: For multi-rotor configurations
- Porous Medium + Heat Transfer: For thermal systems with radiators

**Considerations When Combining Models**:
- Evaluate computational cost impact
- Ensure physical compatibility between models
- Start with simpler configurations before adding complexity
- Validate each added model individually when possible

## Performance Impact

Specialized models increase computational requirements:
- BET Disk models require additional calculations for each blade element
- Rotation models require coordinate transformations
- Porous media calculations add source terms to the equations

Balance modeling fidelity with computational resources based on your simulation goals and available computing capacity. 