def yolo():
    import subprocess

    # detect.py를 실행하는 명령어
    cmd = "cd yolov5 && python detect.py --weights ../best.pt --source \"../image.png\""

    # 명령어 실행하고 결과 받아오기
    completed_process = subprocess.run(cmd, shell=True, capture_output=True, text=True, encoding='utf-8')

    result = completed_process.stdout.split("\n")[:-1]

    # 표준 출력 출력
    # print(result)

    a = {}

    for res in result:
        index, n, c = res.split()
        index = index[:-1]
        if n == "kids":
            age = (13 - int(float(c) * 10)) // 1
        else:
            age = 13 + (int(float(c) * 100) // 3)
        # print(f'{index}번째의 얼굴 나이 : {age}세')
        a[index] = age
        
    if a == {}:
        return {0: -1}
        
    return a
