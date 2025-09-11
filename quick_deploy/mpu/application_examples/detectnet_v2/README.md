## Steps to execute the project Detectnetv2 on RZ/V2L or V2H

Details on this application example and performance metrics can be found [here](/examples/detectnet_v2/readme.md).  
Ensure you have followed the prerequisite [here](../../Readme.md)

### Quick Deploy Steps 

1. Unzip the folder and set execution rights.
	```
	tar -xJvf Detectnet_V2_<Board>.tar.xz && chmod -R +x Detectnet_V2_<Board>/
	```
2. Copy the Detectnet_V2_<Board> folder onto the board via secure copy
	```
	scp -r Detectnet_V2_<Board> root@<IP_address>:/home/root/
	```
3. Have two terminals open, one for ssh-ing into the board, the other to open the inference runner on host

	- SSH into the board via boards set IP address
		```
		ssh root@<IP_address>
		```
	-  Move to the Detectnet_V2_<Board> directory
		```
		cd Detectnet_V2_<Board>
		```  
	-  Start the application from the board using the provided video as input
		```
		./object_detector VIDEO Kitti_video.mp4
		```

	The result should be `attaching soc to port; binded; listened`.  

4. Open a new terminal in project directory while keeping terminal in 3 active.
	
	- In directory with venv, start the virtual enviroment:
		```
		source .venv/bin/activate
		```
	- Run the python file
		```
		python MPU_deploy.py <IP_address>
		```
	- A new video screen should pop displaying the inference.

