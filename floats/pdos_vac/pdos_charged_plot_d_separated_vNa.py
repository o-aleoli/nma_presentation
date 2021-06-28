#!/usr/bin/env python3
import numpy as np
from matplotlib.backends.backend_pgf import PdfPages
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset

input_files_Na1 = [
    'Na1_total',
    'Na1_Nb_d_separated',
    'Na1_O_p_sum'
]
# input_files_O2 = [
#    'O2_total',
#    'O2_Nb_d_separated',
#    'O2_O_p_sum'
# ]
output_file = 'pdos_charged_d_separated_333_vNa'
xlim = (-4.25, 9)
ylim = (-400, 400)

data_Na1 = []
for i in input_files_Na1:
    data_Na1.append(np.load(i+'.npz'))

# data_O2 = []
# for i in input_files_O2:
#    data_O2.append(np.load(i+'.npz'))

width = (160 - 15) - 10
height = 40

"""
INPUT_DATA is a pickled, compressed file with the following numpy arrays:
    * pdos, an np.array, with dimensions (ispin, numpoints), where ispin=2 and numpoints=301 (typically)
    * eigen_energy, an np.array, with dimensions (numpoints)
    * eigen_adjust, a float
    * e_fermi, a float
"""
with PdfPages(output_file+'.pdf') as output:
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
        'legend.fancybox': False,
        'legend.fontsize': 4
    })
    fig, axs = plt.subplots(
        nrows = 1,
        ncols = 1,
    )

    d_colors = [
        "#0d8200",#dxy
        "#13bb00",#dyz
        "#ff00d9",#dz2
        "#18f500",#dxz
        "#860069"# dx2
    ]

###############################################################################

    # x_axis = data_O2[0]['eigen_energy']

    # ax_inset = zoomed_inset_axes(
    #     axs,
    #     8,
    #     loc = 'center',
    #     bbox_to_anchor = [0.49, 0.5],
    #     bbox_transform = axs.transAxes,
    #     axes_kwargs = {'box_aspect': 1.0}
    # )

    # axs.plot(
    #     x_axis,  data_O2[0]['pdos'][0, ...],
    #     x_axis, -data_O2[0]['pdos'][0, ...],
    #     linewidth = 1.0,
    #     color = 'black'
    # )

    # for orb in range(len(d_colors)):
    #     axs.plot(
    #         x_axis,  data_O2[1]['pdos'][0, ...,4 + orb],
    #         x_axis, -data_O2[1]['pdos'][0, ...,4 + orb],
    #         linewidth = 1.0,
    #         color = d_colors[orb]
    #     )

    # axs.plot(
    #     x_axis,  data_O2[2]['pdos'][0, ...],
    #     x_axis, -data_O2[2]['pdos'][0, ...],
    #     linewidth = 1.0,
    #     color = 'red'
    # )

    # axs.plot(
    #     [data_O2[0]['e_fermi'], data_O2[0]['e_fermi']],
    #     [np.amax(data_O2[0]['pdos'][0, ...]), -np.amax(data_O2[0]['pdos'][0, ...])],
    #     linestyle = 'dashed',
    #     linewidth = 2.0,
    #     color = 'black'
    # )

    # ax_inset.plot(
    #     x_axis,  data_O2[0]['pdos'][0, ...],
    #     x_axis, -data_O2[0]['pdos'][0, ...],
    #     color = 'black',
    #     linewidth = 1.0
    # )

    # for orb in range(len(d_colors)):
    #     ax_inset.plot(
    #         x_axis,  data_O2[1]['pdos'][0, ...,4 + orb],
    #         x_axis, -data_O2[1]['pdos'][0, ...,4 + orb],
    #         color = d_colors[orb],
    #         linewidth = 1.0
    #     )

    # ax_inset.plot(
    #     x_axis,  data_O2[2]['pdos'][0, ...],
    #     x_axis, -data_O2[2]['pdos'][0, ...],
    #     color = 'red',
    #     linewidth = 1.0
    # )

    # ax_inset.plot(
    #     [data_O2[0]['e_fermi'], data_O2[0]['e_fermi']],
    #     [np.amax(data_O2[0]['pdos'][0, ...]), -np.amax(data_O2[0]['pdos'][0, ...])],
    #     linestyle = 'dashed',
    #     color = 'black',
    #     linewidth = 1.0
    # )

###############################################################################

    x_axis = data_Na1[0]['eigen_energy']

    axs.plot(
        x_axis,  data_Na1[0]['pdos'][0, ...],
        x_axis, -data_Na1[0]['pdos'][0, ...],
        c='black',
        linewidth=1.0
    )

    for orb in range(len(d_colors)):
        axs.plot(
            x_axis,  data_Na1[1]['pdos'][0, ...,4 + orb],
            x_axis, -data_Na1[1]['pdos'][0, ...,4 + orb],
            linewidth=1.0,
            c=d_colors[orb]
        )

    axs.plot(
        x_axis,  data_Na1[2]['pdos'][0, ...],
        x_axis, -data_Na1[2]['pdos'][0, ...],
        linewidth = 1.0,
        color = 'red'
    )

    axs.plot(
        [data_Na1[0]['e_fermi'], data_Na1[0]['e_fermi']],
        [np.amax(data_Na1[0]['pdos'][0, ...]), -np.amax(data_Na1[0]['pdos'][0, ...])],
        linestyle='dashed',
        linewidth=2.0,
        c='black'
    )

###############################################################################

    lines = [
        Line2D(
            [0], [0],
            color="#860069",
            linewidth=1.0,
            label=r'Nb $4d_{x^2 - y^2}$'
        ),
        Line2D(
            [0], [0],
            color="#ff00d9",
            linewidth=1.0,
            label=r'Nb $4d_{3z^2 - r^2}$'
        ),
        Line2D(
            [0], [0],
            color="#0d8200",
            linewidth=1.0,
            label=r'Nb $4d_{xy}$'
        ),
        Line2D(
            [0], [0],
            color="#18f500",
            linewidth=1.0,
            label=r'Nb $4d_{xz}$'
        ),
        Line2D(
            [0], [0],
            color="#13bb00",
            linewidth=1.0,
            label=r'Nb $4d_{zy}$'
        ),
        Line2D(
            [0], [0],
            color='red',
            linewidth=1.0,
            label=r'O $2p$'
        ),
        Line2D(
            [0], [0],
            color='black',
            linewidth=1.0,
            label='Total'
        ),
        Line2D(
            [0], [0],
            color='black',
            linewidth=2.0,
            linestyle='dashed',
            label=r'$\varepsilon_F$'
        ),
    ]

    axs.legend(
        handles = lines,
        loc = 'lower center',
        bbox_transform = fig.transFigure,
        bbox_to_anchor = (0.5, 0),
        ncol = 8
    )

    axs.set(
        xlim = xlim,
        ylim = ylim,
        yticks = [],
        xlabel = 'Energia (eV)',
        ylabel = r'pDOS (eV${}^{-1}$)'
    )

    # ax_inset.set(
    #     xlim = (3.1, 3.7),
    #     ylim = (-30, 30),
    #     xticks = [],
    #     yticks = []
    # )

    # mark_inset(
    #     axs,
    #     ax_inset,
    #     loc1 = 1,
    #     loc2 = 4,
    #     edgecolor = 'gray'
    # )

    # axs.text(
    #     0.01,
    #     0.85,
    #     r"v$_{\textrm{O}}^{2+}$",
    #     transform = axs.transAxes
    # )

    axs.text(
        0.01,
        0.85,
        r"v$_{\textrm{Na}}^{1-}$",
        transform = axs.transAxes
    )

    fig.subplots_adjust(
        top = 0.95,
        left = 0.05,
        bottom = 0.35,
        right = 0.99
    )

    output.savefig()
