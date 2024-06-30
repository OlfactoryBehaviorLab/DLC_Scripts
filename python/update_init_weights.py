# Update Config Routine 
# DewanLab
# Author: Austin Pauley
# Date: 07/20/2021
# Provides a method for updating the init_weights variable in pose_config.yaml 

### Import Libraries ###
from deeplabcut.utils import auxiliaryfunctions
import re


def update_Config(_main_config_path, shuffle):
	cfg = auxiliaryfunctions.read_plainconfig(_main_config_path) # Load the default config file
	modelprefix=cfg["project_path"] # Get the path of the model folder from the confgi file
	trainFraction = cfg["TrainingFraction"][0] # Get the current training fraction, since this is stored as a list, get the first index

	try:
		modelFolder = auxiliaryfunctions.GetModelFolder(trainFraction, shuffle, cfg, modelprefix="")
	except:
		raise FileNotFoundError("Cannot find Training Model Folder. Has training dataset been created?")
	else:
		modelPath = modelprefix / modelFolder / "train"
		files = auxiliaryfunctions.grab_files_in_folder(modelPath, ext=".meta", relative=True)
		_pose_config_path = modelPath / "pose_cfg.yaml"

	_pose_config = auxiliaryfunctions.read_plainconfig(_pose_config_path)

	snapshots = []

	for k in files:
	 	if "snapshot" in k:
	 		snapshots.append(int(re.split(r'[-.]', k)[1]))
	if snapshots:
		greatest_snapshot = max(snapshots)
		new_init_weight = str(modelPath / "snapshot-{}".format(greatest_snapshot))
		auxiliaryfunctions.edit_config(_pose_config_path, {'init_weights': new_init_weight})
		print("Config File Updated!")
	else:
		print("No snapshots, starting with model: {}".format(cfg["default_net_type"]))
