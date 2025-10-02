from pulp import LpMaximize, LpProblem, LpVariable, lpSum, value
import pandas as pd
prob = LpProblem('BudgetOpt', LpMaximize)
fitness = LpVariable('Fitness', 0, 500)
theology = LpVariable('Theology', 0, 300)
finance_tools = LpVariable('FinanceTools', 0, 200)
prob += 2*fitness + 3*theology + 4*finance_tools
prob += fitness + theology + finance_tools <= 1000
prob.solve()
df = pd.DataFrame({
    'Category': ['Fitness', 'Theology', 'Finance Tools'],
    'Allocated': [value(fitness), value(theology), value(finance_tools)]
})
print(df)
print(f'Total Utility: {value(prob.objective)}')