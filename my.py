import pandas as pd
import numpy as np
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        df = func()
        end = time.perf_counter()
        print(end-start)
        print(df)
    return wrapper

@timer
def dummmy_df():
    df = pd.DataFrame(np.random.rand(5,3))
    return df    
dummmy_df()
