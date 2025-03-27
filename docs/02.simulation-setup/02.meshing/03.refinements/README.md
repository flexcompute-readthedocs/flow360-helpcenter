# Refinements

This document provides an overview of mesh refinement capabilities in Flow360. Refinements enable precise control over mesh resolution in specific regions of your geometry to better capture flow features or geometric details.

## 📋 Available Refinement Types

| **Type** | **Description** | **Applicable To** | **Documentation** |
|----------|----------------|------------------|------------------|
| Surface Edge Refinement | Controls mesh resolution near edges | Edges | [Details](03.1.surface-edge-refinement.md) |
| Surface Refinement | Controls surface mesh cell size | Surfaces | [Details](03.2.surface-refinement.md) |
| Boundary Layer Refinement | Creates prismatic layers near walls | Surfaces | [Details](03.3.boundary-layer-refinement.md) |
| Passive Spacing | Controls mesh behavior without direct refinement | Surfaces | [Details](03.4.passive-spacing.md) |
| Uniform Refinement | Creates uniform mesh spacing in a region | Boxes and cylinders | [Details](03.5.uniform-refinement.md) |
| Axisymmetric Refinement | Creates structured-like mesh with cylindrical bias | Cylinders | [Details](03.6.axisymmetric-refinement.md) |

## 🔍 General Guidelines

### Refinement Selection

1. **Surface Features**
   - Use Surface Edge Refinement for leading/trailing edges
   - Apply Surface Refinement for general surface resolution
   - Implement Boundary Layer Refinement for wall regions

2. **Off-Body Features**
   - Use Uniform Refinement for wakes and shocks
   - Apply Axisymmetric Refinement for rotating machinery
   - Consider Passive Spacing for interface regions

### Best Practices

- Start with coarser refinements and gradually increase resolution where needed
- Ensure smooth transitions between regions of different refinement levels
- Consider geometric scale when setting refinement parameters
- Balance resolution requirements with computational cost
- Account for flow regime and Reynolds number effects

### Common Applications

1. **Aerodynamic Simulations**
   - Surface Edge Refinement for leading edges
   - Boundary Layer Refinement for wall regions
   - Uniform Refinement for wake regions

2. **Rotating Machinery**
   - Axisymmetric Refinement for rotor/propeller regions
   - Boundary Layer Refinement for blade surfaces
   - Uniform Refinement for tip vortex regions

3. **Complex Geometries**
   - Surface Refinement for general resolution
   - Passive Spacing for interface regions
   - Uniform Refinement for critical flow features

---

<details>
<summary><h3 style="display:inline-block"> 💡 Tips</h3></summary>

- Review detailed documentation for each refinement type
- Consider flow physics when selecting refinement types
- Use appropriate units for all parameters
- Ensure compatibility between different refinements
- Monitor mesh quality metrics

</details>

---

<details>
<summary><h3 style="display:inline-block"> ❓ Frequently Asked Questions</h3></summary>

- **How do I choose between different refinement types?**  
  > Consider the geometric features and flow phenomena you need to resolve, then select the most appropriate refinement type(s).

- **What happens if refinements overlap?**  
  > The finest (smallest) spacing will be used in overlapping regions.

- **How do I ensure mesh quality?**  
  > Monitor aspect ratios, skewness, and other quality metrics while adjusting refinement parameters.

</details>

---

<details>
<summary><h3 style="display:inline-block"> 🐍 Python Example Usage</h3></summary>

```python
from flow360 import (
    MeshingParams,
    SurfaceEdgeRefinement,
    SurfaceRefinement,
    BoundaryLayer,
    PassiveSpacing,
    UniformRefinement,
    AxisymmetricRefinement,
    u
)

# Example of combining multiple refinements
meshing=MeshingParams(
    refinements=[
        # Surface edge refinement for leading edge
        SurfaceEdgeRefinement(
            name="leading_edge",
            edges=[leading_edge],
            method=HeightBasedRefinement(value=0.001 * u.m)
        ),
        # Surface refinement for general resolution
        SurfaceRefinement(
            name="wing_surface",
            faces=[wing_surface],
            max_edge_length=0.05 * u.m
        ),
        # Boundary layer refinement for wall regions
        BoundaryLayer(
            name="wing_bl",
            faces=[wing_surface],
            first_layer_thickness=1e-5 * u.m,
            growth_rate=1.2
        ),
        # Passive spacing refinement for interface region
        PassiveSpacing(
            name="interface_region",
            refinement_type="projected",
            faces=[interface_surface]
        ),
        # Wake region refinement
        UniformRefinement(
            name="wake_region",
            entities=[wake_box],
            spacing=0.1 * u.m
        ),
        # Axisymmetric refinement for propeller region
        AxisymmetricRefinement(
            name="propeller_region",
            entities=[prop_cylinder],
            spacing_axial=0.02 * u.m,
            spacing_radial=0.01 * u.m,
            spacing_circumferential=0.015 * u.m
        )
    ]
)
```
</details> 