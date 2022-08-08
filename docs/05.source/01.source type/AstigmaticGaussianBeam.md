---
order: 06
---

# AstigmaticGaussianBeam

This class implements the simple astigmatic Gaussian beam described in *Kochkina et al., Applied Optics, vol. 52, issue 24, 2013*. The simple astigmatic Guassian distribution allows both an elliptical intensity profile and different waist locations for the two principal axes of the ellipse. When equal waist sizes and equal waist distances are specified in the two directions, this source becomes equivalent to [GaussianBeam](/05.source/01.source%20type/GaussianBeam.html).

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

## Polarization Angle

`pol_angle`: Specifies the angle between the electric field polarization of the source and the plane defined by the injection axis and the propagation axis.

-   *0* specifies P polarization (default)
-   *$pi$/2* specifies S polarization

At normal incidence when S and P are undefined, *0* defines: 
-   *Ey* polarization for propagation along *x*
-   *Ex* polarization for propagation along *y*
-   *Ez* polarization for propagation along *z*

Type: floating-point number

-   Unit: rad
-   Default: *0*

## Waist Sizes

`waist_sizes`: Size of the beam at the waist in the local x and y directions.

Type: floating-point number

-   Unit: $\mu$m
-   Constraint: greater than *0*
-   Default: (*1*, *1*)

## Waist Distances

`waist_distances`: Distance to the beam waist along the propagation direction for the waist sizes in the local x and y directions.

Type: floating-point number

-   Unit: $\mu$m
-   Default: (*0*, *0*)
