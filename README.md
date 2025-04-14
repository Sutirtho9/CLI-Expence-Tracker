# 🧾 CLI Expense Tracker

A simple command-line interface (CLI) expense tracker built with Python. You can add, view, summarize, and delete your expenses using intuitive commands. Data is stored in a CSV file.

---

## 🚀 Features
- Add expenses with category, date, and amount
- List all expenses, or filter by category/month
- Show monthly/category-wise summary
- Delete an expense by its ID

---

## 📁 Project Structure

```
CLI_expense_tracker/
├── expense.csv         # Stores the data
├── main.py             # Main application script
```

---

## 📦 Requirements
- Python 3.x

---

## ⚙️ How to Run

```bash
python main.py [command] [options]
```
##📌 Commands & Options
### ➕ Add Expense
```
python main.py add -c CATEGORY -a AMOUNT -d YYYY-MM-DD
```
- c or --category: Category of the expense (e.g., Food)

- a or --amount: Amount spent (e.g., 200)

- d or --date: Date in YYYY-MM-DD format

### 📄 List Expenses
```
python main.py list [--category CATEGORY] [--month MONTH_NUM]
```
- --category or -c : Filter by category

- --month or -m : Filter by month (1–12)

### 📊 Summary
```
python main.py sum [--category CATEGORY] [--month MONTH_NUM]
```
Displays total expenses optionally filtered by category or month

### ❌ Delete Expense
```
python main.py delete --id EXPENSE_ID
```
Deletes the expense with the provided ID

### 🧠 Example Usage

```
python main.py add -c Food -a 120 -d 2025-04-13
python main.py list -m 4
python main.py sum -c Travel
python main.py delete --id 3
```
## 📝 Notes
The script creates expense.csv on first run if it doesn’t exist.

Date must be in YYYY-MM-DD format.

## License
MIT License


