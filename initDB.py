from app import APP
from app.model import DB, Entity

MOCK_DATA = ["dog", "human", "liberty"]


def init_database():
    """Initialize the database"""
    with APP.app_context():
        DB.drop_all()
        DB.create_all()
        # add a few entities
        for name in MOCK_DATA:
            entity = Entity(name)
            DB.session.add(entity)
        DB.session.commit()


if __name__ == "__main__":
    init_database()
