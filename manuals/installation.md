# Setup
Gilg needs some things before you can use it. Here's a quick guide what to do

---

### Binary - Windows
If you are on Windows and want to use .exe version of gilg we recommend completing those teps:

1. Download the latest realease of Gilg *(or specific one)*
2. Move the downloaded .exe to to specific folder. For example `C:\Other Tools`
3. Copy the path of the folder you chose
4. Search for **Edit the system environment variables** in start menu
5. Click on `Advanced -> Environment Variables`
6. Click on **Path** and hit **Edit**
7. Click on **New** and paste the copied path into new field *(you will probably need to remove quotes)*
8. Click **Ok** and then **Ok** again
9. Close the terminal

Congratulations! Now you can run **Gilg** through your terminal regardless of your working directory

### Python - Any OS
If you prefer to run python version of Gilg on your device we recommend completing those steps:

1. Install [Python](https://www.python.org/downloads/) from official website
2. Run the installator <br>
*Recommended*: Check the "add python to path" checkbox
3. Check if python was installed correctly by typing `python --version` in the terminal
4. Install [gallery-dl](https://github.com/mikf/gallery-dl) library by typing `pip install gallery-dl` in the terminal
5. Install [colorama](https://pypi.org/project/colorama/) library by typing `pip install colorama` in the terminal <br> 
*Warning: You may need to replace "pip" with "pip3" depending on which pip version was installed*

Congratulations! Now you can run **Gilg** via your terminal

### Reminder
Please keep in mind gilg is not supposed to be run by double clicking on it. It is required to run it via terminal otherwise absolutely nothing will happen.