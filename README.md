Chocolate House CLI Application
Overview
The Chocolate House CLI Application is a Python-based command-line interface designed to manage the operations of a fictional chocolate business. This application allows users to manage seasonal chocolate flavors, track ingredient inventory, and store customer suggestions related to flavors and allergy concerns. The data is stored using an SQLite database, with optional support for SQLAlchemy ORM to simplify database interactions. The application is packaged using Docker, making it easy to deploy and run in a containerized environment.

Features
Seasonal Flavors: Add, update, view, and delete seasonal chocolate flavors with details like name, description, and availability dates.
Inventory Management: Track ingredients, quantities, and units of measurement to monitor stock levels.
Customer Suggestions: Store and review customer flavor suggestions and any reported allergy concerns.
Dockerized Application: Easily deploy and run the application in a Docker container.
Prerequisites
Python: Version 3.10 or higher
SQLite: Pre-installed with Python; used for lightweight data storage
Docker: Required to build and run the containerized application
Installation
1. Clone the Repository
Clone the repository to your local machine to get started:

bash
Copy code
git clone https://github.com/your-username/chocolate_house_cli.git
cd chocolate_house_cli
2. Set Up Python Environment
It is recommended to use a virtual environment for managing dependencies:

bash
Copy code
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate  # On macOS and Linux
# venv\Scripts\activate  # On Windows
Install the necessary dependencies:

bash
Copy code
pip install -r requirements.txt
The requirements.txt file installs necessary packages, including sqlite3 (built-in with Python), SQLAlchemy for ORM support, and any additional dependencies.

3. Set Up the Database
Run the setup_database() function to initialize the database and create the necessary tables. This setup is automatically handled when the application starts.

Running the Application
The application functions as a command-line interface (CLI). Below are the steps to perform core operations:

1. Add a New Seasonal Flavor
Use the CLI to add a seasonal chocolate flavor with details like name, description, and availability.

2. View All Flavors
List all the seasonal flavors that have been added, with their corresponding details.

3. Additional Operations
Additional functions such as delete, update, and view can be performed on both flavors and ingredients.

Dockerization
To run the application in a Docker container:

Build the Docker Image

bash
Copy code
docker build -t chocolate_house_cli .
Run the Docker Container

bash
Copy code
docker run -it chocolate_house_cli
The application will run as a CLI within the Docker container, allowing you to interact with the database and manage the Chocolate House inventory.

Acknowledgments
This project uses SQLite for lightweight database management, making it easy to set up and manage the database with minimal overhead.
SQLAlchemy is used to provide ORM (Object-Relational Mapping) capabilities, which simplifies database operations and enhances maintainability.
