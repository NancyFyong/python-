from paddleocr import PaddleOCR, draw_ocr
from tqdm import tqdm
# import paddle
# paddle.utils.run_check()
#
# import os
# os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
# Paddleocr目前支持的多语言语种可以通过修改lang参数进行切换
# 例如`ch`, `en`, `fr`, `german`, `korean`, `japan`
ocr = PaddleOCR(use_gpu=True,lang="ch")  # need to run only once to download and load model into memory
img_path = './python作业截图/3.png'
result = ocr.ocr(img_path, cls=True)
for idx in range(len(result)):
    res = result[idx]
    for line in res:
        print(line[1][0])
