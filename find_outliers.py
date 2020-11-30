import numpy as np
import pandas as pd
from typing import Tuple
from copy import deepcopy as dc
from streakimage2.streakimage import StreakImage

def get_mean(df: pd.DataFrame, poi: Tuple[int]) -> Tuple[float]:
    """
    Returns the mean and standard deviation of df without poi.
    """
    values = [val for ar in df.values for val in ar]
    values.remove(
        df.iloc[poi]
    )  # remove value of point of interest, only once if contained multiple times
    val_array = np.array(values)
    return (val_array.mean(), val_array.std())


def find_outliers(img: StreakImage, stdev_factor=4.0, window_size: int = 2, key=None):
    """
    Finds ouliers and replace them with the mean value of their environment.

    Each cell in the dataframe is compared to its environment. The environment comprises the window_size rows and columns arround the cell.
    The mean of the environment (without the value of the cell) is calculated and if the value of the cell deviated more than stdev_factor standard deviations from that mean, it is replaced by the mean.

    Parameters:
        df (pd.DataFrame): The DataFrame to digest.
        stdev_factor (float): The factor for the standard deviation.
        window_size (int): The size of the environment.
    """
    img_new = dc(img)
    df = img.data
    df_new = img_new.data
    for idx in range(0, df.shape[0]):
        for col in range(0, df.shape[1]):
            a = idx - window_size if idx - window_size > 0 else 0
            b = idx + window_size + 1
            c = col - window_size if col - window_size > 0 else 0
            d = col + window_size + 1
            subset = df.iloc[a:b, c:d]

            poi = (
                idx if idx < window_size else window_size,
                col if col < window_size else window_size,
            )
            env_mean, env_std = get_mean(subset, poi)

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
    
    return (key, img_new)
    
def find_outliers_mp(args):
    return find_outliers(*args)

