import argparse
import datetime

expenses=[]
expense_id=1

def add_expense(args):
      global expense_id
      expenses.append({"id": expense_id, 
                       "Description": args.description, 
                       "Amount":args.amount})
      print("Expense Added successfully")
      expense_id+=1

def list_view(args):
     print("ID  Description   Amount")
     for exp in expenses:
          print(f"{exp['id']}  {exp['Description']}  \u20B9{exp['Amount']}")

def summary(args):
    total=0
    for exp in expenses:
         total+=exp['Amount']
    print(f"Total Amount: \u20B9{total}")

def delete_expense(args):
    for exp in expenses:
         if exp['id']==args.id:
              list.remove(exp)
    print("Expense removed successfully")



# main parser
parser=argparse.ArgumentParser(prog="Expense Tracker",description="Manage your expenses")
subparsers=parser.add_subparsers(dest="command")

# add parser
add_parser= subparsers.add_parser("add", help="adds new Expense")
add_parser.add_argument("--description", required=True, help="Expense description")
add_parser.add_argument("--amount", required=True, type=float, help="Amount to be added")
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
