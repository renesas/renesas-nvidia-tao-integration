### Introduction

This directory provides deployable application examples than can be quickly tested on board without requiring package installation. 

**Available application examples for quick deploy:**
| Use Case             | Model                                   | Dataset        | Devices Supported | Reference                                                                                              |
|----------------------|------------------------------------------|----------------|-------------------|--------------------------------------------------------------------------------------------------------|
| Image Classification | MobileNet v2                             | [Biodegradable](https://universe.roboflow.com/gkhang/classification-waste)  | EK-RA8D1          | [NGC Pretrained Classification](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/pretrained_classification) |
| Image Classification | MobileNet v2                             | [Biodegradable](https://universe.roboflow.com/gkhang/classification-waste)  | EK-RA8P1          | [NGC Pretrained Classification](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/pretrained_classification) |
| Image Classification | MobileNet v2                             | [Biodegradable](https://universe.roboflow.com/gkhang/classification-waste)  | AIK-RA8D1          | [NGC Pretrained Classification](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/pretrained_classification) |
| Image Classification | BYOM MobileNet v2                             | [TF-Flowers](https://www.tensorflow.org/datasets/catalog/tf_flowers)  | EK-RA8D1          | [TAO-BYOM](https://github.com/NVIDIA-AI-IOT/tao_byom_examples) |
| Image Classification | SegFormer-FAN hybrid Vision Transformer  | [Cats & Dogs](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/pretrained_segformer_nvimagenet)    | RZ/V2H            | [NGC Pretrained SegFormer](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/pretrained_segformer_nvimagenet) |
| Image Classification | SegFormer-FAN hybrid Vision Transformer  | [Cats & Dogs](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/pretrained_segformer_nvimagenet)    | RZ/V2L            | [NGC Pretrained SegFormer](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/pretrained_segformer_nvimagenet) |
| Object Detection     | DetectNetv2 (ResNet-18 backbone)        | [KITTI](https://www.cvlibs.net/datasets/kitti/eval_object.php?obj_benchmark=2d)          | RZ/V2H            | [TAO Pretrained DetectNet V2](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/pretrained_detectnet_v2)     |
| Object Detection     | DetectNetv2 (ResNet-18 backbone)        | [KITTI](https://www.cvlibs.net/datasets/kitti/eval_object.php?obj_benchmark=2d)          | RZ/V2L            | [TAO Pretrained DetectNet V2](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tao/models/pretrained_detectnet_v2)     |

> **Note:**  for Mobilenetv2 Biodegradable dataset, two compilers are supported, Tensorflow lite for microcontrollers and RUHMI AI compiler.