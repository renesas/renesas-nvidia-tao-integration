## Getting started

To get started using **Renesas AI Model Deployer** and the **Jupyter notebooks**:

1. Please download `Renesas_AI_Model_Deployer_vX.Y.Z.tar` under assets in [releases](https://github.com/ES-Renesas/Renesas-Nvidia-TAO-Integration/releases/latest).

2. Expand the archive at the location for installation and execution/data storage:
    - The following is showing the steps for the home directory

        $ cd ~
        $ tar xf Renesas_AI_Model_Deployer_vX.Y.Z.tar*
        $ cd Renesas_AI_Model_Deployer  

    - In the directory is an additional README.md file with instructions and information (please take care)

3. Get your NVIDIA NGC API Key to access the NVIDIA TAO Toolkit:
    - Go to the [NGC sign-in page](https://ngc.nvidia.com/signin) and log in.
    - Click your username in the top-left corner.
    - Select **Setup** → **Generate API Key**.
    - Choose both services (NGC Catalog & Helm Chart Registry).
    - Click **Generate Key**, then **copy and store it in a safe location**.

4. Run the following shell scripts inside of the project directory:

    - Make the shell scripts executable: **$ chmod ug+x *.sh**
    - Start the installation process: **$ ./setup_tao_env.sh**


    This should start the setup script and prompt you to enter you your  
    username sudo password, followed by an installation options tab.  
    Ensure to select **TAO**, **TOOLs**, **Easy_GUI** and **Pre_image**.  
    This will install the necessary dependencies to use the GUI and the  
    Jupyter notebooks.  
  
    During the first installation the script will ask you for the N **GC token**.  
    Please insert the **Token** you got from **NVIDIA NGC registration process at 3**.
    > **Without the correct token the tool chain will not be functional.**
  
5. Download the required neural models from NVIDA by ngc for this the following call can be used:  
        $ ./bin/ngc_model_download.sh --pull_resnet18 --pull_mobilenet_v2] --pull_fan_small_hybrid_nvimagenet  
 
       - The above line shows he download for all three currently supported ai models, please adapt the  
         cli options to your model use requirement.

6. Install the environment for DRP-AI TVM to support model translation for the RZV2L and RZV2H EVK
  
    For Reneasas RZ/V2H, please install and setup **RZV2H AI SDK (V520)**,  
    steps 3-5 from **[here](https://renesas-rz.github.io/rzv_ai_sdk/5.20/getting_started.html#step3)**.
  
    For Reneasas RZ/V2L, please install and setup **RZV2L AI SDK (V500)**,  
    steps 3-5 from **[here](https://renesas-rz.github.io/rzv_ai_sdk/5.20/getting_started.html#step3)**.
  

7. To start Renesas AI Model deployer GUI run the following command:  

       Execute in Renesas TAO directory: **$ ./gui_start.sh**  
  
8.  For starting jupyter Notebooks we have a wrapper script, which sets the required environment.  
  
    - there are three jupyter_notebooks environments prepared  
      please copy the one you want to use into the **assets**  
      In case it does not exist create it with **$ mkdir assets**  
      Example: **cp -a ./jupyter_notebooks/detectnet_v2 assets**  
  
        - detectnet_v2
        - segformer
        - mobilenet_v2

    - Please follow the steps described in the Read.me file for data set preparation (dataset directory)  

    - Execute in Renesas TAO directory: **$ ./jupyter-notebook**  

***Please check the quick start guide for further information***

