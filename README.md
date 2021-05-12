### 프로젝트 버전 정보
Python Package List

|Package|Version|
|---|---|
|beautifulsoup4|4.9.3|
|bs4|0.0.1|
|cached-property|1.5.2|
|certifi|2020.12.5|
|chardet|3.0.4|
|commonmark|0.9.1|
|dictdiffer|0.8.1|
|dominate|2.5.2|
|idna|2.10|
|mistletoe|0.7.2|
|<b>notion</b>|<b>0.0.25</b>|
|<b>notion-py</b>|<b>0.0.9</b>|
|pip|21.1.1|
|python-dotenv|0.17.1|
|python-slugify|4.0.1|
|pytz|2021.1|
|requests|2.24.0|
|setuptools|56.0.0|
|soupsieve|2.2.1|
|text-unidecode|1.3|
|tzlocal|2.1|
|urllib3|1.25.11|



### ImportError : cannot import name 'TodoBlock' from 'notion.block' 
위 에러가 발생한다면 이유는 Notion Library가 설치 안되었거나 버전이 잘못되어있을 경우이다.=
이를 해결하기 위해서 notion library의 버전 정보를 0.0.25 버전으로 설치한다.
``` shell
pip3 install "notion === 0.0.25"
```