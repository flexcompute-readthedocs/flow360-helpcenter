# Entities in Flow360

Entities are the fundamental components used for simulation setup in Flow360. They provide a hierarchical structure for organizing and managing CFD simulations, from geometry definition to results analysis. The entity structure varies depending on whether you start your project from geometry or from a volume mesh.

---

## Project Started from Geometry

When starting a project from geometry, the entity hierarchy is organized to facilitate the progression from geometric definition to simulation setup.

### Geometry
The root entity that contains all geometric elements. Under geometry, you'll find:

- **Edges grouping** - Settings for organizing edges into groups based on their attributes, e.g. `edgeId`
- **Faces grouping** - Setting for organizing faces into groups based on their attributes, e.g. `faceName`
- **Edges** - Individual edge elements that form the wireframe of geometry
- **Faces** - Individual face elements that define the surfaces of geometry

### Additional Entities
Below the geometry section, you'll find containers for various simulation components:

- **Volumes** - Three-dimensional regions used for mesh refinement, zone definition, and flow field analysis
- **Points** - Zero-dimensional entities used for flow monitoring
- **Slices** - Two-dimensional cross-sections used for flow visualization
- **Derived** - Automatically generated entities based on your geometry, such as farfield and symmetry planes

---

## Project Started from Volume Mesh

When starting a project from an existing volume mesh, the entity hierarchy is structured to focus on mesh-based simulation setup.

### Volume mesh
The root entity for mesh-based projects, containing:

- **Zones** - Mesh zone definitions for specifying different regions with distinct properties or behavior
- **Boundaries** - Boundary condition specifications for the simulation domain

### Additional Entities
Similar to geometry-based projects, with containers for:

- **Volumes** - Three-dimensional regions used for mesh refinement, zone definition, and flow field analysis
- **Points** - Zero-dimensional entities used for flow monitoring
- **Slices** - Two-dimensional cross-sections used for flow visualization

>**Note:** Contrary to starting from geometry, there are no derived entities when project starts from volume mesh.

---

## Related pages

- [Geometry](./01.geometry/README.md)
- [Volume Mesh](./02.volume-mesh/README.md)
- [Volumes](./03.volumes.md)
- [Points](./04.points.md)
- [Slices](./05.slices.md)
- [Derived](./06.derived.md)

---

<details>
<summary><h3 style="display:inline-block">💡 Tips</h3></summary>

### Project Organization
- Use meaningful names for entities to maintain clarity in complex simulations
- Group related entities logically using the provided hierarchy
- Keep track of entity IDs when working with boundary conditions
- Regularly save your project to preserve entity configurations

### Best Practices
- Define geometry entities before creating dependent entities
- Verify boundary assignments before mesh generation
- Use points and slices strategically for result analysis
- Consider symmetry planes to reduce computational cost when applicable

### Common Workflows
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
