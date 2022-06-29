"""Perform fixed-rate mortgage calculations."""
from argparse import ArgumentParser
import math
import sys

def get_min_payment(b, f):
    """
    Calculates the minimum credit card payment based on
    the balance, the percent of the balance that needs to be paid,
    and the amount of fees that would be paid in a month
    """
    #b is the account balance
    #m is the percent of balance that needs to be paid
    # f is the fees
    
    m = 0.02
    min_payment = ((b * m) + f)
    
    if min_payment < 25:
        return 25
    else:
        return min_payment
    
def interest_charged(b, a, y = 365, d = 30):
    """
    Takes in the parameters b (balance), a (APR), y (days in year)
    and d (number of days in billing cycle) and then uses them 
    to calculate the amount of interest, i.
    """
    i = (((a/100)/y) * b * d)
    return i

def remaining_payments(balance_amount, apr, payment = 'None', credit_line = 5000, fees = 0):
    """
    Takes in the balance amount, APR, target payment amount, max credit
    and fees in order to determine the number of payments required
    to pay off the credit card balance.
    
    The program will also take into account the number of times the 
    balance remains over 25%, 50% and 75% of the credit line
    """
    months = 0
    bal_25 = 0
    bal_50 = 0
    bal_75 = 0
    
    while (balance_amount > 0):
        if payment != 'None':
            payment = get_min_payment(balance_amount, 0)
        elif payment == 'None':
            if (balance_amount > (0.75 * credit_line)):
                bal_75+=1
            elif (balance_amount > (0.59 * credit_line)):
                bal_50+=1
            elif (balance_amount > (0.25 * credit_line)):
                bal_25+=1
        
        portionOfPay = balance_amount - interest_charged(balance_amount, 1)
        balance_amount-=portionOfPay
        months+=1
        
        if balance_amount < 0:
            print("The balance on this credit card can not be paid off.")
            break
    
    return months, bal_25, bal_50, bal_75
    
   
    
def main(balance_amount, apr, payment='None', credit_line = 5000, fees = 0):
    """Computes the recommended minimum payment and displays the 
    recommended minimum payment using other functions created to show
    
    The resulting output should include print statements referencing the
    minimum payment, number of months left to pay off and the number 
    of months spent 25%, 50% or 75% over the credit line
    """
    recommended = get_min_payment(balance_amount, 0)
    pays_minimum = False
    
    while (pays_minimum == False):
        if payment == 'None':
            pays_minimum = True
        elif payment < recommended:
            print("Your target payment is less than the minimum payment")
            break
        
    total_required = remaining_payments(balance_amount, 1)
    
        
def parse_args(args_list):
  """Takes a list of strings from the command prompt and passes them through as
  arguments
  Args:
  args_list (list) : the list of strings from the command prompt
  Returns:
  args (ArgumentParser)
  """
  parser = ArgumentParser()
  parser.add_argument('balance_amount', type = float, help = 'The total amount of balance left on the credit account')
  parser.add_argument('apr', type = int, help = 'The annual APR, should be an int between 1 and 100')
  parser.add_argument('credit_line', type = int, help = 'The maximum amount of balance allowed on the credit line.')
  parser.add_argument('--payment', type = int, default = None, help = 'The amount the user wants to pay per payment, should be a positive number')
  parser.add_argument('--fees', type = float, default = 0, help = 'The fees that are applied monthly.')
  
  # parse and validate arguments
  args = parser.parse_args(args_list)
  
  if args.balance_amount < 0:
      raise ValueError("balance amount must be positive")
  if not 0 <= args.apr <= 100:
      raise ValueError("APR must be between 0 and 100")
  if args.credit_line < 1:
      raise ValueError("credit line must be positive")
  if args.payment is not None and args.payment < 0:
      raise ValueError("number of payments per year must be positive")
  if args.fees < 0:
      raise ValueError("fees must be positive")
  
  return args

if __name__ == "__main__":
  try:
      arguments = parse_args(sys.argv[1:])
  except ValueError as e:
      sys.exit(str(e))
      
  print(main(arguments.balance_amount, arguments.apr, 
             credit_line = arguments.credit_line, 
             targetamount = arguments.payment, 
             fees = arguments.fees))
