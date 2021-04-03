import numpy as np
from scipy.signal import find_peaks

import matplotlib.pyplot as plt
import librosa

def return_time_between_impacts(y:np.ndarray, nb:int, sr:int, plot = True):
    heights = np.arange(0, 2, 0.001)
    data = {}
    for height in heights:
        indices, _ = find_peaks(y, height=height)
        if len(indices) >= nb-1 and len(indices) <= nb+1 :
            seconds  = []
            for i in range(len(indices)-1):
                diff = indices[i+1]-indices[i]
                sec = diff * 1./sr
                seconds.append(sec)
            data[height] = seconds
                
    if plot: 
        fig,ax = plt.subplots()

        for height in data:
            ax.plot(data[height], label = f"height:{height}", alpha = 0.3)
        fig.legend()
        plt.show()








    
if __name__ == "__main__":
    y, sr = librosa.load("test.flac", sr=None)

    print(sr)
    return_time_between_impacts(y, 31, sr)



