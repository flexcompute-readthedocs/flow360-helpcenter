# Geometry

Geometry is used to define the physical domain of the simulation in Flow360. Consequently, generation of surface and volume mesh will be based on the provided geometry.

## Geometric Entities

Flow360 recognizes two primary types of geometric entities:

### [Edges](./01.edges.md)
Edges represent geometric elements that form the boundaries of faces. They are crucial for:
- Defining mesh refinement regions
- Controlling anisotropic layer growth
- Marking critical geometric features

### [Faces](./02.faces.md)
Faces are surfaces that constitute the boundaries of the computational domain. They serve multiple purposes:
- Specifying boundary conditions
- Defining regions for mesh refinement
- Organizing geometric features into logical groups

## Interacting with the geometry

In Flow360 you can do the following with geometry:

### Selection
Allows for interactive selection of geometric entities. 

There are 4 entity selection modes that define whether a given entity can be selected or not:
- Select point
- Select edge
- Select face
- Select volume

### Grouping
Grouping is based on geometric attributes and allows for organizing multiple elements into a single group for easier handling and assignment.

### Visualization
Geometric entities are visualized in real-time. You can toggle on/off the visiblity of grouped edges and faces.

## Geometric Considerations

When preparing a simulation, keep in mind:

- **Mesh Generation**: The shape of geometry as well as its level of detail influences the quality and efficiency of the resulting mesh
- **Boundary Conditions and refinements**: Proper grouping of faces and edges makes assigning boundary conditions and local mesh refinements a much easier task.

## Related Topics

For more information about specific aspects of handling geometry entities, refer to:
- [Edges](./01.edges.md) - Detailed information about edge operations and management
- [Faces](./02.faces.md) - Comprehensive guide to face handling and applications 