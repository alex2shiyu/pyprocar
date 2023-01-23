"""

.. _ref_plotting_fermi3d_spin-polarized:

Plotting fermi3d spin-polarized
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Plotting fermi3d spin-polarized example.

First download the example files with the code below. Then replace data_dir below.

.. code-block::
   :caption: Downloading example

    data_dir = pyprocar.download_example(save_dir='', 
                                material='Fe',
                                code='qe', 
                                spin_calc_type='spin-polarized',
                                calc_type='fermi')
"""
# sphinx_gallery_thumbnail_number = 2

###############################################################################

import pyvista
# You do not need this. This is to ensure an image is rendered off screen when generating exmaple gallery.
pyvista.OFF_SCREEN = True

###############################################################################
# importing pyprocar and specifying local data_dir

import os
import pyprocar
parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.getcwd())))
data_dir = f"{parent_dir}{os.sep}data{os.sep}qe{os.sep}fermi{os.sep}spin_colinear{os.sep}Fe"


# First create the FermiHandler object, this loads the data into memory. Then you can call class methods to plot
fermiHandler = pyprocar.FermiHandler(
                                    code="qe",
                                    dirname=data_dir,
                                    apply_symmetry=True)

###############################################################################
# Plain mode
# +++++++++++++++
# 
#

# spins in spins polarized calculations specifies which energy bands to plot
spins =[0,1]

fermiHandler.plot_fermi_surface(mode="plain",
                                spins = spins,
                                spin_colors= ['red','blue'],
                                cmap="jet",
                                show=True,)



###############################################################################
# Parametric mode
# +++++++++++++++
# 
#

# Here you can look at the atomic projections on a given spin energy bands
atoms=[0]
orbitals=[4,5,6,7,8]
spins=[1]
fermiHandler.plot_fermi_surface(mode="parametric",
                              atoms=atoms,
                              orbitals=orbitals,
                              spins=spins,
                              show=True,)


# Here you can look at the atomic projections on a given spin energy bands
spins=[0]
fermiHandler.plot_fermi_surface(mode="parametric",
                              atoms=atoms,
                              orbitals=orbitals,
                              spins=spins,
                              show=True,)


