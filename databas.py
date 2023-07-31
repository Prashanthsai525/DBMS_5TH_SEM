import mysql.connector
import pandas as pd
import streamlit as st
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    #password="root",
    database="E_bill"
)
c = mydb.cursor()



def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS crime(crime_id int NOT NULL, crime_type varchar(100),crime_place varchar(100),crime_date DATE NOT NULL,PRIMARY KEY(crime_id));')


def add_crime_data(crime_id, crime_type,crime_place,crime_date):
    c.execute('INSERT INTO crime (crime_id,crime_type,crime_place,crime_date) VALUES (%s,%s,%s,%s);',
              (crime_id, crime_type,crime_place,crime_date))
    mydb.commit()

def add_criminal_data(crime_id, criminal_id,criminal_name,past_crimes,jail_name):
    c.execute('INSERT INTO criminal (crime_id, criminal_id,criminal_name,past_crimes,jail_name) VALUES (%s,%s,%s,%s,%s);',
              (crime_id, criminal_id,criminal_name,past_crimes,jail_name))
    mydb.commit()

def add_fir_data(crime_id,fir_id,fir_statement,fir_writer,date_of_fir):
    c.execute('INSERT INTO fir(crime_id,fir_id,fir_statement,fir_writer,date_of_fir) VALUES (%s,%s,%s,%s,%s);',
                (crime_id,fir_id,fir_statement,fir_writer,date_of_fir))
    mydb.commit()

def view_crime_data():
    c.execute('SELECT * FROM crime NATURAL JOIN (criminal NATURAL JOIN fir); ')
    data = c.fetchall()
    return data

def edit_details(new_crime_id,new_crime_type, new_crime_place,new_crime_date,crime_id,crime_type,crime_place,crime_date):
    c.execute("UPDATE crime SET crime_id=%s, crime_type=%s, crime_place=%s, crime_date=%s WHERE crime_id=%s and crime_type=%s and crime_place=%s and crime_date=%s", (new_crime_id, new_crime_type, new_crime_place,new_crime_date,crime_id,crime_type,crime_place,crime_date))
    mydb.commit()
    c.execute("select * from crime")
    data = c.fetchall()
    return data

def view_only_crime_ids():
    c.execute('SELECT crime_id FROM crime')
    data = c.fetchall()
    return data

def view_only_fir_ids():
    c.execute('SELECT fir_id FROM fir')
    data = c.fetchall()
    return data

def view_crime():
    c.execute('SELECT * FROM crime;')
    data = c.fetchall()
    return data

def view_fir():
    c.execute('SELECT * FROM fir;')
    data = c.fetchall()
    return data

def get_details(crime_id):
    c.execute('SELECT * FROM crime WHERE crime_id="{}"'.format(crime_id))
    data = c.fetchall()
    return data

def delete_data(crime_id):
    c.execute('DELETE FROM fir WHERE crime_id="{}"'.format(crime_id))
    mydb.commit()
    del1(crime_id)

def del1(crime_id):
    c.execute('DELETE FROM crime WHERE crime_id="{}"'.format(crime_id))
    mydb.commit()
    del2(crime_id)
    
def del2(crime_id):
    c.execute('DELETE FROM criminal WHERE crime_id="{}"'.format(crime_id))
    mydb.commit()

def query(q):
    c.execute(q)
    data = c.fetchall()
    mydb.commit()
    return data

def show_proc():
    c.callproc('view_people_involved')
    for results in c.stored_results():
        data = results.fetchall()
    df = pd.DataFrame(data,columns=['Criminal name','Crime type','Fir','Fir writer name'])
    with st.expander("Names are :"):
        st.dataframe(df)