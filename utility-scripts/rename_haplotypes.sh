#!/bin/bash

# Directory containing the files
DIR="./"

# Loop through each file in the directory
for FILE in "$DIR"/*; do
    # Check if it's a file
    if [ -f "$FILE" ]; then
        # Use sed to replace # with . in the file
        sed -i 's/#/./g' "$FILE"
    fi
done


# Loop through each file in the directory again to rename them
for FILE in .; do
    # Check if it's a file
    if [ -f "$FILE" ]; then
        # Rename the file by replacing # with .
        NEW_FILE=$(echo "$FILE" | sed 's/#/_/g')
        mv "$FILE" "$NEW_FILE"
    fi
done



for x in *"."*; do
    mv -- "$x" "${x//#/_}"
done
