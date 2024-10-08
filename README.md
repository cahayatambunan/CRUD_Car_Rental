# CRUD Car Rental System

A car rental management system built using **Python**. This system features basic **CRUD** (Create, Read, Update, Delete) operations for managing vehicle listings and rental bookings. The application is designed for two types of users: **Admins**, who manage car data, and **Customers**, who browse and book available cars.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Admin Menu](#admin-menu)
  - [Customer Menu](#customer-menu)
- [Project Structure](#project-structure)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)

---

## Overview

This project is designed to simulate a car rental service, allowing the admin to manage vehicle availability, and customers to search for and book cars. The data is displayed in a tabular format using the `tabulate` library, making it easy to view car information. The project is a simple CLI-based (Command Line Interface) system, built for demonstration purposes.

---

## Features

### Admin Features
- **View All Cars**: See a list of all cars in the system, including their type, transmission, seats, status, and price.
- **Add New Car**: Add a new car to the system by providing the necessary details.
- **Update Car Details**: Modify existing car information (e.g., status, price, etc.).
- **Delete Car**: Remove a car from the system.
- **View Car by ID**: Search for a specific car by its unique ID.

### Customer Features
- **Browse Cars**: View available cars for rental.
- **Search for Cars by ID**: Find a car by its ID to get specific details.
- **Book a Car**: Reserve a car for rental.

### Data Display
- All car information is displayed in tabular format for both admin and customer views using the `tabulate` library.

---

## Installation

To run this project locally, follow these steps:

### Step-by-step installation:

1. Clone this repository:
    ```bash
    git clone https://github.com/cahayatambunan/CRUD_Car_Rental.git
    ```

2. Navigate to the project directory:
    ```bash
    cd CRUD_Car_Rental
    ```

3. Install the required dependencies using `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the project:
    ```bash
    python main.py
    ```

---

## Usage
### Main Menu
![Main Menu](./main_menu.png)

The main menu provides options for user to log in as:
1. **Customer**: Displays Customer Menu.
2. **Admin**: Displays Admin Menu.
3. **Exit**: Exit from the program.



### Admin Menu
![Admin Menu](./admin_view.png)

Admins have the following options to manage car listings:
1. **View All Cars**: Displays all cars with their details.
2. **Add a Car**: Input car information such as type, transmission, seats, status, and price.
3. **Update Car**: Modify details of an existing car by providing its ID.
4. **Delete a Car**: Remove a car from the system.
5. **Exit**: Exit the admin menu, go to The Main Menu.

### Customer Menu
![Customer Menu](./cust_view.png)
Customers have the following options to interact with the system:
1. **View All Available Cars**: Displays all cars that are currently available for rent.
2. **Search for a Car by ID**: Input the ID of a car to view its details.
3. **Book a Car**: Reserve a car for a rental by providing the required details.
4. **Exit**: Exit the customer menu, go to The Main Menu.

---

## Project Structure

```
CRUD_Car_Rental/
├── main.py                # Main file to run the project
├── README.md              # Project documentation
└── requirements.txt       # List of dependencies
```

---

## Dependencies

This project uses the following Python libraries:

- **tabulate**: To display data in a tabular format.

You can install the dependencies by running:
```bash
pip install -r requirements.txt
```

---

## Future Improvements

Here are some ideas for expanding this project:

- **Database Integration**: Currently, the car data is hardcoded. Adding a database (e.g., SQLite, MySQL) would allow for persistent storage of cars and bookings.
- **Authentication System**: Implement user authentication for admins and customers.
- **GUI**: Create a graphical user interface (e.g., using Tkinter or a web-based framework) to make the application more user-friendly.
- **Booking History**: Allow customers to view their previous bookings.
- **Payment System**: Integrate a payment gateway to handle transactions for booking a car.

---


## Contributing

Contributions are welcome! If you would like to contribute to the project, feel free to fork the repository and create a pull request with your changes. Be sure to follow the style and format of the existing code.
