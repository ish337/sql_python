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

    conn.commit()





# Create user
# Delete user
# Update user by (name. surname, salary)
# Select user by (Name, Surname, Country)