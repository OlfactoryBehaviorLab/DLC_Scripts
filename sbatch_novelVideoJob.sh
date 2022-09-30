#!/bin/bash

#SBATCH --job-name="Novel Video Processing"
#SBATCH -n 8
#SBATCH -p backfill2
#SBATCH --mail-type="ALL"
#SBATCH -t 04:00:00
#SBATCH --gres=gpu:4

module load cuda/11.1
python Scripts/novelVideo.py
