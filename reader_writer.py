#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import pathlib
import sqlite3
    


# In[10]:


class ReaderWriter:
    #read data from source and convert to pandas dataframe
    
    def __init__(self):
        # initialization of file_name
        self.file_name = ""
    
    def file_reader (self,file_name):
        
        self.file_name = file_name
        
        file_extension = pathlib.Path(file_name).suffix.lower()
        
        print(f'file type is {file_extension}')
        
        if (file_extension == ".csv"):
            return(self.csv_reader())
        else:
            return(self.excel_reader())
        
    def csv_reader(self):
        print(f'in csv_reader')
        df = pd.read_csv(self.file_name)
        return df
    
    def excel_reader(self):
        print(f'in excel_reader')
        df = pd.read_excel(self.file_name)
        return df
    
    def db_table_writer(self):
        
        print(f'in create_db_table')
        
        with sqlite3.connect('movie_ratings.db') as conn: #conn is connection to db
            cursor = conn.cursor() #cursor represents the object on the db in that connection
            df = pd.read_csv("Movie-Ratings.csv")
            df.head()
            #inserting data
            fields = "Movie,Genre,Rotten_Tomatoes_Rating, Audience_Ratings, Budget, Year_of_Release"
            query = f"create TABLE IF NOT EXISTS Movie_Ratings_Table ({fields})"
            cursor.execute(query)
            
            print("table Movie_Ratings_Table created")
            
            rows = [row for name, row in df.iterrows()]
            cursor.executemany(
                'insert into Movie_Ratings_Table values (?,?,?,?,?,?)', rows
            )
            
            
    def db_table_reader(self):
        print(f"in read_db_table")
        with sqlite3.connect('movie_ratings.db') as conn: #conn is connection to db
            cursor = conn.cursor() #cursor represents the object on the db in that connection
            df = pd.read_sql("select * from Movie_Ratings_Table", conn)
            print(df.head())
                 
            
    
        
        

