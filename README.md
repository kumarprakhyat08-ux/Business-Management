# Business Management System

A Python-based command-line application for managing inventory and sales records. This project uses MySQL for database management and features a role-based login system for Managers and Sales staff.

## Features

- **Role-Based Access Control**: Separate functionalities for 'Manager' and 'Salesman' roles.
- **Inventory Management (Manager)**:
  - View all stock records.
  - Add new stock items.
  - Modify existing stock records (update details or delete).
  - Search for specific stock items by name and view their sales history.
- **Sales Management (Salesman)**:
  - View all sales records.
  - Record new sales (automatically deducts sold quantity from the main stock).
  - Delete sales records.
  - Display specific sales transactions by ID.
- **Automated Database Setup**: Automatically creates the required `Business_management` database and `stocks`/`sales` tables upon first run.

## Prerequisites

- **Python 3.x**
- **MySQL Server** (running locally)
- Python packages:
  - `mysql-connector-python`
  - `tabulate`

## Installation and Setup

1. **Clone the repository** (if applicable) or download the python script.
2. **Install the required Python libraries**:
   ```bash
   pip install mysql-connector-python tabulate
   ```
3. **Configure MySQL Credentials**:
   Open the Python script and update the database connection parameters with your MySQL `user` and `password` on line 5:
   ```python
   con = mysql.connector.connect(host="localhost", user='root', password='your_password_here')
   ```
4. **Run the application**:
   ```bash
   python script_name.py
   ```

## Default Credentials

### Manager
- **User ID**: `manager`
- **Password**: `man123`

### Salesman
- **User ID**: `salesman`
- **Password**: `sales123`

## Database Schema

The application automatically creates two tables in the `Business_management` database:

- **`stocks`**:
  - `Stock_ID` (Primary Key, INT)
  - `name` (VARCHAR)
  - `company` (VARCHAR)
  - `price` (FLOAT)
  - `stock` (INT)

- **`sales`**:
  - `sid` (Primary Key, INT) - Sales ID
  - `Stock_ID` (Foreign Key referencing `stocks`, INT)
  - `quantity` (FLOAT)
  - `date` (DATE)
