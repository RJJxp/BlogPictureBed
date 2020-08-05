#!/bin/bash

set -ue
CURRENT_PATH=$(cd `dirname $0`; pwd)
cd ${CURRENT_PATH}

# setup params
INPUT_FOLDER=$1
RESIZE_WIDTH=$2
RENAME_TYPE=$3
OUTPUT_JPG_FOLER=${INPUT_FOLDER}_jpg
OUTPUT_RESIZE_FOLDER=${INPUT_FOLDER}_${RESIZE_WIDTH}
OUTPUT_RENAME_FOLDER=${INPUT_FOLDER}_${RESIZE_WIDTH}_final

# echo ${OUTPUT_JPG_FOLER}
# echo ${OUTPUT_RESIZE_FOLDER}
# echo ${OUTPUT_RENAME_FOLDER}

# run script
# convert to .jpg
python3 toJPG.py --input-dir ${INPUT_FOLDER} --output-dir ${OUTPUT_JPG_FOLER}
# resize 
python3 resize_pic.py --input-dir ${OUTPUT_JPG_FOLER} --output-dir ${OUTPUT_RESIZE_FOLDER} --width ${RESIZE_WIDTH}
# rename
python3 rename_pic.py --input-dir ${OUTPUT_RESIZE_FOLDER} --output-dir ${OUTPUT_RENAME_FOLDER} --rename-type ${RENAME_TYPE}
# generate feature text
python3 gen_f_image_txt.py --input-dir ${OUTPUT_RENAME_FOLDER}