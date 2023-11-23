Hi, 
    welcome to the tool which helps you Update all your outdated PIP packages !!!


Let me explain you how is this working. First of all, 
the scripts, is getting the pip -outdated packages under a .txt file.

After this, the script reads the file, is getting the LATEST UPDATE date for each package,
is sorting it in an ascendent order, and then, depends on the interval of DATE you want your packages to be updated, you can choose. 
eg. If the latest update to a package is 2020.10, and you want to update only the packages after 2021.01, you set the 2021.01 date, and all the package under this date,
will be skipped, and then eliminated from your requirements.txt file.

The script will also create a csv file with all the packages-dates within the interval of date you set.

