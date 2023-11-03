import requests
import veryfing_updating
import subprocess
import csv

with open("checking_dates.csv", "w", encoding='UTF8') as csvfile: # Write the data to a csv file
    writer = csv.writer(csvfile)
    writer.writerow(["Package", "Date"])

    if __name__ == "__main__":
        packages_lines = veryfing_updating.verifying("requirements.txt")


    for package in packages_lines:
        package = package.strip()
        r = requests.get(f"https://pypi.org/pypi/{package}/json")
        data = r.json()

        finding = [y for y in data.values()][-2] # Getting the [-2] list of values from the data requested

        date = [x['upload_time'] for x in finding if 'upload_time' in x][0][:10] # Get the first data in format (Y/M/D)
        print(f"{[package]} \n{date}")

    
        writer.writerow([package, date])


subprocess.run(["open", "checking_dates.csv"]) # Open the csv file when is done