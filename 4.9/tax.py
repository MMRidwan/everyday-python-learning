# Problem

# You are building a payroll system. 
# Write a function calculate_tax(income) that computes the total tax owed using a progressive (marginal) bracket system. 
# This means each bracket only applies to the income that falls within it — not the full amount.

# $0 – $10,000 → 10%
# $10,001 – $40,000 → 20%
# $40,001 – $80,000 → 30%
# Above $80,000 → 40%

# Example — income of $50,000:
# First $10,000 × 10% = $1,000
# Next $30,000 × 20% = $6,000
# Last $10,000 × 30% = $3,000
# Total tax = $10,000

# Also return: the effective tax rate as a percentage (tax / income × 100, rounded to 2 decimal places).

def tax_calculator(income) :
    total = 0
    
    if income <= 10000 :
        tax = .1
        total = income + income * tax
    
    elif 10001 <= income <= 40000 :
        
        txIncome1 = (10000 - (10000 * .1))
        txIncome2 = (income - 10000) -  ((income - 10000) * .2)
        
        total = txIncome1 + txIncome2
        
    elif 40001 <= income <= 80000 :

        txIncome1 = (10000 - (10000 * .1))
        txIncome2 = (30000) -  ((30000) * .2)
        txIncome3 = (income - 40000) - ((income - 40000)  * .3)
        total = txIncome1 + txIncome2 + txIncome3
        
    elif income > 80000 : 

        txIncome1 = (10000 - (10000 * .1))
        txIncome2 = (30000) -  ((30000) * .2)
        txIncome3 = (40000) -  ((40000) * .3)
        txIncome4 = (income - 80000) - ((income - 80000)  * .4)
        
        total = txIncome1 + txIncome2 + txIncome3 + txIncome4
    
    else :
        total = 0
        
    print(total)
    print(str(100- (total*100)/income))
        

tax_calculator(50000)


# Next Time do 
# def take_home_calculator(income):
#     if income < 0:
#         print("Invalid income")
#         return

#     tax = 0

#     if income <= 10000:
#         tax = income * 0.10

#     elif income <= 40000:
#         tax = (10000 * 0.10) + ((income - 10000) * 0.20)

#     elif income <= 80000:
#         tax = (10000 * 0.10) + (30000 * 0.20) + ((income - 40000) * 0.30)

#     else:
#         tax = (10000 * 0.10) + (30000 * 0.20) + (40000 * 0.30) + ((income - 80000) * 0.40)

#     take_home = income - tax
#     effective_rate = round((tax / income) * 100, 2)

#     print(f"Gross income:   ${income:,.2f}")
#     print(f"Tax owed:       ${tax:,.2f}")
#     print(f"Take-home pay:  ${take_home:,.2f}")
#     print(f"Effective rate: {effective_rate}%")


# take_home_calculator(50000)