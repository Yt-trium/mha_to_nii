import skimage.io as io
import os

# Change with your root path
root = '/home/yttm/Cours/TER/ITKTubeTK - Bullitt - Healthy MR Database/Designed Database of MR Brain Images of Healthy Volunteers/'

# Browse all files from all directories, subdirectories...
for path, subdirs, files in os.walk(root):
    for name in files:
        print(os.path.join(path, name))
        # Only convert .mha files
        if name.endswith('.mha'):
            # Use SimpleITK and skimage to convert file
            img = io.imread(os.path.join(path, name),plugin='simpleitk')
            io.imsave(os.path.join(path, name + '.nii'),img,plugin='simpleitk')
            print("DONE")
        else:
            # Skip other files
            print("SKIPPED")