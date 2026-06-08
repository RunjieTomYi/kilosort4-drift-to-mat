# kilosort4-drift-to-mat
This is an independent utility for exporting drift estimates from Kilosort4 output files into MATLAB-readable format. It only exports the drift estimate already stored in ops.npy.

Sometimes there are issues with readNPY.mat from npy-matlab that gives an error message when trying to read the ops.npy file from Kilosort4. This script converts the ops.npy to ks4_drift.mat and saves under the same directory. 

To use, simply download the .py file, and run it under the /kilosort4 folder where your Kilosort4 output is stored.
