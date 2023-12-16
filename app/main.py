import sqlite3


def connect_db():
  return sqlite3.connect('../expenses.db')


def add_expense(date, amount, category, description):
  conn = connect_db()
  cursor = conn.cursor()
  cursor.execute("INSERT INTO expenses (date, amount, category, description) VALUES (?, ?, ?, ?)",
                 (date, amount, category, description))
  conn.commit()
  conn.close()

def modify_expense(id, date, amount, category, description):
  conn = connect_db()
  cursor = conn.cursor()
  cursor.execute("UPDATE expenses SET date = ?, amount = ?, category = ?, description = ? WHERE id = ?",
                 (date, amount, category, description, id))
  conn.commit()
  conn.close()

def delete_expense():
  conn = connect_db()
  cursor = conn.cursor()
  cursor.execute("DELETE FROM expenses WHERE id = ?", (id,))
  conn.commit()
  conn.close()

def get_expenses():
  conn = connect_db()
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM expenses")
  expenses = cursor.fetchall()
  conn.close()
  return expenses

def get_expenses_filtered_by_category(category):
  conn = connect_db()
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM expenses WHERE category = ?", (category,))
  expenses = cursor.fetchall()
  conn.close()
  return expenses

def get_expenses_filtered_by_date(date):
  conn = connect_db()
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM expenses WHERE date = ?", (date,))
  expenses = cursor.fetchall()
  conn.close()
  return expenses

print(get_expenses())
