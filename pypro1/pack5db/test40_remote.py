# 원격 데이터베이스 연동
import MySQLdb

#conn = MySQLdb.connect(host = '127.0.0.1', user = 'root', password='123', database='test')
#print(conn)
#conn.close

config = { #dict type 사용
    'host':'127.0.0.1',
    'user':'root',
    'password':'',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}

try:
    conn = MySQLdb.connect(**config) #dict는 **로 받는다.
    cursor=conn.cursor()
    #insert 연습
    '''
    print('insert ---')
    #isql = "insert into sangdata(code, sang, su, dan) values(10,'신상',5,5000)"
    #isql = "insert into sangdata(code, sang, su, dan) values(%s,%s,%s,%s)"
    isql = "insert into sangdata values(%s,%s,%s,%s)"
    sql_data = (10, '신상', 5, 5000)
    #sql_data = 10, '신상', 5, 5000
    cursor.execute(isql, sql_data)
    conn.commit()
    '''
    # update 연습
    '''
    print('update ---')
    usql = "update sangdata set sang=%s, su=%s where code=%s"
    sql_data = ('얼죽아',30,10)
    cou = cursor.execute(usql, sql_data)
    print('cou:',cou)
    conn.commit()
    '''
    # delete 연습
    """
    print('delete ---')
    input_code = '10'
    #dsql = "delete from sangdata where code=" + input_code #secure coding 가이드 라인에 위배
    #dsql = "delete from sangdata where code=%s"
    #cou = cursor.execute(dsql, (input_code,))
    
    dsql = "delete from sangdata where code='{0}'".format(input_code)
    cou = cursor.execute(dsql)
    conn.commit()
    
    if cou > 0:
        print('삭제 성공')
    else:
        print('삭제 실패')
    """    
    
    print('select ---')#select 연습
    sql = "select code, sang, su, dan from sangdata" # *보다 칼럼으로 써주면 속도도 빠르고 가독성도 좋다.
    
    cursor.execute(sql)
    
    for data in cursor.fetchall():
        #print(data)
        print('%s %s %s %s'%data)
    '''
    print()
    for data in cursor:
        print(data[0], data[1], data[2], data[3])   
    
    print()
    for (code, sang, su, dan) in cursor:
        print(code, sang, su, dan)     
        
    print()
    for (a, kbs, mbc, dan) in cursor: #변수라 생각한다.
        print(a, kbs, mbc, dan)    
    '''       
except Exception as e:
    print('err:',e)
    conn.rollback()
finally:
    cursor.close()
    conn.close()
#except MySQLdb.connections.Error as e:
 #   if e.errno == errcode.ER_ACC