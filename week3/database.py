import os
import pymysql

class MyDB():
    # 생성자 함수
    # class 내부에서 사용하려는 변수의 데이터를 대입하는 함수
    # class 생성 될 때 한번만 실행이 되는 함수
    # 입력 받을 데이터는 데이터베이스 서버의 정보 -> 기본값 설정(로컬피씨의 데이터베이스 정보)

    def __init__(
            self, 
            # _host = os.getenv('host'),
            # _port = int(os.getenv('port')),
            # _user = os.getenv('user'),
            # _pw = os.getenv('pw'),
            # _db_name = os.getenv('db_name')
            _host = '127.0.0.1',
            _port = 3306,
            _user = 'root',
            _pw = '',
            _db_name = 'multicam'
    ):
        # self.변수를 생성
        # class에서 사용할 서버의 정보를 변수에 저장
        self.host = _host
        self.port = _port
        self.user = _user
        self.pw = _pw
        self.db_name = _db_name

    def sql_query(
            self,
            #위에서 작성한 self 변수들을 써야하기 때문에
            _query,
            *_data_list
    ):
        # _query 매개변수는 기본값이 존재하지 않으므로 필수 입력 공간
        # _data_list는 인자의 개수를 가변으로 받는다. 개수가 0개면 ()을 생성

        # database 서버와의 연결(_db 변수를 생성하여 연결)
        # pymysql.connect 함수는 입력값이 서버의 정보

        try: 
            # self._db라는 변수를 확인
            self._db
            # 해당 변수가 선언이 되어있지 않다면 NameError 발생
        except:
            # self._db
            self._db = pymysql.connect(
                host = self.host,
                port = self.port,
                user = self.user,
                password = self.pw,
                db = self.db_name
            )

        # self._db 이용하여 cursor 생성
        # pymysql의 cursor 들 중에 딕셔너리 커서를 사용하여 만들기
        self.cursor = self._db.cursor(pymysql.cursors.DictCursor)

        #_query와 _data_list를 이용하여 self.cursor에 질의 보낸다.
        # 질의를 보내는 과정에서 문제가 발생하면 예외처리를 한다.
        try:
            self.cursor.execute(_query, _data_list)
        except Exception as e:
            # 무슨 에러인지 출력
            print(e)
            # query 문에서 문제가 발생했으니 
            return 'Query Error'
        
        if _query.lower().strip().startswith('select'):
            # query 문이 select문이라면
            result = self.cursor.fetchall()
        else:
            # select문이 아닌경우
            result = "Query OK"
        return result


    def commit_db(self):
        try:
            self._db.commit()
            print('Commit 완료')
            self._db.close()
            print('서버와의 연결 종료')
            # 변수를 삭제
            del self._db
        except Exception as e:
            print(e)
            # self._db와 self._cursor가 생성되지 않은 상황
            print('''데이터베이스 서버와의 연결이 없습니다. sql_query() 함수를 이용하여 서버와의 연결을 해주세요''')