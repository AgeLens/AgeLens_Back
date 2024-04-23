from flask import request, Blueprint
from yolo import yolo
import base64
import cv2
import numpy as np
import io
from PIL import Image
import json

server_blueprint = Blueprint('server', __name__)

@server_blueprint.route('/api', methods=['POST'])
def server():
    # 요청에서 이미지 데이터 가져오기
    req = request.get_json()['img']
    
    if req == None:
        return "사진이 없어요ㅠㅠ"
    
    img_base64 = req.split(',')[1]
    
    imgdata = base64.b64decode(img_base64)
    
    dataBytesIO = io.BytesIO(imgdata)
    
    image = Image.open(dataBytesIO)
    
    img = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)
    
    # OpenCV를 사용하여 이미지 저장
    cv2.imwrite('./image.png', img)
    
    resultObj = yolo()
    
    resultImg = open('./result.jpg', 'rb')
    
    base64Str = base64.b64encode(resultImg.read())
    
    returnStr = base64Str.decode("utf-8")
    
    
    # 이미지 처리 결과 반환
    return json.dumps({"age": resultObj, "img": returnStr})
