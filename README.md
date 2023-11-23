
# PIP Package Updater Tool

Welcome to the PIP Package Updater tool! This utility simplifies the process of updating outdated PIP packages in your Python projects.

## How It Works

### 1. Overview

The tool operates in a few simple steps to manage your project dependencies efficiently.

### 2. Gathering Outdated Packages

Initially, the script fetches a list of outdated PIP packages and stores them in a readable format within a `.txt` file.

### 3. Identifying Latest Updates

Next, the script scans this file to determine the latest update date for each package. It then organizes this information in ascending order.

### 4. Setting Update Intervals

You have control over the update process by specifying a date interval. For instance, if the latest update for a package is in October 2020, and you only want updates after January 2021, you can set the date to '2021.01'. The script will skip and remove packages updated before this date.

### 5. Package Management

The tool not only skips and delete the packages outside the defined interval but also generates a convenient CSV file containing all packages and their corresponding update dates within the specified range.

## How to Use

1. Run the script to fetch outdated packages.
2. Set the desired update interval by specifying the minimum date.
3. Execute the script to update and manage your project's requirements.

By following these steps, you can effortlessly keep your project dependencies up-to-date and well-organized.

Feel free to explore the tool and improve your Python project's development experience! If you have any questions or suggestions, please don't hesitate to reach out.

### To do list:

1. Adding a way to check for the packages locally and if there is any version found delete it.