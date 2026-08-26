import pandas as pd
import time 
from functools import wraps
import logging 

def timeit(method):
    """
    Timeit Decorator 
        Description: adds timekeeping functionality for any logging function, usses the logger from the function 
    """
    # inner function that will be timed
    @wraps(method)
    def timed(*args, **kwargs):
        # get logger from function 
        logger = logging.getLogger(method.__module__)

        ts = time.time()
        result = method(*args, **kwargs)
        te = time.time()

        # rounding to n decimals and printing timed output 
        elapsed = round((te - ts), 5)
        logger.info(f"{method.__name__} took {elapsed} seconds to run")

        return result
    return timed


df = pd.read_csv("../Datasets/sinac2016DatosAbiertos.csv")

print(df.head)
