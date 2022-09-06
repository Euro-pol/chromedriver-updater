import subprocess
import requests
import os

print("Checking if there is any ChromeDriver exists...")

if (os.path.isfile("chromedriver.exe")):
    print("ChromeDriver exists, removing...")
    try:
        os.remove("chromedriver.exe")
    except PermissionError:
        print("Please restart the program as admin or close any running ChromeDriver(s).")
        exit()    
else:
    print("ChromeDriver does not exist, skipping...")    

output = subprocess.run(["powershell", '(Get-Item -path "C:\Program Files\Google\Chrome\Application\chrome.exe").VersionInfo.ProductVersion'], capture_output=True).stdout.decode()
version = output.split('.')[0]
driverver = requests.get(f"https://chromedriver.storage.googleapis.com/LATEST_RELEASE_{version}").text
print(f"Downloading ChromeDriver Version {driverver}...")
driverfile = requests.get(f"https://chromedriver.storage.googleapis.com/{driverver}/chromedriver_win32.zip")
with open("chromedriver.zip", "wb") as f:
    f.write(driverfile.content)
print("Downloaded ChromeDriver! Extracting...")
subprocess.run(["powershell", "Expand-Archive -Path chromedriver.zip -DestinationPath ."])
print("Extracted ChromeDriver! Deleting zip file...")
subprocess.run(["powershell", "Remove-Item -Path chromedriver.zip"])
print("Done.")