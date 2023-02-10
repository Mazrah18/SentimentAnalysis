from pymysql import *

class DataBaseHelper:

    @staticmethod
    def get_data(query,parameters=None):
        conn=connect(host='localhost',database='world',user='root',password='mukesh')
        cur=conn.cursor()
        if(parameters is None):
            cur.execute(query)
        else:
            cur.execute(query%parameters)
        result=cur.fetchone()#fetchone row , result is a tuple
        cur.close()
        conn.close()
        return result

    @staticmethod
    def get_all_data(query, parameters=None):
        conn = connect(host='localhost', database='world', user='root', password='mukesh')
        cur = conn.cursor()
        if (parameters is None):
            cur.execute(query)
        else:
            cur.execute(query % parameters)
        result = cur.fetchall()  # to get all data
        cur.close()
        conn.close()
        return result

    @staticmethod
    def execute_query(query, parameters=None):
        conn = connect(host='localhost', database='world', user='root', password='mukesh')
        cur = conn.cursor()
        if (parameters is None):
            cur.execute(query)
        else:
            cur.execute(query % parameters)
        conn.commit()#if this is not return then there will be no changes in database , this is usually used inside try catch (to catch the errors)
        cur.close()
        conn.close()
        #insert , update , delete

    @staticmethod
    def execute_all_data_multiple_input(query, params):
        conn = connect(host='localhost', database='world', user='root', password='mukesh')
        cur = conn.cursor()
        format_strings = ','.join(['%s'] * len(params))
        print(format_strings)
        cur.execute(query % format_strings, params)
        conn.commit()
        cur.close()
        conn.close()
