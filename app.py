import streamlit as st
import mysql.connector
from mysql.connector import Error
from datetime import datetime, date, time

def main():
    if st. button('저장'):
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
                cursor = connection.cursor()

                #3. 우리가 원하는거 실행 가능
                # cursor.execute('select database();')
               
                query = '''
                        insert into cats4(name,age)
                        values(%s, %s);
                        '''
                record=[('냐옹이', 1),('야옹', 1) ]        
                cursor.executemany(query,record)
                connection.commit()
                print('{}개 적용됨'.format(cursor.rowcount))
                #4. 실행 후 커서에서 결과를 빼냄
                # record = cursor.fetchone()
                # print('Connected to db : ', record)
                
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
