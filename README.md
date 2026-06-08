# kilosort4-drift-to-mat
This is an independent utility for exporting drift estimates from Kilosort4 output files into MATLAB-readable format. It only exports the drift estimate already stored in ops.npy.

## What this does
Sometimes there are issues with readNPY.mat from npy-matlab that gives an error message when trying to read the ops.npy file from Kilosort4. This script converts the ops.npy to ks4_drift.mat and saves under the same directory. 

## Installation and Example Usage
Simply download the export_ks4_drift.py and store it under desired folder. Recommended to run under anaconda environment where kilosort4 is installed, as kilosort is dependency. 

### Example Usage
In Anaconda Prompt
```bash
cd your_kilosort4_output_folder
activate kilosort
python "your_script_directory/export_ks4_drift.py"
```

After the script finishes, you should see a file named `ks4_drift.mat` in the same Kilosort4 output folder.

## Output Variables

The script saves the following variables into `ks4_drift.mat`:

| Variable             |                   Size | Description                                                                  |
| -------------------- | ---------------------: | ---------------------------------------------------------------------------- |
| `dshift_um`          | `n_batches × n_blocks` | Drift estimate in micrometers. Each column corresponds to one drift block.   |
| `time_sec`           |        `n_batches × 1` | Time vector in seconds.                                                      |
| `time_min`           |        `n_batches × 1` | Time vector in minutes.                                                      |
| `yblk_um`            |         `n_blocks × 1` | Drift block depth locations in micrometers, if available from `ops.npy`.     |
| `fs`                 |                 scalar | Sampling rate from `ops.npy`.                                                |
| `batch_size_samples` |                 scalar | Kilosort batch size in samples.                                              |
| `n_batches`          |                 scalar | Number of drift time bins.                                                   |
| `n_blocks`           |                 scalar | Number of drift depth blocks.                                                |
| `drift_abs_max_um`   |         `1 × n_blocks` | Maximum absolute drift for each drift block.                                 |
| `drift_range_um`     |         `1 × n_blocks` | Drift range for each block, calculated as maximum drift minus minimum drift. |
| `drift_median_um`    |         `1 × n_blocks` | Median drift for each drift block.                                           |
