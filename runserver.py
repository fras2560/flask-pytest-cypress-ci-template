import os
from app import APP
if __name__ == "__main__":
    if (os.environ.get("DATABASE_URL") == "" or
            os.environ.get("DATABASE_URL") is None):
        # init a memory database to use
        from initDB import init_database
        print("Initializing database")
        init_database()
    start = False
    port = 5000
    debug = os.environ.get("DEBUG", False)
    while not start and port < 5010:
        try:
            APP.run(debug=debug, port=port)
            start = True
        except OSError as e:
            print(e)
            print(f"Port:{port} taken trying another")
            port += 1
