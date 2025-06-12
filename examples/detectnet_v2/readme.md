## Introduction

DetectNet_v2 is a deep learning object detection model provided by NVIDIA through the TAO Toolkit. It uses a grid-based, anchor-free approach for detecting objects, making it ideal for real-time applications on embedded systems. Renesas AI Model Deployer leverages Detectnetv2 with ResNet-18 backbone and exports to ONNX without TensorRT plugin layers, ensuring compatibility with DRP-AI accelerator. The GUI provides access to pruning and quantized aware training (QAT) features from NVIDIA TAO along with `.yaml` file definition for Detectnetv2 hyperparameters.  

> **Note** : DetectNet v2 uses unstructured pruning in TAO to zero out low-magnitude weights. While the model architecture remains unchanged, retraining with sparsity encourages generalization and can improve accuracy.  

High level flow of DetectNet v2 pipeline:

![Renesas TAO GUI DetectNetv2 pipeline](../../docs/assets/Detectnet_v2_workflow.png)

> **Note** : To optimize the pipeline further, developers are encouraged to tune the various hyperparameters in `.yaml` file to achieve better performance.

## Before you start

### Hardware setup 

Ensure you have completed the board setup steps  for [RZ/V2L](../../board_bringup/rz_v2l/readme.md) and [RZ/V2H](../../board_bringup/rz_v2h/readme.md) in their respective READMEs.


### Software setup

#### Model download 
To train the model, download the pretrained weights from Nvidia NGC [here](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/pretrained_classification/files?version=resnet18).   
Please store the `.hdf5` model under `<projectdirectory>/utils/config/detection/pretrained_models/`. 

#### Dataset download

For this demo, a KITTI-formatted dataset is used to train the model with three classes: pedestrian, cyclist, and car. While the original KITTI dataset includes additional labels, the `.yaml` configuration file merges certain categories to simplify the task and focus on three primary object types. Bounding boxes are drawn for each of the three classes during inference.


- The dataset can be downloaded from [here](https://www.cvlibs.net/download.php?file=data_object_image_2.zip).
- The labels are available [here](https://www.cvlibs.net/download.php?file=data_object_label_2.zip).

For more details on the dataset, please visit the KITTI vision benchmark suite webpage [here](https://www.cvlibs.net/datasets/kitti/eval_object.php?obj_benchmark=2d).

The folder structure for the dataset follows KITTI convention:
```
KITTI/
├── images/         # contains image files (.png or .jpg)
│   ├── 000000.png
│   ├── 000001.png
│   └── ...
├── labels/         # contains label files (.txt) with class names and bounding boxes
│   ├── 000000.txt
│   ├── 000001.txt
│   └── ...
```

## GUI 


To launch the GUI, navigate to project directory:
```bash
./gui_start.sh
```

A simple end-to-end GIF can be viewed below:
![DetectNetv2 end-to-end](../../docs/assets/Detectnetv2_workflow.gif)

For more detailed instructions, please visit [GUI directory](../../gui/readme.md).  

## Results 

The results of training can be seen in table below:

| Model             | Model size | Accuracy (mAP) | Remarks                                                                 |
|------------------|------------|----------------|-------------------------------------------------------------------------|
| Trained model    | ~59 MB     | 38%            | Trained with 100 epochs on KITTI dataset (car, pedestrian, cyclist)    |
| Pruned model (Th: 0.5) | ~31 MB     | -              | No evaluation for pruned model                                          |
| Retrained model  | ~31 MB     | 40%            | Retrained the pruned model with 100 epochs on KITTI dataset            |
------------------

A snippet of inference on board via a pre-recorded slideshow is shown below:

![Detectnet V2 inference output](../../docs/assets/Detectnet_v2_result_1.png)


> **Note:** Currently an embedded bug has been found in the preprocessing that cause the bounding boxes to be drawn incorrectly, the following issue will be fixed in the next release of the tool.

## Jupyter Notebook

Before using the Jupyter Notebooks, make sure the setup scripts have been executed.

1. Copy the `detectnet_v2` folder from `jupyter_notebooks` folder to the `assets` directory.
    ```
    cp -r jupyter_notebooks/detectnet_v2/ assets/
    ```
2. Open terminal in application root directory and run below command to start the Jupyter notebook server:
    ```
    ./jupyter-notebook
    ```
3. After server is up, navigate into the `assets/detectnet_v2` directory and start the jupyter notebook `detectnet_v2_V2L_V2H.ipynb`
    take care that the selected jupyter kernel is SOS.
4. Select Jupyter notebook kernel as `SoS` and all the cells to be executed with `SoS` kernel.
5. Please take care of dataset  as you would need to move it to the dataset directory..


## Known Issues

- In the DetectNet_v2 demo, bounding boxes are drawn incorrectly and only for one class due to a post-processing issue during deployment. This will be fixed in the next release.

- For the DetectNet_v2 demo on RZ/V2L, inference speed is currently ~1–3 seconds as the first convolution layer runs on the CPU. A patch in the next release will offload this to DRP-AI, reducing inference time to ~220 ms.
