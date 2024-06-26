#!/usr/bin/bash

source /etc/profile.d/modules.sh
module load cuda/11.4.3

eval "$(conda shell.bash hook)"
conda activate DEEPLABCUT

exec python -m ipykernel "$@"
