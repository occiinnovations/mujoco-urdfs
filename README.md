# MuJoCo URDF Templates

A clean project template to load, view, and test different robot models using the MuJoCo physics engine.

When you run the script, a menu pops up in your terminal allowing you to type a choice and instantly load that specific robot model into a separate viewing window.

## Project Structure

```text
MuJoCb/
├── .gitignore          # Stops temporary files from uploading to GitHub
├── requirements.txt    # The short list of libraries you need (NumPy, MuJoCo)
└── src/
    ├── main.py         # The main script with the menu loop
    ├── mjmodel.xml     # The UR10e robot arm model file
    └── tiny.xml        # The simple box test model file
```

## How to Run It

### 1. Install the tools
Open your terminal and install the required coding libraries:
```powershell
python -m pip install -r requirements.txt
```

### 2. Start the simulation
Change into the source folder and start the main script:
```powershell
cd src
python main.py
```
Type `ONE` for the UR10e arm or `TWO` for the simple box, and the MuJoCo Viewer will open.

