#!bin/bash


for image in results/desert_images_mask/*
do
    python3 lang_segment.py \
        --input_img /workspace/Inpaint-Anything/${image}\
        --text_prompt person
done