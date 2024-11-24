python3 remove_anything.py \
    --input_img ./input/case4_raw.png \
    --coords_type key_in \
    --point_coords 558 224 \
    --point_labels 1 \
    --dilate_kernel_size 15 \
    --output_dir ./results/remove \
    --sam_model_type "vit_t" \
    --sam_ckpt ./weights/mobile_sam.pt \
    --lama_config ./lama/configs/prediction/default.yaml \
    --lama_ckpt ./pretrained_models/big-lama


    
