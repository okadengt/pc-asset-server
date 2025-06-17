from app import create_app
from app.models import init_db

app = create_app()

@app.cli.command("db_init")
def db_init():
    """Initialize the database (create tables if not exist)"""
    init_db()
    print("Database initialized.")

if __name__ == "__main__":
    app.run(host="192.168.1.119", port=5000)