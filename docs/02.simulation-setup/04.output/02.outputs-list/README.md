# Outputs List

*Control what data is generated during and after simulation runs, including which flow variables are saved, where they are saved, and how frequently they are written to files.*

---

## **Available Output Types**

| *Output Type* | *Description* | *Use Case* |
|---------------|---------------|------------|
| **[Volume Output](./01.volume-output.md)** | Flow field data throughout the computational volume | Visualizing 3D flow structures, vortex development |
| **[Time-averaging Volume Output](./02.time-averaging-volume-output.md)** | Time-averaged flow field data throughout the volume | Statistical analysis of unsteady flows |
| **[Surface Output](./03.surface-output.md)** | Flow field data on geometry or volume mesh boundaries | Analyzing surface forces, pressure distributions |
| **[Time-averaging Surface Output](./04.time-averaging-surface-output.md)** | Time-averaged flow field data on surfaces | Statistical analysis of surface phenomena |
| **[Slice Output](./05.slice-output.md)** | Flow field data on user-defined slice planes | Examining flow cross-sections |
| **[Time-averaging Slice Output](./06.time-averaging-slice-output.md)** | Time-averaged flow field data on slice planes | Statistical analysis on planes |
| **[Probe Outputs](./07.probe-outputs.md)** | Flow field data monitoring during simulation | Tracking convergence and flow properties |
| **[Time-averaging Probe Outputs](./08.time-averaging-probe-outputs.md)** | Time-averaged monitoring data | Statistical monitoring data |
| **[Surface Probe Output](./09.surface-probe-outputs.md)** | Flow field data at specific points projected onto surfaces | Point-specific surface data |
| **[Isosurface Output](./11.isosurface-output.md)** | Flow field data on surfaces of constant variable value | Visualization of vortices, shock waves |
| **[Time-averaging Isosurface Output](./12.time-averaging-isosurface-output.md)** | Time-averaged flow field data on surfaces of constant variable value | Statistical analysis of vortices, shock waves |
| **[Aeroacoustic Output](./13.aeroacoustic-output.md)** | Data for aeroacoustic analysis at observer positions | Noise prediction and analysis |
| **[Force Output](./14.force-output.md)** | Force and moment coefficient outputs with optional statistics | Tracking aerodynamic performance, monitoring convergence |
| **[Streamline Output](./15.streamline-output.md)** | Streamline visualization data | Visualization of 3D flow structures |

---

## **Additional Outputs Available Through Python API**

| *Output Type* | *Description* | *Use Case* |
|---------------|---------------|------------|
| **[Surface Slice Output](./10.surface-slice-output.md)** | Flow field data on slices of surfaces | Cross-sectional analysis of surface phenomena |

---

## **Common Settings**

### **Output Fields**

*The flow variables to include in the output.*

- **Default:** Varies by output type
- **Example:** `["Cp", "Cf", "Mach"]`
>**Note:** See [Output Fields and Nondimensional Values](00.output-fields.md) for details on available fields.

### **Frequency**

*How often to write output files (in number of time steps).*

- **Default:** `-1` (output only at the end of simulation)
- **Example:** `100` (output every 100 time steps)
>**Note:** Increase for animations, decrease for storage efficiency.

### **Frequency Offset**

*The time step at which to start writing output.*

- **Default:** `0` (start at beginning of simulation)
- **Example:** `1000` (start after 1000 time steps)
>**Note:** Controls when output generation begins.

### **Output Format**

*The file format for output data.*

- **Default:** `paraview`
- **Options:**
  - `paraview`
  - `tecplot`
  - `both`
>**Note:** Choose the format that best suits your post-processing workflow.

## 📁 **Output File Formats**

Flow360 supports multiple output file formats:

- **Paraview** (.vtu, .vtp) - For visualization in ParaView
- **Tecplot** (.szplt) - For visualization in Tecplot
- **CSV** - For tabular data

For more information about output file formats, see the [Output Formats](16.output-formats.md) page.

## **Detailed Settings**

Each output type has specific configuration options. For detailed documentation on configuring each type of output, refer to the links in the table above. 

---

## Available Output Fields

### **Universal Variables** (non-dimensional)

- `Cp` - Coefficient of pressure
- `Cpt` - Coefficient of total pressure
- `gradW` - Gradient of primitive solution
- `kOmega` - k and omega
- `Mach` - Mach number
- `mut` - Turbulent viscosity
- `mutRatio` - Turbulent viscosity and freestream dynamic viscosity ratio
- `nuHat` - Spalart-Almaras variable
- `primitiveVars` - Density, velocities (u,v,w), and pressure
- `qcriterion` - Q criterion for vortex identification
- `residualNavierStokes` - N-S residual
- `residualTransition` - Transition residual
- `residualTurbulence` - Turbulence residual
- `s` - Entropy
- `solutionNavierStokes` - N-S solution
- `solutionTransition` - Transition solution
- `solutionTurbulence` - Turbulence solution
- `T` - Temperature
- `velocity` - Velocity vector
- `velocity_magnitude` - Magnitude of velocity vector
- `pressure` - Pressure
- `vorticity` - Vorticity
- `vorticityMagnitude` - Vorticity Magnitude
- `wallDistance` - Wall distance
- `numericalDissipationFactor` - NumericalDissipationFactor sensor
- `residualHeatSolver` - Heat equation residual
- `VelocityRelative` - Velocity with respect to non-inertial frame
- `lowMachPreconditionerSensor` - Low-Mach preconditioner factor

### **Custom Variables**

User defined expressions with dimensions. By default, the following expressions are available:

| Variable Name                         | Expression                                      |
|--------------------------------------|-------------------------------------------------|
| `velocity_with_units`                | `solution.velocity`                             |
| `velocity_magnitude_with_units`      | `math.magnitude(solution.velocity)`             |
| `pressure_with_units`                | `solution.pressure`                             |
| `wall_shear_stress_magnitude_with_units` | `solution.wall_shear_stress_magnitude`     |

---

<details>
<summary><h3 style="display:inline-block"> 💡 Tips</h3></summary>

- Be selective with Output Fields to manage file sizes
- Use Time-Averaged outputs for statistical analysis of unsteady flows
- For large meshes, consider using Slice or Surface outputs instead of Volume outputs
- For better performance, limit output frequency to necessary intervals

</details>

---

<details>
<summary><h3 style="display:inline-block"> ❓ Frequently Asked Questions</h3></summary>

- **How can I visualize vortices in my flow?**  
  > Use Volume Output with Q-criterion field or create dedicated Isosurface Output of Q-criterion.

- **What's the difference between Surface Output and Surface Probe Output?**  
  > Surface Output captures data across entire surfaces, while Surface Probe Output captures data at specific points on surfaces.

- **Can I save outputs in different formats?**  
  > Yes, you can choose between Paraview (.vtu, .vtp), Tecplot (.szplt), or both formats.

</details>

---

```{toctree}
:hidden:
:maxdepth: 3
./01.volume-output.md
./02.time-averaging-volume-output.md
./03.surface-output.md
./04.time-averaging-surface-output.md
./05.slice-output.md
./06.time-averaging-slice-output.md
./07.probe-outputs.md
./08.time-averaging-probe-outputs.md
./09.surface-probe-outputs.md
./10.surface-slice-output.md
./11.isosurface-output.md
./12.time-averaging-isosurface-output.md
./13.aeroacoustic-output.md
./14.force-output.md
./15.streamline-output.md
./00.output-fields.md
./16.output-formats.md
```