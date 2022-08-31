---
order: 02
---

# Boundary Conditions

## Freestream
  
External freestream condition. The velocity components, both at boundaries and inside domain, are initialized according to the following equations, based on the angle of attack, $\alpha$ and the side slip angle, $\beta$:

$U_X =  Mach * \cos(\beta) * \cos(\alpha)$

$U_Y = -Mach * \sin(\beta)$

$U_Z =  Mach * \cos(\beta) * \sin(\alpha)$

Where `Mach` is specified in freestream section of case config. Note that the velocity components on the left hand side are non-dimensional as used in Flow360 solver. Also, for flow simulations with a freestream boundary condition, flow fields will be initialized according to this boundary condition.

Optionally, an expression for each of the non-dimensional velocity components can be specified.

### parameters:
- *optional* `Velocity`: an expression for each of non-dimensional velocity components as a function of x, y and z.

    - example: `["2 * cos(y)", "-2 * sin(x)", "0"]`
 
  
## NoSlipWall 
  
No-slip wall condition for a viscous impermeable boundary. Optionally, a tangential velocity can be prescribed for a moving or rotating wall.

### parameters:
- *optional* `Velocity`: an expression for each of non-dimensional velocity components as a function of x, y and z.

    - example: `["2 * cos(y)", "-2 * sin(x)", "0"]` specifies a wall rotating around the z axis at an angular velocity of 2
    - default: `[0, 0, 0]`


## SlipWall
  
Slip wall condition for a inviscid impermeable boundary. Also used for symmetry condition.
  
## IsothermalWall
  
Isothermal wall boundary condition. A static “Temperature” is specified in Kelvin. Optionally a tangential velocity can be presribed for a moving or rotating wall.
  
### parameters:

- `Temperature`: wall (static) temperature in Kelvin (K),
    - it can be expressed as a function of x, y, z, and t (time).
    - example 

- *optional* `Velocity`: an expression for each of non-dimensional velocity components as a function of x, y and z.

    - example: `["2 * cos(y)", "-2 * sin(x)", "0"]` specifies a wall rotating around the z axis at an angular velocity of 2
    - default: `[0, 0, 0]`

## SubsonicOutflowPressure
  
Subsonic outflow boundary condition, enforced through static pressure ratio. This is the target ratio of boundary static pressure to freestream static pressure.
  
### parameters:

- `staticPressureRatio`: target ratio of boundary static pressure to freestream static pressure.

## SubsonicOutflowMach
  
Equivalent static pressure outflow boundary condition set via a specified subsonic Mach number.

### parameters:

- `MachNumber`: target outflow Mach number at the boundary. Must be less than 1.


## SubsonicInflow
  
Subsonic inflow boundary condition, enforced via total pressure ratio and total temperature ratio, for nozzle or tunnel plenum.
These are the target ratios of boundary total pressure and total temperature to freestream static values.
  
### parameters:
- `totalPressureRatio`: target ratio of boundary total pressure to freestream static pressure.
- `totalTemperatureRatio`: target ratio of boundary total temperature to freestream static temperature.
- `rampSteps`: ramp steps for pressure and total ratios.
    - this is the number of pseudo-time steps during which total pressure and total temperature ratios are ramped up initially from 1 to the target ratios through a steady simulation.


## MassOutflow
  
Outflow boundary condition via mass-flow-rate out of the simulation domain through this boundary.

### parameters:
- `massFlowRate`: Mass Flow Rate
  
    - This is the integrated mass flow rate out of the simulation domain through this boundary, calculated as density * normal velocity * area. 
    - nondimensionalization used: the freestream density, the freestream speed of sound, and the mesh length unit

  
## MassInflow: 
  
Inflow boundary condition via mass-flow-rate into the simulation domain through this boundary.

### parameters:
- `massFlowRate`: Mass Flow Rate
  
    - This is the integrated mass flow rate into the simulation domain through this boundary, calculated as density * normal velocity * area. 
    - nondimensionalization used: the freestream density, the freestream speed of sound, and the mesh length unit



  

