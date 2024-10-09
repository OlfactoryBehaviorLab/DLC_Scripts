#!/usr/bin/bash

source /etc/profile.d/modules.sh
module load cuda/11.0

eval "$(conda shell.bash hook)"
conda activate DEEPLABCUT

exec python -m ipykernel "$@"
