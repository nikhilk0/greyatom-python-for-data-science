# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 


# code starts here
bank = pd.read_csv(path)
categorical_var = bank.select_dtypes(include='object')
print(categorical_var)
numerical_var = bank.select_dtypes(include='number')
print(numerical_var)

# code ends here


# --------------
# code starts here
banks = bank.drop('Loan_ID',1)
print(banks.isnull().sum())
bank_mode = banks.mode().iloc[0]
banks.fillna(bank_mode,inplace=True)
print(banks)
#code ends here


# --------------
# Code starts here
avg_loan_amount = pd.pivot_table(banks,index=['Gender','Married','Self_Employed'],values='LoanAmount',aggfunc='mean')

print(avg_loan_amount)

# code ends here



# --------------
# code starts here
loan_approved_se = banks[(banks['Self_Employed']== 'Yes') & (banks['Loan_Status'] == 'Y')].count()
loan_approved_nse = banks[(banks['Self_Employed']== 'No') & (banks['Loan_Status'] == 'Y')].count()
percentage_se = (loan_approved_se['Self_Employed']*100/614)
percentage_nse = (loan_approved_nse['Self_Employed']*100/614)
print(percentage_se)

# code ends here


# --------------
# code starts here

loan_term = banks['Loan_Amount_Term'].apply(lambda x:x/12)
big_loan_term = loan_term[loan_term >= 25].count()
print(big_loan_term)
# code ends here


# --------------
# code ends here
columns_to_show = ['ApplicantIncome', 'Credit_History']
loan_groupby = banks.groupby(['Loan_Status'])[columns_to_show]

mean_values = loan_groupby.agg([np.mean])
print(mean_values)

# code ends here


