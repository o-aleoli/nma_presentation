#!/bin/env python3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pgf import PdfPages

input_files = ['nn_c5_ACF.dat', 'nn_t1_ACF.dat', 'nn_t5_ACF.dat']
nn_layers = [
    [69, 71, 85, 86],  # L1
    [70, 72, 82, 84],  # L2
    [73, 75, 81, 83],  # L3
    [74, 76, 78, 80],  # L4
    [77, 79]  # L5
]
num_layers_nn = len(nn_layers)
width = ((160 - 15) - 10)/2
height = (90 - 5) - 20

nn_bader = []
for files in input_files:
    nn_bader.append(pd.read_fwf(files, skiprows=[1, 88, 89, 90, 91]))

nn_average_charge = []

# averages individual charges for each layer
for strain, bader_chg in enumerate(nn_bader):
    layer_average = []
    for i, layer in enumerate(nn_layers):
        accumulator = 0
        for j, atom in enumerate(layer):
            accumulator += bader_chg['CHARGE'][atom - 1]/len(layer)
        layer_average.append(accumulator)
    nn_average_charge.append(layer_average)

nn_average_valence = np.array(nn_average_charge)
nn_c4_change = np.divide(nn_average_charge[0], nn_average_charge[1]) - 1
nn_t4_change = np.divide(nn_average_charge[2], nn_average_charge[1]) - 1

with PdfPages('bader_strain_evolution_nn.pdf') as output:
    plt.rcParams.update({
        'figure.figsize': [width/25.4, height/25.4],
        'savefig.dpi': 1200,
        'text.usetex': True,
        'pgf.rcfonts': False,
        'pgf.texsystem': 'pdflatex',
        'pgf.preamble': r'\usepackage[utf8x]{inputenc}',
        'legend.frameon': False,
        'legend.fancybox': False,
        'font.size': 9,
        'legend.fontsize': 'xx-small'
    })

    fig, axs = plt.subplots(constrained_layout=True)

    axs.scatter(
        100*nn_c4_change,
        [1, 2, 3, 4, 5],
        marker='o',
        label=r'$-5\%$',
        color='k'
    )
    axs.scatter(
        100*nn_t4_change,
        [1, 2, 3, 4, 5],
        marker='o',
        label=r'$5\%$',
        color='darkgray'
    )

    axs.legend(loc="lower left")

    axs.set(
        xlabel=r'$\Delta$Carga (\% estado fundamental)',
        xlim=[-2.0, 2.0],
        ylabel=r'Camadas atômicas',
        ylim=[5.5, 0.5]
    )

    axs.tick_params(
        axis='y',
        which='major',
        length=10.0,
        labelleft=False,
        labelright=False,
        left=False,
        right=False
    )

    output.savefig()
