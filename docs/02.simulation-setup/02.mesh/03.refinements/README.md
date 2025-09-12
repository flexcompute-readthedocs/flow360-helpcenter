# Refinements

*This document provides an overview of mesh refinement capabilities in Flow360. Refinements enable precise control over mesh resolution in specific regions of your geometry to better capture flow features or geometric details.*

## **Available Refinement Types**

| *Refinement type* | *Description* |
|--------------------|-----------------|
|[**Surface Edge Refinement**](./01.surface-edge-refinement.md) | Controls mesh resolution near edges |
|[**Surface Refinement**](./02.surface-refinement.md) | Controls surface mesh cell size |
|[**Boundary Layer Refinement**](./03.boundary-layer-refinement.md) | Creates prismatic layers near walls |
|[**Passive Spacing**](./04.passive-spacing.md) | Controls mesh behavior without direct refinement |
|[**Uniform Refinement**](./05.uniform-refinement.md) | Creates uniform mesh spacing in a region |
|[**Axisymmetric Refinement**](./06.axisymmetric-refinement.md) | Creates structured-like mesh with cylindrical bias |
|[**Geometry Refinement**](./07.geometry-refinement.md) | Controls mesh resolution based on geometric features |

## **General Guidelines**

### **Refinement Selection**

1. **Surface Features**
   - Use Surface Edge Refinement for leading/trailing edges
   - Apply Surface Refinement for general surface resolution
   - Implement Boundary Layer Refinement for wall regions
   - Select geometry refinement to accurately capture small features

2. **Off-Body Features**
   - Use Uniform Refinement for wakes and shocks
   - Apply Axisymmetric Refinement for rotating machinery
   - Consider Passive Spacing for interface regions

### **Best Practices**

- Start with coarser refinements and gradually increase resolution where needed
- Ensure smooth transitions between regions of different refinement levels
- Consider geometric scale when setting refinement parameters
- Balance resolution requirements with computational cost
- Account for flow regime and Reynolds number effects

### **Common Applications**

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
import flow360 as fl

# Example of combining multiple refinements
meshing=MeshingParams(
    refinements=[
        # Surface edge refinement for leading edge
        fl.SurfaceEdgeRefinement(
            name="leading_edge",
            edges=[leading_edge],
            method=fl.HeightBasedRefinement(value=0.001 * fl.u.m)
        ),
        # Surface refinement for general resolution
        fl.SurfaceRefinement(
            name="wing_surface",
            faces=[wing_surface],
            max_edge_length=0.05 * fl.u.m
        ),
        # Boundary layer refinement for wall regions
        fl.BoundaryLayer(
            name="wing_bl",
            faces=[wing_surface],
            first_layer_thickness=1e-5 * fl.u.m,
            growth_rate=1.2
        ),
        # Passive spacing refinement for interface region
        fl.PassiveSpacing(
            name="interface_region",
            type="projected",
            faces=[interface_surface]
        ),
        # Wake region refinement
        fl.UniformRefinement(
            name="wake_region",
            entities=[wake_box],
            spacing=0.1 * fl.u.m
        ),
        # Axisymmetric refinement for propeller region
        fl.AxisymmetricRefinement(
            name="propeller_region",
            entities=[prop_cylinder],
            spacing_axial=0.02 * fl.u.m,
            spacing_radial=0.01 * fl.u.m,
            spacing_circumferential=0.015 * fl.u.m
        ),
        # Geometry refinement for fine features
        fl.GeometryRefinement(
            name="fine_features_refinement",
            faces=[wing_surface, fuselage_surface],
            geometry_accuracy=0.001 * fl.u.m,
            preserve_thin_geometry=True
        )
    ]
)
```
</details> 