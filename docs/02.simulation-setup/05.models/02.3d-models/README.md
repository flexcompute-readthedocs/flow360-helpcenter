---
title: 3D Models
---

# 3D Models

This section covers the physical models that simulate the 3D flow behavior in Flow360.


## Overview of 3D Models

3D models in Flow360 define the physical processes that occur within volumetric regions of the simulation domain.

### Fluid Models

| Model | Description | Key Parameters |
|-------|-------------|----------------|
| [Navier-Stokes Solver](./01.fluid/01.navier-stokes-solver.md) | Core flow solver for viscous and inviscid flows | Equations, Time Integration, CFL Number |
| [Turbulence Model](./01.fluid/02.turbulence-model.md) | Models for turbulent flow simulation | Model Type (SA, SST, etc.), Model Coefficients |
| [Transition Model](./01.fluid/03.transition-model.md) | Models for laminar-turbulent transition | Transition Criteria, Intermittency |
| [Initial Condition](./01.fluid/04.initial-condition.md) | Starting solution for the simulation | Freestream Values, Custom Field Initialization |

### Heat Transfer Models

::: warning Project Workflow starting from Volume Mesh Only
The solid model is only available in projects started from volume mesh. They cannot be used with the surface mesh or geometry workflow.
:::

| Model | Description | Key Parameters |
|-------|-------------|----------------|
| [Solid](./02.solid/index.html) | Conjugate heat transfer in solid materials | Material Properties, Heat Equation Settings |

### Special Models

| Model | Description | Key Parameters |
|-------|-------------|----------------|
| [Rotation](./03.rotation.md) | Handling of rotating components | Rotation Type (MRF/SRF/Physical), Angular Velocity |
| [BET Disk](./04.bet-disk.md) | Blade Element Theory for propeller/rotor modeling | Polars, RPM |
| [Actuator Disk](./05.actuator-disk.md) | Simplified model for propellers and rotors | Thrust Coefficient, Swirl Distribution |
| [Porous Medium](./06.porous-medium.md) | Model for flow through porous regions | Darcy Coefficient, Forchheimer Coefficient |

Click on each model to see detailed documentation including available parameters, descriptions, usage tips, and example configurations. 