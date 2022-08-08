---
order: 07
---

# PermittivityMonitor

Monitor that records the diagonal components of the complex-valued relative
permittivity tensor in the frequency domain. 

The recorded data has the same shape as a
[FieldMonitor](/06.monitor/FieldMonitor.html) of the same geometry: the permittivity values are saved at the
Yee grid locations, and can be interpolated to any point inside the monitor.

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
