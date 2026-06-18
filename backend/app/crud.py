from sqlalchemy.orm import Session

from .models import User
from .schemas import UserCreate
from .auth import hash_password

def create_user(
    db: Session,
    user: UserCreate
):
    encrypted_password = hash_password(
        user.password
    )

    db_user = User(
        username=user.username,
        email=user.email,
        phone=user.phone,
        password=encrypted_password
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user