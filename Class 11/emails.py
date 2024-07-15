import os
import pandas as pd

print("My current working directory", os.getcwd())

os.chdir('C:/Users/Administrator/AppData/Local/Programs/Python/Python312/python.exe "c:/Development/Class 11/emails')

print('My lists part 2 folder has a new cwd', os.getcwd())

baseline_df = pd.read_csv('emails(1).csv')

# print(baseline)
baseline_df['uni-id'] = baseline_df['uni-id'] + '@gmail.com'

baseline_df = to_csv ( 'output.xlxs' index=False )
