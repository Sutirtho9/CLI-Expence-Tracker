import argparse
import csv
import os
from datetime import datetime

CSV_FILE="expense.csv"

#Adds Header to csv file
if not os.path.exists(CSV_FILE):
     with open(CSV_FILE, mode='w', newline="") as f:
          writer=csv.DictWriter(f,fieldnames=["ID","Category","Date","Amount"])
          writer.writeheader()

def valid_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        raise argparse.ArgumentTypeError("Date must be in YYYY-MM-DD format")

#Function to get the next row
def get_next_id():
    try:
        with open(CSV_FILE, mode="r", newline="") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            if rows:
                return int(rows[-1]["ID"]) + 1
    except FileNotFoundError:
        pass
    return 1

#Fucntion to read values
def read_expense():
     with open(CSV_FILE, mode='r', newline="") as f:
          reader=csv.DictReader(f)
          return list(reader)
     
def write_expenses(expenses):
    with open(CSV_FILE, mode="w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["ID", "Category", "Date","Amount"])
        writer.writeheader()
        writer.writerows(expenses)

def add_expense(args):
      
      new_expense={"ID": str(get_next_id()), 
                       "Category": args.category,
                       "Date": args.date,
                       "Amount":args.amount}
      with open(CSV_FILE, mode='a',newline="") as f:
           writer=csv.DictWriter(f,fieldnames=["ID","Category","Date","Amount"])
           writer.writerow(new_expense)
      print("Expense Added successfully")

def list_view(args):

    expenses = read_expense()
    
    if args.category:
        expenses = [exp for exp in expenses if exp["Category"].lower() == args.category.lower()]
    
    if args.month:
        expenses = [exp for exp in expenses 
                    if datetime.strptime(exp['Date'], "%Y-%m-%d").month ==args.month]
    
    print(f"{'ID':<5} {'Category':<15} {'Date':<12} {'Amount (₹)':>10}")
    print("-" * 50)
    for exp in expenses:
        print(f"{exp['ID']:<5} {exp['Category']:<15} {exp['Date']:<12} {exp['Amount']:>5}")

def summary(args):
    expenses = read_expense()
    if args.category:
        expenses = [exp for exp in expenses if exp["Category"].lower() == args.category.lower()]
    
    if args.month:
        expenses = [exp for exp in expenses 
                    if datetime.strptime(exp['Date'], "%Y-%m-%d").month ==args.month]
    total=0
    for exp in expenses:
         total+=int(exp['Amount'])
    print(f"Total Amount: \u20B9{total}")

def delete_expense(args):
    expenses = read_expense()
    updated_expense=[exp for exp in expenses if int(exp["ID"])!=args.id]
    if len(expenses)==len(updated_expense):
        print("No expense found")
    else:
        write_expenses(updated_expense)
        print("Expense removed successfully")



# main parser
parser=argparse.ArgumentParser(prog="Expense Tracker",description="Manage your expenses")
subparsers=parser.add_subparsers(dest="command")

# add parser
add_parser= subparsers.add_parser("add", help="adds new Expense")
add_parser.add_argument("--category","-c", required=True, help="Expense description")
add_parser.add_argument("--date","-d", required=True,type=valid_date, help="Expense date in YYYY/MM/DD")
add_parser.add_argument("--amount","-a", required=True, type=int, help="Amount to be added")
add_parser.set_defaults(func=add_expense)

#list parser
list_parser = subparsers.add_parser("list", help="shows transactions history")
list_parser.add_argument("--category","-c",help="sort expenses by category")
list_parser.add_argument("--month","-m",choices=range(1,13),  type=int ,help="sort expenses by month(1-12)")
list_parser.set_defaults(func=list_view)

#summary parser 
summary_parser = subparsers.add_parser("sum", help="shows summary")
summary_parser.add_argument("--category","-c",help="Summary by category")
summary_parser.add_argument("--month","-m",choices=range(1,13),  type=int ,help="sort expenses by month(1-12)")
summary_parser.set_defaults(func=summary)

#delete parser
delete_parser=subparsers.add_parser("delete",help="deletes transaction")
delete_parser.add_argument("--id",required=True,help="Id of record to be deleted", type=int)
delete_parser.set_defaults(func=delete_expense)

args = parser.parse_args()

if hasattr(args, 'func'):
    args.func(args)
else:
    parser.print_help()