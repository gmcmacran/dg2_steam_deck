###################################################
# Overview
#
# A script create zipped files. Each zipped file
# contains 40 community maps. The files need
# to be mannually decompressed and reanamed to
# "DG". This is done because the game can process
# about 40 new maps at a time.
#
# Other set up:
# 1: Open Steam
# 2: Right click on Defense Grid 2.
# 3: Click compatibility
# 4: Force latest version of Photon.
#
# Script is ran in same folder as unzipped folder.
#
# Code is generally not robust and not tested across
# platforms. Assumes running on Mint. Assumes steam
# keeps the App ID as 221540.
#
# Output folder is /home/ixi_eulogy_ixi/.steam/steam/steamapps/compatdata/221540/pfx/drive_c/users/steamuser/Documents
###################################################

import os
import shutil
import zipfile
from functools import partial
from math import ceil

############
# Create input and output folders.
############
base_folder = os.getcwd()
source_folder = os.path.join(base_folder, "unzipped")

profile_name = "ixi_eulogy_ixi"
target_folder = f"/home/{profile_name}/.steam/steam/steamapps/compatdata/221540/pfx/drive_c/users/steamuser/Documents/DG2"

if not os.path.isdir(source_folder):
    print("Error: Unzipped folder not found")


############
# Define function to map files.
############
def move_file(folder, source_folder, target_folder):

    try:
        temp_path = os.path.join(source_folder, folder)
        all_files_in_folder = os.listdir(temp_path)

        # Folder usually have one subfolder. The subfolder may have a different name
        sub_folder = [
            d
            for d in os.listdir(temp_path)
            if os.path.isdir(os.path.join(temp_path, d))
        ]  # List all sub folders.
        if len(sub_folder) == 1:
            sub_folder = sub_folder[0]  # There are never two or more sub folders
            source_subfolder = os.path.join(temp_path, sub_folder)
            target_subfolder = os.path.join(target_folder, sub_folder)
        else:
            # Rarely, sometimes there is no sub folder.
            source_subfolder = os.path.join(source_folder, folder)
            target_subfolder = os.path.join(target_folder, folder)

        # Some maps go through versions.
        # These versions have the same name.
        # Deleting prior copy and writing this iteration's copy.
        # This at least avoids two maps in one folder.
        if os.path.isdir(target_subfolder):
            shutil.rmtree(target_subfolder)

        shutil.copytree(source_subfolder, target_subfolder)

        failed = False

    except:
        failed = True

    return failed


def zip_batch(batch, target_folder):
    batched_files = [
        all_files[i : i + batch_size] for i in range(0, len(all_files), batch_size)
    ][batch]

    # Always copy additional difficulty mod
    if not "all_files" in batched_files:
        batched_files.append("AdditionalDifficultyLevels")

    try:
        if os.path.isdir(target_folder):
            shutil.rmtree(target_folder)
        os.makedirs(target_folder)

        move_file_helper = partial(
            move_file, source_folder=source_folder, target_folder=target_folder
        )

        failed_files = list(map(move_file_helper, batched_files))
        failed = any(failed_files)

        zipped_target = target_folder + f"_batch_{batch}.zip"

        def zip_folder(folder_path, output_path):
            with zipfile.ZipFile(output_path, "w") as zipf:
                for root, dirs, files in os.walk(folder_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        # Keep folder structure inside zip
                        zipf.write(file_path, os.path.relpath(file_path, folder_path))

        zip_folder(target_folder, zipped_target)
        shutil.rmtree(target_folder)

    except:
        failed = True

    return failed


############
# Process map files
############
# Some maps go through versions.
# These versions have the same name.
# Deleting prior copy and writing this iteration's copy.
# This at least avoids two maps in one folder.
# Sorting causes execution order.
all_files = os.listdir(source_folder)
all_files.sort()


batch_size = 40
min_batch_size = 0
max_batch_size = int(ceil(len(all_files) / batch_size))
batches = range(min_batch_size, max_batch_size, 1)

zip_batch_helper = partial(zip_batch, target_folder=target_folder)
list(map(zip_batch_helper, batches))
