# Simulation Setup

*This section covers all aspects of setting up a simulation in Flow360, including flow conditions, meshing, solver configuration, and output settings.*

## **Contents**

| *Section* | *Description* |
|-------------|-----------------|
| [Flow Conditions](./01.flow-conditions/README.md) | Define freestream and operating conditions |
| [Mesh](./02.mesh/README.md) | Configure mesh generation, rotation regions, and refinements |
| [Flow Solver](./03.flow-solver/README.md) | Set solver numerics, boundary conditions, and physics models |
| [Output](./04.output/README.md) | Specify output fields, reference dimensions, and result formats |

---

## **Detailed Subsections**

- **Flow Conditions:**
  - [Operating condition](./01.flow-conditions/01.operating-condition.md): Define physical values of fluid properties
  - [Farfield](./01.flow-conditions/02.farfield.md): Configure farfield boundary settings

- **Mesh:**
  - [Mesh (meshing defaults)](./02.mesh/01.mesh.md): Control parameters for mesh generation
  - [Rotation regions](./02.mesh/02.rotation-regions.md): Specialized regions for rotating features
  - [Refinements](./02.mesh/03.refinements/README.md): Local mesh control for critical regions

- **Flow Solver:**
  - [Boundary conditions](./03.flow-solver/01.boundary-conditions/README.md): Define domain boundaries
  - [Time](./03.flow-solver/02.time.md): Time resolution controls
  - [Physics](./03.flow-solver/03.physics/README.md): Physical models in the simulation
  - [User-defined dynamics](./03.flow-solver/04.user-defined-dynamics.md): Custom dynamics definitions

- **Output:**
  - [Reference dimensions](./04.output/01.reference-dimensions.md): Dimensions for force coefficient calculations
  - [Output list](./04.output/02.outputs-list/README.md): All outputs to generate from the simulation
  

```{toctree}
:hidden:
:maxdepth: 3
./01.flow-conditions/README.md
./02.mesh/README.md
./03.flow-solver/README.md
./04.output/README.md
```