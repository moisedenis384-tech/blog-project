from typing import Optional, List
from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, Field, Session, create_engine, select

# --------------------
# Database model
# --------------------
class Post(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    description: Optional[str] = None
    author: Optional[str] = None


# --------------------
# Database config
# --------------------
DATABASE_URL = "sqlite:///./blog.db"

engine = create_engine(
    DATABASE_URL,
    echo=True
)

def get_session():
    with Session(engine) as session:
        yield session


# --------------------
# Schemas
# --------------------
class PostCreate(SQLModel):
    description: str
    author: str

class PostRead(SQLModel):
    id: int
    description: Optional[str]
    author: Optional[str]


# --------------------
# CRUD
# --------------------
def create_post_db(session: Session, post_in: PostCreate) -> Post:
    post = Post.from_orm(post_in)
    session.add(post)
    session.commit()
    session.refresh(post)
    return post

def get_posts_db(session: Session) -> List[Post]:
    return session.exec(select(Post)).all()


# --------------------
# FastAPI app
# --------------------
app = FastAPI(root_path="/api/v4")

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

@app.post("/posts", response_model=PostRead)
def add_post(
    post: PostCreate,
    session: Session = Depends(get_session)
):
    return create_post_db(session, post)

@app.get("/posts", response_model=List[PostRead])
def read_posts(
    session: Session = Depends(get_session)
):
    return get_posts_db(session)
