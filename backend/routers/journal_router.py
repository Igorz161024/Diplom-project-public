from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import psycopg2
import psycopg2.extras

# Ініціалізація роутера
router = APIRouter()

# Модель для записів журналу
class Journal(BaseModel):
    date: str
    description: str
    status: str
    amount: float
    entry_id: int | None = None

# Параметри підключення до Postgres через ім’я контейнера
conn_params = {
    "dbname": "erp_diplom",
    "user": "postgres",
    "password": "4568",
    "host": "erp_db",   # ✅ ім’я контейнера бази
    "port": 5432        # ✅ внутрішній порт Postgres
}

def get_conn():
    return psycopg2.connect(**conn_params)

# Отримати всі записи
@router.get("/")
def get_all():
    try:
        conn = get_conn()
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute("SELECT * FROM journal ORDER BY id;")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Додати новий запис
@router.post("/")
def add_entry(entry: Journal):
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO journal (date, description, status, amount, entry_id) VALUES (%s, %s, %s, %s, %s) RETURNING id;",
            (entry.date, entry.description, entry.status, entry.amount, entry.entry_id)
        )
        new_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return {"id": new_id, "message": "Inserted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Оновити запис
@router.put("/{id}")
def update_entry(id: int, entry: Journal):
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(
            "UPDATE journal SET date=%s, description=%s, status=%s, amount=%s, entry_id=%s WHERE id=%s;",
            (entry.date, entry.description, entry.status, entry.amount, entry.entry_id, id)
        )
        conn.commit()
        cur.close()
        conn.close()
        return {"message": "Updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Видалити запис
@router.delete("/{id}")
def delete_entry(id: int):
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("DELETE FROM journal WHERE id=%s;", (id,))
        conn.commit()
        cur.close()
        conn.close()
        return {"message": "Deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
