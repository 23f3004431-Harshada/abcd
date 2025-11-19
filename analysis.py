# Marimo notebook
# Your email: 23f3004431@ds.study.iitm.ac.in

import marimo

@marimo.cell
def __():
    import numpy as np
    import pandas as pd
    import marimo as mo
    return np, pd, mo


# Cell 1: Create synthetic dataset
# No dependencies → feeds data to later cells

@marimo.cell
def __(np, pd):
    np.random.seed(42)
    x = np.linspace(0, 20, 200)
    y = 5 * x + np.random.normal(0, 10, size=200)

    df = pd.DataFrame({"x": x, "y": y})
    df.head()
    return df


# Cell 2: Interactive slider
# Depends on mo from cell 0 → used in markdown + plots

@marimo.cell
def __(mo):
    scale_slider = mo.ui.slider(1, 15, value=5, label="Scale for y variable")
    scale_slider
    return scale_slider


# Cell 3: Dynamic Markdown output
# Depends on df (cell 1) and slider (cell 2)

@marimo.cell
def __(df, scale_slider, mo):
    scaled_mean = (df["y"] * scale_slider.value).mean()

    mo.md(f"""
    ## 📊 Dynamic Analysis Summary

    - **Current Scale:** {scale_slider.value}  
    - **Scaled Mean of y:** `{scaled_mean:.2f}`  
    - Adjust the slider to see live updates.

    This Markdown cell updates automatically based on the widget state.
    """)


# Cell 4: Reactive visualization
# Depends on df (cell 1) and slider (cell 2)

@marimo.cell
def __(df, scale_slider):
    import matplotlib.pyplot as plt

    plt.figure(figsize=(6, 4))
    plt.scatter(df["x"], df["y"] * scale_slider.value)
    plt.title(f"Relationship Between X and Scaled Y (Scale = {scale_slider.value})")
    plt.xlabel("x")
    plt.ylabel("scaled y")
    plt.tight_layout()
    plt.show()
