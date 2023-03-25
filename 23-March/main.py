import psycopg2

def connect_to_database():
    conn = psycopg2.connect(database="assignments")
    return conn


def create_table(conn, tableName, columnDetails):
    cur = conn.cursor()
    create_table_statement = f"""CREATE TABLE IF NOT EXISTS {tableName} (
                                {', '.join([f'{column[0]} {column[1]}' for column in columnDetails])}
                            );"""
    cur.execute(create_table_statement)
    conn.commit()


def insert_into_table(conn, tableName, values):
    cur = conn.cursor()
    insert_into_statement = f""" INSERT INTO {tableName} VALUES
                                {', '.join([f'{value}' for value in values])}
                            ;"""
    cur.execute(insert_into_statement)
    conn.commit()


def drop_table(conn, tableName):
    cur = conn.cursor()
    cur.execute(f"DROP TABLE IF EXISTS {tableName} CASCADE")
    conn.commit()


def show_table(conn, tableName):
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {tableName}")
    results = cur.fetchall()
    print(f'\nRows in {tableName} table: \n')
    for row in results:
        print(row)
    conn.commit()


def close_connection(conn):
    conn.close()


# DRIVER CODE

table_1 = 'customers'
columns_1 = [['customer_id', 'integer PRIMARY KEY NOT NULL'],['customer_name', 'text']]
values_1 = [(1,"Selena Gomez"),(2,"Adam Ray"),(3,"Shawn Mendes"),(4,"Justin Bieber"),(5,"Bella Hadid")]

table_2 = 'bank'
columns_2 = [['customer_id','integer NOT NULL REFERENCES customers(customer_id)'],['branch_id','integer NOT NULL'],['branch_name','text']]
values_2 = [(1,1001,"Hyderabad"),(2,1002,"Bangalore"),(3,1001,"Hyderabad"),(4,1003,"Chennai"),(5,1004,"Mumbai")]


conn = connect_to_database()

create_table(conn, table_1, columns_1)
create_table(conn, table_2, columns_2)

insert_into_table(conn, table_1, values_1)
insert_into_table(conn, table_2, values_2)

show_table(conn, table_1)
show_table(conn, table_2)

drop_table(conn, table_1)
drop_table(conn, table_2)

close_connection(conn)