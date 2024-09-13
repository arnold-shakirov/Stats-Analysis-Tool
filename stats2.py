import pandas as pd

df = pd.read_parquet("/data/nyctaxi/yellow_tripdata_2023-11.parquet")
print(df)
print(df.columns)


#cd //our folder sub directory
#//no pandas installed or anything
#python -m virtualenv venv
#it says a lot of things
#one virt env for the whole class
#source venv/bin/activate //EVERY TIME USE THIS
#this command every time we come back to a server
#now we can pip install anything we want
#ssh ashakirov@10.80.23.119 connect to a server //THIS IS FIRST
#go to the right folder and activate the environment
