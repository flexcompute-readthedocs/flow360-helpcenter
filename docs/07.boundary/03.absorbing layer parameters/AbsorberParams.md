---
order: 02
---

# AbsorberParams

Specifies parameters common to Absorbers and PMLs.

## Sigma Order

`sigma_order`: Order of the polynomial describing the absorber profile (~*dist^sigma_order*).

Type: integer

-   Unit: unitless
-   Constraint: greater than or equal to *0*
-   Default: *3*

## Sigma Minimum

`sigma_min`: Minimum value of the absorber conductivity.

Type: floating-point number

-   Unit: 2\*EPSILON_0/dt
-   Constraint: greater than or equal to *0*
-   Default: *0*

## Sigma Maximum

`sigma_max`: Maximum value of the absorber conductivity.

Type: floating-point number

-   Unit: 2\*EPSILON_0/dt
-   Constraint: greater than or equal to *0*
-   Default: *1.5*

