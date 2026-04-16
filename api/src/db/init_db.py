from db.base import Base
from db.session import engine
import db.model_registry


def init_db() -> None:
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    try:
        init_db()
    except Exception as e:
        print(f"Error while creating tables: {e}")
    else:
        print("Tables created successfully.")