import  pandas as pd
data=pd.read_excel('D:\Clout Donations.xlsx')

data.drop_duplicates(subset=["What's your email address?", "What is the public key to your *BitClout*?"],keep = 'first', inplace = True)

df=data

df.to_csv('E:\output.csv')


