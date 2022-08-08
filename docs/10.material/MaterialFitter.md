---
order: 02
---

# Material Fitter

Tool for fitting refractive index data to get a dispersive medium described by [PoleResidue](/04.medium/02.dispersive%20medium/PoleResidue.html) model.

## Upload Data from File

The data file should be in this format: 

-   For lossless media:

    | wl      | n       |
    | ------- | ------- |
    | [float] | [float] |
    | .       | .       |
    | .       | .       |
    | .       | .       |

-   For lossy media:

    | wl      | n       | k       |
    | ------- | ------- | ------- |
    | [float] | [float] | [float] |
    | .       | .       | .       |
    | .       | .       | .       |
    | .       | .       | .       |

`wl`: Wavelengths. A list of wavelengths for dispersion data. Unit: $\mu$m.

`n`: Index of refraction. Real part of the complex index of refraction.

`k`: Extinction coefficient. Imaginary part of the complex index of refraction.

Note: 

-   Delimiters are not displayed here. For .csv, use comma (,) as delimiter. For .txt, use tab (\t) as delimiter.
-   The strings such as “wl”, “n”, "k" need to be included in the file.

## Basic Fitting Parameters

### Number of Poles

`num_poles`: Number of poles in the model. 

Default *1*

### Number of Optimizations

`num_tries`: Number of optimizations to run with random initial guess. 

Default *50*

### Tolerance

`tolerance`: RMS error below which the fit is successful and the result is returned. 

Default *1e-2*

## Advanced Fitting Parameters

### Wavelength Range

`wvl_min` and `wvl_max`: Wavelength range [`wvl_min`, `wvl_max`] for fitting. Truncate the wavelength-nk data to wavelength range [`wvl_min`, `wvl_max`] for fitting. 

Unit: $\mu$m

### Upper Bound of Oscillator Strength

`bound_amp`: Upper bound of real and imagniary part of oscillator strength *c* in the model [PoleResidue](/04.medium/02.dispersive%20medium/PoleResidue.html). 

Unit: Hz

Default: *None*, which will trigger automatic setup based on the frequency range of interest

### Upper Bound of Epsilon at Infinity Frequency

`bound_eps_inf`: Upper bound of epsilon at infinity frequency. 

Constraint: greater than or equal to *1*

Default: *1*

### Upper Bound of Pole Frequency

`bound_f`: Upper bound of real and imaginary part of pole frequency *a* in the model [PoleResidue](/04.medium/02.dispersive%20medium/PoleResidue.html).

Unit: Hz

Default: *None*, which will trigger automatic setup based on the frequency range of interest

### Stability Constraint

`constraint`: Type of constraint for stability.

Options:

-   *hard*
-   *soft*

Default: *hard*

Note: *hard* constraints are generally recommended since they are faster to compute per iteration, and they often require fewer iterations to converge since the search space is smaller. But sometimes the search space is so restrictive that all good solutions are missed, then please try the *soft* constraints for larger search space. However, both constraints improve stability equally well.

### Number of Inner Iterations

`nlopt_maxeval`: Number of iterations in each inner optimization. 

Default: *5000*
