import psycopg2

def is_int(str):
    try:
        int(str)
        return True
    except ValueError:
        return False




while True:
    conn = psycopg2.connect(
        host="localhost",
        database="phonebook",
        user="postgres",
        password="29032003"
    )
    sql = 'select * from MyContacts '
    cursor = conn.cursor()
    cursor.execute(sql)
    MyContacts = cursor.fetchall()
    n = input()
    if n == 'sorted data':
        a = MyContacts
        a.sort(key=lambda tup: tup[0], reverse=False)
        for i in a:
            for j in i:
                print(j, end=' ')
            print()
    if n == 'reversed sorted data':
        a = MyContacts
        a.sort(key=lambda tup: tup[0], reverse=True)
        for i in a:
            for j in i:
                print(j, end=' ')
            print()
    if str(n) == 'sorted by  time':


        for i in MyContacts:
            for j in i:
                print(j, end=' ')
            print()

    elif str(n) == 'insert':
        nn = input().split(" ")
        #cursor.execute(f"DELETE FROM SNAKESCORE1 WHERE username='{name}'")
        cursor.execute("INSERT INTO MyContacts (name,phonenumber) VALUES (%s, %s)", (nn[0], nn[1]))
        conn.commit()
       # print(MyContacts)

    elif str(n) == 'delete':
        nn = input().split(" ")
        for i in nn:
            cursor.execute(f"DELETE FROM MyContacts WHERE name='{i}'")

        conn.commit()
    elif str(n) == "update":
        nn = input()
        if is_int(nn):
            m = input()
            print(nn)
            cursor.execute(f"DELETE FROM MyContacts WHERE name='{m}'")
            cursor.execute(f"DELETE FROM MyContacts WHERE phonenumber='{nn}'")
            cursor.execute("INSERT INTO MyContacts (name,phonenumber) VALUES (%s, %s)", (m, nn))
            conn.commit()
        else:
            m = input()
            cursor.execute(f"DELETE FROM MyContacts WHERE name='{nn}'")
            cursor.execute(f"DELETE FROM MyContacts WHERE phonenumber='{m}'")
            cursor.execute("INSERT INTO MyContacts (name,phonenumber) VALUES (%s, %s)", (nn, m))
            conn.commit()