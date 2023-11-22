import requests
import veryfing_updating
import subprocess
import csv
import datetime


def writing_file(file):
    with open(file, "w", encoding='UTF8') as csvfile: # Write the data to a csv file
        writer = csv.writer(csvfile)
        writer.writerow(["Package", "Date"]) # Header of the file
        result = {}
        for package in packages_lines:
            print(f"This is the package: {package}")
            r = requests.get(f"https://pypi.org/pypi/{package}/json")
            data = r.json()

            finding = [y for y in data.values()][-2] # Getting the [-2] list of values from the data requested

            date = [x['upload_time'] for x in finding if 'upload_time' in x][0][:10] # Get the first data in format (Y/M/D)
            # print(f"{package} : {date}")
            sorting_date = datetime.datetime.strptime(date,"%Y-%m-%d").strftime("%Y %m")
            result[package]=sorting_date # Creating the dict - package-key, sorting_date-value
            sorted_dict = sorted(result.items(), key=lambda item: item[1]) # Sorting the values

    # print(sorted_dict)
        for package_date in sorted_dict:
            pack, date_format = (package_date)
            
            '''
            IF ***(the date you want to be the 'oldest package')*** is less or equal with ***(the date of the current package)***
                    is  less or equal with ***(the date of today)***
            '''
            
            if you_set_date('2022-01') <= date_format <= today_year_month():
                print(pack, date_format)
                writer.writerow([pack, date_format])
            else:
                #Delete package
                try:
                    if packages_lines:
                        packages_lines.pop(0)
                        print(f"Package deleted: {pack}")
                except ValueError as e:
                    print(f"I encountered an error: {e}")



def today_year_month():
    today = datetime.datetime.today().strftime("%Y %m")
    return today

def you_set_date(year_month):
    return datetime.datetime.strptime(year_month, "%Y-%m").strftime("%Y %m")


if __name__ == "__main__":
    print("The script started!!!")  
    packages_lines = veryfing_updating.verifying("requirements.txt")
    packages_lines = list(map(str.strip, packages_lines)) # Eliminate the ( \n ) from the list
    # print(packages_lines)
    # you_set_date('2022-01')
    writing_file("checking_dates.csv")
    print(f"Today date: {today_year_month()}")
    new_lines_package = '\n'.join(packages_lines)
    veryfing_updating.writing("requirements.txt", new_lines_package)

# subprocess.run(["open", "checking_dates.csv"]) # Open the csv file when is done


                





