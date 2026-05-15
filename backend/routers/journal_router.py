from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import psycopg2
import psycopg2.extras

router = APIRouter()

class Journal(BaseModel):
    date: str
    operation: str
    status: str
    amount: int

conn_params = {
    "dbname": "erp_diplom",
    "user": "postgres",
    "password": "4568",
    "host": "localhost",
    "port": 5432
}

def get_conn():
    return psycopg2.connect(**conn_params)

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

@router.post("/")
def add_entry(entry: Journal):
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO journal (date, operation, status, amount) VALUES (%s, %s, %s, %s) RETURNING id;",
            (entry.date, entry.operation, entry.status, entry.amount)
        )
        new_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return {"id": new_id, "message": "Inserted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/{id}")
def update_entry(id: int, entry: Journal):
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(
            "UPDATE journal SET date=%s, operation=%s, status=%s, amount=%s WHERE id=%s;",
            (entry.date, entry.operation, entry.status, entry.amount, id)
        )
        conn.commit()
        cur.close()
        conn.close()
        return {"message": "Updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

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

