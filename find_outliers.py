import numpy as np
import pandas as pd
from typing import Tuple
from copy import deepcopy as dc

def get_mean(df: pd.DataFrame, ex_vals: list[float]) -> Tuple[float, float]:
    """
    Returns the mean and standard deviation of df without poi.
    """
    values = [val for ar in df.values for val in ar]
    for ex in ex_vals:
        values.remove(
            ex
        )  # remove value of point of interest, only once if contained multiple times
    val_array = np.array(values)
    return (val_array.mean(), val_array.std())


def find_outliers(df: pd.DataFrame, stdev_factor=4.0, window_size: int = 2, key=None, exclude_nnn=True):
    """
    Finds ouliers and replace them with the mean value of their environment.

    Each cell in the dataframe is compared to its environment. The environment comprises the window_size rows and columns arround the cell.
    The mean of the environment (without the value of the cell and - if exclude_nnn - next-nearest neighbours) is calculated and if the value of the cell deviates more than stdev_factor standard deviations from that mean, it is replaced by the mean.

    Parameters:
        df (pd.DataFrame): The DataFrame to digest.
        stdev_factor (float): The factor for the standard deviation.
        window_size (int): The size of the environment.
    """
    df_new = dc(df)
    xrange = range(0, df.shape[0])
    yrange = range(0, df.shape[1])
    for idx in xrange:
        for col in yrange:
            a = idx - window_size if idx - window_size > 0 else 0
            b = idx + window_size + 1
            c = col - window_size if col - window_size > 0 else 0
            d = col + window_size + 1
            subset = df.iloc[a:b, c:d]

            if exclude_nnn:
                ex_vals = [df.iloc[pa,pb] for pa in [idx-1, idx, idx+1] for pb in [col-1, col, col+1] if pa in xrange and pb in yrange] #values of all nnn
            else:
                ex_vals = [df.iloc[idx, col]]

            env_mean, env_std = get_mean(subset, ex_vals)

            if (
                df.iloc[idx, col]
                > max(
                    env_mean + (env_std * stdev_factor),
                    env_mean - (env_std * stdev_factor),
                )
                or df.iloc[idx, col]
                < min(
                    env_mean + (env_std * stdev_factor),
                    env_mean - (env_std * stdev_factor),
                )
                or df.iloc[idx, col] < 0
            ):
                df_new.iloc[idx, col] = env_mean
    
    return (key, df_new)
    
def find_outliers_mp(args):
    return find_outliers(*args)

