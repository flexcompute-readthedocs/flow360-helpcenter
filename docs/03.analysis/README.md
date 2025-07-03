# Analysis

*A comprehensive suite of tools for analyzing and visualizing simulation results in Flow360.*

---

## 📋 **Available Options**

| *Option* | *Description* | *Purpose* |
|------------|-----------------|-------------|
| [Dashboard](./01.dashboard.md) | Interactive overview of simulation progress and key metrics | Real-time monitoring and analysis |
| [Convergence](./02.convergence.md) | Analysis of solution convergence behavior | Solution quality assessment |
| [Monitor](./03.monitor.md) | Tracking of flow field variables at specific locations | Detailed flow analysis |
| [Visualization](./04.visualization.md) | Advanced visualization tools for flow field data | Flow pattern analysis |
| [Aeroacoustic](./05.aeroacoustic.md) | Acoustic analysis and noise prediction | Sound generation and propagation |

---

## 🔍 **Detailed Descriptions**

### **Dashboard**

*The Dashboard provides an interactive overview of your simulation's progress and key performance metrics.*

**Features:**
- Real-time progress tracking
- Key performance indicators
- Simulation status overview
- Resource utilization metrics

### 🎯 **Convergence**

*Convergence analysis tools help assess the quality and stability of your simulation results.*

**Features:**
- Nonlinear residual monitoring
- Linear residual tracking
- CFL number visualization
- State variable bounds
- Maximum residual location tracking

### 📊 **Monitor**

*Monitors enable detailed tracking of flow field variables at specific locations during simulation.*

**Available Types:**
- Total Forces
- Forces by Surface
- Heat Transfer by Surface
- BET Forces and Moments
- Force Distribution (X/Y)
- Actuator Disk metrics


### 🎨 **Visualization**

*Advanced visualization tools for analyzing flow field data and patterns.*


**Features:**
- Surface visualization
- Volume visualization
- Slice analysis
- Isosurface generation
- Streamline visualization

### 🔊 **Aeroacoustic**

*Specialized tools for acoustic analysis and noise prediction.*

**Features:**
- Acoustic pressure monitoring
- Frequency spectrum analysis
- Overall Sound Pressure Level (OASPL) calculation
- A-weighting support
- Multiple observer positions

---

<details>
<summary><h3 style="display:inline-block"> 💡 Tips</h3></summary>

- **Dashboard Usage:**
  - Monitor simulation progress in real-time
  - Track key performance metrics
  - Identify potential issues early

- **Convergence Analysis:**
  - Check residual history for stability
  - Monitor CFL numbers for numerical stability
  - Use maximum residual location to identify problematic regions

- **Monitor Setup:**
  - Place monitors strategically for meaningful data collection
  - Consider both steady and unsteady simulation needs
  - Use appropriate sampling frequencies

- **Visualization Best Practices:**
  - Start with surface visualization for quick insights
  - Use slices for detailed flow analysis
  - Generate isosurfaces for specific flow features

- **Aeroacoustic Analysis:**
  - Ensure sufficient temporal resolution for acoustic analysis
  - Place observers outside the flow domain
  - Consider both solid and permeable approaches

</details>

---

<details>
<summary><h3 style="display:inline-block"> ❓ Frequently Asked Questions</h3></summary>

- **What is the difference between pseudo steps and physical steps?**
  > Pseudo steps are used in steady-state simulations, while physical steps are used in unsteady simulations (though they consist of pseudo steps). Physical steps represent actual time advancement in the simulation.

- **How do I interpret convergence plots?**
  > Look for decreasing residuals over time. A stable, decreasing trend indicates good convergence. Sudden spikes or oscillations may indicate numerical issues.

- **When should I use aeroacoustic analysis?**
  > Aeroacoustic analysis is valuable for applications where noise prediction is important, such as aircraft design, wind turbine performance, and automotive aerodynamics.

- **What is the purpose of A-weighting in acoustic analysis?**
  > A-weighting adjusts sound levels to match human hearing sensitivity, providing more meaningful noise assessment for human perception.

</details>
