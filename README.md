[한국어](README.kr.md)

# Youtube statistics
You can get any youtube channel statistics with this code.

## What you need
- Youtube API key
    - Reference in English: https://blog.hubspot.com/website/how-to-get-youtube-api-key
    - Reference in Korean: https://brunch.co.kr/@mystoryg/156
- write these commands in terminal to download modules

    - (required) to use google api

        `pip install --upgrade google-api-python-client`

    - (not required) to make your DataFrame look good

        `pip install tabulate`

## How to use
1. Put your API key in "PUTAPIKEYHERE" in line 3 of statistics_withoutAPI.py
2. Put the channel name you want to get statistics from in "PUTCHANNELNAMEHERE" in line 10 of statistics_withoutAPI.py
3. Go to Terminal and run `python statistics_withoutAPI.py`
4. Input index number of playlists of channel (first playlist of the channel would be 0 and others are in ascending order)


## My Example: LINEDEVLOG channel


<p align = "center"><img src = "https://github.com/euiminnn/image-upload/blob/master/index0-Meetup.png?raw=true" width = "900"></p>

<p align = "center"><img src = "https://github.com/euiminnn/image-upload/blob/master/index1-Teatime.png?raw=true" width = "900"></p>

<p align = "center"><img src = "https://github.com/euiminnn/image-upload/blob/master/index2-Tamgu.png?raw=true" width = "900"></p>

<p align = "center"><img src = "https://github.com/euiminnn/image-upload/blob/master/index3-Interview.png?raw=true" width = "900"></p>


The code from here(https://yobro.tistory.com/190?category=793224) helped me a lot.
