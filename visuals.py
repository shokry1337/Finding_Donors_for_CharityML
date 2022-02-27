import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display_html

def set_color(c: int) -> None:
    '''
        Sets the color of titles/subtitles, x/y ticks, axes labels and edges.
    '''
    global _c
    if c == 0: _c = 'k'
    elif c == 1: _c = 'w'
    else: raise ValueError('Invalid Color!')
    plt.rcParams.update({
        'text.color' : _c,
        'xtick.color' : _c,
        'ytick.color' : _c,
        'axes.labelcolor' : _c,
        'axes.edgecolor' : _c})

def handle_legend(l: plt.legend) -> None:
    f = l.get_frame()
    f.set_facecolor('w' if _c == 'k' else 'k')
    f.set_edgecolor('w' if _c == 'k' else 'k')


def distribution(data: pd.DataFrame, features: list, log_transformed: bool = False) -> None:
    '''
        Visualizes distributions of continuous features
    '''
    
    fig = plt.figure(figsize=(11,5))

    if log_transformed:
        fig.suptitle('Log-transformed Distribution(s) of Feature(s)', fontsize=16, y=1.03)
    else:
        fig.suptitle('Distribution(s) of Feature(s)', fontsize=16, y=1.03)

    for i, feature in enumerate(features):
        ax = fig.add_subplot(1, 2, i+1)
        ax.hist(data[feature], bins=25, color='#00A0A0')
        ax.set_title(f'{feature}', fontsize=14)
        ax.set_xlabel('Value')
        ax.set_ylabel('Number of Records')
        ax.set_ylim((0, 2000))
        ax.set_yticks([0, 500, 1000, 1500, 2000])
        ax.set_yticklabels([0, 500, 1000, 1500, '>2000'])

    fig.tight_layout()

# https://stackoverflow.com/a/44923103
def displayx(_dfs):
    '''
        Renders two or more dataframes vertically
    '''
    html_str = ''
    for df in _dfs:
         html_str += df.to_html()
    display_html(html_str, raw=True)