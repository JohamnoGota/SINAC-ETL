import pandas as pd
import time 

def timeit(method):
    """
    Timeit Decorator 
        Description: adds timekeeping functionality for any function, output is not modified and time is printed to terminal  
    """
    # inner function that will be timed
    def timed(*args, **kwargs):
        ts = time.time()
        result = method(*args, **kwargs)
        te = time.time()
        # rounding to n decimals and printing timed output 
        timed = round((te - ts), 5)
        print(f"{method.__name__} took {timed} seconds to run")
        return result
    return timed


df = pd.read_csv("/Users/juanmagonzalez/Documents/GitHub/SINAC - ETL/Datasets/sinac2016DatosAbiertos.csv")

print(df.head)
