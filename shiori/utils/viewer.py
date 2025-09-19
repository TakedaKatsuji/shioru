import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def set_plot_params():
    sns.set_theme()
    plt.style.use("ggplot")
    plt.rcParams["font.family"] = "Arial"
    plt.rcParams["xtick.color"] = "black"
    plt.rcParams["ytick.color"] = "black"
    plt.rcParams["axes.labelcolor"] = "black"
    plt.rcParams["text.color"] = "black"
    plt.rcParams["figure.facecolor"] = "white"


def freedman_diaconis_bins(arr):
    n = arr.shape[0]
    q25, q75 = np.percentile(arr, [25,75])
    iqr = q75 - q25
    bin_width = 2 * iqr / np.cbrt(n)
    bins = int(np.ceil((arr.max()- arr.min())/bin_width))
    return bins, bin_width