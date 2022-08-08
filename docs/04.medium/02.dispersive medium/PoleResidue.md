---
order: 03
---

# PoleResidue

A dispersive medium described by the pole-residue pair model.
The frequency-dependence of the complex-valued permittivity is described by:

$$\epsilon(\omega) = \epsilon_\infty - \sum_i\left[\frac{c_i}{j \omega + a_i} + \frac{c_i^\ast}{j \omega + a_i^\ast}\right]$$

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

## Poles

`poles`: List of complex-valued ($a_i, c_i$) poles for the model.

*a*: complex number

-   Unit: rad/sec

*c*: complex number

-   Unit: rad/sec
