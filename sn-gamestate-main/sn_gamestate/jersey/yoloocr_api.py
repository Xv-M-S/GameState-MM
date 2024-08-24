import pandas as pd
import torch
import numpy as np
from mmocr.apis import MMOCRInferencer
# from mmengine.infer.infer import BaseInferencer
from mmocr.apis import TextDetInferencer, TextRecInferencer
from mmocr.utils import ConfigType, bbox2poly, crop_img, poly2bbox
import logging

from tracklab.utils.collate import default_collate, Unbatchable
from tracklab.pipeline.detectionlevel_module import DetectionLevelModule

from multiprocessing import Pool
from ultralytics import YOLO
log = logging.getLogger(__name__)


class YOLOOCR(DetectionLevelModule):
    input_columns = ["bbox_ltwh"]
    output_columns = ["jersey_number_detection", "jersey_number_confidence"]
    collate_fn = default_collate

    def __init__(self, batch_size, device, tracking_dataset=None):
        super().__init__(batch_size=batch_size)
        # self.recognition_model = YOLO('/home/sxm/JNR_Ensemble/ultralytics-main/sxm-workspace/test/soccerNet_test/models/AugSocv3PaperRoboMQY.pt')
        # self.detect_model = YOLO('/home/sxm/JNR_Ensemble/ultralytics-main/sxm-workspace/test/soccerNet_test/models/DetectPaperRoboSvhnSocv3MQY_n.pt')
        self.recognition_model = YOLO('/home/sxm/JNR_Ensemble/ultralytics-main/sxm-workspace/train/runs/detect/train19/weights/best.pt')
        self.detect_model = YOLO('/home/sxm/JNR_Ensemble/ultralytics-main/sxm-workspace/train/runs/detect/train20/weights/best.pt')
        self.batch_size = batch_size


    def no_jersey_number(self):
        return None, 0

    @torch.no_grad()
    def preprocess(self, image, detection: pd.Series, metadata: pd.Series):
        l, t, r, b = detection.bbox.ltrb(
            image_shape=(image.shape[1], image.shape[0]), rounded=True
        )
        crop = image[t:b, l:r]
        # print('crop shape', crop.shape)
        if crop.shape[0] == 0 or crop.shape[1] == 0:
            crop = np.zeros((10, 10, 3), dtype=np.uint8)
        # print('crop shape', crop.shape)
        crop = Unbatchable([crop])
        batch = {
            "img": crop,
        }

        return batch
    

    @torch.no_grad()
    def process(self, batch, detections: pd.DataFrame, metadatas: pd.DataFrame):
        jersey_number_detection = []
        jersey_number_confidence = []
        images_np = [img.cpu().numpy() for img in batch['img']]
        del batch['img']


        for img in images_np:
            rec_result = self.recognition_model(source=img,task="detect",imgsz=256,device=4)
            det_result = self.detect_model(source=img,task="detect",imgsz=256,conf=0.7,device=4) 
            is_exists_number = det_result[0].boxes.cls.cpu().numpy()
            detect_cls = ""
            if len(is_exists_number)==1:
                detect_cls = str(int(is_exists_number[0]))
            if detect_cls == "1":
                # 不存在球号
                jersey_number_detection.append(None)
                jersey_number_confidence.append(0)
                continue
            jn = rec_result[0].boxes.cls.cpu().numpy()
            conf = rec_result[0].boxes.conf.cpu().numpy()
            if len(jn)==1:
                jn = str(int(jn[0]))
            else:
                jn = None
            if len(conf)==1:
                conf = conf[0]
            else:
                conf = 0
            jersey_number_detection.append(jn)
            jersey_number_confidence.append(conf)

        detections['jersey_number_detection'] = jersey_number_detection
        detections['jersey_number_confidence'] = jersey_number_confidence

        return detections

    
