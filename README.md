# Overview

This repo contains a few helpful python scripts and community levels for defense grid.

# Just give me the levels


1: In steam, set defense grid 2 to run in compatibility model.

  * Properties -> Comparability -> Check the force box -> latest stable proton.
  * At writing, latest stable proton is 9.0-4.

2: In file explorer navigate to folder

* **Mint**: home/<profile name>/.steam/steam/steamapps/compatdata/221540/pfx/drive_c/users/steamuser/Documents
* **Steam Deck**: /home/deck/.steam/steam/steamapps/compatdata/221540/pfx/drive_c/users/steamuser/Documents
* App ID 221540 is Defense Grid 2.


3: Make folder called DG2 inside the above folders.

4: Download the DG2_batch_<number>.zip files from [google drive](https://drive.google.com/drive/u/0/folders/11ZdOrdAJ0FocGhqsKybbOFtW3hV3C4h9).
There are 

5: Unzip the DG2_batch_<number>.zip files and copy contents into the DG2 folder in step 3.

  * Only copy one batch into the DG2 folder. When you are done with those maps, delete them from DG2 folder and copy the next batch in. Don't have more than 40 maps in the DG2 folder at any one point in time.

# Background

## What is a map?
The map is the inner folder that contains files and no sub directories. The map is not the outer folder containing one sub directory and one file. For example, the “Aces-Wild” downloaded zip file contains the “Ace Wild” subfolder. The inner “Ace Wild” (with space) is the map and should be copied over to DG2 folder. Coping the “Ace-Wild” (with hyphen) outer folder will not work.

## How many maps can I have inside of the DG2 foler?
You cannot copy all maps into the folder at once because Defense grid 2 will crash. 40 maps at any point in time works well. This repo contains batches of 40 maps.

I included the AdditionalDifficultyLevels folder in each batch. This is a difficulty changer, not a map.

# Code
There are two python scripts. One to unzip all downloaded files (unzip_all_files.py). Another to do file manipulation and group maps together. This code is not robust and will require modification to run on another machine. I included it in case I need to modify it in the future.

Hope this helps the next guy! Thanks [dg2freemaps.com](https://www.dg2freemaps.com/).
