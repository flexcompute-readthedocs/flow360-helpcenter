# Workbench Layout

The Flow360 workbench provides an intuitive interface for computational fluid dynamics (CFD) simulations. This document describes the key areas of the workbench layout and their functions.

![Workbench Layout Overview](../Figures/workbench_arrows.png)

---

## 📋 **Main Interface Sections**

| *Section* | *Description* |
|-------------|-----------------|
| 1 | [Viewer region](./05.viewer-region.md) |
| 2 | [Simulation setup](./../../02.simulation-setup/README.md) / [Analysis](./../../03.analysis/README.md) |
| 3 | [Entities browser](./06.entities-browser/README.md) |
| 4 | Coordinate system |
| 5 | [Top navigation bar](./04.top-bar.md) |
| 6 | [Bottom status bar](./07.status-bar.md) |
| 7 | [Viewer bar](./05.viewer-region.md) | 

---

## 🔍 **Detailed Descriptions**

### 1️⃣ **Viewer region**

*The central workspace where the geometry, mesh, and simulation results are displayed.* 

**This interactive 3D viewport allows you to:**
- Rotate (hold left mouse button), pan (hold right mouse button), and zoom the model (use the scroll)
- Select and inspect geometric features (left click)
- Preview created entities such as volumes or slices
- View mesh details
- Visualize simulation results and flow fields

>**Note:** Click right-mouse button while hovering in the model view area to see additional settings.

#### 2️⃣ **Simulation setup / Analysis**

*A comprehensive control panel containing all simulation parameters and settings.*

**In this panel you will:**

- Type in your meshing parameters
- Set up the simulation's physics
- Change the solver numerics
- Define anticipated outputs
- Analyze and monitor the solution
- Visualise the results

#### 3️⃣ **Entities browser**

*Dedicated controls for visual representation of the model and results.*
- Geometry display options
- Mesh visualization settings
- Results visualization tools
- Display modes and rendering options

#### 4️⃣ **Coordinate system**

*Persistent coordinate system.*

- X, Y, and Z axes orientation
- Current view direction

#### 5️⃣ **Top navigation bar**

*Primary navigation and tool selection area.*

**Actions available through the top bar:**
- Return to Flow360 dashboard
- Project tree
- Information about the current selected asset
- More button
- View only information (optional)
- Assets
- Help
- Project settings
- Fork / run case

#### 6️⃣ **Bottom status bar**

*Information and status display*

- Current operation status
- Progress indicators
- Inspector tools
- Run status information

#### 7️⃣ **Viewer bar**

*Allows you to switch between different modes as well as choosing selection options.*

The possible view modes depend on the [project creation method](../02.starting-project.md) and are:
- Geometry: presents the geometry of the simulated object.
- Mesh: shows the surface mesh generated on the surfaces
- Visualisation: visualises the flow field according to the chosen criteria (eg. Cp contour on surface)

The selection methods can be checked and unchecked and allow for the selection of following entities:
- Points
- Edges 
- Faces 
- Bodies

---

<details>
<summary><h3 style="display:inline-block"> 💡 Tips</h3></summary>

- Click items in the left sidebar to expand/collapse sections
- The interface can be customized to show/hide various panels

</details>

---

<details>
<summary><h3 style="display:inline-block"> ❓ Frequently Asked Questions</h3></summary>

- **How do I reset the view to default?**
  > Use the home button in the view controls or press the Home key.

- **Can I customize the layout?**
  > Yes, panels can be resized, minimized, or rearranged to suit your workflow.

- **How do I access advanced visualization options?**
  > Advanced visualization settings are available in the top-right region (Section 3).

- **Where can I monitor simulation progress?**
  > The bottom status bar (Section 6) shows current simulation status and progress.

</details>