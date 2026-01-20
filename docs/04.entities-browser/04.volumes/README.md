# Volumes

*Volume entities in Flow360 are used to define regions for volume zones, local refinements, and 3D physics models. Flow360 provides four volume primitives that can be used individually or combined to create complex geometric configurations.*

## Contents

| *Volume Type* | *Description* |
|---------------|---------------|
| [**Box**](./00.box.md) | Rectangular prism defined by center, size, and orientation |
| [**Cylinder**](./01.cylinder.md) | Cylindrical volume defined by axis, radius, and height |
| [**Axisymmetric volume**](./02.axisymmetric-volume.md) | Body of revolution defined by a profile curve |
| [**Custom volume**](./03.custom-volume.md) | Volume zone defined by its enclosing surfaces |

---

<details>
<summary><h3 style="display:inline-block"> 💡 Tips</h3></summary>

- Choose volume type based on your specific needs and geometry shape
- Consider volume placement and orientation carefully
- Ensure proper scaling relative to your simulation domain
- Review volume overlap implications before implementation
- Toggle volume visibility by clicking the eye icon that appears when hovering over or selecting the volume

</details>

---

<details>
<summary><h3 style="display:inline-block"> ❓ Frequently Asked Questions</h3></summary>

- **Can volumes overlap?**
  > Yes, volumes can overlap, but this should be done intentionally as it may affect mesh generation and simulation results.

- **Can I use volumes for boundary conditions?**
  > No, volumes are used for defining regions within the domain, not for boundary conditions. Use surfaces for boundary condition assignment.

- **How do I create a complex shape?**
  > Combine multiple volumes by positioning them appropriately, or use Custom volume to define a region by its enclosing surfaces.

</details>

```{toctree}
:hidden:
:maxdepth: 1
./00.box.md
./01.cylinder.md
./02.axisymmetric-volume.md
./03.custom-volume.md
```

