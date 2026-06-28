import cv2
import numpy

# 读取 raw 文件（YUV420 格式，1280x720）
长, 高 = 1280, 720
with open('test.raw', 'rb') as f:
    原始数据 = f.read()

# YUV420 (NV12) 格式: Y 平面 + UV 交错平面
# Y 平面大小 = width * height
# UV 平面大小 = width * height / 2
Y平面字节数  = 长 * 高
U平面字节数  = (长 * 高) // 4
V平面字节数  = (长 * 高) // 4
uv_size = 长 * 高 // 2

Y平面数据 = numpy.frombuffer(原始数据[0                         : Y平面字节数                            ], dtype=numpy.uint8).reshape((高, 长))
U平面数据 = numpy.frombuffer(原始数据[Y平面字节数               : Y平面字节数 + U平面字节数              ], dtype=numpy.uint8).reshape((高 // 4, 长))
V平面数据 = numpy.frombuffer(原始数据[Y平面字节数 + U平面字节数 : Y平面字节数 + U平面字节数 + V平面字节数], dtype=numpy.uint8).reshape((高 // 4, 长))

# 将 Y 和 UV 合并为 NV12 再转为 BGR
YUV图片数据 = numpy.concatenate([Y平面数据, U平面数据, V平面数据])

bgr = cv2.cvtColor(YUV图片数据, cv2.COLOR_YUV2BGR_NV12)

# 显示图片
cv2.imshow('test.raw (1280x720 YUV420)', bgr)
print("按任意键关闭窗口...")
cv2.waitKey(0)
cv2.destroyAllWindows()
