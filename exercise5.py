import psycopg2
def connect():
    try:
        conn=psycopg2.connect(host="localhost",database="pycoders", user="postgres", password="1")
        cur=conn.cursor()
        cur.execute(""" create table students (student_id int primary key, name varchar(50) not null) """)
        cur.execute(""" create table teachers(teacher_id int primary key, name varchar(50) not null)""")
        cur.execute("""insert into students(student_id,name) values (1,'inci')""")
        cur.execute("""insert into students(student_id,name) values (2,'betul')""")
        cur.execute("""insert into students(student_id,name) values (3,'asel')""")
        cur.execute("""insert into teachers(teacher_id,name) values (1,'yunus')""")
        cur.execute("""insert into teachers(teacher_id,name) values (2,'mamudo')""")
        cur.execute ("""insert into teachers(teacher_id,name) values (3,'ahmet')""" )
        cur.execute("""select *from students""")
        students=cur.fetchall()
        for student in students:
            print(student)
        cur.execute("""select *from teachers """)
        teachers=cur.fetchall
        for teacher in teachers():
            print(teacher)
        

        cur.close()
        conn.commit()
    

    except (Exception) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('data base connection closed')

if __name__ == '__main__':
    connect()