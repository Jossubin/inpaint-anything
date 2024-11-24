#!bin/bash

inputs=$(ls /workspace/Inpaint-Anything/input/flip/labels/val)


for input in ${inputs}
do
    python3 boundary_box_flip.py \
            --input /workspace/Inpaint-Anything/input/flip/labels/val/${input} \
            --output /workspace/Inpaint-Anything/results/flip_datasets/val/labels/flip_${input}
done