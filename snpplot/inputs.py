import os

datadir = r''  # location of device SnP files
opendir = r''  # location of device open deembedding files

# Device overview plot
filterRegex = r''  # regex to filter SNP files in datadir
regexSinglePlot = r''  # regex to select single device for detailed plots

####################
# User Inputs ######
####################


mixedmodeport = [0, 1, 2, 3]  # 1+, 1-, 2+, 2-
# Default is 13 input, 24 output.
debug = False
deembed = 0     # 0 - no deembedding
                # 1- Deembeds data with open that has matching bias conditions,
                # 2- Deembeds data with open & short - Work In Progress
bal = False  # Set true if importing true mode SNP data

### plot options ###
plotS = 0  # Plots singled ended and differential reflection parameters  for regexSinglePlot
plotZ = 0  # Plots input impedances: re, im, and mag  for regexSinglePlot
plotSmith = 0  # Plots reflection parameters  for regexSinglePlot
plot21 = 0  # Plots Sdd21 and Sdd12: mag, phase, and ifft  for regexSinglePlot
plot21all = 0  # Plots Smm21 mag for regexSinglePlot
plotgmddRatio = 0  # Plots ratio of gmdd to gmcc, gmdc, and gmcd  for regexSinglePlot
plotgm = 0  # Plots gmdd for filterRegex

gmrel = False  # controls whether gmddrel plot is relative or not - data controlled by filterRegex
nsmoothgm = 1  # smooths gm plots (gm, gmddratio, gmddrel) with rolling average
####################

opendir = os.path.join(datadir, 'open')
shortdir = os.path.join(datadir, 'short', 'short_test')