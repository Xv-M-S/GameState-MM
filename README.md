# GameState-MM
 The code of XJTU_MM for SoccerNet2024 GameState
# Installation guide
## Clone the repository
```txt
git clone https://github.com/Xv-M-S/GameState-MM.git
```
## Manage the environment
**Create and activate a new environment**
```txt
conda create -n tracklab pip python=3.10 pytorch==1.13.1 torchvision==0.14.1 pytorch-cuda=11.7 -c pytorch -c nvidia -y
conda activate tracklab
```
**Install the dependencies for tracklab**
```txt
cd tracklab/plugins/track
pip install -e . -i https://pypi.org/simple  # note：使用pip的默认源安装

cd tracklab
pip install -e . -i https://pypi.org/simple  # note 使用pip默认源安装
mim install mmcv==2.0.1
```
**Install the dependencies for sn-gamestate**
```txt
cd sn-gamestate/plugins/calibration
pip install -e . -i https://pypi.org/simple  # note 使用pip默认源安装

cd sn-gamestate
pip install -e . -i https://pypi.org/simple  # note 使用pip默认源安装
```

**External dependencies**

- **DATA:** Get the **SoccerNet Tracking** dataset [here](https://github.com/SoccerNet/sn-tracking), rename the root folder as "SoccerNetMOT" and put it under the global dataset directory (specified under the `data_dir` config as explained below). Otherwise, you can modify the `dataset_path` config in [soccernet_mot.yaml](tracklab/configs/dataset/soccernet_mot.yaml) with your custom SoccerNet dataset directory.
- **MODEL:** Download the pretrained model weights [here](https://drive.google.com/drive/folders/1MmDkSHWJ1S-V9YcLMkFOjm3zo65UELjJ?usp=drive_link) and put the "pretrained_models" directory under the main project directory (i.e. "/path/to/tracklab/pretrained_models").

## Setup

```txt
cd sn-gamestate
python -m tracklab.main -cn soccernet
```
