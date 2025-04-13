import argparse
import csv
import os


CSV_FILE="expense.csv"

if not os.path.exists(CSV_FILE):
     with open(CSV_FILE, mode='w', newline="") as f:
          writer=csv.DictWriter(f,fieldnames=["ID","Description","Amount"])
          writer.writeheader()

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


def read_expense():
     with open(CSV_FILE, mode='r', newline="") as f:
          reader=csv.DictReader(f)
          return list(reader)
     
def write_expenses(expenses):
    with open(CSV_FILE, mode="w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["ID", "Description", "Amount"])
        writer.writeheader()
        writer.writerows(expenses)

def add_expense(args):
      
      new_expense={"ID": str(get_next_id()), 
                       "Description": args.description, 
                       "Amount":args.amount}
      with open(CSV_FILE, mode='a',newline="") as f:
           writer=csv.DictWriter(f,fieldnames=["ID","Description","Amount"])
           writer.writerow(new_expense)
      print("Expense Added successfully")

def list_view(args):
    expenses = read_expense()
    print(f"{'ID':<5} {'Description':<20} {'Amount (₹)':>10}")
    print("-" * 40)
    for exp in expenses:
        print(f"{exp['ID']:<5} {exp['Description']:<20} {exp['Amount']:>5}")

def summary(args):
    expenses = read_expense()
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
add_parser.add_argument("--description", required=True, help="Expense description")
add_parser.add_argument("--amount", required=True, type=int, help="Amount to be added")
add_parser.set_defaults(func=add_expense)

#list parser
list_parser = subparsers.add_parser("list", help="shows transactions history")
list_parser.set_defaults(func=list_view)

#summary parser 
summary_parser = subparsers.add_parser("sum", help="shows summary")
summary_parser.set_defaults(func=summary)

#delete parser
delete_parser=subparsers.add_parser("delete",help="deletes transaction")
delete_parser.add_argument("--id",required=True,help="Id of record to be deleted", type=int)
delete_parser.set_defaults(func=delete_expense)

args=parser.parse_args()
args.func(args)
