Chocolate House CLI Application

Overview:
This Python-based CLI application helps manage a fictional Chocolate House business. It allows the management of seasonal chocolate flavors, inventory of ingredients, and customer suggestions related to flavors and allergies. The app uses an SQLite database for storage and is packaged using Docker.

Features
SeasonalFlavors: Manage seasonal flavors with details like name, description, and availability.
Inventory: tracking ingredients, quantities, and units of measurement.
CustomerSuggestions: Store customer flavor suggestions and allergy concerns.
Dockerized Application: The app is containerized using Docker.

Prerequisites
Python 3.10 .
SQLite 
Docker 

Installation
1. Clone the repository
First, clone the repository to your local machine.

2. Set Up Python Environment
Create a virtual environment and install dependencies:
The requirements.txt file will install all the necessary Python packages, including sqlite3, SQLAlchemy for ORM support, and other dependencies.

3. Set Up Database
Run the setup_database() function to initialize the database and create necessary tables. This is done automatically when the application runs.



Running the Application
The application can be run as a CLI (command-line interface). 
1. Add a New Seasonal Flavor :


2. List of all added flavours : 

3. We can also perform other operations such as delete and display the list as well.

4. Dockerization
To run the application within a Docker container, follow these steps:
Build the Docker Image:


