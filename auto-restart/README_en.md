# Mangata-AVS Operator Auto Restart

This script restarts the container if the Mangata operator raises the `err: connection is shut down` error. Consequences are at your own responsibility. It is running on my server. Check the `container_name` variable if you changed the default name of the container before starting the script (`docker ps` to check container name).

**Note:**

* This script requires the user to be added to the `docker` user group.
* The script may fail if you don't have the required permissions.

## Installation
```bash
## Cloning repository
git clone https://github.com/walter-s0bch4k/mangata-AVS-with-auto-restart.git
# Change directory to downloaded repository
cd mangata-AVS-with-auto-restart
# If you downloaded the repo from a different location, please navigate to the folder containing the
# `requirements.txt` and `restart_container_if_err.py` files by checking the file names in the download location.
# To verify you are in the correct location, run the following command:
ls -al
# You should see the `requirements.txt` and `restart_container_if_err.py` files in the output of the command.

## Installing pip 
# Get pip installation script
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
# Execute script to install, you might need to replace python3 to python etc.
sudo python3 get-pip.py

## Docker settings
# Create docker user group
sudo groupadd docker
# Add current user to docker group
sudo usermod -aG docker $USER

## Executing the script
# Install required packages
pip install -r requirements.txt
# Execute using nohup to make it run in background even if you disconnect
nohup python3 -u restart_container_if_err.py > logs.txt &
# Checking logs. Please read content carefully, there should be no errors. 
cat logs.txt

## !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
## Kill the process if you manually restart container or close it!
# Get PID by
ps -aux | grep restart_container_if_err.py
# Then kill process
kill -9 <PID>
```