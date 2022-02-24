import sqlite3
#conn = db와 파일 연결 #cur = 커서 이용해 명령 내리고 결과값 받음
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

#만약 위에 db가 컴퓨터 내에 존재하면 삭제함
cur.execute('DROP TABLE IF EXISTS Counts')

#db 생성
cur.execute('''
CREATE TABLE Counts (email TEXT, count INTERGER)''')

#파일 이름 지어서 생성, 밑에 반복문은 이름 짧을 때 예비 이름
fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox=short.txt'
fh = open('/Users/hallucy/Desktop/Coding/VSC/Python/boostcamp/py_database/' + fname)

#데이터 읽고 쪼개서 데이터 있는지 확인, 없으면 새로 넣고 있으면 업데이트하는 코드
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,)) 
    #이 구절은 데이터 빼오는게 아니라 문제가 있는 지만 확인하는 거, 
    #데이터 읽진 않고 커서를 열어놓은 상태, 즉 파일에 있는 레코드(로우)들 열어둔 것과 같음
    #윗부분 ?: sql에서 자리 표시해줌 그 안에 내용 들어감 / (email,) 파이썬에서 원소 하나뿐인 튜플 넣을때 이렇게 넣음
    row = cur.fetchone()
    #로우에 내용 없으면 인서트 써서 새로 값 넣고 카운트 올려줌, 밸류에 ? 이용해서 값 넣어줌
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count)
                VALUES (?, 1)''', (email,))
    # 로우에 내용 있으면 업데이트해서 값 넣기, 카운트 올리기
    #업데이트가 값 받아서 파이썬에서 값 증가시키고 db에 새 값 반영하는 방식보다 sql 문 개수도 적고 단위 코드라 좋음
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
                    (email,))
    conn.commit()
    #db는 데이터 메모리에 저장했다가 특정 시점에 정보를 디스크에 옮겨씀 (커밋)
    #반복할 때마다 매번 할 수도 있고 10번에 한번씩 할 수도 있음
    #온라인은 화면 내용 끝날때마다 해주는게 좋음

# https://www.sqlite.org/lang_select.html
# 이메일 선택해서 카운츠에서 카운트 따서 10까지 내림차순으로 정렬
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

# 로우에 이메일, 조회수 순써쌍으로 프린트
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()