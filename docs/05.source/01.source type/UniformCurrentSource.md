---
order: 02
---

# UniformCurrentSource

Source in a rectangular volume with uniform time dependence. 

## Center

`center`: Center of object in x, y, and z.

Type: floating-point number

-   Unit: $\mu$m
-   Default: (*0*, *0*, *0*)

## Size

`size`: Size in x, y, and z directions.

Note: `size`=(*0*, *0*, *0*) gives point source.

Use *Infinity* to define geometry extending to infinity to both directions along an axis.

Type: floating-point number

-   Unit: $\mu$m
-   Constraint: greater than or equal to *0*
-   Required field

## Source Time

`source_time`: Specification of the source time-dependence.

Options:

-   [GaussianPulse](/05.source/02.source%20time/GaussianPulse.html)

Required field

## Name

`name`: Optional name for the source.

## Polarization

`polarization`: Specifies the direction and type of current component.

Options:

-   *Ex*
-   *Ey*
-   *Ez*
-   *Hx*
-   *Hy*
-   *Hz*

Required field
