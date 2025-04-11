# Meshing Settings

*Comprehensive guide to Flow360's meshing capabilities, covering default parameters, volume zones, and refinement techniques for optimal CFD simulations.*

## 📋 **Available Options**

| **Component** | **Description** |
|---------------|-----------------|
| [Meshing Defaults](./01.meshing-defaults.md) | Fundamental control parameters for mesh generation |
| [Volume Zones](./02.volume-zone.md) | Specialized regions for specific flow features |
| [Refinements](./03.refinements/README.md) | Local mesh control for critical regions |

## 🔍 **Detailed Descriptions**

### Meshing Defaults
*Core parameters controlling the fundamental aspects of mesh generation.*

- Surface mesh characteristics
- Boundary layer properties
- Global refinement levels
- Gap treatment strategies

### Volume Zones
*Specialized regions for specific flow applications.*

- Farfield zones for external flow simulations
- Rotation cylinder zones for rotating machinery
- Custom volume zones for specific flow features

### Refinements
*Local mesh control mechanisms for critical regions.*

- Surface edge refinements
- Boundary layer refinements
- Uniform refinements
- Axisymmetric refinements
- Passive spacing controls

</edit>

---

<details>
<summary><h3 style="display:inline-block"> 💡 Tips</h3></summary>

- Begin with default settings and adjust based on specific needs
- Use refinement regions strategically for critical flow features
- Consider using passive spacing for interface regions
- Monitor solution convergence when adjusting mesh parameters
- Validate mesh quality metrics before proceeding with simulation
- Start with coarser meshes and refine based on solution quality
- Ensure smooth transitions between different mesh regions
- Consider computational resources when setting refinement levels

<details style="padding-left:20px">
<summary><h4 style="display:inline-block"> Common Pitfalls</h4></summary>

- Over-refinement in non-critical regions
- Insufficient wake resolution
- Poor boundary layer transition
- Inadequate gap treatment
- Inconsistent refinement levels

</details>

<details style="padding-left:20px">
<summary><h4 style="display:inline-block"> Meshing Considerations</h4></summary>

1. **Surface Mesh Quality**
   - Maintain element quality metrics
   - Ensure proper resolution of geometric features
   - Consider curvature-based refinement

2. **Boundary Layer Resolution**
   - Target appropriate y+ values
   - Use suitable growth rates (typically 1.1-1.2)
   - Ensure sufficient layers for boundary layer development

3. **Wake and Off-Body Features**
   - Extend refinement regions appropriately
   - Consider flow angles and operating conditions
   - Account for expected flow features

</details>
</details>

---

<details>
<summary><h3 style="display:inline-block"> ❓ Frequently Asked Questions</h3></summary>

- **How do I determine appropriate refinement levels?**  
  > Start with default settings and adjust based on flow features and geometric complexity. Use refinement regions for critical areas and monitor solution quality.

- **What's the best approach for rotating machinery?**  
  > Combine boundary layer refinement with axisymmetric refinement, ensuring proper resolution of tip vortices and wake regions.

- **When should I use different volume zone types?**  
  > Use farfield zones for external flows, rotation cylinders for rotating machinery, and custom zones for specific flow features requiring specialized treatment.

</details>

---

<details>
<summary><h3 style="display:inline-block"> 🐍 Python Example Usage</h3></summary>

```python
from flow360 import (
    MeshingParams,
    MeshingDefaults,
    AutomatedFarfield,
    RotationCylinder,
    SurfaceRefinement,
    BoundaryLayer,
    u
)

# Configure meshing parameters
meshing_params = MeshingParams(
    defaults=MeshingDefaults(
        surface_edge_growth_rate=1.2,
        surface_max_edge_length=0.1 * u.m,
        boundary_layer_growth_rate=1.2,
        boundary_layer_first_layer_thickness=0.01 * u.mm
    ),
    volume_zones=[
        AutomatedFarfield(method="auto"),
        RotationCylinder(
            spacing_axial=0.02 * u.m,
            spacing_radial=0.01 * u.m,
            spacing_circumferential=0.015 * u.m,
            entities=[propeller_cylinder]
        )
    ],
    refinements=[
        SurfaceRefinement(
            name="wing_surface",
            faces=[left_wing_surface],
            max_edge_length=0.05 * u.m
        ),
        BoundaryLayer(
            name="wing_bl",
            faces=[right_wing_surface],
            first_layer_thickness=1e-5 * u.m,
            growth_rate=1.2
        )
    ]
)
```

</details>