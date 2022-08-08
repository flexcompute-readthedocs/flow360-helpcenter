---
order: 02
---

# FieldTimeMonitor

Monitor that records electromagnetic fields in the time domain.

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

## Field Components

`fields`: Collection of field components to store in the monitor.

Options: select one or more of

-   *Ex*
-   *Ey*
-   *Ez*
-   *Hx*
-   *Hy*
-   *Hz*

Default: [*Ex*, *Ey*, *Ez*, *Hx*, *Hy*, *Hz*]

## Spatial Interval

`interval_space`: Number of grid step intervals between monitor recordings. 

-   If equal to *1*, there will be no downsampling. 
-   If greater than *1*, fields will be downsampled and automatically colocated.

Type: integer

-   Unit: unitless
-   Constraint: greater than *0*
-   Default: (*1*, *1*, *1*)


## Colocate Fields

`colocate`: Toggle whether fields should be colocated to grid cell centers. 

Type: Boolean

-   Default: *None*, which means

    -   *False*: if interval_space is *1* in each direction
    -   *True*: if interval_space is greater than *1* in any direction
    