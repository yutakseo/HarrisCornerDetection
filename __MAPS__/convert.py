import numpy as np
from site2_uav import MAP

# 원본 맵 데이터


# 원본 맵을 NumPy 배열로 변환
original_array = np.array(MAP)

# 원본 맵의 차원 가져오기
rows, cols = original_array.shape

# 패딩이 추가된 새로운 배열 생성 (크기는 (rows+4) x (cols+4))
padded_array = np.zeros((rows + 4, cols + 4), dtype=int)

# 새로운 패딩 배열 중앙에 원본 배열 배치
padded_array[2:rows + 2, 2:cols + 2] = original_array

# 필요 시 리스트로 변환
padded_map = padded_array.tolist()

# 패딩된 맵 출력
for row in padded_map:
    print(row)

