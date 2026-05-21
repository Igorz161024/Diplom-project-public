from fastapi import FastAPI
from backend.schemas import journal_router

app = FastAPI(title="ERP Diplom Project")

# Підключення роутера журналу
app.include_router(journal_router.router, prefix="/api/journal", tags=["journal"])
