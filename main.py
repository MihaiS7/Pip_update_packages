import requests
import reading_writing
import subprocess
import csv
import datetime
import os

def writing_file(file): 

    with open(file, "w", encoding='UTF8') as csvfile: # Write the data to a csv file
        writer = csv.writer(csvfile)
        writer.writerow(["Package", "Date"]) # Header of the file
        result = {}

        for packages in packages_lines[2:]:
            package = packages[0]
            r = requests.get(f"https://pypi.org/pypi/{package}/json")
            data = r.json()

            finding = [y for y in data.values()][-2] # Getting the [-2] list of values from the data requested

            date = [x['upload_time'] for x in finding if 'upload_time' in x][0][:10] # Get the first data in format (Y/M/D)
            sorting_date = datetime.datetime.strptime(date,"%Y-%m-%d").strftime("%Y %m")
            result[package]=sorting_date # Creating the dict - package-key, sorting_date-value
            sorted_dict = sorted(result.items(), key=lambda item: item[1]) # Sorting the values

        for package_date in sorted_dict:
            pack, date_format = (package_date)
            # print(f"This is the pack: {pack}, this is the date_format: {date_format}")
            '''
            IF 'you_set_date'***(the date you want to be the 'oldest package')*** is less or equal with 'date_format'***(the date of the current package)***
                    is  less or equal with ***(the date of today)***
            '''
            
            if you_set_date('2022-01') <= date_format <= today_year_month():
                # subprocess.run(['pip', 'uninstall', pack], capture_output=True, text=True)
                result = subprocess.run(['pip', 'install', '--no-cache-dir', '--upgrade' ,pack], capture_output=True, text=True)
                writer.writerow([pack, date_format])
                # print(result.stdout)
            else:
                #Delete package
                try:
                    if packages_lines:
                        packages_lines.pop(0)
                        # print(f"Package deleted: {pack} because of the date: {date_format}")
                except ValueError as e:
                    print(f"I encountered an error: {e}")


def today_year_month():
    today = datetime.datetime.today().strftime("%Y %m")
    return today

def you_set_date(year_month):
    return datetime.datetime.strptime(year_month, "%Y-%m").strftime("%Y %m")

def getting_input_file(input_file):
    os.system(f"pip3 list --outdated --format=columns > {input_file}")
    return input_file

if __name__ == "__main__":
    print("The script begun...")  
    input_file = getting_input_file("requirements.txt")
    packages_lines = reading_writing.verifying(input_file)
    print('\033[1m'+"The script currently is reading the input file!\nPlease be patient!"+'\033[0m')
    # packages_lines = list(map(str.strip, packages_line)) # Eliminate the ( \n ) from the list
    # you_set_date('2022-01') # You set the date here
    writing_file("checking_dates.csv")
    
    print('\033[1m'+"\nThe script finished to read the file")
    print("\nNow we are writing the output file")
    print(f"\nToday date: {today_year_month()}"+'\033[0m')
    # new_lines_package = '\n'.join(packages_lines)
    # pip_install = [f'\npip install {element}' for element in packages_lines] # Was trying a feature
    # print(f"Before pip_install: {packages_lines}")
    # pip_install = '\n'.join()
    
    # reading_writing.writing("requirements.txt", pip_install)

print("The script is done!")
print("Opening the csv file...")
subprocess.run( ["open", "checking_dates.csv"] ) # Open the csv file when is done


                





