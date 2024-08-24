# GameState-MM
 The code of XJTU_MM for [SoccerNet2024 GameState](https://github.com/SoccerNet/sn-gamestate)
# Our Method
The method is shown in the report of `Optimizing Jersey Number Recognition for Effective Player Tracking in the Game
State Reconstruction`
# Rank Results
The [leaderboard](https://eval.ai/web/challenges/challenge-page/2251/leaderboard/5565) of SoccerNet2024 GameState
| Rank | Participant team | GS-HOTA (↑) | GS-DetA (↑) | GS-AssA (↑) | Last submission at |
| --- | --- | --- | --- | --- | --- |
| 1 | Constructor tech | 55.82 | 41.67 | 74.86 | 2 months ago |
| 2 | UPCxMobius | 42.19 | 30.83 | 57.78 | 2 months ago |
| 3 | XJTU_MM (JNR) | 31.17 | 19.95 | 48.74 | 2 months ago |
| 4 | VIPLab | 29.59 | 17.82 | 49.18 | 2 months ago |
| 5 | playbox x NUSG | 23.27 | 9.59 | 56.45 | 2 months ago |
| 6 | Eidos | 22.32 | 10.53 | 47.37 | 3 months ago |
| 7 | Host_17134_Team (GSR-Baseline) | 22.26 | 10.67 | 46.46 | 5 months ago |
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

## Manual downloading of SoccerNet-gamestate
If you want to download the dataset manually, you can run the following snippet
after installing the soccernet package (`pip install SoccerNet`) : 

```
from SoccerNet.Downloader import SoccerNetDownloader
mySoccerNetDownloader = SoccerNetDownloader(LocalDirectory="data/SoccerNetGS")
mySoccerNetDownloader.downloadDataTask(task="gamestate-2024",
                                       split=["train", "valid", "test", "challenge"])
```

After running this code, please unzip the folders, so that the data looks like : 
```
data/
   SoccerNetGS/
      train/
      valid/
      test/
      challenge/
```

You can unzip them with the following command line : 
```bash
cd data/SoccerNetGS
unzip gamestate-2024/train.zip -d train
unzip gamestate-2024/valid.zip -d valid
unzip gamestate-2024/test.zip -d test
unzip gamestate-2024/challenge.zip -d challenge
cd ../..
```

**External dependencies**

- **DATA:** You will need to set up some variables before running the code in soccernet.yaml(sn_gamestate/configs/soccernet.yaml)
  - `data_dir`: the directory where you will store the different datasets (must be an absolute path !). If you opted for the automatic download option, `data_dir` should already point to the correct location.
- **MODEL:** Download the pretrained model weights [here](https://drive.google.com/drive/folders/1MmDkSHWJ1S-V9YcLMkFOjm3zo65UELjJ?usp=drive_link) and put the "pretrained_models" directory under the main project directory (i.e. "/path/to/tracklab/pretrained_models/reid").
- **YoloModel:** Dowlaod the pretrained YOLOv8 model weights [here](https://drive.google.com/drive/folders/1tsr27sBYAwHJjTk0ynpTVE7uNr73FuA8) and put the "yolov8x6.pt" file under the main project directory (i.e. "/path/to/tracklab/pretrained_models/yolo").

## Setup

```txt
cd sn-gamestate
python -m tracklab.main -cn soccernet
```
