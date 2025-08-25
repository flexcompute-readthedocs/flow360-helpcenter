# Fluid model

*The Fluid model represents the primary medium for CFD simulations in Flow360. It integrates several components that together govern the fluid dynamics behavior, including the Navier-Stokes solver, turbulence modeling, transition effects, and initial conditions. The Fluid model is applied to volume entities within your simulation domain.*

> **Note:** The Fluid model itself does not contain fluid parameters such as density and temperature. These properties are instead specified in the **[Operating Condition](../../../01.flow-conditions/01.operating-condition.md)** section of your simulation setup. This separation allows the same Fluid model configuration to be used with different conditions.

## **Major Components**

The Fluid model consists of four primary components, each documented in detail in its own section:

1. [**Navier-Stokes Solver**](./01.navier-stokes-solver.md): Controls the core flow equations that govern momentum, continuity, and energy in the fluid. This component determines how the simulation resolves velocity, pressure, and density fields.

2. [**Turbulence Model**](./02.turbulence-model.md): Handles the modeling of turbulent flow structures through various approaches such as Spalart-Allmaras or k-Omega SST. This significantly impacts flow separation prediction and overall solution accuracy.

3. [**Transition Model**](./03.transition-model.md): Determines how and when flow transitions from laminar to turbulent within the simulation, which is critical for correctly predicting aerodynamic performance, especially at moderate Reynolds numbers.

4. [**Initial Condition**](./04.initial-condition.md): Defines the starting flow state for the simulation, which can significantly impact convergence rates and stability, especially for complex flows.

## **Configuration Example**

Below is a representative example of a Fluid model configuration (shown for reference purposes):

```
Fluid:
  Navier-Stokes Solver:
    Absolute Tolerance: 1.0e-10
    Order of Accuracy: 2
    Low Mach Preconditioner: True
    
  Turbulence Model:
    Type: Spalart-Allmaras
    Absolute Tolerance: 1.0e-8
    
  Transition Model:
    Type: None
    
  Initial Condition:
    Type: NavierStokesInitialCondition
    Rho: "rho"
    U: "u"
    V: "v"
    W: "w"
    P: "p"
```

## **Common Applications**

The Fluid model is used in virtually all Flow360 simulations, including:

- External aerodynamics (aircraft, automobiles, sports equipment)
- Internal flows (ducts, channels, pipes)
- Turbomachinery (fans, compressors, turbines)
- Propulsion systems (propellers, rotors, jets)
- Heat transfer applications (when coupled with thermal models)

## **Best Practices**

- Match the solver settings to your specific application requirements and flow regime
- For most aerospace applications, the Spalart-Allmaras turbulence model provides a good balance of accuracy and efficiency
- Consider enabling the transition model for flows at moderate Reynolds numbers where transition location significantly impacts results
- For challenging simulations, start with more robust settings (lower CFL, higher gradient limiters) and then relax these constraints as the solution develops
- Remember that fluid properties (viscosity, etc.) must be specified in the Operating Condition section, not in the Fluid model

```{toctree}
:hidden:
:maxdepth: 3
./01.navier-stokes-solver.md
./02.turbulence-model.md
./03.transition-model.md
./04.initial-condition.md
``` 

