import cx_Oracle
conn=cx_Oracle.Connection('System/ manager@mother')
cur=conn.cursor()

def createtable():
    query='''create table mcanagendra(id number(2)primary key,name varchar(70))
                                       
    '''
    cur.execute(query)
def insertrecord(sid,name):
    record={'id':str(sid),'name':name}
     
    cur.excute("insert into mcanagendra(id,name) values(:id,:name)",record)
    conn.commit()
# insertrecord(3,'kataramma')  
# insertrecord(4,'kajanaa')
# insertrecord(5,'kavya')
# insertrecord(6,'kamakshi')    

def read_records():
    query = 'select * from mcanagendra'
    cur.execute(query)
    records = cur.fetchall()
    (row)

read_records()            
