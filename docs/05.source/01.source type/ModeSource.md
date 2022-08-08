---
order: 04
---

# ModeSource

Injects current source to excite modal profile on finite extent plane.

## Center

`center`: Center of object in x, y, and z.

Type: floating-point number

-   Unit: $\mu$m
-   Default: (*0*, *0*, *0*)

## Size

`size`: Size in x, y, and z directions.

Note: One element of `size` must be zero.

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

## Direction

`direction`: Specifies propagation in the positive or negative direction of the injection axis.

Options:

-   *+*: Propogate in the positive direction of the injection axis
-   *-*: Propogate in the negative direction of the injection axis

Required field

## Mode Specification

`mode_spec`: Parameters to feed to mode solver which determine modes measured by monitor.

See: [ModeSpec](/09.mode/ModeSpec.html)

## Mode Index

`mode_index`: Index into the collection of modes returned by mode solver. Specifies which mode to inject using this source. 

If larger than [num_modes](/09.mode/ModeSpec.html#number-of-modes) in `mode_spec`, [num_modes](/09.mode/ModeSpec.html#number-of-modes) in the solver will be set to `mode_index` + *1*.
