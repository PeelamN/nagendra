import cx_Oracle
import csv
conn=cx_Oracle.Connection('System/ manager@mother')
cur=conn.cursor()

def createtable():
    query='''create table mcanagendra(id number(2)primary key,name varchar(70))
                                       
    '''
    cur.execute(query)
def insertrecord():
     
    query='''insert into mcanagendra(id,name) values(1,'praveen')
'''
    cur.exacute(query)
    conn.commit()
# insertrecord(3,'kataramma')  
# insertrecord(4,'kajanaa')
# insertrecord(5,'kavya')
# insertrecord(6,'kamakshi')    

def read_records():
    query = 'select * from mcanagendra'
    cur.execute(query)
    records = cur.fetchall()
    for row in records:
        print(row)
        #for row in records:
        #data.writerow(row)
read_records() 

def fetch_record(sid):
    record={'id':str(sid)}
    query = 'select * from mcanagendra where id =:id'
    cur.execute(query,record)
    record=cur.fetchall()
    for row in record:
        print(row)

def update_name(sid,name): 
    fetch_record(sid)
    name=input('enter new name to update :-')
    record={'id':str(sid),'name':name}
    query = 'update mcanagendra set name = :name where id = :id'
    cur.execute(query,record)
    conn.commit()
    fetch_record(sid)
def delete_(sid):
    query = 'delete from mcanagendra where id = :id'
    cur.execute(query,sid)
    conn.commit()

def delete_record(sid):
    record={'id':str(sid)} 
    query = 'delete from mcanagendra where id = :id'  
    cur.execute(query,record)
    conn.commit()

    def truncate():
        query ='truncate table macnagedra'
        cur.execute(query)

def insert_from_csv():
    with open('records.csv','r') as csvfiles:
        data=csv.reader(csvfiles)
        data= list(data) 
        for row in range(1,len(data)):
            insertrecord(*data[row])
             

    