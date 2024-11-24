#!bin/bash

# lists=$(ls results/green_images)

# echo ${lists}

# for image in results/green_images
# do
#     for list in ${lists}
#     do
#         cp ${image}/${list}/${list}_inpainting_mask_.png  results/green_images_mask/inpainting3_${list}.png
#     done
# done


lists=$(ls inpainting_dataset/labels/train)
echo ${lists}

for image in inpainting_dataset/labels/train
do
    for list in ${lists}
    do
        cp ${image}/${list} ${image}/inpainting_${list}
    done
done