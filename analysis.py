# Marimo notebook
# Your email: 23f3004431@ds.study.iitm.ac.in

import marimo

@marimo.cell
def __():
    import numpy as np
    import pandas as pd
    import marimo as mo
    return np, pd, mo

# Cell 1: Generate synthetic data
# This cell has no dependencies.
# Output is used by Cell 2.

@marimo.cell
def __(np, pd):
    np.random.seed(0)
    x = np.linspace(0, 10, 100)
    y = 3 * x + np.random.normal(0, 2, size=100)
    df = pd.DataFrame({"x": x, "y": y})
    df.head()
    return df


# Cell 2: Slider widget controlling multiplier
# This cell depends on `mo` from the first cell.
@marimo.cell
def __(mo):
    multiplier = mo.ui.slider(1, 10, value=3, label="Y-scale multiplier")
    multiplier
    return multiplier


# Cell 3: Dynamic Markdown output
# Depends on: df (cell 1), multiplier (cell 2)
@marimo.cell
def __(df, multiplier, mo):
    scaled_mean = (df["y"] * multiplier.value).mean()
    mo.md(f"""
    ### 📌 Dynamic Analysis  
    - **Multiplier:** {multiplier.value}  
    - **Scaled Mean of y:** {scaled_mean:.2f}

    Adjust the slider to update results in real-time.
    """)


# Cell 4: Plot (reactive)
# Shows how data from earlier cells flows into this visualization.
@marimo.cell
def __(df, multiplier):
    import matplotlib.pyplot as plt

    plt.figure(figsize=(6,4))
    plt.scatter(df["x"], df["y"] * multiplier.value)
    plt.title(f"Scaled Y vs X (Multiplier = {multiplier.value})")
    plt.xlabel("x")
    plt.ylabel("scaled y")
    plt.tight_layout()
    plt.show()
