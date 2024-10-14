import cv2
import numpy as np
from Visual import *

class ComputerVision():
    def __init__(self, map):
        self.map = map
        self.map_data = np.array(self.map, dtype=np.uint8)
        self.vis  = VisualTool()
        self.vis.showJetMap("",self.map_data)
        
        
    def harris_corner(self, block_size, ksize, k):
        # Gaussian Blur 적용
        self.map_data = cv2.GaussianBlur(self.map_data, (5, 5), sigmaX=2, sigmaY=2)
        self.vis.showJetMap("", self.map_data)
        
        # Harris Corner 적용
        self.result = cv2.cornerHarris(self.map_data, block_size, ksize, k)
        self.vis.showJetMap("",np.array(self.result))
        
        # 값 처리
        threshold = np.percentile(self.result, 98)
        print(threshold)
        
        max_val = np.max(self.result)
        binary_image = np.zeros_like(self.result, dtype=np.uint8)
        
        binary_image[self.result > threshold] = 1 
        dst = np.where(binary_image == 1)
        
        return list(zip(dst[0],dst[1]))

    def canny_edge(self, thres1, thres2):
        self.map_data = cv2.GaussianBlur(self.map_data, (3, 3), sigmaX=2)
        self.vis.showJetMap("", self.map_data)
        self.result = cv2.Canny(self.map_data, thres1, thres2)
        max_val = np.max(self.result)
        binary_image = np.zeros_like(self.result, dtype=np.uint8)
        binary_image[self.result == max_val] = 1 
        dst = np.where(binary_image == 1)
        
        return list(zip(dst[0],dst[1]))


    def edge_detector(self):
        #행방향 변환작업
        row_converted_data = []
        input_data = self.map
        for i in range(len(input_data)): #세로축 반복
                row_data = []
                for j in range(len(input_data[0])): #가로축 반복
                        if input_data[i][j] == 1:  #기준셀이 1일때,
                            if (input_data[i][j-1] == 0) & (input_data[i][j+1] == 0): 
                                    row_data.append(1) #후미,선두=0 일때, 1 추가
                            elif (input_data[i][j-1] == 1) & (input_data[i][j+1] == 0):
                                    row_data.append(1) #후미=1,선두=0 일때, 1 추가
                            elif (input_data[i][j-1] == 0) & (input_data[i][j+1] == 1):
                                    row_data.append(1) #후미=0,선두=1 일때, 1 추가
                            else:
                                    row_data.append(0) #후미,선두=1 일때, 0 추가
                        else:
                            row_data.append(0)        
                row_data.append(0)
                row_converted_data.append(row_data)
        
    #열방향 변환작업
        column_converted_data = []        
        for j in range(len(input_data)):
                column_data = []
                for i in range(len(input_data[0])):
                        if input_data[j][i] == 1:
                                if (input_data[j-1][i] == 0) & (input_data[j+1][i] == 0):
                                        column_data.append(1)
                                elif (input_data[j-1][i] == 1) & (input_data[j+1][i] == 0):
                                        column_data.append(1)
                                elif (input_data[j-1][i] == 0) & (input_data[j+1][i] == 1):
                                        column_data.append(1)
                                else:
                                        column_data.append(0)
                        else:
                                column_data.append(0)       
                column_converted_data.append(column_data)  
                    
        
    #행변환 배열과 열변환 배열 통합
        converted_data = []
        for i in range(len(row_converted_data)):
                raw_data=[]
                for j in range(len(column_converted_data[0])):
                    if (row_converted_data[i][j] ==1) or (column_converted_data[i][j]==1):
                        raw_data.append(1)
                    else:
                        raw_data.append(0)
                converted_data.append(raw_data)
        
        return converted_data

