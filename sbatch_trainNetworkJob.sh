#!/bin/bash

#SBATCH --job-name="Network Train Job "
#SBATCH -n 8
#SBATCH -p backfill2
#SBATCH --mail-type="ALL"
#SBATCH -t 04:00:00
#SBATCH --gres=gpu:4
#SBATCH -a 0-6%1

module load cuda/11.1

python Scripts/trainModel.py
