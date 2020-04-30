# Code to plot Triple Differential Cross Sections
# Author: Carlos Mario Granados Castro
# 2013 - 2020

import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

#PERSONALIZED GOOGLE MATERIAL COLORS
import ModColors as gc
gc.SetGMaterialColors()

class tdcsPlot(object):
    
    """
       NAME : tdcsPlot
    
       DESCRIPTION : Module to plot the TDCSs in either xy- or polar-form.
       It reads the data files for the calculated TDCSs and the experimental
       data, if any. It labels the plots with the given kinematic conditions,
       and save the Figs. in pdf and pgn or pgf formats.
       
       import it as: from tdcsPlot import tdcsPlot
       
       Developed by Carlos Mario Granados--Castro, 2013-2020
       
       CONTENT :
       selQ()
       readFile()
       readExpData()
       yTicks()
       prepFig()
       tdcs()
    
       PARAMETERS :
       All parameters are optional...
       pathData: str. Path to the data files. Default: "./Data"
       pathFig:  str. Path to save the Figs. Default: "./Figures"
       data:     str. File name containing the calculated TDCS. Usually it
                      is constructed in the Module, following sysName and the
                      kinematic conditions. Default: "" 
       dataExp:  str. File name of the experimental TDCS. Default: ""
       typeName: str. Type of plot, "xy" or "polar". Default: "xy"
       sysName:  str. System name. Used to rename Fig files. For molecules,
                      it must include the initial MO. Default: "None"
       Ei:       float. Incident electron energy, in eV. Default: 0.0
       Eb:       float. Energy of ejected electron, in eV. Defaul: 0.0
       thf:      float. Scattering angle, in deg. Default: 0.0
       readCols: int.tuple. Columns to read in dataExp. Default: (0, 1, 2)
       tdcsCol:  gcCol. Color assigned to the TDCS. Default: gc.gblue500
       expCol:   gcCol. Color assigned to the Exp. TDCS. Default: gc.gred500
       errCol:   gcCol. Color assigned to the error bars in the Exp. TDCS.
                        Default: gc.gred700
       labExp:   str. Label for experimental data. Default: ""
       tmaj_len: int. Length of major ticks. Only used in "xy". Default: 10
       tmin_len: int. Length on minor ticks. Only used in "xy". Default: 4
       textSty:  str. Text style: TeX or some default font. Default: "tex"
       showPlot: boolean. To show or not the final plot. Default: True
    """
    
    def __init__(self, pathData="./Data", pathFig="./Figures", data="", dataExp="",
                 typeName="xy", sysName="None",
                 Ei=0.0, Eb=0.0, thf=0.0, readCols=(0, 1, 2),
                 tdcsCol=gc.gblue500, expCol=gc.gred500, errCol=gc.gred700,
                 labExp="", tmaj_len=10, tmin_len=4, textSty="tex",
                 showPlot=True):
        """ Constructor. Define variables
            data: Data file with the TDCSs to plot
            typeName: xy-plot or polar-plot
            sysName: System type - name (atom, H, molecule, CH4, H2O...)
        """
        self.pathData = pathData
        self.pathFig = pathFig
        self.data = data
        self.dataExp = dataExp
        self.typeName = typeName
        self.sysName = sysName
        # Kinematic Conditions
        self.Ei = Ei
        self.Eb = Eb
        self.thf = thf
        # Cols to Read in Exp. Data
        self.readCols = readCols
        # Colors... Usually Using ModColos - Google Material Design...
        self.tdcsCol = tdcsCol
        self.expCol = expCol
        self.errCol = errCol
        # Experimental label
        self.labExp = labExp
        # To configure the Plot
        self.tmaj_len = tmaj_len
        self.tmin_len = tmin_len
        self.textSty = textSty
        # To Show Plot
        self.showPlot = showPlot
        # To Control if the data file is readed or not
        self.q1 = None
        
    def selQ(self):
        """Method to calculate the transfer vector magnitude
        and its angle"""
        # Initial State Energy
        Eg = 0.0
        # To transform a.u. to eV
        Eauev = 27.2113962
        #Initial state energy in a.u.
        if self.sysName == "H":
            Eg = -0.5
        elif self.sysName == "H-2p":
            Eg = -0.125
            self.sysName = "H_2p"
        elif self.sysName == "H2O-1b1":
            Eg = -0.4954
        elif self.sysName == "CH4-2a1":
            Eg = -0.9204
        elif self.sysName == "CH4-1t2":
            Eg = -0.5042
        # Initial energies in eV to a.u.
        Eiau = self.Ei / Eauev
        Ebau = self.Eb / Eauev
        
        # Final energy scattered electron (Energy conservation)
        Efau = Eiau + Eg - Ebau
        # Initial and final linear momenta
        ki = np.sqrt(2.0 * Eiau)
        kf = np.sqrt(2.0 * Efau)
        thfrad = self.thf * np.pi / 180.0
        # Magnitud transfer vector
        q = np.sqrt( (ki**2) + (kf**2) - 2.0 * ki * kf * np.cos(thfrad) )
        if q == 0.0:
            q = 1.0e-15
        argq = (ki - kf * np.cos(thfrad)) / q
        # Scattering angle (classical)
        self.thq = -np.sign(self.thf) * np.arccos(argq) * 180.0 / np.pi
        self.q1 = self.thq
        self.q2 = self.thq + 180.0
        if self.typeName == "polar":
            self.q1 = self.q1 * np.pi / 180.0
            self.q2 = self.q2 * np.pi / 180.0
        #print(self.q1)
        
    def readFile(self):
        """Method to read the data and prepare it to plot it"""
        # Check if any data file name were given. If not,
        # build one following the kinematic conditions
        self.selQ()
        i1 = int(self.Ei//1)
        i2 = int(self.Eb//1)
        i3 = int(abs(self.thf)//1)
        self.c1 = str(i1)
        self.c2 = str(i2)
        self.c3 = str(i3)
        if self.thf < 0.0:
            self.c3a = '_m' + str(i3)
            self.c3b = r'$-$' + r'$' + str(i3) + '$' 
        else:
            self.c3a = '_p' + str(i3)
            self.c3b = r'$+$' + r'$' + str(i3) + '$'
            self.c3c = '_' + str(i3) + 'o'
        if self.data == "":
            cname = self.sysName + '_' + self.c1 + '-' + self.c2 + self.c3a
            dname = self.sysName + '-' + self.c1 + '-' + self.c2 + self.c3a
            # File to Read
            cfile = self.pathData + '/TDCS_' + cname + '.dat'
            # Name of Figure Files (to Save)
            self.figPNG = self.pathFig + '/Fig_TDCS_' + dname + '.png'
            self.figPDF = self.pathFig + '/Fig_TDCS_' + dname + '.pdf'
            self.figPGF = self.pathFig + '/Fig_TDCS_' + dname + '.pgf'
        else:
            #File to Read
            cfile = self.pathData + '/' + self.data
            # Name of Figure Files (to Save)
            self.figPNG = self.pathFig + '/Fig_' + self.data + '.png'
            self.figPDF = self.pathFig + '/Fig_' + self.data + '.pdf'
            self.figPGF = self.pathFig + '/Fig_' + self.data + '.pgf'
        # Read TDCS from file
        self.x, self.y = np.loadtxt(cfile, usecols=(0, 1), unpack=True)
        # Check if x (Scatt. Angle) is in radians or if it has negative values
        if self.typeName == "xy":
            if self.x[-1] < 7.0 and self.x[-1] > 0.0:
                self.x = self.x * 180.0 / np.pi
            else:
                if self.x[-1] < 0.0:
                    nVal = len(self.x)
                    xold, yold = self.x, self.y
                    for i in range(nVal):
                        self.x[i] = xold[nVal-i-1]
                        self.y[i] = yold[nVal-i-1]
        elif self.typeName == "polar":
            dth = np.pi / 180.0
            if self.x[-1] > 7.0:
                self.x *= dth
                self.q1 *= dth
                self.q2 *= dth
    
    def readExpData(self):
        """Method to read experimental data, if any. Prepare it to plot it"""
        #print(self.q1)
        if self.q1 is None:
            self.readFile()
        cfile = self.pathData + "/" + self.dataExp
        self.xExp, self.yExp, self.yErr = np.loadtxt(cfile, usecols=self.readCols, unpack=True)
        if self.sysName == "H":       #H
            self.xExp = 360.0 - self.xExp
        if self.typeName == "xy":
            dq = 360.0
            if self.xExp[-1] < 7.0:
                self.xExp = xExp * 180.0 / np.pi
        elif self.typeName == "polar":
            dq = 2.0 * np.pi
            if self.xExp[-1] > 7.0:
                self.xExp = self.xExp * np.pi / 180.0
        if self.q1 < 0.0:
            self.q1 += dq
        if self.q2 < 0.0:
            self.q2 += dq
        r12 = self.y.max() / self.yExp.max()
        self.yExp *= r12
        self.yErr *= r12
    
    def yTicks(self):
        """Method to determine the ticks on y-axis
           I didn't like the default on matplotlib...""" 
        i = 0
        ymax = self.y.max()
        val = ymax
        if ymax < 1.0 and ymax < 0.50:
            while val < 1.0:
                i += 1
                val *= 10.0
        else:
            while val > 10.0:
                i -= 1
                val /= 10.0
        y0 = round(val, 0)
        if( y0 < val ):
            y0 += 1.0
        ymax = int(y0//1) / (10.0**i)
        if ymax == self.y.max():
            ymax *= 1.1
        if 1.0 <= y0 <= 2.5:
            y1loc = 5.0 / (10.0**(i+1))
            y2loc = y1loc / 5.0
        elif 2.5 < y0 <= 5.0:
            y1loc = 1.0 / (10.0**i)
            y2loc = y1loc / 5.0
        else:
            y1loc = 2.0 / (10.0**i)
            y2loc = y1loc / 4.0
        self.y1loc = y1loc
        self.y2loc = y2loc
        self.ymax = ymax
        self.iexp = i
        self.yform = '%0.' + str(i) + 'f'
    
    def prepFig(self):
        """Method to prepare the data and several
           parameters needed to plot the TDCS """ 
        # Read the file
        self.readFile()
        if self.dataExp != "":
            self.readExpData()
        # x and y Limits and Ticks
        self.xmin = 0.0
        self.xmax = 10.0
        if self.typeName == "xy":
            self.xmax = 360.0
        elif self.typeName == "polar":
            self.xmax = 2.0 * np.pi
        self.xmax = self.x.max()
        self.ymin = 0.0
        self.yTicks()
        # Locators, based on the calculated ticks
        self.xmajor_locator = MultipleLocator(60.0)
        self.xminor_locator = MultipleLocator(10.0)
        self.ymajor_locator = MultipleLocator(self.y1loc)
        self.yminor_locator = MultipleLocator(self.y2loc)
        self.ymajor_formatter = FormatStrFormatter(self.yform)
        # For Fig. Text
        strtxt1 = r'$E_i=$' + r'$' + self.c1 + '$' + ' eV'
        strtxt2 = r'$E_b=$' +  r'$' + self.c2 + '$' + ' eV' 
        strtxt3 = r'$\theta_{a}=$' + self.c3b + r'$^\circ$'
        self.strtxt = strtxt1 + '\n' + strtxt2 + '\n' + strtxt3
        # Plot Label
        self.labCS = r'GSF'
        # To use TeX Text Style
        params = {
            'xtick.labelsize' : 22,
            'ytick.labelsize' : 22,
            'axes.labelsize'  : 24,
            'legend.fontsize': 16
            }
        plt.rcParams.update(params)
        if self.textSty == 'tex':
            plt.rc('text', usetex=True)
            plt.rc('font', family='serif')
        elif self.textSty == 'pgf':
            mpl.use('pgf')
            pgf_with_custom_preamble = {
                'font.family': 'serif',
                'text.usetex': True,
                'pgf.rcfonts': False
                }
            mpl.rcParams.update(pgf_with_custom_preamble)
        
    def tdcs(self):
        """Method to plot the TDCSs, either in xy- or polar-form.
           Include all labels, kinematic conditions and specified
           colors. Figures are saved in pdf and png or pgf formats.
           prepFig() must be executed before this method"""
        if self.typeName == "xy":
            ax = plt.subplot()
            ax.xaxis.set_major_locator(self.xmajor_locator)
            ax.xaxis.set_minor_locator(self.xminor_locator)
            ax.tick_params(axis='both', which='both', direction='inout')
            ax.tick_params(axis='both', which='major', length=self.tmaj_len)
            ax.tick_params(axis='both', which='minor', length=self.tmin_len)
            ax.xaxis.set_ticks_position('both')
            ax.yaxis.set_ticks_position('both')
            ax.set_xlabel(r'Ejection Angle, $\theta_b$ (deg.)')
            ax.set_ylabel(r'TDCS (a.u.)')
            xref = 2.0 * self.xmax / 3.0
            yref = 0.75 * self.ymax
            if self.sysName == 'H':
                xref = 0.05 * self.xmax
                yref = 0.65 * self.ymax
        elif self.typeName == "polar":
            self.ymin = 0.0
            ax = plt.subplot(polar=True)
            ax.set_theta_zero_location('N')
            ax.set_theta_direction(-1)
            xref = np.pi
            yref = 0.35 * self.ymax
            print(self.q1)
        else:
            print("Error! Plot type not recognized")
            sys.exit(1)
        # Plot TDCS
        ax.plot(self.x, self.y, c=self.tdcsCol, lw=3, label=self.labCS)
        if self.dataExp != "":
            ax.errorbar(self.xExp, self.yExp, yerr=self.yErr, ls='', marker='.', ms=14, c=self.expCol, ecolor=self.errCol, elinewidth=2, capsize=4, label=self.labExp)
        ax.legend(loc="best", fancybox=True, framealpha=0.50)
        # Auxiliar Info Text
        ax.text(xref, yref, self.strtxt, size=22, va = 'top', ha='left')
        ax.text(self.q1, 1.025*self.ymax, r'$+\mathbf{q}$', color=gc.ggrey800, size = 18, ha='center')
        ax.text(self.q2, 1.025*self.ymax, r'$-\mathbf{q}$', color=gc.ggrey800, size = 18, ha='center')
        # Plot Lines for the Transfer Vector
        ax.plot([self.q1, self.q1], [self.ymin, self.ymax], lw=2.0, c=gc.ggrey700, dashes = (4, 3))
        ax.plot([self.q2, self.q2], [self.ymin, self.ymax], lw=2.0, c=gc.ggrey700, dashes = (4, 3))
        # Plot ticks and formatting
        ax.yaxis.set_major_locator(self.ymajor_locator)
        ax.yaxis.set_minor_locator(self.yminor_locator)
        # Plot limits
        ax.set_xlim(self.xmin, self.xmax)
        ax.set_ylim(self.ymin, self.ymax)
        plt.tight_layout()
        # Save Fig to File
        plt.savefig(self.figPDF, bbox_inches='tight', pad_inches=0.1, transparent=True)
        if self.textSty != 'pgf':
            plt.savefig(self.figPNG, bbox_inches='tight', pad_inches=0.1, transparent=True)
        else:
            plt.savefig(self.figPGF, bbox_inches='tight', pad_inches=0.1, transparent=True)
        # Show plot
        if self.showPlot:
            plt.show()
        