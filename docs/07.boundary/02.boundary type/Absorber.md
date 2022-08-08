---
order: 06
---

# Absorber

Specifies an adiabatic absorber along a single dimension.
This absorber is well-suited for dispersive materials intersecting with absorbing edges of the simulation at the expense of more layers.

## Number of Layers

`num_layers`: Number of layers of absorber.

Type: integer

-   Unit: unitless
-   Constraint: greater than or equal to *0*
-   Default: *40*

## Absorber Parameters

`parameters`: Adiabatic absorber parameters.

See: [AbsorberParams](/07.boundary/03.absorbing%20layer%20parameters/AbsorberParams.html)

Default:

-   `sigma_order` = *3*
-   `sigma_min` = *0.0*
-   `sigma_max` = *6.4*
