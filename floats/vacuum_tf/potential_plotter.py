#!/usr/bin/env python3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.backends.backend_pgf import PdfPages

output_file = 'x_potential'
width = (160 - 15) - 10
height = 55

potential_x = pd.read_csv(
    'pot_x.dat',
    sep = ' ',
    header = None
)

with PdfPages(output_file + '.pdf') as output:
    plt.rcParams.update({
        'font.family': 'serif',
        'font.size': 7,
        'figure.figsize': [width/25.4, height/25.4],
        'savefig.dpi': 1200,
        'text.usetex': True,
        'pgf.rcfonts': False,
        'pgf.texsystem': 'pdflatex',
        'pgf.preamble': r'\usepackage[utf8x]{inputenc}',
        'legend.frameon': False,
        'legend.fontsize': 4
    })
    fig, axs = plt.subplots(nrows = 1, ncols = 1)

    axs.plot(
        potential_x[0],
        potential_x[1],
        color = 'black',
        linestyle = 'solid',
        linewidth = 1.0,
        label = 'Potencial'
    )

    axs.hlines(
        -12.5543,
        0,
        np.max(potential_x[0]),
        color = 'red',
        linestyle = 'dashed',
        linewidth = 1.0,
        label = r'$\tilde{V}_{interna} = -12,\!55$ eV'
    )

    axs.hlines(
        4.4448,
        0,
        np.max(potential_x[0]),
        color = 'blue',
        linestyle = 'dashed',
        linewidth = 1.0,
        label = r'$V_{vac} = 4,\!44$ eV'
    )

    axs.set(
        xlim = [0, np.max(potential_x[0])],
        ylim = [1.2*np.min(potential_x[1]), 1.2*np.max(potential_x[1])],
        xlabel = r'Eixo em $[100]$ (\AA)',
        ylabel = r'Potencial cristalino (eV)',
    )

    fig.subplots_adjust(
        top = 0.99,
        left = 0.1,
        bottom = 0.3,
        right = 0.99
    )

    axs.legend(
        loc = 'lower center',
        bbox_transform = fig.transFigure,
        bbox_to_anchor = (0.5, 0),
        ncol = 3
    )

    output.savefig()
