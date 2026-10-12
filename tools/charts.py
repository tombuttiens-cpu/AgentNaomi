"""Charts for the report attachment (her request: Bourdon row times with trend line)."""

from __future__ import annotations


def bourdon_chart(row_times: list[float], out_png: str, mark_row: int = 25) -> float:
    """Line chart of all row times with a linear trend line. Returns the slope
    (seconds per row; negative = getting faster)."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np

    x = np.arange(1, len(row_times) + 1)
    y = np.asarray(row_times, dtype=float)
    slope, intercept = np.polyfit(x, y, 1)

    fig, ax = plt.subplots(figsize=(6.3, 2.4), dpi=200)
    ax.plot(x, y, color="#1f4e79", lw=1.2, marker="o", ms=2.5, label="Regeltijd")
    ax.plot(x, slope * x + intercept, color="#c00000", lw=1.2, ls="--", label="Trendlijn")
    if mark_row and len(y) > mark_row:
        ax.axvline(mark_row + 0.5, color="#888", lw=0.8, ls=":")
        ax.text(mark_row + 0.8, y.max() + 0.2, f"regel {mark_row}", fontsize=7, color="#666")
    ax.set_xlabel("Regel", fontsize=8)
    ax.set_ylabel("Tijd (s)", fontsize=8)
    ax.tick_params(labelsize=7)
    ax.set_xlim(0.5, len(y) + 0.5)
    ax.legend(fontsize=7, frameon=False, loc="upper right")
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    fig.tight_layout()
    fig.savefig(out_png)
    plt.close(fig)
    return float(slope)
