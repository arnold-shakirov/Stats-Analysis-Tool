import pandas as pd
import rich
import sys

df = pd.read_csv("hd2022.csv", encoding='latin1')
rich.print(df)
rich.print(df.colums)
rich.print(df.shape)
# picking columns
rich.print(df[['UNITID', 'INSTNM']])
rich.print(df.filter(regex='.*URL'))

# picking rows

# PICKING INSTITUTIONS IN FL
rich.print(df[df['STABBR'] == 'FL' and df['INSTNM']])

# Picking institutions in Florida that have 'University' in their name
fl_univ = df.query('STABBR.str == "FL" and INSTNM.str.contains("University")', engine='python')

#first 10 rows
rich.print(fl_univ.iloc[0:10])

#first 10 rows, third column
rich.print(fl_univ.iloc[0:10,2])

#first 10 rows WHats the difference ILOC and LOC
rich.print(fl_univ.iloc[0:10])

rich.print(fl_univ.loc[651])

#reset the index to the UNITID WHATS GOING ON
fl_univ.index = fl_univ['INSTNM']
rich.print(fl_univ)
rich.print(fl_univ.loc['Stetson University'])

rich.print(fl_univ.describe())
rich.print(fl_univ.count())
#rich.print(fl_univ[['ADDR',.count())

rich.print(type(df))

sys.exit()
