def select_all(cursor):
    SQL_QUERY = "SELECT * FROM myTable;"
    cursor.execute(SQL_QUERY)

    records = cursor.fetchall()
    for row in records:
        print(row)

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
    removed_row_querry = f"SELECT * FROM myTable WHERE myTableID = ?"
    cursor.execute(removed_row_querry, myTableID)
    removed_row = cursor.fetchone()
    cursor.execute(SQL_QUERY, myTableID)
    conn.commit()
    print (f"Successfully removed row: {removed_row}")



# Create user
# Delete user
# Update user by (name. surname, salary)
# Select user by (Name, Surname, Country)