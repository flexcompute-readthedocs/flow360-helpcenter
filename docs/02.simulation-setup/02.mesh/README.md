# Mesh 
A section for defining the meshing settings.

## 📋 **Contents** 

| *Settings group* | *Description* |
|--------------------|-----------------|
|[**Mesh (meshing defaults)**](./01.mesh.md) | Fundamental control parameters for mesh generation | 
|[**Rotation regions**](./02.rotation-regions.md) | Specialized regions for rotating flow features |
|[**Refinements**](./03.refinements/README.md)| Local mesh control for critical regions |

---

## 🔍 **Detailed Descriptions**

### **[Mesh (meshing defaults)](./01.mesh.md)**

*Fundamental control parameters for mesh generation affecting both surface and volume mesh characteristics. Provides global defaults for element size progression, boundary layer characteristics, surface mesh properties, and overall mesh quality control.*

### **[Rotation regions](./02.rotation-regions.md)**

*Specialized cylindrical volume zones designed for regions containing rotating components. Ensures proper mesh refinement and enables accurate simulation of rotating machinery with concentric mesh structure ideal for rotating components.*

### **[Refinements](./03.refinements/README.md)**

*Comprehensive local mesh control system for critical regions. Provides six refinement types.*

**Subsections:**
- **[Surface Edge Refinement](./03.refinements/01.surface-edge-refinement.md)** - Controls mesh resolution near edges
- **[Surface Refinement](./03.refinements/02.surface-refinement.md)** - Controls surface mesh cell size
- **[Boundary Layer Refinement](./03.refinements/03.boundary-layer-refinement.md)** - Creates prismatic layers near walls
- **[Passive Spacing](./03.refinements/04.passive-spacing.md)** - Controls mesh behavior without direct refinement
- **[Uniform Refinement](./03.refinements/05.uniform-refinement.md)** - Creates uniform mesh spacing in a region
- **[Axisymmetric Refinement](./03.refinements/06.axisymmetric-refinement.md)** - Creates structured-like mesh with cylindrical bias