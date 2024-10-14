import os
import sys
import time
import importlib
import numpy as np
import json
from cpuinfo import get_cpu_info
from Visual import *
from cv_detector import *
from SensorModule.Sensor import *

# 사용할 알고리즘



class Main:
    def __init__(self, map_name, COV, GEN):
        self.coverage = COV

        # 동적으로 MAP 모듈 임포트
        map_module_path = f"__MAPS__.{map_name}"
        map_module = importlib.import_module(map_module_path)
        self.MAP = np.array(getattr(map_module, "MAP"))

        self.GEN = GEN
        self.vis = VisualTool()
        self.map_name = map_name



    def run(self):
        start = time.time()
        sensor = Sensor(self.MAP)

        # 최외곽 지점 추출 및 배치
        corner_position = ComputerVision(self.MAP).harris_corner(2, 3, 0.01)
        #corner_position = ComputerVision(self.MAP).canny_edge(10000,20000)
        print(np.array(corner_position))
        for i in corner_position:
            sensor.deploy(i, self.coverage)
        self.MAP = sensor.result()



        # 결과 처리
        dst = corner_position
        dst = [(y, x) for x, y in dst] 
        runtime = time.time() - start
        num_sensor = len(dst)

        # 결과 프롬프트 출력
        print(dst)
        print(f"경과시간(초) : {runtime:.4f}")
        print(f"총 센서 수 : {num_sensor}")

        # 센서 배치 형태 시각화
        self.MAP = sensor.result()
        self.vis.showJetMap("RESULT", self.MAP)

        return dst


if __name__ == "__main__":
    for i in range(1):
        #map_name = "truncated_140by140"
        map_name = "site2_uav"
        algorithm = Main(map_name, 1, 1).run()
        
        map_name = "site3_uav"
        algorithm = Main(map_name, 1, 1).run()
        
        map_name = "site4_uav"
        algorithm = Main(map_name, 1, 1).run()
        
    """for i in range(1):
        map_name = "truncated_140by140"
        algorithm = Main(map_name, 1, 1).run()

        map_name = "stair_140by140"
        algorithm = Main(map_name, 1, 1).run()
        
        map_name = "rectangle_140by140"
        algorithm = Main(map_name, 1, 1).run()"""