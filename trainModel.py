# Name: DeepLabCut Train Network FSU HPC Script
# Lab: DewanLab
# Author: Austin Pauley
# Initial Date: 07/11/2021
# Further training configuration options are located in the main config.yaml and the model config.yaml

import os
os.environ["DLClight"]="True"
import tensorflow as tf
################################# DONT CHANGE ANYTHING ABOVE THIS LINE ############################################
###################################################################################################################

#Insert absolute path to the config for the active project
config_path = "/gpfs/home/acp18/Projects/SC25_BW-DewanLab-2021-09-01/config.yaml"

# How often you want to display the number of iterations. This will display the total iterations every 100 iterations
num_iters = 10

# How often to save the progress of the training. E.G. This will save every 2000 iterations
save_iters = 2000

# Which shuffle are we using?
_shuffle = 1
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



#import the DLC framework
import deeplabcut
import update_Config

update_Config.update_Config(config_path,_shuffle)

#Train the network
deeplabcut.train_network(config_path, shuffle=_shuffle, displayiters=num_iters, saveiters=save_iters, allow_growth=True)
