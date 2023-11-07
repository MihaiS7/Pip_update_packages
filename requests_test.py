import requests
import veryfing_updating
import subprocess
import csv
import datetime
        

if __name__ == "__main__":
    packages_lines = veryfing_updating.verifying("requirements.txt")
def writing_file(file):
    with open(file, "w", encoding='UTF8') as csvfile: # Write the data to a csv file
        writer = csv.writer(csvfile)
        writer.writerow(["Package", "Date"]) # Header of the file
        result = {}
        for package in packages_lines:
            package = package.strip() # Strip the \n
            r = requests.get(f"https://pypi.org/pypi/{package}/json")
            data = r.json()

            finding = [y for y in data.values()][-2] # Getting the [-2] list of values from the data requested

            date = [x['upload_time'] for x in finding if 'upload_time' in x][0][:10] # Get the first data in format (Y/M/D)
            # print(f"{package} : {date}")
            sorting_date = datetime.datetime.strptime(date,"%Y-%m-%d").strftime("%Y %m")
            result[package]=date # Creating the dict - package-key, sorting_date-value
            sorted_dict = sorted(result.items(), key=lambda item: item[1]) # Sorting the values
    # print(sorted_dict)
        for package_date in sorted_dict:
            pack, da = (package_date)

            if sorting_date <= today_year_month():
                print(pack, da)
                writer.writerow([pack, da])

def today_year_month():
    today = datetime.datetime.today().strftime("%Y %m")
    return today

writing_file("checking_dates.csv")
print(today_date())

# subprocess.run(["open", "checking_dates.csv"]) # Open the csv file when is done


                





