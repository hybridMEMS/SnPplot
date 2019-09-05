# SnPplot


This program inputs raw snp files and provides many different functions for
viewing them. It is set up for plotting differential data and can handle normal
or mixed mode s parameters as data input. Deembedding with an open will also
be done if deembed is set to true and a directory of open files is given. The
code will scan the open directory for a file with identical DC bias conditions
and save the deembedded s parameters in a seperate file for easy export to
other programs such as ADS or Matlab. 

Inputs are stored in a separate inputs.py file. After the initial repo sync, run 
