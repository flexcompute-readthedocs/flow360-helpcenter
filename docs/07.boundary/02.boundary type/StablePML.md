---
order: 05
---

# StablePML

Specifies a \'stable\' PML along a single dimension.
This PML deals handles possbly divergent simulations better, but at the expense of more layers.

## Number of Layers

`num_layers`: Number of layers of \'stable\' PML.

Type: integer

-   Unit: unitless
-   Constraint: greater than or equal to *0*
-   Default: *40*

## Stable PML Parameters

`parameters`: \'Stable\' parameters of the complex frequency-shifted absorption poles.

See: [PMLParams](/07.boundary/03.absorbing%20layer%20parameters/PMLParams.html)

Default:

-   `sigma_order` = *3*
-   `sigma_min` = *0.0*
-   `sigma_max` = *1.0*
-   `kappa_order` = *3*
-   `kappa_min` = *1.0*
-   `kappa_max` = *5.0*
-   `alpha_order` = *1*
-   `alpha_min` = *0.0*
-   `alpha_max` = *0.9*
