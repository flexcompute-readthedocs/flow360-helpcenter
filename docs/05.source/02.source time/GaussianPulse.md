---
order: 01
---

# GaussianPulse

Source time dependence that describes a Gaussian pulse.

## Amplitude

`amplitude`: Real-valued maximum amplitude of the time dependence.

Type: floating-point number

-   Unit: unitless
-   Constraint: greater than or equal to *0*
-   Default: *1*

## Phase

`phase`: Phase shift of the time dependence.

Type: floating-point number

-   Unit: rad
-   Default: *0*

## Central Frequency

`freq0`: Central frequency of the pulse.

Type: floating-point number

-   Unit: Hz
-   Constraint: greater than *0*
-   Required field

## Fwidth

`fwidth`: Standard deviation of the frequency content of the pulse.

Type: floating-point number

-   Unit: Hz
-   Constraint: greater than *0*
-   Required field

## Offset

`offset`: Time delay of the maximum value of the pulse in units of *1 / (2$pi$* * `fwidth`).

Type: floating-point number

-   Unit: *1 / (2$pi$* * `fwidth`)
-   Constraint: greater than or equal to *2.5*
-   Default: *5*
