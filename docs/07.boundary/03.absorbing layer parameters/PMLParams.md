---
order: 01
---

# PMLParams

Specifies full set of parameters needed for complex, frequency-shifted PML.

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

## Kappa Order

`kappa_order`: Order of the polynomial describing the PML kappa profile (kappa~*dist^kappa_order*).

Type: integer

-   Unit: unitless
-   Constraint: greater than or equal to *0*
-   Default: *3*

## Kappa Minimum

`kappa_min`

Type: floating-point number

-   Unit: 2\*EPSILON_0/dt
-   Constraint: greater than or equal to *0*
-   Default: *0*

## Kappa Maximum

`kappa_max`

Type: floating-point number

-   Unit: 2\*EPSILON_0/dt
-   Constraint: greater than or equal to *0*
-   Default: *1.5*

## Alpha Order

`alpha_order`: Order of the polynomial describing the PML alpha profile (alpha~*dist^alpha_order*).

Type: integer

-   Unit: unitless
-   Constraint: greater than or equal to *0*
-   Default: *3*

## Alpha Minimum

`alpha_min`: Minimum value of the PML alpha.

Type: floating-point number

-   Unit: 2\*EPSILON_0/dt
-   Constraint: greater than or equal to *0*
-   Default: *0*

## Alpha Maximum

`alpha_max`: Maximum value of the PML alpha.

Type: floating-point number

-   Unit: 2\*EPSILON_0/dt
-   Constraint: greater than or equal to *0*
-   Default: *1.5*

