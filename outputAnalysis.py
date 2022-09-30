# Name: DeepLabCut Train Network FSU HPC Script
# Lab: DewanLab
# Author: Austin Pauley
# Initial Date: 07/11/2021
# Further training configuration options are located in the main config.yaml and the model config.yaml

import os
import tensorflow as tf
os.environ["DLClight"]="True"

################################# DONT CHANGE ANYTHING ABOVE THIS LINE ############################################
###################################################################################################################

#Insert absolute path to the config for the active project
config_path = "/gpfs/home/acp18/Projects/SC25_BW-DewanLab-2021-09-01/config.yaml"

novel_video = ['/gpfs/home/acp18/Projects/SC25_BW-DewanLab-2021-09-01/videos/BW_2.mp4']


################################# DONT CHANGE ANYTHING BELOW THIS LINE ###########################################
##################################################################################################################



## Some kind of configuration to prevent memory errors. Don't know how it works but it kept the project from crashing?

devices = tf.config.list_physical_devices('GPU')
try:
     tf.config.experimental.set_memory_growth(devices[0], True)
     tf.config.experimental.set_memory_growth(devices[1], True)
     tf.config.experimental.set_memory_growth(devices[2], True)
     tf.config.experimental.set_memory_growth(devices[3], True)
except:
     pass





import deeplabcut

deeplabcut.plot_trajectories(config_path, novel_video,videotype=".mp4")

deeplabcut.create_labeled_video(config_path, novel_video, videotype=".mp4")
