# Solid model

::: warning Volume Mesh Workflow Only
The Solid model is only available in the volume mesh workflow. It cannot be used with the surface mesh workflow.
:::

*The Solid model is used for setting up conjugate heat transfer volume models that contain all the common fields every heat transfer zone should have. This model is essential for simulating heat transfer in solid materials within the Flow360 simulation environment.*

## **Major Components**

1.  **[Heat equation solver](./01.heat-equation-solver.md)**: Controls settings for the heat equation solver, including tolerances and iteration limits.
2.  **[Material](./02.material.md)**: Defines material properties of the solid, such as thermal conductivity, density, and specific heat capacity.
3.  **Volume heat source**: Specifies a heat source per unit volume within the solid material.
4.  **[Initial condition](./03.initial-condition.md)**: Sets initial temperature field for the heat equation.
5.  **Assigned zones**: A list of volume zones where the heat transfer equations will be solved.

## **Configuration Example**

Below is a representative example of a Solid model configuration (shown for reference purposes):

```
Solid:
  Heat equation solver:
    Absolute tolerance: 1.0e-10
    Equation evaluation frequency: 2
    Relative tolerance: 0.001
    Linear solver:
      
      Max iterations: 50
  Material:
    Name: "aluminum"
    Thermal conductivity: 235 kg*m/(K*s**3)
    Density: 2710 kg/m**3
    Specific heat capacity: 903 m**2/(K*s**2)
  Volumetric heat source: 100 W/m**3
  Initial condition:
    Temperature: 1.0
  Assigned zones: ["solid-*"]
```

## **Common Applications**

The Solid model is used in conjugate heat transfer simulations, including:

- Electronics cooling (heat sinks, PCBs)
- Engine component analysis (cylinder heads, exhaust manifolds)
- Heat exchangers
- Building insulation and thermal management
- Aerospace applications (re-entry vehicle heat shields, turbine blade cooling)

## **Best Practices**

- Ensure all material properties are specified in consistent units.
- When using patterns in entities, verify all matched volumes are intended for heat transfer simulation.
- Consider mesh resolution near areas with high temperature gradients.
- For conjugate heat transfer, ensure proper interface matching with fluid regions.

```{toctree}
:hidden:
:maxdepth: 3
./01.heat-equation-solver.md
./02.material.md
./03.initial-condition.md
``` 