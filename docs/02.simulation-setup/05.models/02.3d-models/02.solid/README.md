## **Solid Model**

*The Solid model is used for setting up conjugate heat transfer volume models that contain all the common fields every heat transfer zone should have. This model is essential for simulating heat transfer in solid materials within the Flow360 simulation environment.*

---

### 📋 **Available Options**

| **Option** | **Description** | **Unit** |
|------------|----------------|-----------|
| `name` | Optional name identifier for the Solid model | |
| `entities` | List of volume entities where heat transfer equations will be solved | |
| `material` | Material properties of the solid | thermal conductivity (e.g., W/m·K), density (e.g., kg/m³), specific heat capacity (e.g., J/kg·K) |
| `heat_equation_solver` | Settings for the heat equation solver. See [Heat Equation Solver](./01.heat-equation-solver.md) documentation for details. | |
| `volumetric_heat_source` | Heat source per unit volume | power per volume (e.g., W/m³) |
| `initial_condition` | Initial temperature condition for the heat equation | temperature (e.g., K) |

---

### 🔍 **Detailed Descriptions**

#### `name`

*An optional identifier for the Solid model instance.*

- **Default:** `None`
- **Example:** `"solid_block"`
- **Notes:** Used for identification and reference purposes.

#### `entities`

*List of volume entities where the heat transfer equation will be solved.*

- **Default:** Required field
- **Example:** `[volume_mesh["solid-*"]]`
- **Notes:** Accepts volume mesh entities or patterns matching multiple volumes.

#### `material`

*Material properties of the solid, defining thermal characteristics.*

- **Default:** Required field
- **Example:** See Python example below
- **Notes:** Must specify thermal conductivity, density, and specific heat capacity.

#### `heat_equation_solver`

*Configuration for the heat equation solver settings. See [Heat Equation Solver](./01.heat-equation-solver.md) documentation for details.*

- **Default:** See [Heat Equation Solver](./01.heat-equation-solver.md#-available-options) for default values
- **Example:** See Python example below
- **Notes:** Controls solver parameters like tolerance and iteration limits.

#### `volumetric_heat_source`

*Specifies the heat source per unit volume in the solid.*

- **Default:** `0 W/m³`
- **Example:** `1.0 * fl.u.W / fl.u.m**3`
- **Notes:** Can be a constant value or a string expression.

#### `initial_condition`

*Initial temperature condition for the heat equation solver.*

- **Default:** `None`
- **Example:** `HeatEquationInitialCondition(temperature="1.0")`
- **Notes:** Can be specified using expressions for spatial variation.

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
  > The solver will use a default uniform temperature field.

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