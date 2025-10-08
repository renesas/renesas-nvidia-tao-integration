## Steps to execute the project FAN-Segformer RZ/V2L or V2H

Details on this application example and performance metrics can be found [here](/examples/segformer/readme.md).  
Ensure you have followed the prerequisite [here](../../Readme.md)

### Quick Deploy Steps

0. Setup Variables (on Host PC)
	```
	BOARD=V2L        # or V2H
	IP=192.168.1.12  # replace with your board IP
	```
1. Unzip the folder and set execution rights.
	```
	tar -xJvf FAN_Segformer_${BOARD}.tar.xz && chmod -R +x FAN_Segformer_${BOARD}/
	```
2. Copy the FAN_Segformer_<Board> folder onto the board via secure copy
	```
	scp -r FAN_Segformer_${BOARD} root@${IP}:/home/root/
	```
3. Have two terminals open, one for ssh-ing into the board, the other to open the inference runner on host

	- SSH into the board via boards set IP address
		```
		ssh root@${IP}
		```
	-  Move to the FAN_Segformer_<Board> directory
		```
		cd FAN_Segformer_${BOARD}
		```  
	-  Start the application from the board using the provided video as input
		```
		./image_classifier VIDEO dog_cat_dataset_long.mp4
		```

The result should be `attaching soc to port; binded; listened`.  

4. Open a new terminal in project directory while keeping terminal in 3 active. Do note you need to set `IP variable` again.

	- In directory with venv, start the virtual enviroment:
		```
		source .venv/bin/activate
		```
	- Run the python file
		```
		python MPU_deploy.py ${IP}
		```
	- A new video screen should pop displaying the inference.
