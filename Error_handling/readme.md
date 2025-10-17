## Error handling 

At times, the GUI or Jupyter notebook may cause some errors, these are some that have been found during testing.

### (I) GPU Driver and CUDA Version Check

Before starting the application, ensure that the NVIDIA driver and CUDA versions are appropriate by running the following commands in the Ubuntu terminal:

``` sh
nvidia-smi
nvcc --version
```
###  (II) Backend application running on GPU 

Before running the application, ensure that no other backend applications are occupying the GPU. Sometimes, lingering processes can cause the GPU to appear "busy" or lead to NVML-related errors.

> 🔄 Tip: It's recommended to restart the system to clear any stuck processes and ensure the GPU is available for training or inference.


### (III) GUI not starting due to port conflict

If run ./gui_start.sh and immediately the Renesas AI Model Deployer terminal opens and closes, follow these steps to kill the process using port 8000:

1. Identify the Process-ID (PID) using the command:
    ``` sh
    sudo lsof -i :8000
    ```

2. Gracefully or forcefully kill the identified PID:
    ``` sh
    sudo kill <PID>  # Graceful kill
    sudo kill -9 <PID>  # Force kill
    ```
3. Verify if port 8000 is free:
    ``` sh
    sudo lsof -i :8000
    ```

### (IV) NGC Access Errors
In case NGC access errors are reported, rerun the `./setup_tao_env.sh` script with the `-f` option:    

```sh 
./setup_tao_env.sh -f
```

### (V) Model deployment on MPU board not executing

During installation procedure, if `libtvm_runtime.so` runtime library is not moved under root filesystem, execution would not happen. Please ensure its available and should be in the following structure. 
```
usr/
└── lib64/
    └── libtvm_runtime.so
home/
└── root/
```

1. If `libtvm_runtime.so` is missing, start your AI SDK docker container on host PC.

    ``` 
    docker start -i <container_name> 
    i.e., <rzv2l_ai_sdk_container> 
    ```
2. Confirm that it exists by naviagating to directory to your respective MPU `<V2L> or <V2H>` and `ls`:

    ```
    cd /drp-ai_tvm/obj/build_runtime/<V2L>
    ```
3. Copy `libtvm_runtime.so` to host machine, open a new terminal and run the following:

    ```
    docker cp <container_name>:/drp-ai_tvm/obj/build_runtime/<V2L>/libtvm_runtime.so 
    ```
    This will copy `libtvm_runtime.so` to your current directory on the host.

4. Copy `libtvm_runtime.so` to the Board
    ```
    scp libtvm_runtime.so root@<IP Address>:/usr/lib64/
    ```

### (VI) GUI works but TAO functionalities dont operate

During data curation phase, if you try to execute  `analyze` and no graphs pop-up.  
This is may be an issue with NVIDIA TAO installation, to verify, in terminal:
```
docker images
```
If, the following image not visible `nvcr.io/nvidia/tao/tao-toolit v5.5.0-data-services`, then please re-run `./setup_tao_env.sh` and insure in installation options, `Pre_image` has been selected. 

### (VII) At deployment stage, image not displayed

For MPUs, once you input the IP address and successfully detect the board, if you press deploy and see `WebSocket is fetching data please wait...` and do not see the image being displayed, please confirm that your H/W is connected correctly with a USB camera. 


### (VIII) Pre-trained model paths is empty
In training page, once you select your model, if the `Pre Trained Model Paths` does not provide a selection, you may have either missed downloading the model or moved it into an incorrect directory. Review the example `Readme.md` page to understand where and how to leverage a pretrained model.

### (IX) Training fails error
Care should be taken choosing the batch size, an out of memory can occur causing the training to fail. 
Please reduce the batch size and try again.  
From testing, batch size of 4 did not fail on all systems. 

### (X) V2H DetectNetV2 inference is slow
Please ensure that you are not using the AI SDK v5.20 as is. As described in [V2H_board_bringup](../board_bringup/rz_v2h/readme.md), replacing the DockerFile and DRP-AI Translator file.

### (XI) SSH permission denied  
On V2L/V2H, sometimes an error of permission denied may pop up when you try to SSH into the board. 
```sh
ssh root@<IP Address> ls
ssh-keygen -f "<Path>/.ssh/known_hosts" -R "<IP address>"
ssh root@<IP Address> ls
```
### (XII) Accuracy during training/evaluation is low
The accuracy being low can be due to several reasons, a few ways to solve it:
- Train the model for more number of epochs, if accuracy goes up with every epochs, train till stagnation
- If increase in epochs does not help in accuracy, add more high quality data
- If adding more data and expanding number of epochs do not improve accuracy, vary the hyperparamter in `.yaml` file, this requires higher level expertise, so we recommend to transition to the Jupyter notebooks.
