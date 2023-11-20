# Generalized Surface Loss

Code for implementing and testing the Generalized Surface Loss (GSL).

[//]: # (Please cite the following if you use this loss function or code for your own work:)

[//]: # (> [A. Celaya, B. Riviere, D. Fuentes. "A Generalized Surface Loss for Reducing the Hausdorff Distance in )

[//]: # (> Medical Imaging Segmentation," arXiv preprint arXiv:2302.03868, 2023.]&#40;https://arxiv.org/abs/2302.03868&#41;)

[//]: # (> )

[//]: # (> [A. Celaya et al., "PocketNet: A Smaller Neural Network For Medical Image Analysis," in )

[//]: # (> IEEE Transactions on Medical Imaging, doi: 10.1109/TMI.2022.3224873.]&#40;https://ieeexplore.ieee.org/document/9964128&#41;)

### Data

MICCAI Liver and Tumor Segmentation Challenge 2017 dataset (LiTS) - <https://competitions.codalab.org/competitions/17094#learn_the_details-overview>

MICCAI Brain Tumor Segmentation Challenge 2020 dataset (BraTS) - <https://www.med.upenn.edu/cbica/brats2020/registration.html>

### Usage

This code is based on the [Medical Imaging Segmentation Toolkit (MIST)](https://github.com/aecelaya/MIST/) framework. 
Please see its documentation for setup details.

To run our experiments, use the following commands:

```
python run_experiments_lits.py
```
and
```
python run_experiment_brats.py
```
