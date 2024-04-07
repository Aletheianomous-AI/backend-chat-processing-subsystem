# Backend Chat Processing Subsystem
This repo contains files that are responsible for the chat processing subsystem, as defined in the SDD. 

# Pre-requisites
You need to ensure that Docker is installed by following the [installation instructions]

# Setup
## Using Docker
1. Using a terminal on your pc, make sure the root folder of this repo is the current directory.
2. Type `sudo docker build -t aletheianomous_ai_backend_docker .`.
3. Type `sudo docker run -it -e "$(pwd)"/:code` -p 5000:5000 -p 8888:8888 --gpus all bash
4. To exit, type `logout`.
5. To re-enter the environment, type `sudo docker container ps -a` to view the container id that has been created, then type `sudo docker exec -it <container_id> bash`.

## Using VirtualEnv
1. Using a terminal on your pc, make sure the root folder of this repo is the current directory.
2. Type `python3 -m venv .env`.
3. Activate the environment on Windows Powershell by typing `.env\Scripts\Activate.ps1`. On Linux, type `source .env/bin/activate`.
4. Install the requirements by typing `python3 -m pip install -r requirements.txt`.

# Running Jupyterlab 
To run Jupyter Lab, type `jupyter lab --ip 0.0.0.0 --no-browser --allow-root`. Copy the URL into your computer's browser.

# Running Flask for Handling REST API calls
To run Flask, type `flask run --host 0.0.0.0`.
