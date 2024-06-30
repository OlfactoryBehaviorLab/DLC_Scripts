# Name: DeepLabCut Create Training Dataset
# Author: Austin Pauley
# Initial Date: 07/12/2021
# Further training configuration options are located in the main config.yaml and the model config.yaml

import os
os.environ["DLClight"]="True"

################################# DONT CHANGE ANYTHING ABOVE THIS LINE ############################################
###################################################################################################################

#Insert absolute path to the config for the active project
config_path = "/gpfs/home/acp18/Projects/SC25_BW-DewanLab-2021-09-01/config.yaml"


################################# DONT CHANGE ANYTHING BELOW THIS LINE ###########################################
##################################################################################################################

import deeplabcut

#Train the network
deeplabcut.create_training_dataset(config_path, num_shuffles=1, augmenter_type='imgaug')



