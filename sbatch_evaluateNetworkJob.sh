#!/bin/bash

#SBATCH --job-name="Evaluate Network Job"
#SBATCH -n 4
#SBATCH -p backfill2
#SBATCH --mail-type="ALL"
#SBATCH -t 01:00:00
#SBATCH --gres=gpu:2

module load cuda/11.1
python Scripts/evaluateNetwork.py
