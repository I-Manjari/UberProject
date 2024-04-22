**Uber-Like Cab Booking System**

**Description:**
This project is a simple implementation of a cab booking system similar to Uber. It consists of functionalities for registering drivers, assigning cabs to users, and managing driver availability.

**Technologies Used:**
- Python
- MySQL
- mysql.connector library

**Project Structure:**
- **main.py:** Contains the main functionality of the cab booking system.
- **README.md:** This file, providing an overview of the project and instructions for usage.
- **database.sql:** SQL script to create the necessary database schema.

**Installation:**
1. Install Python (if not already installed) from [python.org](https://www.python.org/).
2. Install MySQL (if not already installed) from [mysql.com](https://www.mysql.com/).
3. Install the mysql.connector library:
    ```
    pip install mysql-connector-python
    ```

**Setup:**
1. Run the `database.sql` script in your MySQL database to create the necessary schema.
2. Update the database connection details in `main.py`:
    - Update the `host`, `user`, `password`, and `database` variables in the `mysql.connector.connect()` function with your MySQL connection details.

**Usage:**
1. Open a terminal or command prompt.
2. Navigate to the directory containing `main.py`.
3. Run the following command to start the program:
    ```
    python main.py
    ```
4. Choose between "driver" and "user" modes:
    - **Driver Mode:** Register new drivers by providing their name and car number.
    - **User Mode:** Assign cabs to users by entering their name.

**Functionality:**
- **Register Driver:**
    - Allows adding new drivers to the system.
    - Requires input of driver name and car number.
    - Updates the database with the new driver's information.

- **Assign Cab to User:**
    - Assigns an available cab to a user.
    - Checks for available drivers in the database.
    - If available, assigns the first available driver to the user.
    - Marks the assigned driver as unavailable in the database.

**Contributors:**
- Manjari

**License:**
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

**Disclaimer:**
This project is for educational purposes only and is not affiliated with Uber or any other company.
