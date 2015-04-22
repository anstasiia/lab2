import pandas as pd

def read_and_filter(fileName):
    df = pd.read_csv("downloads/%s"%fileName, index_col=False, header=1)
    df = df[['year','week','VCI','TCI','VHI','%Area_VHI_LESS_15','%Area_VHI_LESS_35']]
    df = df[(df['VHI']>=0)]
    return df
