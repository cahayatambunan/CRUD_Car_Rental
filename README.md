# CRUD Car Rental System

### Overview

This project is a **Car Rental Management System** built using **Python**. It features basic CRUD (Create, Read, Update, Delete) operations to manage vehicle data for a car rental service. It is designed for two types of users: **Customers** and **Admins**. Admins can manage car listings, while customers can view, search, and book available cars.

---

## Features

### Admin Features
- View all cars in the system.
- Add new cars to the listing.
- Update existing car details.
- Delete cars from the system.

### Customer Features
- Browse available cars.
- Search for cars by ID.
- Book a car.

### Data Display
The project uses the `tabulate` library to display data in a neat, tabular format for both admins and customers.

---

## Installation

To run this project, you need to have **Python 3.x** installed on your machine.

### Step-by-step installation:

1. Clone this repository:
    ```bash
    git clone https://github.com/cahayatambunan/CRUD_Car_Rental.git
    ```

2. Navigate to the project directory:
    ```bash
    cd CRUD_Car_Rental
    ```

3. Install the required dependencies:
    ```bash
    pip install tabulate
    ```

4. Run the project:
    ```bash
    python main.py
    ```

---

## Usage

### Admin Menu

Admins can:
- View all cars.
- Add new cars by providing details like type, transmission, seats, status, and price.
- Update existing car details.
- Delete cars from the database.

### Customer Menu

Customers can:
- Browse all available cars.
- Search for cars using a specific car ID.
- Book a car by selecting from the available listings.

---

## Project Structure

```
├── main.py                # Main file to run the project
├── README.md              # Project description and instructions
└── requirements.txt       # Required Python libraries
```

---

## Dependencies

This project uses the following Python libraries:

- **tabulate**: To display data in a table format.
  
Install them using:
```bash
pip install -r requirements.txt
```

---

## Future Improvements

- Implement database integration for persistent data storage.
- Add a user authentication system.
- Introduce a front-end interface for a more user-friendly experience.
- Implement booking history and payment management.

---

## Contributing

Feel free to fork this project, make your improvements, and submit a pull request!

