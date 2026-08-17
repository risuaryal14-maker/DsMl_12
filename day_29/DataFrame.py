import pandas as pd
a={
     'name': ['rickson','rohan','rahul',None,None,],
     'state':['kathmandu','bhaktapur','koshi',None,None],
     'country':['Nepal', 'Nepal','Nepal',None,None],
     'qualification':['ai/ml','BCA','MA',None,None]


}
df=pd.DataFrame(a)
print(df)