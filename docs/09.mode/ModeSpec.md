# ModeSpec

Stores specifications for the mode solver to find an electromagntic mode.
Note, the planar axes are found by popping the injection axis from {x,y,z}.
For example, if injection axis is y, the planar axes are ordered {x,z}.

## Number of Modes

`num_modes`: Number of modes returned by mode solver.

Type: integer

-   Unit: unitless
-   Constraint: greater than *0*
-   Default: *1*

## Target Effective Index

`target_neff`: Guess for effective index of the mode.

Type: floating-point number

-   Unit: unitless
-   Constraint: greater than *0*
-   Default: *None*   

## Number of PML Layers

`num_pml`: Number of standard pml layers to add in the two tangential axes.

Type: integer

-   Unit: unitless
-   Constraint: greater than or equal to *0*
-   Default: (*0*, *0*)

## Polarization Filtering

`filter_pol`: The solver always computes the [num_modes](/09.mode/ModeSpec.html#number-of-modes) modes closest to the given [target_neff](/09.mode/ModeSpec.html#target-effective-index). If [filter_pol](/09.mode/ModeSpec.html#polarization-filtering)=*None*, they are simply sorted in order of decresing effective index. If a polarization filter is selected, the modes are rearranged such that the first *n_pol* modes in the list are the ones with the selected polarization fraction larger than or equal to *0.5*, while the next [num_modes](/09.mode/ModeSpec.html#number-of-modes) - *n_pol* modes are the ones where it is smaller than *0.5* (i.e. the opposite polarization fraction is larger than *0.5*). Within each polarization subset, the modes are still ordered by decreasing effective index. 

*te*-fraction is defined as the integrated intensity of the E-field component parallel to the first plane axis, normalized to the total in-plane E-field intensity. Conversely, *tm*-fraction uses the E field component parallel to the second plane axis.

Options:

-   *None*
-   *te*
-   *tm*

Default: *None*

## Polar Angle

`angle_theta`: Polar angle of the propagation axis from the injection axis.

Type: floating-point number

-   Unit: rad
-   Default: *0*

## Azimuth Angle

`angle_phi`: Azimuth angle of the propagation axis in the plane orthogonal to the injection axis.

Type: floating-point number

-   Unit: rad
-   Default: *0*

## Single or Double Precision in Mode Solver

`precision`: The solver will be faster and using less memory under single precision, but more accurate under double precision.

Options:

-   *single*
-   *double*

Default: *single*



## Bend Radius

`bend_radius`: A curvature radius for simulation of waveguide bends. 

Can be negative, in which case the mode plane center has a smaller value than the curvature center along the tangential axis perpendicular to the bend axis. 

Type: floating-point number

-   Unit: $\mu$m
-   Default: *None*

## Bend Axis

`bend_axis`: Index into the two tangential axes defining the normal to the plane in which the bend lies. 

This must be provided if [bend_radius](/09.mode/ModeSpec.html#bend-radius) is not *None*. 

For example, for a ring in the global xy-plane, and a mode plane in either the xz or the yz plane, the `bend_axis` is always *1* (the global z axis).

Options:

-   *None*
-   *0*
-   *1*

Default: *None*
