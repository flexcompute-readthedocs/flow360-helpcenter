---
order: 03
---

# CustomGrid

Custom 1D grid supplied as a list of grid cell sizes centered on the simulation center.

## Customized Grid Sizes

`dl`: An array of custom nonuniform grid sizes. The resulting grid is centered on the simulation center such that it spans the region *(center - sum(dl)/2, center + sum(dl)/2)*. 

Note: if supplied sizes do not cover the simulation size, the first and last sizes are repeated to cover the simulation domain. 

Type: floating-point number

-   Unit: $\mu$m
-   Constraint: greater than *0*
-   Required field
