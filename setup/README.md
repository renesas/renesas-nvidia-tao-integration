## Getting started

To get started using **Renesas AI Model Deployer** and the **Jupyter notebooks**:

1. Please download `Renesas_AI_Model_Deployer_vX.Y.Z.tar` under assets in [releases](https://github.com/ES-Renesas/Renesas-Nvidia-TAO-Integration/releases/latest).

2.  Get your NVIDIA NGC API Key to access the NVIDIA TAO Toolkit:
    - Go to the [NGC sign-in page](https://ngc.nvidia.com/signin) and log in.
    - Click your username in the top-left corner.
    - Select **Setup** → **Generate API Key**.
    - Choose both services (NGC Catalog & Helm Chart Registry).
    - Click **Generate Key**, then copy and store it in a safe location.

3. Run the following shell scripts in project directory:

    Make your shell scripts in directory as executables:
    ```sh
    chmod ug+x *.sh
    ```

    Run the docker and GPU installer scripts:
    ```sh
    ./docker_gpu_install.sh
    ```

    Setting up TAO with required libraries:

    ```sh
    ./setup_tao_env.sh
    ```


    This should start the setup script and prompt you to enter you username sudo password, followed by an installation options tab. Ensure to select `TAO`, `TOOLs`, `Easy_GUI` and `Pre_image`.This will install the necessary dependancies to use the GUI and the Jupyter notebooks.  
    For Reneasas RZ/V, please install and setup AI SDK that includes DRP-AI TVM v2.5, steps 3-5 from [here](https://renesas-rz.github.io/rzv_ai_sdk/5.20/getting_started.html#step3).

5. To start Renesas AI Model deployer:
    ```sh
    ./gui_start.sh 
    ```
6.  For the Jupyter Notebooks, execute in Renesas TAO directory:
    ```sh
    ./jupyter-notebook
    ```

