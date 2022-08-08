---
order: 04
---

# PolySlab

Polygon extruded with optional sidewall angle along axis direction.

## Axis

`axis`: Specifies dimension of the planar axis.

Note: PolySlab can only support `axis`=*z* in this version of Tidy3D. Support for slabs oriented in other axes will be available in future releases.

Options:
-   *z* (*2* in Simulation JSON)

Default: *z*

## Slab Bounds

`slab_bounds`: Minimum and maximum positions of the slab along axis dimension.

Type: floating-point number

-   Unit: $\mu$m
-   Required field

## Dilation

`dilation`: Dilation of the polygon in the base by shifting each edge along its normal outwards direction by a distance; a negative value corresponds to erosion.

Type: floating-point number

-   Unit: $\mu$m
-   Default: *0*

## Sidewall Angle

`sidewall_angle`: Angle of the sidewall. 

-   `sidewall_angle`=*0* specifies vertical wall (default)
-   *0*<`sidewall_angle`<*$pi$/2* for the base to be larger than the top

Type: floating-point number

-   Unit: rad
-   Constraint: [*0*, *$pi$/2*)
-   Default: *0*

## Vertices

`vertices`: List of (d1, d2) defining the 2 dimensional positions of the base polygon face vertices along dimensions parallel to slab normal axis. 


Type: floating-point number

-   Unit: $\mu$m
-   Required field
