python3 /workspace/inpaint_anything/fill_anything.py \
            --input_img "/workspace/inpaint_anything/input/model.jpg" \
            --coords_type key_in \
            --point_coords 200 400 \
            --point_labels 1 \
            --text_prompt "A bold chest print features a distressed black "22" with a vintage vibe, surrounded by dense catalog-like text for a modern touch. The subtly textured knit fabric adds sophistication, blending urban style with cozy knitwear for versatile wear.
" \
            --output_dir "${output_folder}/${input}/ably2" \
            --sam_model_type "vit_h" \
            --sam_ckpt /workspace/inpaint_anything/weights/sam_vit_h_4b8939.pth\
            --seed 0