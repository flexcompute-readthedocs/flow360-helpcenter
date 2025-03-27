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
    - U_∞ = Mach · cos(β) · cos(α)
    - W_∞ = Mach · cos(β) · sin(α)

#### `Beta`

The sideslip angle defining the orientation of the freestream flow relative to the model. Positive values typically indicate flow from the right.

- **Default:** 0 degrees
- **Example:** 2 degrees
- **Notes:** 
  - The angle is applied around the Z-axis of the global coordinate system after alpha is applied.
  - Affects velocity components according to these formulas:
    - U_∞ = Mach · cos(β) · cos(α)
    - V_∞ = -Mach · sin(β)
    - W_∞ = Mach · cos(β) · sin(α)

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

### 💡 **Tips**

- For steady hover simulations, set freestream velocity to zero and provide a reference velocity.
- Use standard atmosphere for simulations that need realistic atmospheric conditions.
- When comparing with wind tunnel data, match Reynolds number by adjusting both velocity and thermal state.
- For low-speed simulations (M < 0.3), incompressible formulations may be more efficient.
- Reynolds number in the simulation is calculated using the mesh unit length, not necessarily a physical reference length.

---

### ❓ **Frequently Asked Questions**

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
  > - U_∞ = Mach · cos(β) · cos(α)
  > - V_∞ = -Mach · sin(β)
  > - W_∞ = Mach · cos(β) · sin(α)
  > 
  > This simplifies comparing results at different angles without modifying the mesh.

- **Can I specify a different material other than Air?**  
  > In the GUI, only Air is available. For custom materials, you need to use the Python API. 