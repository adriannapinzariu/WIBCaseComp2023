#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Initialize variables
sales = [12000]
operating_expenses = [12000]
advertising_expense = [5000]
research_and_development_expense = [10000]
startup_costs = [10000]
cash = [40000]
accounts_receivable = [30000]
prepaid_assets = [3000]
property_plant_and_equipment = [40000]
accounts_payable = [15000]
unearned_revenue = [5000]
long_term_debt = [20000]
equity = [73000]


# In[6]:


# Set growth rates for various financial metrics
sales_growth_rate = 0.05
operating_expenses_growth_rate = 0.04
advertising_expense_growth_rate = 0.03
research_and_development_expense_growth_rate = 0.02
startup_costs_growth_rate = 0.01
accounts_receivable_growth_rate = 0.01
prepaid_assets_growth_rate = 0.01
property_plant_and_equipment_growth_rate = 0.01
accounts_payable_growth_rate = 0.02
unearned_revenue_growth_rate = 0.03
long_term_debt_growth_rate = 0.03
equity_growth_rate = 0.05


# In[7]:


# Generate financial projections for the next 10 years
for year in range(2023, 2033):
    # Calculate financial metrics for the current year
    sales.append(sales[-1] * (1 + sales_growth_rate))
    operating_expenses.append(operating_expenses[-1] * (1 + operating_expenses_growth_rate))
    advertising_expense.append(advertising_expense[-1] * (1 + advertising_expense_growth_rate))
    research_and_development_expense.append(research_and_development_expense[-1] * (1 + research_and_development_expense_growth_rate))
    startup_costs.append(startup_costs[-1] * (1 + startup_costs_growth_rate))
    accounts_receivable.append(accounts_receivable[-1] * (1 + accounts_receivable_growth_rate))
    prepaid_assets.append(prepaid_assets[-1] * (1 + prepaid_assets_growth_rate))
    property_plant_and_equipment.append(property_plant_and_equipment[-1] * (1 + property_plant_and_equipment_growth_rate))
    accounts_payable.append(accounts_payable[-1] * (1 + accounts_payable_growth_rate))
    unearned_revenue.append(unearned_revenue[-1] * (1 + unearned_revenue_growth_rate))
    long_term_debt.append(long_term_debt[-1] * (1 + long_term_debt_growth_rate))
    equity.append(equity[-1] * (1 + equity_growth_rate))
    cash.append(cash[-1] + sales[-1] - operating_expenses[-1])   


# In[8]:


# Print financial projections for the next 10 years
print("Year\tSales\tOperating Expenses\tCash\tAccounts Receivable\tPrepaid Assets\tProperty, Plant, and Equipment\tAccounts Payable\tUnearned Revenue\tLong-term Debt\tEquity")
for i in range(len(sales)):
    print(f"{2022+i}\t{sales[i]:.2f}\t{operating_expenses[i]:.2f}\t{cash[i]:.2f}\t{accounts_receivable[i]:.2f}\t{prepaid_assets[i]:.2f}\t{property_plant_and_equipment[i]:.2f}\t{accounts_payable[i]:.2f}\t{unearned_revenue[i]:.2f}")



