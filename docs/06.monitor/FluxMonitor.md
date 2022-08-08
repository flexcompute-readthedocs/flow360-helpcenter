---
order: 03
---

# FluxMonitor

Monitor that records power flux through a plane in the frequency domain.

## Center

`center`: Center of object in x, y, and z.

Type: floating-point number

-   Unit: $\mu$m
-   Default: (*0*, *0*, *0*)

## Size

`size`: Size in x, y, and z directions.

Use *Infinity* to define geometry extending to infinity to both directions along an axis.

Type: floating-point number

-   Unit: $\mu$m
-   Constraint: greater than or equal to *0*
-   Required field

## Name

`name`: Unique name for monitor.

Required field

## Frequencies

`freqs`: Array or list of frequencies stored by the field monitor.

Type: floating-point number

-   Unit: Hz
-   Constraint: greater than *0*
-   Required field
