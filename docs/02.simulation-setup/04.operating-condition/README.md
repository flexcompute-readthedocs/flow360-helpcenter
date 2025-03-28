# Operating Condition

The Operating Condition section in Flow360 allows you to specify the freestream flow conditions and reference values for your simulation. These settings determine how the simulation interacts with the surrounding environment and how force coefficients are calculated.

## 📝 **Aerospace Condition**

The Aerospace Condition defines both the freestream flow condition for the simulation and reference parameters used to compute non-dimensional coefficients in post-processing.

---

### 📋 **Available Options**

| **Option** | **Description**                  | **Unit** |
|------------|----------------------------------|----------|
| `Velocity Magnitude` | Freestream velocity | velocity (e.g., m/s) |
| `Mach` | Freestream Mach number | dimensionless |
| `Alpha` | Angle of attack | degrees |
| `Beta` | Sideslip angle | degrees |
| `Thermal State - Direct` | Temperature and density | temperature (e.g., K), density (e.g., kg/m³) |
| `Thermal State - Standard Atmosphere` | Altitude and temperature offset | altitude (e.g., m), temperature offset (e.g., K) |
| `Reference Velocity` | Reference value for coefficient calculation | velocity (e.g., m/s) |
| `Reference Mach` | Reference Mach for coefficient calculation | dimensionless |

---

### 🔍 **Detailed Descriptions**

#### `Velocity Magnitude`

Define the freestream velocity using direct velocity magnitude. 

- **Default:** None (must be specified)
- **Example:** 100 m/s
- **Notes:** For hover or static conditions, you can set this to zero but must provide a reference velocity for coefficient calculations.

#### `Mach`

Define the freestream Mach number. 

- **Default:** None (must be specified)
- **Example:** Mach 0.8
- **Notes:** For hover or static conditions, you can set this to zero but must provide a reference velocity for coefficient calculations.

#### `Alpha`

The angle of attack defining the orientation of the freestream flow relative to the model. Positive values typically indicate nose-up orientation.

- **Default:** 0 degrees
- **Example:** 5 degrees
- **Notes:** 
  - The angle is applied around the Y-axis of the global coordinate system.
  - Affects velocity components according to these formulas:
    - U_∞ = U_mag · cos(β) · cos(α)
    - W_∞ = U_mag · cos(β) · sin(α)
  - Where:
    - U_mag is the velocity magnitude prescribed by either Velocity Magnitude or Mach number
    - U_∞ is the x-component of velocity in the global coordinate system
    - W_∞ is the z-component of velocity in the global coordinate system

#### `Beta`

The sideslip angle defining the orientation of the freestream flow relative to the model. Positive values typically indicate flow from the right.

- **Default:** 0 degrees
- **Example:** 2 degrees
- **Notes:** 
  - The angle is applied around the Z-axis of the global coordinate system after alpha is applied.
  - Affects velocity components according to these formulas:
    - U_∞ = U_mag · cos(β) · cos(α)
    - V_∞ = -U_mag · sin(β)
    - W_∞ = U_mag · cos(β) · sin(α)
  - Where:
    - U_mag is the velocity magnitude prescribed by either Velocity Magnitude or Mach number
    - U_∞ is the x-component of velocity in the global coordinate system
    - V_∞ is the y-component of velocity in the global coordinate system
    - W_∞ is the z-component of velocity in the global coordinate system

#### `Thermal State - Direct`

Defines the freestream temperature and density directly.

- **Default:** None (must be specified)
- **Example:** 250 K, 1.0 kg/m³
- **Notes:** Fluid material is fixed as Air in the GUI.

#### `Thermal State - Standard Atmosphere`

Defines the freestream temperature and density using standard atmosphere model.

- **Default:** None (must be specified)
- **Example:** 10,000 m altitude with -5 K offset
- **Notes:** Fluid material is fixed as Air in the GUI.

#### `Reference Velocity`

Optional reference velocity used for calculating force and moment coefficients. Required when freestream velocity is zero.

- **Default:** Same as freestream value
- **Example:** 100 m/s
- **Notes:** Particularly important for static/hover cases or when you want coefficients referenced to a different velocity than freestream.

#### `Reference Mach`

Optional reference Mach number used for calculating force and moment coefficients. Required when freestream Mach number is zero.

- **Default:** Same as freestream value
- **Example:** Mach 0.8
- **Notes:** Particularly important for static/hover cases or when you want coefficients referenced to a different Mach number than freestream.

---

<details>
<summary><h3 style="display:inline-block"> 💡 Tips</h3></summary>

- For steady hover simulations, set freestream velocity to zero and provide a reference velocity.
- Use standard atmosphere for simulations that need realistic atmospheric conditions.
- When comparing with wind tunnel data, match Reynolds number by adjusting both velocity and thermal state.
- For low-speed simulations (M < 0.3), using a low Mach preconditioner is recommended for better efficiency.
- Reynolds number in the simulation is calculated using the mesh unit length, not necessarily a physical reference length.

<details style="padding-left:20px">
<summary><h4 style="display:inline-block"> Advanced Mach and Reynolds Number Considerations</h4></summary>

- For transonic flows (0.8 < M < 1.2), use finer meshes near shock regions to capture discontinuities.
- When matching experimental data, ensure you're using the same reference values for non-dimensionalization.
- Remember that the Reynolds number affects boundary layer thickness—higher Reynolds numbers result in thinner boundary layers requiring finer near-wall mesh resolution.
- For simulations containing multiple components (e.g., many propellers), the same reference values will be used across all components.
- When using Standard Atmosphere, be aware that density decreases exponentially with altitude, which affects Reynolds number significantly.

</details>
</details>

---
<details>
<summary><h3 style="display:inline-block"> ❓ Frequently Asked Questions</h3></summary>

- **What is the difference between velocity magnitude and reference velocity?**  
  > Velocity magnitude defines the actual freestream flow speed, while reference velocity is used for calculating non-dimensional coefficients. For most cases, they are the same, but for hover or special cases, you might want different values.

- **How is Reynolds number calculated in Flow360?**  
  > Reynolds number is calculated as Re = ρ·V·L/μ, where ρ is density, V is reference velocity, L is the reference length unit in the mesh, and μ is dynamic viscosity.

- **Can I simulate altitude effects?**  
  > Yes, by using the Standard Atmosphere option in Thermal State. This automatically sets temperature and density based on the specified altitude.

- **What happens if I leave Reference Velocity blank?**  
  > If freestream velocity is non-zero, the reference velocity defaults to the freestream value. If freestream velocity is zero, a reference velocity must be provided.

- **How do alpha and beta affect the simulation?**  
  > Rather than rotating the geometry, Flow360 adjusts the freestream flow direction based on alpha and beta using the formulas:
  > - U_∞ = U_mag · cos(β) · cos(α)
  > - V_∞ = -U_mag · sin(β)
  > - W_∞ = U_mag · cos(β) · sin(α)
  > 
  > Where U_mag is the velocity magnitude prescribed by either Velocity Magnitude or Mach number and U_∞, V_∞, and W_∞ represent the x, y, and z components of velocity in the global coordinate system, respectively. This simplifies comparing results at different angles without modifying the mesh.

- **Can I specify a different material other than Air?**  
  > In the GUI, only Air is available. For custom materials, you need to use the Python API. 

</details>

---

<details>
<summary><h3 style="display:inline-block"> 🐍 Python Example Usage</h3></summary>

Below is a Python code example showing how to configure operating conditions using the Flow360 Python API:

```python
import flow360 as fl
from flow360 import u

# Example 1: Setting up a condition with velocity magnitude
condition = fl.AerospaceCondition(
    velocity_magnitude=100 * u.m / u.s,
    alpha=5 * u.degree,
    beta=0 * u.degree,
    thermal_state=fl.ThermalState(
        temperature=288.15 * u.K,
        density=1.225 * u.kg / u.m**3
    )
)

# Example 2: Setting up a condition using from_mach with a reference Mach
condition = fl.AerospaceCondition.from_mach(
    mach=0.8,
    alpha=2 * u.degree,
    beta=1 * u.degree,
    thermal_state=fl.ThermalState(
        temperature=250 * u.K,
        density=0.9 * u.kg / u.m**3
    ),
    reference_mach=0.75  # For coefficient calculations
)

# Example 3: Setting up a hover condition (zero freestream) with reference values
hover_condition = fl.AerospaceCondition(
    velocity_magnitude=0 * u.m / u.s,
    alpha=0 * u.degree,
    beta=0 * u.degree,
    thermal_state=fl.ThermalState(
        temperature=288.15 * u.K,
        density=1.225 * u.kg / u.m**3
    ),
    reference_velocity_magnitude=100 * u.m / u.s  # Required for hover cases
)

# Example 4: Using standard atmosphere model for thermal state
condition = fl.AerospaceCondition(
    velocity_magnitude=200 * u.m / u.s,
    alpha=3 * u.degree,
    beta=0 * u.degree,
    thermal_state=fl.ThermalState.from_standard_atmosphere(
        altitude=10000 * u.m,
        temperature_offset=-5 * u.K
    )
)

# Example 5: Creating a condition from Mach and Reynolds number

condition = fl.operating_condition_from_mach_reynolds(
    mach=0.85,
    reynolds=1e6,
    project_length_unit=1 * u.m,
    temperature=288.15 * u.K,
    alpha=2.0 * u.degree,
    beta=0.0 * u.degree,
    reference_mach=0.85
)

# Example 6: Calculating Reynolds number for an existing condition
project_length_unit = 1 * u.m  # Physical length represented by unit length in mesh
reynolds = condition.flow360_reynolds_number(length_unit=project_length_unit)
print(f"Reynolds number: {reynolds}")


```

</details>