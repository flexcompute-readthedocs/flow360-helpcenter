---
orphan: true
---

# Form Name

*A concise description of the purpose of this form goes here.*

---

## 📋 **Available Options**

| *Option* | *Description*                  | *Unspecified additional column (added only in special cases)* |
|------------|----------------------------------|----------|
| **Option_1** | Brief description of option 1,   | Additional info for **Option 1** |
| **Option_2** | Brief description of option 2,   | Additional info for **Option 2**  |
| **Option_n** | Brief description of option n,   | Additional info for **Option n**  |

---

## 🔍 **Detailed Descriptions**

### Option_1

*More detailed explanation or additional context of Option_1.*

- **Default:** `default value`  
- **Example:** `sample input`  
- **Notes:** Additional notes or caveats.

### Option_2

*Detailed explanation for Option_2, clarifying possible values or scenarios.*

- **Default:** `default value`  
- **Example:** `sample input`  
- **Notes:** Additional notes or caveats.

### Option_n

*Explanation of the last option.*

- **Default:** `default value`  
- **Example:** `sample input`  
- **Notes:** Additional notes or caveats.

---

<details>
<summary><h3 style="display:inline-block"> 💡 Tips</h3></summary>

- Keep input concise and accurate.
- Review required fields marked with (*).
- Ensure values match specified units.

<details style="padding-left:20px">
<summary><h4 style="display:inline-block"> This is a nested collapsable tip</h4></summary>

- Keep input concise and accurate.
- Review required fields marked with (*).
- Ensure values match specified units.

</details>
</details>


---

<details>
<summary><h3 style="display:inline-block"> ❓ Frequently Asked Questions</h3></summary>

- **What happens if I leave a field blank?**  
  > Explanation about form validation or default handling.

- **How can I reset the form?**  
  > Instructions on resetting or undoing changes.



</details>


---

<details>
<summary><h3 style="display:inline-block"> 🐍 Python Example Usage</h3></summary>


Below is a Python code example showing how to configure a porous medium model:

```python
# Example (for reference only, not included in GUI documentation)
porous_medium_model = fl.PorousMedium(
    entities=[porous_zone],
    darcy_coefficient=(1e6, 0, 0) / fl.u.m**2,
    forchheimer_coefficient=(1, 0, 0) / fl.u.m,
    volumetric_heat_source=1.0 * fl.u.W/ fl.u.m**3,
)
```

</details>
