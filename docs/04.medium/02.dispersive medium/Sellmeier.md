---
order: 04
---

# Sellmeier

A dispersive medium described by the Sellmeier model.
The frequency-dependence of the refractive index is described by:

$$n(\lambda)^2 = 1 + \sum_i \frac{B_i \lambda^2}{\lambda^2 - C_i}$$

## Name

`name`: Optional unique name for medium.

## Frequency Range

`frequency_range`: Optional range of validity for the medium.

Type: floating-point number

-   Unit: Hz
-   Constraint: greater than *0*
-   Default: *None*

## Coefficients

`coeffs`: List of Sellmeier ($B_i, C_i$) coefficients.

Required field

$B$: floating-point number

-   Unit: unitless

$C$: floating-point number

-   Unit: $\mu m^2$
-   Constraint: greater than or equal to *0*
