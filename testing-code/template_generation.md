# Template Generation for Testing CalB/C Models

This code is designed to automate the generation of **testbed templates** for testing **CalB/C models**. The template creation process includes duplicating specific sheets from a source model, renaming them with version numbers (e.g., `1.0`, `2.0`, etc.), and ensuring that the **named ranges** are updated correctly to maintain functionality across the new versions.

## Key Features

### 1. **Named Ranges and Versioning**
- When duplicating sheets and creating new versions (e.g., `Project_info_1.0`, `Project_info_2.0`), it's essential to preserve the **named ranges** so that all **formulas** and **references** in the duplicated sheets continue to function as intended.
- **Versioning Named Ranges**: The code appends the version number to the named ranges in the duplicated sheets to make them unique. For example, if there is a named range `ProjLoc` in the `Project_info_1.0` sheet, the corresponding named range in `Project_info_2.0` will be `ProjLoc2.0`. This ensures no conflict between the original and versioned sheets.

### 2. **Dynamic Output Filename**
- The **output filename** for the generated testbed template is dynamically based on the original model’s name. This means that if the input model is `AT_model.xlsm`, the output file will be `AT_model_template.xlsx`. This approach ensures that the output file is clearly associated with the source model, making file management easy.

### 3. **Flexible Model Handling**
- The code is designed to handle different model types (e.g., `AT_model`, `Sketch_model`, `Intermodal_freight_model`, etc.) seamlessly. You can assign any model (e.g., `main_model = at_model` or `main_model = sketch_model`) and proceed with the template generation without needing any code modifications specific to each model type.
- Additionally, you can **specify exactly which sheets to copy** for each model. This is crucial since each model may have input sheets with different names. For example, one model may use sheets like `Project_info`, `Model_Inputs`, and `Non-Inf_Program_Info`, while another model may have differently named input sheets. You can simply list the sheets you want to copy (via the `sheets_to_copy` parameter) without needing to change the code to match the sheet names of each specific model.

### 4. **Replicating Input Sheets**
- The code allows you to generate as many replicated versions of the specified input sheets as needed. This is controlled by the `num_replicas` parameter, which defines how many versioned sheets (e.g., `Project_info_1.0`, `Project_info_2.0`, etc.) will be created from the original.


This approach is ideal for automating the creation of testbed templates for **CalB/C models**, ensuring consistency, reducing manual work, and minimizing errors.
