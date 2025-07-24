# Solid Model

::: warning Volume Mesh Workflow Only
The Solid model is only available in the volume mesh workflow. It cannot be used with the surface mesh workflow.
:::

*The Solid model is used for setting up conjugate heat transfer volume models that contain all the common fields every heat transfer zone should have. This model is essential for simulating heat transfer in solid materials within the Flow360 simulation environment.*

---

## **Available Parameters**

| *Parameter* | *Description* |
|-------------|---------------|
| **[Material](./02.material.md)** | Material properties of the solid |
| **[Heat equation solver](./01.heat-equation-solver.md)** | Settings for the heat equation solver |
| **Volumetric heat source** | Heat source per unit volume |
| **[Initial condition](./03.initial-condition.md)** | Initial temperature condition for the heat equation |
| **Assigned zones** | List of volume entities where heat transfer equations will be solved |

---

## **Detailed Descriptions**


### **[Material](./02.material.md)** 

*Material properties of the solid, defining thermal characteristics.*

The details of the material setup are outlined [here](./02.material.md).

### **[Heat equation solver](./01.heat-equation-solver.md)**

*Configuration for the heat equation solver settings. See [Heat Equation Solver](./01.heat-equation-solver.md) documentation for details.*

The details of the heat equation solver setup are outlined [here](./01.heat-equation-solver.md).

### **Volumetric heat source**

*Specifies the heat source per unit volume in the solid.*

- **Default:** `0 W/m³`
- **Example:** `1.0  W/m`
>**Note:** Can be a constant value or a string expression.

###  **[Initial condition](./03.initial-condition.md)**

*Initial temperature condition for the heat equation solver.*

The details of the initial condition setup are outlined [here](./03.initial-condition.md).

### **Assigned zones**

*List of volume entities where the heat transfer equation will be solved.*

- **Required**
> **Note:** Accepts volume mesh entities or patterns matching multiple volumes.

---

<details>
<summary><h3 style="display:inline-block"> 💡 Tips</h3></summary>

- Ensure all material properties are specified in consistent units.
- When using patterns in entities, verify all matched volumes are intended for heat transfer simulation.
- Consider mesh resolution near areas with high temperature gradients.
- For conjugate heat transfer, ensure proper interface matching with fluid regions.

</details>

---

<details>
<summary><h3 style="display:inline-block"> ❓ Frequently Asked Questions</h3></summary>

- **What happens if I don't specify an initial condition?**  
  > For steady simulations, the solver will use a default uniform temperature field. For unsteady simulations, an initial condition must be specified.

- **Can I simulate multiple solid materials?**  
  > Yes, create multiple Solid model instances with different materials and assign them to different volumes.

</details>

---

<details>
<summary><h3 style="display:inline-block"> 🐍 Python Example Usage</h3></summary>

Below is a Python code example showing how to configure a Solid model for conjugate heat transfer:

```python
# Define a Solid model for volumes with the name pattern "solid-*"
solid_model = fl.Solid(
    entities=[volume_mesh["solid-*"]],
    heat_equation_solver=fl.HeatEquationSolver(
        equation_evaluation_frequency=2,
        linear_solver=fl.LinearSolver(
            absolute_tolerance=1e-10,
            max_iterations=50
        ),
        relative_tolerance=0.001,
    ),
    initial_condition=fl.HeatEquationInitialCondition(temperature="1.0"),
    material=fl.SolidMaterial(
        name="aluminum",
        thermal_conductivity=235 * fl.u.kg / fl.u.s**3 * fl.u.m / fl.u.K,
        density=2710 * fl.u.kg / fl.u.m**3,
        specific_heat_capacity=903 * fl.u.m**2 / fl.u.s**2 / fl.u.K,
    ),
    volumetric_heat_source=1.0 * fl.u.W / fl.u.m**3,
)
```

</details> 