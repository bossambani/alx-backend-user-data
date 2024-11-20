from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)
    session_id = Column(String, nullable=True)
    reset_token = Column(String, nullable=True)

    def __repr__(self):
        return f"<User(id={self.id}, email='{self.email}')>"
    
if __name__ == "__main__":
    engine = create_engine("sqlite:///example.db")
    Base.metadata.create_all(engine)
    print("Database and users table created.")