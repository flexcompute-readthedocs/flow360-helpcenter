# Output

*A section responsible for the definitions of simulation outputs.*

## **Contents**

| **Settings group** | **Short description** |
|--------------------|-----------------------|
| [Reference dimensions](./01.reference-dimensions.md) | Form for filling in dimensions that are used for force coefficients calculation. |
| [Outputs list](./02.outputs-list/README.md) | A list containing all outputs to generate from the simulation | 

---

## **Detailed Descriptions**

### **[Reference dimensions](./01.reference-dimensions.md)**

*Form for defining dimensions used in force coefficient calculations. Specifies reference area, length, and other geometric parameters essential for computing aerodynamic coefficients and non-dimensionalizing results.*

### **[Outputs list](./02.outputs-list/README.md)**

*Comprehensive list of all outputs to generate from the simulation. Controls what data is generated during and after simulation runs, including flow variables, output locations, frequencies, and file formats.*

**Subsections:**
- **[Volume Output](./02.outputs-list/01.volume-output.md)** - Flow field data throughout the computational volume
- **[Time Average Volume Output](./02.outputs-list/02.time-averaging-volume-output.md)** - Time-averaged flow field data throughout the volume
- **[Surface Output](./02.outputs-list/03.surface-output.md)** - Flow field data on geometry or volume mesh boundaries
- **[Time Average Surface Output](./02.outputs-list/04.time-averaging-surface-output.md)** - Time-averaged flow field data on surfaces
- **[Slice Output](./02.outputs-list/05.slice-output.md)** - Flow field data on user-defined slice planes
- **[Time Average Slice Output](./02.outputs-list/06.time-averaging-slice-output.md)** - Time-averaged flow field data on slice planes
- **[Probe Outputs](./02.outputs-list/07.probe-outputs.md)** - Flow field data monitoring during simulation
- **[Time Average Probe Outputs](./02.outputs-list/08.time-averaged-probe-outputs.md)** - Time-averaged monitoring data
- **[Surface Probe Output](./02.outputs-list/09.surface-probe-outputs.md)** - Flow field data at specific points projected onto surfaces
- **[Surface Slice Output](./02.outputs-list/10.surface-slice-output.md)** - Flow field data on slices of surfaces
- **[Isosurface Output](./02.outputs-list/11.isosurface-output.md)** - Flow field data on surfaces of constant variable value
- **[Aeroacoustic Output](./02.outputs-list/12.aeroacoustic-output.md)** - Data for aeroacoustic analysis at observer positions
- **[Output Formats](./02.outputs-list/13.output-formats.md)** - File format specifications for output data
- **[Streamline Output](./02.outputs-list/14.streamline-output.md)** - Visualization of 3D flow structures 