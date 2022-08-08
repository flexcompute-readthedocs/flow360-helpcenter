---
order: 01
---

# Medium

Dispersionless medium.

## Name

`name`: Optional unique name for medium.

## Permittivity

`permittivity`: Relative permittivity. 

Type: floating-point number

-   Unit: unitless
-   Constraint: greater than or equal to *1*
-   Default: *1*

## Conductivity

`conductivity`: Electric conductivity. Defined such that the imaginary part of the complex permittivity at angular frequency omega is given by conductivity/omega.

Type: floating-point number

-   Units: S/m
-   Constraint: greater than or equal to *0*
-   Default: *0*
