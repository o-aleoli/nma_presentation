#!/usr/bin/env python3
"""
input_files is a pickled, compressed file with the following numpy arrays:
    * pdos, an np.array, with dimensions (ispin, numpoints), where ispin=2 and numpoints=301 (typically)
    * eigen_energy, an np.array, with dimensions (numpoints)
    * eigen_adjust, a float
    * e_fermi, a float
"""
import numpy as np
from matplotlib.backends.backend_pgf import PdfPages
import matplotlib.pyplot as plt
from matplotlib.legend import Line2D

data_Nb = [np.load('nn_total_c5.npz'), np.load('Nb_d_separated_1_c5.npz')]
data_Ta = [np.load('nt_total_c5.npz'), np.load('Ta_d_separated_1_c5.npz')]
output_file = 'pdos_c5_nn_nt_surface'
xlim = (0, 9)
ylim_Nb = (-2.5, 2.5)
ylim_Ta = (-0.5, 0.5)
width = 0.5*((160 - 15) - 10)
height = (90 - 5) - 17

with PdfPages(output_file + '.pdf') as output:
    plt.rcParams.update({
        'font.family': 'serif',
        'font.size': 7,
        'figure.figsize': [width/25.4, height/25.4],
        'savefig.dpi': 1200,
        'text.usetex': True,
        'pgf.rcfonts': False,
        'pgf.texsystem': 'pdflatex',
        'pgf.preamble': r"\usepackage[utf8x]{inputenc}\usepackage[locale = DE, separate-uncertainty = true]{siunitx}\usepackage[version = 4]{mhchem}",
        'legend.frameon': False,
        'legend.fancybox': False,
        'legend.fontsize': 'xx-small'
    })
    fig, axs = plt.subplots(
        nrows=2,
        ncols=1,
        constrained_layout=True
    )

    d_colors = [
        "#0d8200",#dxy
        "#13bb00",#dyz
        "#ff00d9",#dz2
        "#18f500",#dxz
        "#860069"# dx2
    ]

    legend = [
        Line2D(
            [0], [0],
            color = d_colors[4],
            linewidth = 1.0,
            label = r'M $d_{x^2 - y^2}$'
        ),
        Line2D(
            [0], [0],
            color = d_colors[2],
            linewidth = 1.0,
            label = r'M $d_{3z^2 - r^2}$'
        ),
        Line2D(
            [0], [0],
            color = d_colors[0],
            linewidth = 1.0,
            label = r'M $d_{xy}$'
        ),
        Line2D(
            [0], [0],
            color = d_colors[3],
            linewidth = 1.0,
            label = r'M $d_{xz}$'
        ),
        Line2D(
            [0], [0],
            color = d_colors[1],
            linewidth = 1.0,
            label = r'M $d_{zy}$'
        ),
        # Line2D(
        #     [0], [0],
        #     color = 'red',
        #     linewidth = 1.0,
        #     label = r'O $2p$'
        # ),
        Line2D(
            [0], [0],
            color = 'black',
            linewidth = 1.0,
            label = 'Total'
        ),
        Line2D(
            [0], [0],
            color = 'black',
            linewidth = 1.0,
            linestyle = 'dashed',
            label = r'$\varepsilon_F$'
        ),
    ]

###############################################################################

    x_axis_Nb = data_Nb[0]['eigen_energy'] + data_Nb[0]['eigen_adjust']

    for orb in range(len(d_colors)):
        axs[0].plot(
            x_axis_Nb,  data_Nb[1]['pdos'][0, :,4 + orb],
            x_axis_Nb, -data_Nb[1]['pdos'][1, :,4 + orb],
            linewidth = 1.0,
            color = d_colors[orb]
        )

    axs[0].plot(
        x_axis_Nb,  data_Nb[0]['pdos'][0, :],
        x_axis_Nb, -data_Nb[0]['pdos'][1, :],
        linewidth = 1.0,
        color = 'black'
    )

    axs[0].vlines(
        data_Nb[0]['e_fermi'] + data_Nb[0]['eigen_adjust'],
        ylim_Nb[0],
        ylim_Nb[1],
        linestyle = 'dashed',
        linewidth = 2.0,
        color = 'black'
    )

###############################################################################

    x_axis_Ta = data_Ta[0]['eigen_energy'] + data_Ta[0]['eigen_adjust']

    for orb in range(len(d_colors)):
        axs[1].plot(
            x_axis_Ta,  data_Ta[1]['pdos'][0, :,4 + orb],
            x_axis_Ta, -data_Ta[1]['pdos'][0, :,4 + orb],
            linewidth = 1.0,
            color = d_colors[orb]
        )

    axs[1].plot(
        x_axis_Ta,  data_Ta[0]['pdos'][0, :],
        x_axis_Ta, -data_Ta[0]['pdos'][0, :],
        linewidth = 1.0,
        color = 'black'
    )

    axs[1].vlines(
        data_Ta[0]['e_fermi'] + data_Ta[0]['eigen_adjust'],
        ylim_Ta[0],
        ylim_Ta[1],
        linestyle = 'dashed',
        linewidth = 2.0,
        color = 'black'
    )

    axs[0].set(
        xlim = xlim,
        ylim = ylim_Nb,
        ylabel = r"pDOS (\si{\per\electronvolt})",
        xticklabels = [],
        yticks = []
    )

    axs[1].set(
        xlim = xlim,
        ylim = ylim_Ta,
        ylabel = r"pDOS (\si{\per\electronvolt})",
        xlabel = r"Energia (\si{\electronvolt})",
        yticks = [],
    )

    axs[1].legend(
        handles = legend,
        loc = 'lower center',
        bbox_to_anchor = (0.5, -0.8),
        ncol = 4
    )
    axs[0].set_title(r'Superfície, \ce{NaNbO3} (M $=\ce{Nb}$)', loc = 'left')
    axs[1].set_title(r'Superfície, \ce{NaTaO3} (M $=\ce{Ta}$)', loc = 'left')

    output.savefig()
