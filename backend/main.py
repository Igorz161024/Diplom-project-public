from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from backend.database import engine
from backend.modules.finance import Base, get_account_balance, add_account, add_entry
from backend.auth import create_access_token, get_current_user_role
from backend.modules.users import User   # приклад
from backend.modules.products import Product   # приклад

# нові роутери
from backend.finance_router import router as finance_router
from backend.inventory_router import router as inventory_router
from backend.purchases_router import router as purchases_router
from backend.sales_router import router as sales_router
from backend.legal_router import router as legal_router

import datetime
import pandas as pd
import io
import matplotlib.pyplot as plt
import psycopg2

app = FastAPI(
    title="ERP Diplom Project",
    description="Backend API для фінансів, інвентаризації, закупівель, продажів та юридичних документів",
    version="1.0.0"
)

# ✅ Додаємо CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# створюємо таблиці у базі при старті
Base.metadata.create_all(bind=engine)

# 🔗 Підключаємо нові роутери
app.include_router(finance_router, prefix="/api/finance", tags=["Finance"])
app.include_router(inventory_router, prefix="/api/inventory", tags=["Inventory"])
app.include_router(purchases_router, prefix="/api/purchases", tags=["Purchases"])
app.include_router(sales_router, prefix="/api/sales", tags=["Sales"])
app.include_router(legal_router, prefix="/api/legal", tags=["Legal"])

# Логін з різними ролями (9 ролей)
@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username == "admin" and form_data.password == "1234":
        role = "admin"
    elif form_data.username == "accountant" and form_data.password == "1234":
        role = "accountant"
    elif form_data.username == "hr" and form_data.password == "1234":
        role = "hr"
    elif form_data.username == "products" and form_data.password == "1234":
        role = "products"
    elif form_data.username == "pkash" and form_data.password == "1234":
        role = "pkash"
    elif form_data.username == "inventory" and form_data.password == "1234":
        role = "inventory"
    elif form_data.username == "purchases" and form_data.password == "1234":
        role = "purchases"
    elif form_data.username == "sales" and form_data.password == "1234":
        role = "sales"
    elif form_data.username == "legal" and form_data.password == "1234":
        role = "legal"
    else:
        raise HTTPException(status_code=400, detail="Невірний логін або пароль")

    access_token = create_access_token({"sub": form_data.username, "role": role})
    return {"access_token": access_token, "token_type": "bearer", "role": role}

# Ендпоінт для журналу операцій (Postgres)
def get_connection():
    return psycopg2.connect(
        dbname="erp_diplom",
        user="postgres",
        password="4568",
        host="db",
        port="5432"
    )

@app.get("/api/journal")
def read_journal():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT date, operation, status FROM journal ORDER BY date;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [{"date": str(r[0]), "operation": r[1], "status": r[2]} for r in rows]

# Ендпоінти для ролей
@app.get("/finance")
def read_finance(role: str = Depends(get_current_user_role)):
    if role not in ["accountant", "admin"]:
        raise HTTPException(status_code=403, detail="Access denied")
    return {"msg": "Finance data visible"}

@app.get("/hr")
def read_hr(role: str = Depends(get_current_user_role)):
    if role not in ["hr", "admin"]:
        raise HTTPException(status_code=403, detail="Access denied")
    return {"msg": "HR data visible"}

@app.get("/admin")
def read_admin(role: str = Depends(get_current_user_role)):
    if role != "admin":
        raise HTTPException(status_code=403, detail="Admins only")
    return {"msg": "Admin panel visible"}

@app.get("/products")
def read_products(role: str = Depends(get_current_user_role)):
    if role not in ["products", "admin"]:
        raise HTTPException(status_code=403, detail="Access denied")
    return {"msg": "Products data visible"}

@app.get("/pkash")
def read_pkash(role: str = Depends(get_current_user_role)):
    if role not in ["pkash", "admin"]:
        raise HTTPException(status_code=403, detail="Access denied")
    return {"msg": "PKash data visible"}

@app.get("/inventory")
def read_inventory(role: str = Depends(get_current_user_role)):
    if role not in ["inventory", "admin"]:
        raise HTTPException(status_code=403, detail="Access denied")
    return {"msg": "Inventory data visible"}

@app.get("/purchases")
def read_purchases(role: str = Depends(get_current_user_role)):
    if role not in ["purchases", "admin"]:
        raise HTTPException(status_code=403, detail="Access denied")
    return {"msg": "Purchases data visible"}

@app.get("/sales")
def read_sales(role: str = Depends(get_current_user_role)):
    if role not in ["sales", "admin"]:
        raise HTTPException(status_code=403, detail="Access denied")
    return {"msg": "Sales data visible"}

@app.get("/legal")
def read_legal(role: str = Depends(get_current_user_role)):
    if role not in ["legal", "admin"]:
        raise HTTPException(status_code=403, detail="Access denied")
    return {"msg": "Legal data visible"}

# Додавання проводки (захищено токеном)
@app.post("/add_entry")
def create_entry(
    amount: int,
    description: str = "Продаж товару за готівку",
    role: str = Depends(get_current_user_role)
):
    if role not in ["accountant", "admin"]:
        raise HTTPException(status_code=403, detail="Access denied")

    cash = add_account("30", "Cash", "актив")
    revenue = add_account("70", "Revenue", "дохід")

    add_entry(
        date=datetime.date.today(),
        description=description,
        lines=[
            {"account_id": cash.id, "debit": amount, "credit": 0},
            {"account_id": revenue.id, "debit": 0, "credit": amount}
        ]
    )

    return {
        "Баланс Cash": get_account_balance(cash.id),
        "Баланс Revenue": get_account_balance(revenue.id)
    }

@app.get("/balance/{account_id}")
def balance(account_id: int, role: str = Depends(get_current_user_role)):
    if role not in ["accountant", "admin"]:
        raise HTTPException(status_code=403, detail="Access denied")
    return {"account_id": account_id, "balance": get_account_balance(account_id)}

@app.get("/report")
def report(role: str = Depends(get_current_user_role)):
    if role not in ["accountant", "admin"]:
        raise HTTPException(status_code=403, detail="Access denied")

    accounts = [
        {"id": 30, "name": "Cash", "balance": get_account_balance(30)},
        {"id": 70, "name": "Revenue", "balance": get_account_balance(70)},
    ]
    df = pd.DataFrame(accounts)
    summary = df.to_dict(orient="records")
    total = df["balance"].sum()
    return {"accounts": summary, "total_balance": total}

@app.get("/plot")
def plot_report(role: str = Depends(get_current_user_role)):
    if role not in ["accountant", "admin"]:
        raise HTTPException(status_code=403, detail="Access denied")

    accounts = [
        {"id": 30, "name": "Cash", "balance": get_account_balance(30)},
        {"id": 70, "name": "Revenue", "balance": get_account_balance(70)},
    ]
    names = [acc["name"] for acc in accounts]
    balances = [acc["balance"] for acc in accounts]

    fig, ax = plt.subplots()
    ax.bar(names, balances, color=["green", "blue"])
    ax.set_title("Баланс рахунків")
    ax.set_ylabel("Сума")

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)

    return
