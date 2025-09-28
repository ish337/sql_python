def select_all(cursor):
    SQL_QUERY = "SELECT * FROM myTable ORDER BY myTableID;"
    cursor.execute(SQL_QUERY)

    records = cursor.fetchall()
    for row in records:
        print(row)

def select_id(cursor, conn, myTableID):
    row_querry = f"SELECT * FROM myTable WHERE myTableID = ?"
    cursor.execute(row_querry, myTableID)
    row = cursor.fetchone()
    return row

def create_user(cursor, conn):
    name = input("Enter person's name: ")
    surname = input("Enter person's surname: ")
    email = input("Enter person's email: ")
    country = input("Enter person's country: ")
    city = input("Enter person's city: ")
    salary = int(input("Enter person's salary: "))
    cvv = int(input("Enter person's cvv: "))
    SQL_QUERY = f"INSERT INTO myTable ([name], surname, email, country, city, salary, cvv) VALUES (?, ?, ?, ?, ?, ?, ?)"
    cursor.execute(SQL_QUERY, (name, surname, email, country, city, salary, cvv))
    conn.commit()

    cursor.execute("SELECT TOP 1 * FROM myTable ORDER BY myTableID DESC;")
    last_id = cursor.fetchone()
    print("Inserted row ID:", last_id)

# DELETE FROM myTable WHERE myTableID = 2007;
# SELECT * FROM myTable WHERE myTableID = 2007;

def delete_user(cursor, conn):
    myTableID=int(input("Enter ID to remove: "))
    SQL_QUERY = f"DELETE FROM myTable WHERE myTableID = ?"
    row = select_id(cursor, conn, myTableID)
    cursor.execute(SQL_QUERY, myTableID)
    conn.commit()
    print (f"Successfully removed row: {row}")

# UPDATE myTable SET [name]= 'value1', surname = 'value2', email = 'value3', country= 'value4', city = 'value5', salary = 8888, cvv = 111 WHERE myTableID = 2003;

def update_user(cursor, conn):
    myTableID=int(input("Enter ID to update: "))
    choice = input((f"Select fields to update(for choice multiple use spaces)\n1. name\n2. surname\n3. email\n4. country\n5. city\n6. salary\n7. cvv\n-> "))
    choice = choice.split()
    SQL_QUERY = f"UPDATE myTable SET "
    val = []
    for i in range(len(choice)):
        if choice[i] == '1':
            name = input("Enter new name: ")
            SQL_QUERY = SQL_QUERY + "[name]= ?, "
            val.append(name)
        elif choice[i] == '2':
            surname = input("Enter new surname: ")
            SQL_QUERY = SQL_QUERY + "surname= ?, "
            val.append(surname)
        elif choice[i] == '3':
            email = input("Enter new email: ")
            SQL_QUERY = SQL_QUERY + "email= ?, "
            val.append(email)
        elif choice[i] == '4':
            country = input("Enter new country: ")
            SQL_QUERY = SQL_QUERY + "country= ?, "
            val.append(country)
        elif choice[i] == '5':
            city = input("Enter new city: ")
            SQL_QUERY = SQL_QUERY + "city= ?, "
            val.append(city)
        elif choice[i] == '6':
            salary = int(input("Enter new salary: "))
            SQL_QUERY = SQL_QUERY + "salary= ?, "
            val.append(salary)
        elif choice[i] == '7':
            cvv = int(input("Enter new cvv: "))
            SQL_QUERY = SQL_QUERY + "cvv= ?, "
            val.append(cvv)
    SQL_QUERY = SQL_QUERY.rstrip(", ")
    SQL_QUERY += " WHERE myTableID = ?"
    val.append(myTableID)
    cursor.execute(SQL_QUERY, val)
    conn.commit()
    row = select_id(cursor, conn, myTableID)
    print (f"Was affected next row: {row}")

def select_user(cursor, conn):
    choice = input((f"Search by(for choice multiple use spaces)\n1. name\n2. surname\n3. email\n4. country\n5. city\n6. salary\n7. cvv\n8. ID\n-> "))
    choice = choice.split()
    SQL_QUERY = f"SELECT * FROM myTable WHERE "
    val = []
    for i in range(len(choice)):
        if choice[i] == '1':
            name = input("Enter name: ")
            SQL_QUERY = SQL_QUERY + "[name]= ? AND "
            val.append(name)
        elif choice[i] == '2':
            surname = input("Enter surname: ")
            SQL_QUERY = SQL_QUERY + "surname= ? AND "
            val.append(surname)
        elif choice[i] == '3':
            email = input("Enter email: ")
            SQL_QUERY = SQL_QUERY + "email= ? AND "
            val.append(email)
        elif choice[i] == '4':
            country = input("Enter country: ")
            SQL_QUERY = SQL_QUERY + "country= ? AND "
            val.append(country)
        elif choice[i] == '5':
            city = input("Enter city: ")
            SQL_QUERY = SQL_QUERY + "city= ? AND "
            val.append(city)
        elif choice[i] == '6':
            salary = int(input("Enter salary: "))
            SQL_QUERY = SQL_QUERY + "salary= ? AND "
            val.append(salary)
        elif choice[i] == '7':
            cvv = int(input("Enter cvv: "))
            SQL_QUERY = SQL_QUERY + "cvv= ? AND "
            val.append(cvv)
        elif choice[i] == '8':
            myTableID = int(input("Enter myTableID: "))
            SQL_QUERY = SQL_QUERY + "myTableID= ? AND "
            val.append(myTableID)
    SQL_QUERY = SQL_QUERY.rstrip(" AND ")
    cursor.execute(SQL_QUERY, val)
    records = cursor.fetchall()
    for row in records:
        print(row)

def menu(cursor, conn):
    while True:
        print(f"--------------------------CHOICE OPTION--------------------------")
        print(f"1. Select all\n2. Create user\n3. Delete user\n4. Update user\n5. Select user\n6. Exit")
        choice = int(input("Enter option: "))
        if choice == 1:
            select_all(cursor)
        elif choice == 2:
            create_user(cursor, conn)
        elif choice == 3:
            delete_user(cursor, conn)
        elif choice == 4:
            update_user(cursor, conn)  
        elif choice == 5:
            select_user(cursor, conn)
        elif choice == 6:
            break
        else:
            print("Wrong option")  


# Create user
# Delete user
# Update user by (name. surname, salary)
# Select user by (Name, Surname, Country)