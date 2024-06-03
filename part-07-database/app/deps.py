from typing import Generator

from app.db.session import SessionLocal


def get_db() -> Generator:
    db = SessionLocal()
    db.current_user_id = None
    try:
        yield db # we yield the db here, so that it is available to use in any of our path operations
    finally:
        db.close()
