from fastapi import FastAPI
from app import models, database
from app.routes import user, ai

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="AI Education API")

app.include_router(user.router)
app.include_router(ai.router)
