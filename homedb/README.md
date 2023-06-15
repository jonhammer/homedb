# HomeDB: Smart Home Device Inventory Management

HomeDB is an inventory management solution for smart home devices. HomeDB is built with the Django Web Framework, inspired by the functionality and effectiveness of [Netbox](https://github.com/netbox-community/netbox), but specifically tailored for smart home devices.

## Features

- **Device Tracking:** Track all your smart home devices with their types, models, specifications, locations and more.
- **Vendor-Agnostic:** Designed to be compatible with a wide array of smart home devices, regardless of the manufacturer or model.
- **Search & Filter:** Powerful search and filter options that help you find devices based on different criteria.
- **APIs for Integration:** HomeDB provides an API allowing for integration with other systems or services.

## Getting Started

Before starting, make sure you have `Python 3.9+`, `Poetry`, and `make` installed.

1. Clone the repository:
    ```bash
    git clone https://github.com/jonhammer/homedb.git
    ```
2. Go to the project directory:
    ```bash
    cd homedb
    ```
3. Install the project requirements:
    ```bash
    make install
    ```
4. Run migrations:
    ```bash
    make migrate
    ```
5. Add a superuser:
    ```bash
    make superuser
    ```
6. Run the development server:
    ```bash
    make runserver
    ```
   
7. Navigate to the admin page or API documentation:
    - Admin: http://localhost:8000/admin
    - API: http://localhost:8000/api/v1/docs

## Tests and Linting

To run the tests:
```
make test
```

To format with Black and isort:
```
make format
```
