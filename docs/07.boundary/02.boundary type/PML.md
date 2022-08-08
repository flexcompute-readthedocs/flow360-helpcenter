---
order: 04
---

# PML

Specifies a standard PML along a single dimension.

## Number of Layers

`num_layers`: Number of layers of standard PML.

Type: integer

-   Unit: unitless
-   Constraint: greater than or equal to *0*
-   Default: *12*

## PML Parameters

`parameters`: Parameters of the complex frequency-shifted absorption poles.

See: [PMLParams](/07.boundary/03.absorbing%20layer%20parameters/PMLParams.html)

Default:

-   `sigma_order` = *3*
-   `sigma_min` = *0.0*
-   `sigma_max` = *1.5*
-   `kappa_order` = *3*
-   `kappa_min` = *1.0*
-   `kappa_max` = *3.0*
-   `alpha_order` = *1*
-   `alpha_min` = *0.0*
-   `alpha_max` = *0.0*
