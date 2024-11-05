import sqlite3

class Database:
    def __init__(self, db_name="chocolate_house.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS seasonal_flavors (
                    id INTEGER PRIMARY KEY,
                    flavor_name TEXT NOT NULL,
                    description TEXT,
                    availability BOOLEAN DEFAULT 1
                )
            ''')
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS ingredients (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    quantity INTEGER,
                    unit TEXT
                )
            ''')
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS customer_suggestions (
                    id INTEGER PRIMARY KEY,
                    customer_name TEXT NOT NULL,
                    flavor_suggestion TEXT,
                    allergy_concerns TEXT
                )
            ''')

    # Add a Seasonal Flavor
    def add_flavor(self, flavor_name, description, availability=True):
        with self.conn:
            self.conn.execute(
                "INSERT INTO seasonal_flavors (flavor_name, description, availability) VALUES (?, ?, ?)",
                (flavor_name, description, availability)
            )

    # List Seasonal Flavors
    def list_flavors(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM seasonal_flavors")
        return cursor.fetchall()

    # Delete Seasonal Flavor by ID
    def delete_flavor(self, flavor_id):
        with self.conn:
            self.conn.execute("DELETE FROM seasonal_flavors WHERE id = ?", (flavor_id,))
        print(f"Flavor with ID {flavor_id} deleted.")

    # Add Ingredient
    def add_ingredient(self, name, quantity, unit):
        with self.conn:
            self.conn.execute(
                "INSERT INTO ingredients (name, quantity, unit) VALUES (?, ?, ?)",
                (name, quantity, unit)
            )

    # List Ingredients
    def list_ingredients(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM ingredients")
        return cursor.fetchall()

    # Delete Ingredient by ID
    def delete_ingredient(self, ingredient_id):
        with self.conn:
            self.conn.execute("DELETE FROM ingredients WHERE id = ?", (ingredient_id,))
        print(f"Ingredient with ID {ingredient_id} deleted.")

    # Add Customer Suggestion
    def add_customer_suggestion(self, customer_name, flavor_suggestion, allergy_concerns=""):
        with self.conn:
            self.conn.execute(
                "INSERT INTO customer_suggestions (customer_name, flavor_suggestion, allergy_concerns) VALUES (?, ?, ?)",
                (customer_name, flavor_suggestion, allergy_concerns)
            )

    # List Customer Suggestions
    def list_suggestions(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM customer_suggestions")
        return cursor.fetchall()

    # Delete Customer Suggestion by ID
    def delete_suggestion(self, suggestion_id):
        with self.conn:
            self.conn.execute("DELETE FROM customer_suggestions WHERE id = ?", (suggestion_id,))
        print(f"Customer suggestion with ID {suggestion_id} deleted.")
