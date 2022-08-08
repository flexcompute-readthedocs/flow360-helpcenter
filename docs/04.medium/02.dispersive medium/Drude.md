---
order: 01
---

# Drude

A dispersive medium described by the Drude model.
The frequency-dependence of the complex-valued permittivity is described by:

$$\epsilon(f) = \epsilon_\infty - \sum_i\frac{ f_i^2}{f^2 + jf\delta_i}$$

## Name

`name`: Optional unique name for medium.

## Frequency Range

`frequency_range`: Optional range of validity for the medium.

Type: floating-point number

-   Unit: Hz
-   Constraint: greater than *0*
-   Default: *None*

## Epsilon at Infinity

`eps_inf`: Relative permittivity at infinite frequency ($\epsilon_\infty$).

Type: floating-point number

-   Unit: unitless
-   Constraint: greater than or equal to *1*
-   Default: *1*

## Coefficients

`coeffs`: List of ($f_i, \delta_i$) values for model.

Required field

$f$: floating-point number

-   Unit: Hz

$\delta$: floating-point number

-   Unit: Hz
-   Constraint: greater than or equal to *0*
