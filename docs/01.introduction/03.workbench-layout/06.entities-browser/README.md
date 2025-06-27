# Entities browser


*Entities are the fundamental components used for simulation setup in Flow360. They provide a hierarchical structure for organizing and managing CFD simulations, from geometry definition to results analysis. The entity structure varies depending on whether you start your project from geometry or from a volume mesh.*

**Showing/hiding the entities browser**: The Entities browser is shown by clicking the button in the top-right corner of the viewer area.  

**Entities visibility, highlighting (hover)**: As you hover the mouse over items in the Entities browser, they are highlighted in the viewer.  

**Entities browser modes**: The Entities browser shows the Geometry, Mesh or Visualization items currently available in the viewer, and so it changes when the View mode is selected. The Entities available in each mode are described below.

**"View only" mode**: The Entities browser has limited functionality when the Workbench is in "View only" mode. It can be used to show/hide elements and to browse the available entities and highlight them in the viewer. Creating and updating viewpoints is also supported at any time.  


---

## **Project Started from Geometry**

*When starting a project from geometry, the entity hierarchy is organized to facilitate the progression from geometric definition to simulation setup.*

### [**Geometry**](./01.geometry/README.md)
The root entity that contains all geometric elements. Under geometry, you'll find:

- **Edges grouping** - Settings for organizing edges into groups based on their attributes, e.g. `edgeId`
- **Faces grouping** - Setting for organizing faces into groups based on their attributes, e.g. `faceName`
- [**Edges**](./01.geometry/01.edges.md) - Individual edge elements that form the wireframe of geometry
- [**Faces**](./01.geometry/02.faces.md) - Individual face elements that define the surfaces of geometry

### **Additional Entities**
Below the geometry section, you'll find containers for various simulation components:

- [**Volumes**](./04.volumes.md) - Three-dimensional regions used for mesh refinement, zone definition, and flow field analysis
- [**Points**](./05.points.md) - Zero-dimensional entities used for flow monitoring
- [**Slices**](./06.slices.md) - Two-dimensional cross-sections used for flow visualization
- [**Derived**](./07.derived.md) - Automatically generated entities based on your geometry, such as farfield and symmetry planes

---

## **Project Started from Surface Mesh**

*When starting a project from an existing surface mesh, the entity hierarchy is structured to focus on surface-mesh-based simulation setup.*

### [**Surface mesh**](./02.surface-mesh.md)
The root entity for surface-mesh-based projects, containing:

- [**Boundaries**](./03.volume-mesh/02.boundaries.md) - Surface mesh patches for boundary condition specifications in the simulation domain (same as in volume mesh)

### **Additional Entities**
Similar to geometry-based projects, with containers for:

- [**Volumes**](./04.volumes.md) - Three-dimensional regions used for mesh refinement, zone definition, and flow field analysis
- [**Points**](./05.points.md) - Zero-dimensional entities used for flow monitoring
- [**Slices**](./06.slices.md) - Two-dimensional cross-sections used for flow visualization

---

## **Project Started from Volume Mesh**

*When starting a project from an existing volume mesh, the entity hierarchy is structured to focus on volume-mesh-based simulation setup.*

### [**Volume mesh**](./03.volume-mesh/README.md)
The root entity for mesh-based projects, containing:

- [**Zones**](./03.volume-mesh/01.zones.md) - Mesh zone definitions for specifying different regions with distinct properties or behavior
- [**Boundaries**](./03.volume-mesh/02.boundaries.md) - surface patches for oundary condition specifications in the simulation domain

### **Additional Entities**
Similar to geometry-based projects, with containers for:

- [**Volumes**](./04.volumes.md) - Three-dimensional regions used for mesh refinement, zone definition, and flow field analysis
- [**Points**](./05.points.md) - Zero-dimensional entities used for flow monitoring
- [**Slices**](./06.slices.md) - Two-dimensional cross-sections used for flow visualization

>**Note:** Contrary to starting from geometry and surface mesh, there are no derived entities when project starts from volume mesh.

---

## **Related pages**

- [Geometry](./01.geometry/README.md)
- [Surface Mesh](./02.surface-mesh.md)
- [Volume Mesh](./03.volume-mesh/README.md)
- [Volumes](./04.volumes.md)
- [Points](./05.points.md)
- [Slices](./06.slices.md)
- [Derived](./07.derived.md)
- [Viewpoints](./08.viewpoints.md)

---

<details>
<summary><h3 style="display:inline-block">💡 Tips</h3></summary>

- **Project Organization**
  - Use meaningful names for entities to maintain clarity in complex simulations
  - Group related entities logically using the provided hierarchy
  - Keep track of entity IDs when working with boundary conditions
  - Regularly save your project to preserve entity configurations

- **Best Practices**
  - Define geometry entities before creating dependent entities
  - Verify boundary assignments before mesh generation
  - Use points and slices strategically for result analysis
  - Consider symmetry planes to reduce computational cost when applicable

- **Common Workflows**
  - Start with geometry cleanup and edge/face grouping
  - Define volumes for mesh refinement regions
  - Set up monitoring points in areas of interest
  - Create visualization slices at key locations

</details>

---

<details>
<summary><h3 style="display:inline-block">❓ Frequently Asked Questions</h3></summary>

- **What's the difference between edges grouping and individual edges?**  
  > Edge grouping allows you to manage multiple edges as a single entity for boundary conditions and mesh control, while individual edges represent the actual geometric elements.

- **Can I add new entities after starting the simulation?**  
  > Yes, monitoring entities like points and slices can be added after simulation start. However, geometric entities and mesh zones must be defined before simulation begins.

- **How do derived entities differ from user-created entities?**  
  > Derived entities are automatically generated based on your geometry and simulation settings, while user-created entities are manually defined for specific purposes.

- **What happens to entities when I modify the geometry?**  
  > Geometry-dependent entities may need to be updated or recreated after geometry modifications. Always verify entity assignments after geometry changes.

- **Can I share entities between different projects?**  
  > While entity definitions can be exported and imported, ensure compatibility between projects, especially regarding coordinate systems and units.

</details>
