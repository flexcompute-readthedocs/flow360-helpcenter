---
order: 03
---

# Cylinder

Cylindrical geometry.

## Center

`center`: Center of object in x, y, and z.

Type: floating-point number

-   Unit: $\mu$m
-   Default: (*0*, *0*, *0*)

## Axis

`axis`: Specifies dimension of the planar axis.

Options:
-   *x* (*0* in Simulation JSON) 
-   *y* (*1* in Simulation JSON)
-   *z* (*2* in Simulation JSON)

Default: z

## Length

`length`: Defines thickness of cylinder along axis dimension.

Use *Infinity* to define geometry extending to infinity to both directions along an axis.

Type: floating-point number

-   Unit: $\mu$m
-   Constraint: greater than or equal to *0*
-   Required field

## Radius

`radius`: Radius of geometry.

Type: floating-point number

-   Unit: $\mu$m
-   Constraint: greater than or equal to *0*
-   Required field
