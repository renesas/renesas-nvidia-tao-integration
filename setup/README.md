## Getting started

To get started using **Renesas AI Model Deployer** and the **Jupyter notebooks**:

1. Please download `Renesas_AI_Model_Deployer_vX.Y.Z.tar` under assets in [releases](https://github.com/renesas/Renesas-Nvidia-TAO-Integration/releases/latest).

2. Expand the archive at the location for installation and execution/data storage:
    - The following is showing the steps for the home directory
        ```sh
        cd ~
        tar xf Renesas_AI_Model_Deployer_vX.Y.Z.tar*
        cd Renesas_AI_Model_Deployer  
        ```
    - In the directory is an additional README.md file with instructions and information (please take care)

4. Get your NVIDIA NGC API Key to access the NVIDIA TAO Toolkit:
    - Go to the [NGC sign-in page](https://ngc.nvidia.com/signin) and log in.
    - Click your username in the top-left corner.
    - Select **Setup** → **Generate API Key**.
    - Choose both services (NGC Catalog & Helm Chart Registry).
    - Click **Generate Key**, then **copy and store it in a safe location**.

5. Run the following shell scripts inside of the project directory:

    - Make the shell scripts executable: 
        ```
        sh chmod ug+x *.sh
        ```  
    - Setup Docker and NVIDIA GPU:
        ```
        ./docker_gpu_install.sh
        ```

    - Start the installation process: 
        ```
        sh ./setup_tao_env.sh
         ```  


    This should start the setup script and prompt you to enter you your username sudo password, followed by an installation options tab.Ensure to select **TAO**, **TOOLs**, **Easy_GUI** and **Pre_image**.This will install the necessary dependencies to use the GUI and the Jupyter notebooks.  
  
    During the first installation, the script will ask you for the  **NGC token**.  
    Please insert the **Token** you got from NVIDIA NGC registration process at 3.
    > **Notes:** Without the correct token the tool chain will not be functional.
  
### Quick method to download models

Download the required models from NVIDA by ngc for this the following call can be used:
     
   ```
   sh ./bin/ngc_model_download.sh --pull_resnet18 --pull_mobilenet_v2 --pull_fan_small_hybrid_nvimagenet 
   ```
   
   - The above line shows the download for all three currently supported AI models, please adapt the  CLI options to your model use requirement. Alternatively, you can manually download the models as explained in each example page.


### Board enviroment setup
Install the environment for DRP-AI TVM to support model translation for the RZ/V2L and RZ/V2H EVK
  
-   For Reneasas RZ/V2H, please install and setup **RZ/V2H AI SDK (V5.20)**, steps 3-5 from **[here](https://renesas-rz.github.io/rzv_ai_sdk/latest/getting_started.html#step3)**.

-   For Reneasas RZ/V2L, please install and setup **RZV2L AI SDK (V500)**,  steps 3-5 from **[here](https://renesas-rz.github.io/rzv_ai_sdk/latest/getting_started.html#step3)**.

> **Note:** Please visit the [board_bringup](../board_bringup/) page to learn more
  

### Jupyter notebook setup

For starting jupyter Notebooks we have a wrapper script, which sets the required environment.  
  
There are three jupyter_notebooks environments prepared. Please copy the one you want to use into the **assets**.  
In case it does not exist create it with following command:
```
mkdir assets 
```

Example:
```
cp -a ./jupyter_notebooks/<demo_name> assets
```   
Repalce `<demo_name>` with one of the following:
- detectnet_v2
- segformer
- mobilenet_v2

Please follow the steps described in the Read.me file for data set preparation (dataset directory)  
Execute in project directory:  
```
sh ./jupyter-notebook 
```  



