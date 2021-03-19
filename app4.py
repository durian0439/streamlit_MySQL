import streamlit as st
import mysql.connector
from mysql.connector import Error

from mysql_select import mysql_select


def main() :

    menu = ['Select', 'Insert', 'Update', 'Delete']
    choie = st.sidebar.selectbox('메뉴', menu)

    if choie == 'Select' :
        mysql_select()



if __name__ == '__main__' :
    main()




