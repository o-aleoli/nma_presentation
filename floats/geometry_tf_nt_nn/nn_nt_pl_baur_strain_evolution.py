#!/usr/bin/env python3
import pandas as pd
from matplotlib.backends.backend_pgf import PdfPages
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator

pl_data = pd.read_fwf('pl.dat')
baur_index_data = pd.read_fwf('baur.dat')
average_bond_data = pd.read_fwf('bond.dat')

width = (160 - 15) - 10
height = ((90 - 5) - 15)*0.6

with PdfPages('nn_nt_pl_baur_strain_evolution.pdf') as output:
    plt.rcParams.update({
        'figure.figsize': [width/25.4, height/25.4],
        'savefig.dpi': 1200,
        'text.usetex': True,
        'pgf.rcfonts': False,
        'pgf.texsystem': 'pdflatex',
        'pgf.preamble': r'\usepackage[utf8x]{inputenc}\usepackage[version = 4]{mhchem}',
        'legend.frameon': False,
        'legend.fancybox': False,
        'font.size': 9,
        'legend.fontsize': 'xx-small'
        })

    fig, axs = plt.subplots(
            nrows = 1,
            ncols = 3,
            sharex = True,
            constrained_layout = True
    )
# Planarity
    axs[0].scatter(
        pl_data['strain'],
        pl_data['nno'],
        color = '#4CB276',
        marker = 'o'
    )
    axs[0].scatter(
        pl_data['strain'],
        pl_data['nto'],
        color = '#B79A56',
        marker = 'o'
    )
# Baur's DI
    axs[1].scatter(
        baur_index_data['strain'],
        baur_index_data['nno_ss'],
        color = '#4CB276',
        marker = 'o'
    )
    axs[1].scatter(
        baur_index_data['strain'],
        baur_index_data['nto_ss'],
        color = '#B79A56',
        marker = 'o'
    )
    axs[2].scatter(
        baur_index_data['strain'],
        baur_index_data['nno_bl'],
        color = '#4CB276',
        marker = 'o',
        label = r'\ce{NaNbO3}'
    )
    axs[2].scatter(
        baur_index_data['strain'],
        baur_index_data['nto_bl'],
        color = '#B79A56',
        marker = 'o',
        label = r'\ce{NaTaO3}'
    )

    for axis in axs:
        axis.set(
            xlim = (-6, 6)
        )

    axs[0].set(ylabel = r'$P_L$ superfície (\%)')
    axs[0].xaxis.set_minor_locator(AutoMinorLocator())
    axs[0].yaxis.set_minor_locator(AutoMinorLocator())
    axs[1].set(ylabel = r'$\Delta_d$ subsuperfície (\%)', xlabel = r'Tensão biaxial (\%)')
    axs[1].yaxis.set_minor_locator(AutoMinorLocator())
    axs[2].set(ylabel = r'$\Delta_d$ interna (\%)')
    axs[2].yaxis.set_minor_locator(AutoMinorLocator())
    axs[2].legend(
        loc = 'lower center',
        ncol = 2,
        bbox_to_anchor = (0.5, -0.4)
    )

    # plt.minorticks_off()

    # axs[0].annotate('a', xy=(0.0 + 0.110, 0.875), xycoords='figure fraction')
    # axs[1].annotate('b', xy=(1/3 + 0.140, 0.875), xycoords='figure fraction')
    # axs[2].annotate('c', xy=(2/3 + 0.140, 0.875), xycoords='figure fraction')

    output.savefig()
