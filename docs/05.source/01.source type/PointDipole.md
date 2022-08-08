---
order: 01
---

# PointDipole

Uniform current source with a zero size.

## Center

`center`: Center of object in x, y, and z.

Type: floating-point number

-   Unit: $\mu$m
-   Default: (*0*, *0*, *0*)

## Size

`size`: Size in x, y, and z directions.

Note: `size`=(*0*, *0*, *0*)

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
