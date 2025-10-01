from flask import Flask, request, render_template, url_for
import pandas as pd
# __name__: 현재 파일의 이름
app = Flask(__name__)

# =====================
# 웹 서버에서 사용할 주소들의 목록

# base url + '/' 주소로 요청이 들어왔을 때 바로 아래의 함수를 호출
# base url -> 127.0.0.1:5000
# 함수 생성시 유의할 점: 함수의 이름은 중복 불가
@app.route('/')
def index():
    # 현재 작업 경로에서 하위 디렉토리인 templates 안에 있는 index.html을 되돌려준다.
    # 샘플 데이터프레임을 로드
    df = pd.read_csv('./static/data/AAPL.csv')
    # 하위의 데이터 30개만 필터
    df = df.tail(30)
    # index.html에서 table에 컬럼의 이름들을 사용하기 위해 list형태의 columns를 생성
    cols = list(df.columns)
    # table에 데이터의 값들을 [{}, {}, {}] 형태로 생성
    # chart에서 사용할 x축의 데이터와 y축의 데이터를 list 형태로 생성
    x = df['Date'].to_list()
    y = df['Volume'].to_list()
    values = df.to_dict(orient = 'records')
    # cols와 values를 이용하여 index.html에서 table 태그를 생성
    return render_template('index.html',
                           cols = cols,
                           values = values,
                           x = x,
                           y = y)

@app.route('/second')
def second():
    # AAPL 로드
    df = pd.read_csv("static/data/AAPL.csv")
    df = df.tail(30)
    cols = list(df.columns)
    values = df.to_dict(orient = 'records')
    x = df['Date'].to_list()
    y = df['Adj Close'].to_list()
    return render_template('index2.html',
                           cols = cols,
                           values = values,
                           x = x,
                           y = y)
    
@app.route('/third')
def third():
    # AAPL 데이터에서 y축의 데이터를 2개를 사용
    # 저가와 고가를 사용
    df = pd.read_csv('static/data/AAPL.csv')
    df = df.tail(30)
    cols = list(df.columns)
    values = df.to_dict(orient = 'records')
    x = df['Date'].to_list()
    y = df['Low'].to_list()
    y2 = df['High'].to_list()
    return render_template('index3.html',
                           columns = cols,
                           value_data = values,
                           date = x,
                           low_data = y,
                           high_data = y2)






# =======================

# 웹 서버를 실행
# debug=True는 파일이 저장될 때마다 웹서버를 자동으로 재시작
app.run(debug=True)