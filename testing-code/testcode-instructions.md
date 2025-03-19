# CalB/C Testbed 

## Scope of Work 
As part of upgrading the Caltrans Benefit-Cost Analysis (BCA) tool, we are developing a Python-based testbed to automate validation of calculated results. Given the complexity of the formulas and multiple performance metrics involved, errors are inevitable. This testbed will identify discrepancies early, ensuring accuracy and streamlining automation as the tool evolves.

## Testbed Workflow
### 1. Install Python on Your Local Machine
Since CalB/C is Excel-based, testing requires the xlwings package, which is not compatible with JupyterHub (a Linux-based environment). Therefore, Python must be installed locally:
- For ArcGIS Users: Use the ArcGIS Python environment if available.
- For Other Users: Download and install Python from the official [website](https://www.python.org/downloads/windows/). Note: Installation may require Admin permission.
- Install any Integrated Development Environment (IDE) for better code editing and debugging, such as [VS Code](https://code.visualstudio.com/).

### 2. Clone the Repository 
- Set Up [SSH for Git](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) if needed 
- Follow [this](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)  to clone [CalB/C repository](https://github.com/cal-itp/cal-bc)

### 3. Sync SharePoint files and folders
We use the [input folder](https://caltrans.sharepoint.com/:f:/r/sites/DOTHQPMPCalBCUpdate/Shared%20Documents/General/Testbed/Input?csf=1&web=1&e=JVfrJX) to read input files and the [output folder](https://caltrans.sharepoint.com/:f:/r/sites/DOTHQPMPCalBCUpdate/Shared%20Documents/General/Testbed/Output?csf=1&web=1&e=VBAYtZ)  to generate outputs, ensuring that everyone always has access to the most up-to-date test results or updates, which can be viewed asynchronously.
- Select the Sync button at the top right to sync all shared files to your personal OneDrive.
- [Input folder](https://caltrans.sharepoint.com/:f:/r/sites/DOTHQPMPCalBCUpdate/Shared%20Documents/General/Testbed/Input?csf=1&web=1&e=JVfrJX) should have `models` and `templates` folder holding main models and template files.

### 4. Update testbed template 
- The `_template.xlsx` is an Excel workbook that contains various sheets, with multiple input sheets for projects 1.0, 2.0, 3.0 and so on. We can make changes to the inputs in those sheets depending on the number of projects we want to test. 

### 5. Running code 
- Once the `testbed_template.xlsm` file is updated, run the `Testcode_allmodels.ipynb` code available in the `cal-bc/testing-code` folder.
- After running the first two lines `pip install xlwings` and `pip install openpyxl` restart the kernel to ensure the necessary packages are available. 
- The output folder will contain one output file for each project based on the data processed from the `testbed_template.xlsm` file.


