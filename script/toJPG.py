import argparse
import io
import os
import shutil
from PIL import Image as PilImage 

def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input-dir', type=str, help='Enter the origin directory.')
    parser.add_argument('--output-dir', type=str, help='Enter the output directory.')
    args = parser.parse_args()
    print ("parse args complete")
    return args

def toJPG(in_dir, out_dir):
    print("start converting.")

    if os.path.exists(out_dir):
        shutil.rmtree(out_dir)
        print('outputdir already exists.')
    os.mkdir(out_dir)
    
    for pic_name in os.listdir(in_dir):
        pic_path = os.path.join(in_dir, pic_name)
        pic = PilImage.open(pic_path)
        pic_rgb = pic.convert("RGB")
        index_dot = pic_name.rfind('.')    # find the last '.'
        save_name = pic_name[0:index_dot] + ".jpg"
        save_path = os.path.join(out_dir, save_name)
        pic_rgb.save(save_path)
        # print("converted %s" %pic_name)

    print("finished all pics in in_dir converting.")

if __name__ == "__main__":
    print("***********************************")
    print("******* start toJPG script. *******")
    print("***********************************")
    args = getArgs()
    in_dir = args.input_dir
    out_dir = args.output_dir
    toJPG(in_dir, out_dir)
    print("**************************************")
    print("******* finished toJPG script. *******")
    print("**************************************")
    print("\n\n")
