[영어](README.md)

# 유튜브 통계자료
코드를 실행하면 유튜브 채널의 통계를 받아올 수 있습니다.

## 필요한것
- Youtube API key
    - 한국어 참고자료: https://brunch.co.kr/@mystoryg/156
    - 영어 참고자료: https://blog.hubspot.com/website/how-to-get-youtube-api-key
- 필요한 모듈을 다운로드하기 위해 아래 코드를 터미널에 입력하세요.

    - (필수) 구글 API 다운로드 위한 명령어

        `pip install --upgrade google-api-python-client`

    - (옵션) 출력을 예쁘게 하기 위한 명령어

        `pip install tabulate`

## 사용방법
1. 발급받은 API key를 statistics_withoutAPI.py 파일의 5번째 라인에 위치한 "PUTAPIKEYHERE" 에 넣어주세요.
2. 통계자료를 받고싶은 유튜브 채널 명을 statistics_withoutAPI.py 파일의 11번째 라인에 위치한 "PUTCHANNELNAMEHERE" 에 넣어주세요.
3. 터미널에 가서 `python statistics_withoutAPI.py` 를 실행해주세요. 
4. 플레이리스트의 인덱스를 입력하세요.
    - 첫 번째 인덱스는 0이며, 그 다음 인덱스는 1, 2, 3으로 오름차순입니다.


## 라인개발실록 채널 예시


<p align = "center"><img src = "https://github.com/euiminnn/image-upload/blob/master/index0-Meetup.png?raw=true" width = "900"></p>

<p align = "center"><img src = "https://github.com/euiminnn/image-upload/blob/master/index1-Teatime.png?raw=true" width = "900"></p>

<p align = "center"><img src = "https://github.com/euiminnn/image-upload/blob/master/index2-Tamgu.png?raw=true" width = "900"></p>

<p align = "center"><img src = "https://github.com/euiminnn/image-upload/blob/master/index3-Interview.png?raw=true" width = "900"></p>


이 곳(https://yobro.tistory.com/190?category=793224)의 코드에서 도움을 많이 받았습니다.
