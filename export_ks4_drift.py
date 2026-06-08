from pathlib import Path
import numpy as np
from scipy.io import savemat
from kilosort.io import load_ops


def export_ks4_drift(results_dir):
    results_dir = Path(results_dir).resolve()
    ops_path = results_dir / "ops.npy"

    if not ops_path.exists():
        raise FileNotFoundError(f"Could not find ops.npy in: {results_dir}")

    ops = load_ops(ops_path)

    if "dshift" not in ops:
        raise KeyError("No 'dshift' key found in ops.npy.")

    dshift = ops["dshift"]

    if dshift is None:
        raise ValueError("ops['dshift'] is None. Drift correction was probably disabled.")

    dshift = np.asarray(dshift)

    if dshift.ndim == 1:
        dshift = dshift[:, np.newaxis]

    n_batches, n_blocks = dshift.shape

    yblk = np.asarray(ops.get("yblk", np.arange(n_blocks))).squeeze()

    fs = ops.get("fs", None)
    batch_size = ops.get("batch_size", None)

    if fs is None:
        raise KeyError("Could not find sampling rate key ops['fs'].")

    if batch_size is None:
        raise KeyError("Could not find batch size key ops['batch_size'].")

    fs = float(fs)
    batch_size = float(batch_size)

    time_sec = np.arange(n_batches) * batch_size / fs
    time_min = time_sec / 60.0

    drift_abs_max_um = np.nanmax(np.abs(dshift), axis=0)
    drift_range_um = np.nanmax(dshift, axis=0) - np.nanmin(dshift, axis=0)
    drift_median_um = np.nanmedian(dshift, axis=0)

    mat_out = results_dir / "ks4_drift.mat"

    savemat(
        mat_out,
        {
            "dshift_um": dshift,
            "time_sec": time_sec[:, np.newaxis],
            "time_min": time_min[:, np.newaxis],
            "yblk_um": yblk[:, np.newaxis] if yblk.ndim == 1 else yblk,
            "fs": fs,
            "batch_size_samples": batch_size,
            "n_batches": n_batches,
            "n_blocks": n_blocks,
            "drift_abs_max_um": drift_abs_max_um,
            "drift_range_um": drift_range_um,
            "drift_median_um": drift_median_um,
        },
    )

    print("Export complete.")
    print(f"Folder: {results_dir}")
    print(f"dshift shape: {dshift.shape}")
    print(f"Saved: {mat_out}")


if __name__ == "__main__":
    export_ks4_drift(".")
