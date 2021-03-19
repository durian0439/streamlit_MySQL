import streamlit as st
import mysql.connector
from mysql.connector import Error
from datetime import datetime, date, time

def main():
    st.header('몇년도 이후 몇페이지 이상의 책을 찾을것인가?')
    released_year = st.number_input('년도 입력', min_value = 1800, max_value = 2050)
    pages = st.number_input('페이지 수 입력',  min_value = 10)
    order = 'asc'
    if st.checkbox('오름차순/ 내림차순'):
        order = 'desc'






    if st. button('조회'):
        try:
            #1. 커넥터로부터 커넥션을 받는다.
            connection = mysql.connector.connect(
                host = 'database-1.cqduiaqdroex.us-east-2.rds.amazonaws.com',
                database = 'yhdb',
                user = 'streamlit',
                password = 'yh1234'
        
            )

            if connection.is_connected() : 
                print('연결될떄')
                db_info = connection.get_server_info()
                print('MySQL server virsion : ', db_info)

                #2. 커서를 가져온다
                cursor = connection.cursor(dictionary= True)
                #네트워크에서 사용할 시 제이슨형식을 채택하기에 
                #딕셔너리로 제이슨형식으로 바꾼다.

                #3. 우리가 원하는거 실행 가능
                # cursor.execute('select database();')
                # record = cursor.fatchone()
                if order = 'asc'
                query = '''
                        select * 
                        from books 
                        where released_year > %s and pages > %s
                        order by releaded_year asc;
                        '''   
                if order = 'desc'
                query = '''
                        select * 
                        from books 
                        where released_year > %s and pages > %s
                        order by releaded_year desc;
                        '''   
                
                # released_year = 2005
                # pages = 400
                # updown = desc
                param = (released_year, pages) # 콤마를 입력하지 않을 시 튜플이 되지 않음.


                cursor.execute(query, param)
                # connection.commit() # 셀렉트에는 커밋이 없다.

                # print('{}개 적용됨'.format(cursor.rowcount))
                # 4. 실행 후 커서에서 결과를 빼냄
                record = cursor.fetchall()
                # print('Connected to db : ', record)
                
                for data in record:
                    print(data['title'], data['released_year'])







        except Error as e:
            print('디비 관련 에러 발생',e)
            
        
        finally :
            #5. 모든 데이터 베이스 실행 명령을 끝냈으면 커서와 커넥션을 모두 닫아줌.
            cursor.close()
            connection.close()
            print('MySQL 커넥션 종료')




if __name__ == '__main__':
    print(__name__)
    main()
