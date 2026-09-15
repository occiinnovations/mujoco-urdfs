import mujoco
import mujoco.viewer
import time

ONE = "mjmodel.xml"
TWO = "tiny.xml"

model_choice = input("Type ONE for UR10 model, TWO for tiny model: ")

if model_choice == "ONE":
    model_choice = ONE
elif model_choice == "TWO":
    model_choice = TWO

ur10_model = mujoco.MjModel.from_xml_path(model_choice)
data = mujoco.MjData(ur10_model)

with mujoco.viewer.launch_passive(ur10_model, data) as viewer:
    while viewer.is_running():

        mujoco.mj_step(ur10_model, data)
        viewer.sync()

        time.sleep(0.002)
