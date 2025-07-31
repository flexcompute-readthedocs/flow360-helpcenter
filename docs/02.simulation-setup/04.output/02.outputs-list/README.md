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
| **[Time-averaging Probe Outputs](./08.Time-averaging-probe-outputs.md)** | Time-averaged monitoring data | Statistical monitoring data |
| **[Surface Probe Output](./09.surface-probe-outputs.md)** | Flow field data at specific points projected onto surfaces | Point-specific surface data |
| **[Isosurface Output](./11.isosurface-output.md)** | Flow field data on surfaces of constant variable value | Visualization of vortices, shock waves |
| **[Time-averaging Isosurface Output](./12.time-averaging-isosurface-output.md)** | Time-averaged flow field data on surfaces of constant variable value | Statistical analysis of vortices, shock waves |
| **[Aeroacoustic Output](./13.aeroacoustic-output.md)** | Data for aeroacoustic analysis at observer positions | Noise prediction and analysis |
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
- **Notes:** 
  - See [Output Fields and Nondimensional Values](00.output-fields.md) for details on available fields.

### **Frequency**

*How often to write output files (in number of time steps).*

- **Default:** `-1` (output only at the end of simulation)
- **Example:** `100` (output every 100 time steps)
- **Notes:**
  - Increase for animations, decrease for storage efficiency.

### **Frequency Offset**

*The time step at which to start writing output.*

- **Default:** `0` (start at beginning of simulation)
- **Example:** `1000` (start after 1000 time steps)
- **Notes:** 
  - Controls when output generation begins.

### **Output Format**

*The file format for output data.*

- **Default:** `paraview`
- **Options:**
  - `paraview`
  - `tecplot`
  - `both`
- **Notes:** 
  - Choose the format that best suits your post-processing workflow.

## 📁 **Output File Formats**

Flow360 supports multiple output file formats:

- **Paraview** (.vtu, .vtp) - For visualization in ParaView
- **Tecplot** (.szplt) - For visualization in Tecplot
- **CSV** - For tabular data

For more information about output file formats, see the [Output Formats](13.output-formats.md) page.

## **Detailed Settings**

Each output type has specific configuration options. For detailed documentation on configuring each type of output, refer to the links in the table above. 

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

