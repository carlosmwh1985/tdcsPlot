#Check Python version. Example developed with Python 3.6

import sys
print(sys.version)

# Import tdcsPlot module, and see the available methods.
from tdcsPlot import tdcsPlot
print(dir(tdcsPlot))

# See documentation of the method,
# Special attention to the parameters. The module can be sensitive to them
print(tdcsPlot.__doc__)

# Modified Color Set. Also print its documentation
import ModColors as gc
gc.SetGMaterialColors()
print(gc.SetGMaterialColors.__doc__)

# USE EXAMPLES



# EXAMPLE 1A:
# Example to plot some dummy data, in a default Conf.
# xy-plot, using TeX fonts, saving it in pgn and pdf format.
# The Fig. is shown after calculate it.
tp_xy = tdcsPlot(data="data_dummy.dat")     # Constructor
tp_xy.prepFig()                             # Prepare data
print(tp_xy.ymin, tp_xy.ymax)               # Check some Vars.
tp_xy.tdcs()                                # Plot



# EXAMPLES 1B:
# Similar to Ex. 1A, but for a polar plot
tp_pol = tdcsPlot(data="data_dummy.dat", typeName="polar")
tp_pol.prepFig()
tp_pol.tdcs()



# EXAMPLE 2A:
# Examples to plot the TDCS for the H atom.
# Ei = 250 eV, Eb = 5 eV, th_scatt = +3 deg.
# Include experimental data.
# Parameters:
dataExp = "H_250-5_p3_PRA30_758.dat"    #File containing Exp. data
Ei = 250.0       #Incident electron energy, in eV
Ef = 5.0         #Ejected eletron energy, in eV
thf = 3.0        #Scattering angle, in deg.
targetName = "H" #Target system: Hydrogen atom in its ground state
expLabel = "Exp. Data (PRA 30, 758)"

tpH5 = tdcsPlot(dataExp=dataExp, Ei=Ei, Eb=Ef, thf=thf, sysName=targetName,
                labExp=expLabel)
tpH5.prepFig()
tpH5.tdcs()



# EXAMPLE 2B:
# Similar to Ex. 2A, but for a polar plot
tpH5 = tdcsPlot(dataExp=dataExp, Ei=Ei, Eb=Ef, thf=thf, sysName=targetName,
                labExp=expLabel, typeName='polar')
tpH5.prepFig()
tpH5.tdcs()



# EXAMPLE 3A:
# Examples to plot the TDCS for the H atom.
# Ei = 250 eV, Eb = 10 eV, th_scatt = +5 deg.
# Include experimental data.
# Parameters:
dataExp = "H_250-10_p5_PRA30_758.dat"    #File containing Exp. data
Ei = 250.0       #Incident electron energy, in eV
Ef = 10.0         #Ejected eletron energy, in eV
thf = 5.0        #Scattering angle, in deg.
targetName = "H" #Target system: Hydrogen atom in its ground state
expLabel = "Exp. Data (PRA 30, 758)"

tpH5 = tdcsPlot(dataExp=dataExp, Ei=Ei, Eb=Ef, thf=thf, sysName=targetName,
                labExp=expLabel, tdcsCol=gc.gcyan800, expCol=gc.gdorange600,
                errCol=gc.gdorange900)
tpH5.prepFig()
tpH5.tdcs()



# EXAMPLE 3B:
# Same as Ex. 3A, but for a polar plot
tpH5 = tdcsPlot(dataExp=dataExp, Ei=Ei, Eb=Ef, thf=thf, sysName=targetName,
                labExp=expLabel, tdcsCol=gc.gcyan800, expCol=gc.gdorange600,
                errCol=gc.gdorange900, typeName='polar')
tpH5.prepFig()
tpH5.tdcs()

# END