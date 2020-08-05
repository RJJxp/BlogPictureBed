import argparse
import io
import os
import shutil

def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input-dir', type=str, help='Enter the origin directory.')
    args = parser.parse_args()
    print ("parse args complete")
    return args

def genTxt(input_dir):
    txt_filename= os.path.join(input_dir, "content.txt")

    with open(txt_filename, 'w') as f1:
        lines = []
        for pic in os.listdir(input_dir):
            if (pic[-4:] != '.jpg'):
                continue
            line = "- /medias/featureimages/" + pic + "\n"
            lines.append(line)
        f1.writelines(lines)
        print("writed all the lines to the file.")
    
    print("finished generated txt.")

if __name__ == "__main__":
    print("***************************************")
    print("******* start genFtxt script. *********")
    print("***************************************")
    args = getArgs()
    input_dir = args.input_dir
    genTxt(input_dir)
    print("*****************************************")
    print("******* finshed genFtxt script. *********")
    print("*****************************************")
    print("\n\n")
