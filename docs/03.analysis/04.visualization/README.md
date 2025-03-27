# Visualization

Flow360's visualization interface provides powerful capabilities for analyzing and understanding computational fluid dynamics (CFD) simulation results. The interactive 3D viewer allows users to examine flow features through various visualization techniques, enabling both qualitative and quantitative analysis of simulation data.

---

## 🎯 Interface Overview

| **Component** | **Description** |
|--------------|-----------------|
| `Visualization Panel` | Left-side panel with controls for selecting and configuring visualization methods |
| `3D Viewer` | Central area displaying the interactive 3D visualization |
| `Entity Tree` | Right-side panel showing hierarchical view of geometric entities |
| `Colormap Controls` | Bottom panel for customizing color scales and ranges |

---

## 📊 Surface Visualization

*Display flow field variables on geometric surfaces of the model.*

### 📋 Available Fields

Selectable fields depend on the surface output configuration in simulation settings. For a complete list, refer to [surface output](../../01.simulation-setup/08.output-settings/03.surface-output.md).

---

## 🔪 Slice Visualization

*Create 2D cross-sectional views of the flow field for detailed examination of flow features.*

### 📋 Available Fields

Selectable fields depend on the slice output configuration. For a complete list, refer to [slice output](../../01.simulation-setup/08.output-settings/05.slice-output.md).

---

## 🌐 Isosurface Visualization

*Generate 3D surfaces of constant value for selected flow variables.*

### 📋 Available Fields

Selectable fields depend on the isosurface output configuration. For a complete list, refer to [isosurface output](../../01.simulation-setup/08.output-settings/10.isosurface-output.md).

---

<details>
<summary><h3 style="display:inline-block"> 💡 Tips</h3></summary>

- **Surface Visualization**
  - Start with pressure coefficient (`Cp`) for quick flow behavior assessment
  - Use `yPlus` to verify mesh resolution near walls
  - Enable log scale for variables with large value ranges

- **Slice Visualization**
  - Place initial slices at key geometric features
  - Use multiple slices to track flow development
  - Compare variables on the same slice plane for correlation analysis

- **Isosurface Visualization**
  - Combine with surface visualization for comprehensive analysis

</details>

---

<details>
<summary><h3 style="display:inline-block"> ❓ Frequently Asked Questions</h3></summary>

- **Why are some fields not available in my visualization?**
  > Available fields depend on the output configuration in your simulation settings. Check the corresponding output settings in your simulation configuration.

- **Can I export visualization images?**
  > Yes, either manually create a screenshot or use the report generation capability in Python API.

</details>

---

<details>
<summary><h3 style="display:inline-block"> 🐍 Python Example Usage</h3></summary>

Below is a Python code example showing how to download visualizations:

```python
import flow360 as fl

case = fl.Case(id="case-XXXXX") # provide a valid case id
case.wait() # wait for the case to finish running
results = case.results

# Volumes
results.volumes.to_file("volume_output")

# Slices
results.slices.to_file("slice_output")

# Surfaces
results.surfaces.to_file("surface_output")
```

</details> 