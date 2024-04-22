import mysql.connector

# Establish database connection
conn = mysql.connector.connect(host='localhost', user='root', password='Manjari@14', database='uber')
my_cursor = conn.cursor(dictionary=True)

def insert_driver_into_db(driver_name, car_number):
    sql = "INSERT INTO driver (car_number, driver_name, availability) VALUES (%s, %s, %s)"
    val = (car_number, driver_name, "true")
    my_cursor.execute(sql, val)
    conn.commit()

def update_availability(driver):
    cab_id = driver["driver_id"]
    update_sql = "UPDATE driver SET availability = 'False' WHERE driver_id = %s"
    val = (cab_id,)
    my_cursor.execute(update_sql, val)
    conn.commit()

def get_available_drivers():
    sql = 'SELECT * FROM driver WHERE availability = "true"'
    my_cursor.execute(sql)
    driver_list = my_cursor.fetchall()
    return driver_list

def register_driver(driver_name, car_number):
    insert_driver_into_db(driver_name, car_number)
    print("Driver registered successfully!")

def assign_cab_to_user():
    user_name = input("Enter user name: ")
    available_drivers = get_available_drivers()

    if available_drivers:
        driver = available_drivers[0]
        print("Your cab is assigned.")
        print("Driver name:", driver["driver_name"])
        print("Car number:", driver["car_number"])
        update_availability(driver)
    else:
        print("Sorry, no cabs available at the moment.")

while True:
    choice = input("Enter choice (driver/user): ")

    if choice == "driver":
        driver_name = input("Enter driver name: ")
        car_number = input("Enter car number: ")
        register_driver(driver_name, car_number)

    elif choice == "user":
        assign_cab_to_user()

    else:
        print("Invalid choice.")

