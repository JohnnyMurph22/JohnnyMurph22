# -*- coding: utf-8 -*-
"""
Config file for the program. All constants should be stored here.
"""
import os
import datetime
import secrets
import dropbox
# Retrieves the dropbox API oauth 2 access token saved as an environment variable.
# TOKEN = os.environ.get("TOKEN")
# TOKEN = 'sl.BH8FweahY-fjR3CkjZgjA8sH33g2AsuyNR6Q1FKJg_fExiUcOiZ5oRNJuYBJC78-Z9fXVOyt3MMhOWCtlU-R_VEZ04If5lu_FY8zd1tYzi0imFKKwQML4e6u8X1MF99MnOdK-eE'

# Sets the log file to the path provided or defaults to the tmp folder.
LOGFILE = os.environ.get("LOGFILE", "Downloads")

# Constant to store the source directory. Must contain a leading "/" and no trailing "/".
SOURCE_DIR = "/Pictures"

# Constant to store the destination directory. Must contain a leading and trailing "/".
DEST_DIR = "/Dropbox/"

# Set the base path dynamically using the current year.
BASE_DEST_PATH = f"{DEST_DIR}{datetime.datetime.now().year}"

# Category constants - used to define the overall types of files that will be dropsaved.
# These will also be the keywords we look for in the file names of the source files.
# Must be lowercase.
PICTURES = "pictures"
VIDEOS = "videos"

# Path associations - used to map categories to destination paths.
CATEGORY_TO_PATH_MAP = {
    PICTURES: f"{BASE_DEST_PATH} Pictures",
    VIDEOS: f"{BASE_DEST_PATH} Videos",
}