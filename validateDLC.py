# DLC Project Verification Script
# DewanLab
# Author: Austin Pauley
# Date: 04/08/2022
# Verifies project is corretly configured to be run by anyone on the RCC server

from deeplabcut.utils import auxiliaryfunctions
import re
import colorama
import os
import stat
from colorama import Fore
from colorama import Style
colorama.init()


print(Fore.GREEN + Style.BRIGHT + "###DewanLab DLC Vallidation Script###\n")
print(Fore.BLUE + Style.BRIGHT + "  ___        ()-().----.          .")
print(Fore.BLUE + Style.BRIGHT + " |   |_       \\\"/` ___  ;________.'")
print(Fore.BLUE + Style.BRIGHT + " |    <|~~~    ` ^^   ^^")
print(Fore.BLUE + Style.BRIGHT + " -------                            ")


#Check if Log Folders Exist, create them if not

if not os.path.exists('logs'):
	os.makedirs('logs')
	print(Fore.RED + Style.BRIGHT + 'log folder not found, creating it!')
if not os.path.exists('logs/train'):
	os.makedirs('logs/train')
	print(Fore.RED + Style.BRIGHT + 'log/train folder not found, creating it!')
if not os.path.exists('logs/novel'):
	os.makedirs('logs/novel')
	print(Fore.RED + Style.BRIGHT + 'log/novel folder not found, creating it!')


#Get all files and folders in project

filelist = []
folderlist = []
for root,dirs,files in os.walk('.'):
	for file in files:
		filelist.append(os.path.join(root,file))
	for folder in dirs:
		folderlist.append(os.path.join(root,folder))

#Set GID for all files to dewangroup
#Dewangroup gid = 60142
print(Fore.GREEN + Style.BRIGHT + 'Setting group to dewangroup for all files.')
for file in filelist:
	try:
		os.chown(file, -1, 60142)
	except OSError as e:
		print(Fore.RED + Style.BRIGHT + 'Error while trying to chown {} \n {}'.format(file, e))
print(Fore.GREEN + Style.BRIGHT + 'Success!')

#Set GID for all folders to dewangroup
print(Fore.GREEN + Style.BRIGHT + 'Setting group to dewangroup for all folders.')
for folder in folderlist:
	try:
		os.chown(folder, -1, 60142)
	except OSError as e:
		print(Fore.RED + Style.BRIGHT + 'Error while trying to chown {} \n {}'.format(folder,e))
print(Fore.GREEN + Style.BRIGHT + 'Success!')

#Set permissions for all files u=rwx,g=rwx,o=r
print(Fore.GREEN + Style.BRIGHT + 'Setting permissions for all files.')

for file in filelist:
	try:
		st = os.stat(file)
		os.chmod(file, stat.S_IRWXU | stat.S_IRWXG | stat.S_IROTH )
	except OSError as e:
		print(Fore.RED + Style.BRIGHT + 'Error while trying to chmod {} \n {}'.format(file, e))

print(Fore.GREEN + Style.BRIGHT + 'Success!')

#Set permissions for all folders u=rwx,g=rwx,o=r

print(Fore.GREEN + Style.BRIGHT + 'Setting permissions for all folders.')

for folder in folderlist:
	try:
		st = os.stat(folder)
		os.chmod(folder, stat.S_IRWXU | stat.S_IRWXG | stat.S_IROTH )
	except OSError as e:
		print(Fore.RED + Style.BRIGHT + 'Error while trying to chown {} \n {}'.format(folder, e))
print(Fore.GREEN + Style.BRIGHT + 'Success!')

#Update project path to current working directory
print(Fore.GREEN + Style.BRIGHT + 'Updating project path.')
auxiliaryfunctions.edit_config('config.yaml', {'project_path': os.getcwd()})
print(Fore.GREEN + Style.BRIGHT + 'Success!')


#Update the init-weights to /gpfs/research/dewangroup/Pretrained_Model/resnet_v1_50.ckpt
print(Fore.GREEN + Style.BRIGHT + 'Updating pose_cfg.yaml')

model_path = '/gpfs/research/dewangroup/Pretrained_Model/resnet_v1_50.ckpt'
main_cfg = auxiliaryfunctions.read_plainconfig('config.yaml') # Load the default config file
modelprefix=main_cfg["project_path"] # Get the path of the model folder from the confgi file
trainFraction =main_cfg["TrainingFraction"][0] # Get the current training fraction, since this is stored as a list, get the first index

try:
	modelFolder = auxiliaryfunctions.GetModelFolder(trainFraction, 1, main_cfg, modelprefix="")
except:
	raise FileNotFoundError("Cannot find Training Model Folder. Has training dataset been created?")
else:
	modelPath = modelprefix / modelFolder / "train"
	pose_config = modelPath / "pose_cfg.yaml"

auxiliaryfunctions.edit_config(pose_config, {'init_weights': model_path})

print(Fore.GREEN + Style.BRIGHT + 'Success!')

print(Fore.BLUE + Style.BRIGHT + 'Project is ready!')
