#!bin/bash

inputs=$(ls /workspace/Inpaint-Anything/input/flip/images/val)


for input in ${inputs}
do
    python3 image_flip.py \
            --input /workspace/Inpaint-Anything/input/flip/images/val/${input} \
            --output /workspace/Inpaint-Anything/results/flip_datasets/val/images/flip_${input}
done