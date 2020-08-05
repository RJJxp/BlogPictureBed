import argparse
import io
import os
import shutil
from PIL import Image as PilImage 

def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input-dir', type=str, help='Enter the origin directory.')
    parser.add_argument('--output-dir', type=str, help='Enter the output directory.')
    parser.add_argument('--rename-type', type=str, default='0', help='0-->0001.jpg; 1-->1.jpg')
    args = parser.parse_args()
    print ("parse args complete")
    return args

def renameIt(in_dir, out_dir, rename_type):
    print("start resizing.")
    # judge output_dir existence
    if os.path.exists(out_dir):
        shutil.rmtree(out_dir)
        print('outputdir already exists.')
    os.mkdir(out_dir)
    
    count = 0
    for pic_name in os.listdir(in_dir):
        pic_path = os.path.join(in_dir, pic_name)
        pic = PilImage.open(pic_path)
        # 2 ways to name the picture
        if (rename_type == '0'):
            pic_save_name = "%04d" %count + ".jpg"
        else:
            pic_save_name = "%d" %count + ".jpg"
        save_path = os.path.join(out_dir, pic_save_name)
        pic.save(save_path)
        count = count + 1
        # print("renamed %s" %pic_name)

    print("finished all pics in in_dir resizing.")

if __name__ == "__main__":
    print("***************************************")
    print("******* start renamePic script. *******")
    print("***************************************")
    args = getArgs()
    in_dir = args.input_dir
    out_dir = args.output_dir
    rename_type = args.rename_type
    renameIt(in_dir, out_dir, rename_type)
    print("***************************************")
    print("******* start renamePic script. *******")
    print("***************************************")
    print("\n\n")
