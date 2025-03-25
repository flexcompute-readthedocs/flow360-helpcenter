# Output Settings

Output settings in Flow360 control what data is generated during and after simulation runs. These settings determine which flow variables are saved, where they are saved, and how frequently they are written to files.

The **Output Settings** panel in the GUI allows you to configure various types of outputs for visualization and analysis.

## Available Output Types

Flow360 supports the following output types:

1. **Volume Output** - Flow field data throughout the computational volume
2. **Time Average Volume Output** - Time-averaged flow field data throughout the computational volume
3. **Surface Output** - Flow field data on geometry or volume mesh boundaries
4. **Time Average Surface Output** - Time-averaged flow field data on geometry or volume mesh boundaries
5. **Slice Output** - Flow field data on user-defined slice planes
6. **Time Average Slice Output** - Time-averaged flow field data on user-defined slice planes
7. **Probe Output** - Flow field data at specific points in the volume
8. **Time Average Probe Output** - Time-averaged flow field data at specific points in the volume
9. **Surface Probe Output** - Flow field data at specific points projected onto surfaces
10. **Isosurface Output** - Flow field data on surfaces of constant variable value
11. **Aeroacoustic Output** - Data for aeroacoustic analysis at observer positions

## Output Fields and Nondimensional Values

For detailed information about the available output fields, their nondimensionalization, and visualization tips, see the [Output Fields and Nondimensional Values](00.output-fields.md) page.

## Common Settings

Most output types share the following common settings:

- **Name** - A descriptive name for the output
- **Output Fields** - The flow variables to include in the output
- **Frequency** - How often to write output files (in number of time steps)
- **Frequency Offset** - The time step at which to start writing output
- **Output Format** - The file format for output data (Paraview, Tecplot, or both)

## Output File Formats

Flow360 supports multiple output file formats:

- **Paraview** (.vtu, .vtp) - For visualization in ParaView
- **Tecplot** (.szplt) - For visualization in Tecplot
- **CSV** - For tabular data (used with some monitor outputs)

For more information about output file formats, see the [Output Formats](12.output-formats.md) page.

## Detailed Settings

Each output type has specific configuration options. Refer to the individual documentation pages for details on configuring each type of output. 