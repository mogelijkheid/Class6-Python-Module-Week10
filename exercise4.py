import psycopg2
def connect():
    try:
        """ Connect to the PostgreSQL database server """
        conn = psycopg2.connect(
            host="localhost",
            database="pycoders",
            user="postgres",
            password="1")

        cur = conn.cursor()

        #First part of the question
        cur.execute("""
        
            SELECT * from "actor"
            """,
            
        )
        actor = cur.fetchall()
        for all in actor:
            print(all)
        

        #Second part of the question
        cur.execute("""
        
            SELECT * from "category"
            """,
            
        )    
        category = cur.fetchone()
        print(category)

        #Third part of the question
        cur.execute("""
        
            SELECT * from "address"
            """,
            
        )    
        category = cur.fetchmany(50)
        for row in category:
            print(row)         


        cur.close()
        conn.commit()

    except (Exception) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

if __name__ == '__main__':
    connect()