---
order: 04
---

# FluxTimeMonitor

Monitor that records power flux through a plane in the time domain.

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

## Start Time

`start`: Time at which to start monitor recording.

Type: floating-point number

-   Unit: sec
-   Constraint: greater than or equal to *0*
-   Default: *0*

## Stop Time

`stop`: Time at which to stop monitor recording. 

If not specified, record until end of simulation.

Type: floating-point number

-   Unit: sec
-   Constraint: greater than or equal to *0*
-   Default: *None*, which means end of simulation

## Time Interval

`interval`: Number of time step intervals between monitor recordings.

Type: integer

-   Unit: unitless
-   Constraint: greater than *0*
-   Default: *1*
