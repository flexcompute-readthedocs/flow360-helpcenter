# Models in Flow360

This section covers the various models available in Flow360, organized into two main categories:
1. Boundary Conditions - defining how the simulation interacts with its boundaries
2. 3D Models - defining physics models applied to volumetric regions

## Boundary Conditions

Boundary conditions specify how the fluid behaves at the boundaries of the simulation domain. Flow360 provides a comprehensive set of boundary conditions to support various simulation scenarios.

| Boundary Condition | Description | Key Parameters |
|-------------------|-------------|----------------|
| [Wall](./01.boundary-conditions/01.wall.md) | Solid surface where fluid cannot penetrate | Wall Motion, Thermal Condition, Wall Function, Roughness Height |
| [Freestream](./01.boundary-conditions/02.freestream.md) | Far-field condition with uniform flow | Mach Number, Angle of Attack, Sideslip Angle, Static Pressure |
| [Inflow](./01.boundary-conditions/03.inflow.md) | Boundary where flow enters the domain | Velocity Profile, Total Pressure, Flow Direction |
| [Outflow](./01.boundary-conditions/04.outflow.md) | Boundary where flow exits the domain | Static Pressure, Mass Flow Rate, Backflow Treatment |
| [Periodic](./01.boundary-conditions/05.periodic.md) | Repeating boundary condition for cyclic geometries | Rotation Angle, Translation Vector |
| [Symmetry](./01.boundary-conditions/06.symmetry.md) | Boundary that enforces symmetry of the solution | Symmetry Plane |
| [Slip Wall](./01.boundary-conditions/07.slip-wall.md) | Wall with zero normal velocity but allows tangential flow | - |
| [Turbulence Quantities](./01.boundary-conditions/08.turbulence-quantities.md) | Specification of turbulence parameters at boundaries | Turbulence Intensity, Eddy Viscosity Ratio, Length Scale |

## 3D Models

3D models in Flow360 define the physical processes that occur within volumetric regions of the simulation domain.

### Fluid Models

| Model | Description | Key Parameters |
|-------|-------------|----------------|
| [Navier-Stokes Solver](./02.3d-models/01.fluid/01.navier-stokes-solver.md) | Core flow solver for viscous and inviscid flows | Equations, Time Integration, CFL Number |
| [Turbulence Model](./02.3d-models/01.fluid/02.turbulence-model.md) | Models for turbulent flow simulation | Model Type (SA, SST, etc.), Model Coefficients |
| [Transition Model](./02.3d-models/01.fluid/03.transition-model.md) | Models for laminar-turbulent transition | Transition Criteria, Intermittency |
| [Initial Condition](./02.3d-models/01.fluid/04.initial-condition.md) | Starting solution for the simulation | Freestream Values, Custom Field Initialization |

### Special Models

| Model | Description | Key Parameters |
|-------|-------------|----------------|
| [Rotation](./02.3d-models/02.rotation.md) | Handling of rotating components | Rotation Type (MRF/SRF/Physical), Angular Velocity |
| [BET Disk](./02.3d-models/03.bet-disk.md) | Blade Element Theory for propeller/rotor modeling | Blade Geometry, Airfoil Data, RPM |
| [Actuator Disk](./02.3d-models/04.actuator-disk.md) | Simplified model for propellers and rotors | Thrust Coefficient, Swirl Distribution |
| [Porous Medium](./02.3d-models/05.porous-medium.md) | Model for flow through porous regions | Darcy Coefficient, Forchheimer Coefficient |

Each model is explained in detail in its respective documentation page. Click on the model name to access the comprehensive documentation including available parameters, detailed descriptions, usage tips, and example configurations. 