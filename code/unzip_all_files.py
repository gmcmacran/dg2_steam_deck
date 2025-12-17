###################################################
# Overview
#
# A script to decompress maps downloaded from https://www.dg2freemaps.com/.
# Downloaded all available files as of 12-03-2025
# Total of 541 files.
###################################################

import os
import zipfile
from functools import partial

############
# Define input and output folders.
############
base_folder = os.getcwd()
source_folder = os.path.join(base_folder, "original zips")
target_folder = os.path.join(base_folder, "unzipped")

os.path.isdir(source_folder)
os.path.isdir(target_folder)


############
# Define function to process zip files.
############
def process_zipped_file(zipped_file, source_folder, target_folder):

    try:
        unzipped_folder = os.path.join(target_folder, zipped_file.replace(".zip", ""))
        zipped_file = os.path.join(source_folder, zipped_file)

        with zipfile.ZipFile(zipped_file, "r") as zip_ref:
            zip_ref.extractall(unzipped_folder)
        failed = False

    except:
        failed = True

    return failed


############
# Process zip files
############
process_zipped_file = partial(
    process_zipped_file, source_folder=source_folder, target_folder=target_folder
)

all_files = os.listdir(source_folder)

failed_files = list(map(process_zipped_file, all_files))
len(all_files) == len(failed_files)
any(failed_files) == False

############
# Process rar files
############
# Process these folders w/ GUI.
[file for file, failure in zip(all_files, failed_files) if failure]
