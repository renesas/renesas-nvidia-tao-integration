## Introduction

FAN Classification is a vision transformer-based image classification model provided by NVIDIA through TAO. It leverages the SegFormer architecture with a FAN (Fully Attentional Network) backbone, combining efficient hierarchical encoding with robust attentional processing. The Renesas AI Model Deployer integrates this model as part of an end-to-end proof of concept (PoC) pipeline to demonstrate image classification workflows. The model is exported to ONNX format for compatibility with the DRP-AI accelerator, and the GUI supports standard TAO features using YAML-based configuration files.

High level flow of Segformer pipeline:

![Renesas TAO GUI Segformer pipeline](../../docs/assets/Segformer_workflow.png)


## Before you start

### Hardware setup 

Ensure you have completed the board setup steps  for [RZ/V2L](../../board_bringup/rz_v2l/readme.md) and [RZ/V2H](../../board_bringup/rz_v2h/readme.md) in their respective READMEs.


### Software setup

#### Model download 
To train the model, the model should be downloaded from NVIDIA NGC [here](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/pretrained_segformer_nvimagenet).   

Please store the `.hdf5` model under `<projectdirectory>/utils/configs/Classification/segformer/pretrained_models/`. 

### Dataset download

For this demo, a simple cat/dog classification dataset will be used to demonstrate the operation of the pipeline. 
The dataset can be downloaded from [Kaggle](https://www.kaggle.com/datasets/tongpython/cat-and-dog/data).

The folder structure for the dataset should be as follows:
```
Dataset/
├── Cats/     # contains .jpg images of cats
│   ├── cat1.jpg
│   ├── cat2.jpg
│   └── ...
├── Dogs/     # contains .jpg images of dogs
│   ├── dog1.jpg
│   ├── dog2.jpg
│   └── ...
```

## GUI  

To launch the GUI, navigate to project directory:
```bash
./gui_start.sh
```

A simple end-to-end GIF can be viewed below:
![Segformer end-to-end](../../docs/assets/Segformer_workflow.gif)

For more detailed instructions, please visit [GUI directory](../../gui/readme.md).  


## Results 

The results of training after 300 epochs can be seen in table below:

|          | precision | recall | f1-score |
|----------|-----------|--------|----------|
| cats     | 0.93      | 0.86   | 0.9      |
| dogs     | 0.87      | 0.94   | 0.91     |
| accuracy | 0.9       | 0.9    | 0.9      |

### FAN-Segformer – Inference Benchmark

| Board   | Inference Time (ms) |
|------------|-------------------------|
| **RZ/V2L** | 11,000 – 13,000         |
| **RZ/V2H** | 4,500 – 5,500           |

AI inference on RZ/V boards for this model runs entirely on the CPU, as it is not currently supported by the DRP-AI accelerator. As a result, inference performance is significantly lower compared to models optimized for DRP-AI.

A snippet of inference on board via a pre-recorded slideshow is shown below:

![FAN-Segformer inference output on RZ/V2H](../../docs/assets/FAN_Segformer_result_1.png)


## Deploy without GUI

The GUI allows you to run inference via a connected USB camera to the MPU board. For demo purposes, the model was trained on static images which would lead to reduced accuracy via the USB camera, as such, it is possible to run inference on a video with a collection of training images. 
To achieve that, after export and deployment via GUI, a new folder will be created under `<project_directory>/assets/<Project_name>/<Project_name>`.
This folder will be the app that contains the embedded code and model object code that has been deployed on to the board. 
You will need to secure copy a set of images bundled into a video to the same directory onto the MPU `/home/root/<Project_name>`, from there you can then run the app with `VIDEO <name_of_video>` command. 
In general, this is the same method use as in [quick deploy](/quick_deploy/README.md). Following that method would allow you to vizualize your trained model performance on a test dataset of your choice in a video format. 
A video test dataset is provided in the `.tar.gz` files in quick deploy as well.


## Jupyter Notebook
Before using the Jupyter Notebooks, make sure the setup scripts have been executed.

1. Copy the `segformer` folder from `jupyter_notebooks` folder to the `assets` directory.
    ```
    cp -r jupyter_notebooks/segformer/ assets/
    ```
2. Open terminal in application root directory and run below command to start the Jupyter notebook server:
    ```
    ./jupyter-notebook
    ```
3. After server is up, navigate into the `assets/segformer` directory and start the jupyter notebook `Segformer_RZ_V2H_V2L.ipynb`
    take care that the selected jupyter kernel is SOS.
4. Select Jupyter notebook kernel as `SoS` and all the cells to be executed with `SoS` kernel.
5. Please take care of dataset as you would need to move it to the dataset directory and split it to `train:valid:test` manually.


