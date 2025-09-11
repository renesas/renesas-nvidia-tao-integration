### Quick Deploy (MPU) 

These are **prebuilt application examples** for RZ/V2L and RZ/V2H with viewer displayed over host.  

### Prerequisites

**Board**
- RZ/V2L or RZ/V2H with DRP-AI TVM runtime image
- SSH enabled; reachable over the network

**Host (Linux Ubuntu 20.04/22.04)**
- Python 3.9+
- `ssh` and `scp`


**Install minimal Python env:**
```bash
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install -y python3.9 python3.9-venv python3.9-dev openssh-client
python3.9 -m venv .venv && source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```
