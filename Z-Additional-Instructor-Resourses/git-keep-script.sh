#!/bin/bash

# This function will search for all empty directories within the current directory recursively.
find_empty_directories() {
    find . -type d -empty
}

# This function will add a .gitkeep file to all empty directories.
add_gitkeep_to_empty_directories() {
    local empty_dirs="$(find_empty_directories)"
    if [ -z "$empty_dirs" ]; then
        echo "No empty directories found."
    else
        echo "$empty_dirs" | while read -r dir; do
            touch "${dir}/.gitkeep"
            echo ".gitkeep added to $dir"
        done
    fi
}

# Run the function to add .gitkeep to all empty directories.
add_gitkeep_to_empty_directories
