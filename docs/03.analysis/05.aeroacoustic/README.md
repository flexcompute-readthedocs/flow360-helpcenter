# Aeroacoustic

This document describes how to perform aeroacoustic analysis in Flow360. 

## 📊 **Analysis Interface**

*The Analysis interface provides comprehensive tools for analyzing acoustic data through various representations and processing methods.*

---

### 📋 **Available Plots**

| **View Type** | **Description** |
|---------------|-----------------|
| `Spectra` | Frequency-domain representation of acoustic signals. |
| `OASPL` | Overall Sound Pressure Level analysis across frequency spectrum. To download the OASPL file, click on three dots next to plot type. |
| `Pressure-time history` | Temporal evolution of pressure fluctuations. |
| `Harmonic content` | Analysis of frequency components and their amplitudes. To download the tonal OASPL file, click on three dots next to plot type when Harmonic content is selected. |
| `Thickness and loading component` | Separate analysis of thickness noise and loading noise contributions. |

---

### 🔧 **Processing Options**

#### Observers

List of selectable observers based on their group for which the calculations will be performed.

#### Boundaries

List of selectable boundaries for which the calculations will be performed. Total is selected by default and refers to the aggregate of all boundaries.

#### Frequency Range

| **Parameter** | **Description** | **Default Range** | **Unit** |
|---------------|----------------|------------------|----------|
| `Frequency range` | Range of frequencies to include in calculations | `10 - 10000` | Hz |

#### Averaging Settings

| **Option** | **Description** |
|------------|----------------|
| `Number of segments` | Number of segments used for averaging |
| `Segmentation method` | Method for dividing the signal into segments: RPM-based or Time interval-based |


#### Signal Processing Options

| **Option** | **Description** |
|------------|----------------|
| `Use 1/3 octave band` | Apply 1/3 octave band filtering for frequency analysis |
| `Use A-weighting` | Apply A-weighting curve to better represent human hearing perception |
| `Welch method` | Enable Welch's method for power spectral density estimation |

#### Welch Method Parameters

| **Parameter** | **Description** | **Options** |
|---------------|----------------|-------------|
| `Segment length` | Length of segments for Welch's method analysis | `None` or user-specified value |
| `Scaling` | Scaling method for power spectrum calculation | `Spectrum`, `Density` |
| `Average` | Statistical method for averaging across segments | `Mean`, `Median` |

---

### 🔍 **Detailed Descriptions**

#### Frequency Range Configuration

The frequency range setting determines the span of frequencies included in the acoustic analysis:

- **Default range:** `10 Hz` to `10000 Hz`
- **Notes:** 
  - This parameter affects the calculation itself, not just the display
  - Choose a range appropriate for your analysis requirements and the phenomena being studied

#### Averaging Configuration

The averaging system allows for detailed control over how the acoustic data is processed:

- **Default segments:** `3`
- **Segmentation options:**
  - **RPM-based:** Suitable for rotating machinery analysis
  - **Time interval-based:** General purpose, with configurable time step

>**Note:** Increasing the number of segments improves statistical reliability but requires longer time series.

#### Welch Method Settings

The Welch method implementation provides advanced spectral estimation capabilities:

- **Segment length options:**
  - `None`: Automatic segment length determination (default)
  - `Value`: User-specified custom segment length
- **Scaling options:**
  - `Spectrum`: Power spectrum scaling (default)
  - `Density`: Power spectral density scaling
- **Averaging methods:**
  - `Mean`: Arithmetic mean across segments (default)
  - `Median`: Median value across segments
>**Note:** The Welch method helps reduce noise in spectral estimates through segment averaging.

---

<details>
<summary><h3 style="display:inline-block"> 💡 Tips</h3></summary>

- Use A-weighting when comparing results to experimental measurements or regulatory requirements
- The 1/3 octave band analysis is useful for noise certification analysis
- For transient phenomena, consider using shorter time intervals
- Balance the number of averaging segments with the available time series length

</details>

---

<details>
<summary><h3 style="display:inline-block"> ❓ Frequently Asked Questions</h3></summary>

- **What is the recommended number of segments for averaging?**
  > The default of 3 segments provides a good balance between statistical reliability and temporal resolution. Increase for more stable results if your time series is long enough.

- **When should I use A-weighting?**
  > Use A-weighting when comparing results to human perception or when working with certification requirements that specify A-weighted levels.

- **What is the difference between RPM and Time interval segmentation?**
  > RPM-based segmentation is useful for rotating machinery analysis, while time interval segmentation is more general and suitable for most applications. When using time interval segmentation, you can specify the exact time step between samples.

</details> 