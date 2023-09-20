import pandas as pd
from utils.constants import PARTITION_KEY_PRETTY, G_PROTEIN_PER_GBP_PRETTY

def plot_bar(
        data: pd.DataFrame,
        y_col: str,
        x_col: str,
        y_label: str,
        x_label: str
    ):
    ax = data.plot.barh(x=x_col, y=y_col)
    ax.get_legend().remove()
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.invert_yaxis()
    fig = ax.figure
    return fig, ax