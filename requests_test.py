import requests
import veryfing_updating
import subprocess
import csv

if __name__ == "__main__":
    packages_lines = veryfing_updating.verifying("requirements.txt")


for package in packages_lines:
    package = package.strip()
    print(package)
    r = requests.get(f"https://pypi.org/pypi/{package}/json")
    data = r.json()

    finding = [y for y in data.values()][-2]

    date = [x['upload_time'] for x in finding if 'upload_time' in x][0]
    print(date[:10])
    print(f"{package} \n{date}")

    with open("checking_dates.csv", "w", encoding='UTF8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Package", "Date"])
        writer.writerows([date])


subprocess.run(["open", "checking_dates.csv"])