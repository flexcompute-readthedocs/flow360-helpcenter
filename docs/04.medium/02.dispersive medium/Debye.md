# Debye

A dispersive medium described by the Debye model.
The frequency-dependence of the complex-valued permittivity is described by:

$$\epsilon(f) = \epsilon_\infty + \sum_i\frac{\Delta\epsilon_i}{1 - jf\tau_i}$$

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

`coeffs`: List of ($\Delta\epsilon_i, \tau_i$) values for model.

Required field

$\Delta\epsilon$: floating-point number

-   Unit: Hz

$\tau$: floating-point number

-   Unit: sec
-   Constraint: greater than *0*
