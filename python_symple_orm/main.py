import sqlite3


class SimpleORM:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, columns):
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})")
        self.conn.commit()

    def insert_data(self, table_name, **kwargs):
        columns = ", ".join(kwargs.keys())
        placeholders = ", ".join(["?"] * len(kwargs))
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        values = tuple(kwargs.values())
        self.cursor.execute(query, values)
        self.conn.commit()

    def read_data(self, table_name):
        self.cursor.execute(f"SELECT * FROM {table_name}")
        return self.cursor.fetchall()

    def update_data(self, table_name, id, **new_data):
        set_values = ", ".join([f"{key} = ?" for key in new_data.keys()])
        query = f"UPDATE {table_name} SET {set_values} WHERE id = ?"
        values = tuple(list(new_data.values()) + [id])
        self.cursor.execute(query, values)
        self.conn.commit()

    def delete_data(self, table_name, id):
        query = f"DELETE FROM {table_name} WHERE id = ?"
        self.cursor.execute(query, (id,))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()


# Example usage:
if __name__ == "__main__":
    orm = SimpleORM("db.sqlite3")

    # # Create a table with an auto-incremental ID
    orm.create_table(
        "users", "id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER"
    )

    # # Insert data (ID is auto-incremented)
    orm.insert_data("users", name="John", age=32)

    # # Read and print data
    data = orm.read_data("users")
    print("Data:", data)

    # Update data
    orm.update_data("users", id=1, name="Alicy", age=27)
    updated_data = orm.read_data("users")
    print("Updated Data:", updated_data)

    # Delete data
    orm.delete_data("users", id=3)
    new_data = orm.read_data("users")
    print("Data after deletion:", new_data)

    # Close the connection
    orm.close_connection()
