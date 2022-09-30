#!/bin/bash

#SBATCH --job-name="Output Analysis Data"
#SBATCH -n 8 
#SBATCH -p backfill2
#SBATCH --mail-type="ALL"
#SBATCH -t 02:00:00
#SBATCH --gres=gpu:4

module load cuda/11.1
python Scripts/outputAnalysis.py
