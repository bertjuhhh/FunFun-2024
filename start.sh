#!/bin/bash
git pull

# Set the directory you want to upload
SOURCE_DIR=~/FunFun-2024/Raspberry-Pi-Pico

# Set the port for the Raspberry Pi Pico
PORT=/dev/ttyACM0

# Function to create directories recursively
function create_dir() {
    local DIR_PATH="$1"
    local IFS='/'
    local PARTIAL_PATH=""
    for PART in $DIR_PATH; do
        PARTIAL_PATH="$PARTIAL_PATH/$PART"
        if ! ampy --port "$PORT" ls "$PARTIAL_PATH" &>/dev/null; then
            ampy --port "$PORT" mkdir "$PARTIAL_PATH"
        fi
    done
}

# Find all files in the source directory
find "$SOURCE_DIR" -type f | while read FILE; do
    # Strip the source directory prefix to get the relative path
    REL_PATH="${FILE#$SOURCE_DIR/}"

    # Create the target directory structure on the Pico
    DIR_PATH=$(dirname "$REL_PATH")
    create_dir "$DIR_PATH"

    # Upload the file
    ampy --port "$PORT" put "$FILE" "/$REL_PATH"
done

# Run the python script to play music
python3 ~/FunFun-2024/Raspberry-Pi-1b/music.py