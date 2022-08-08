---
order: 02
---

# AutoGrid

Specification for non-uniform grid along a given dimension.

## Minimal Number of Steps per Wavelength

`min_steps_per_wvl`: Minimal number of steps per wavelength in each medium.

Type: floating-point number

-   Unit: unitless
-   Constraint: greater than or equal to *6*
-   Default: *10*

## Maximum Grid Size Scaling

`max_scale`: Sets the maximum ratio between any two consecutive grid steps.

Type: floating-point number

-   Unit: unitless
-   Constraint: [*1.2*, *2*)
-   Default: *1.4*
