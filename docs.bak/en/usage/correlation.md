# Correlation Plot

A scatter plot with correlation line is a type of visualization graph used to show the correlation relationship between two variables. Usually, each sample's pair of variable values is plotted as points in the graph, and their correlation degree is reflected through fitting lines, correlation coefficients, and significance annotations.
It is a common method for exploring linear or nonlinear relationships between variables, especially common in scientific research and data analysis.

`plot_correlation_figure` provides a simple and easy-to-use scatter plot with correlation line functionality, capable of automatically plotting variable scatter points and fitting lines, and calculating and displaying either Spearman or Pearson correlation coefficients (Spearman correlation is calculated by default).
At the same time, `plot_correlation_figure` automatically annotates `*`, `**`, or `***` based on significance levels, helping users quickly determine whether the correlation is significant, suitable for use in scientific research charts, presentation slides, or paper illustrations.

## Quick Plotting

Suppose we have two sets of data with consistent sample sizes (each set contains 100 samples), and we want to visually show whether there is a correlation between them.
This can typically be achieved through a scatter plot with correlation line, plotting each pair of sample values as scatter points, and judging the correlation degree and significance between variables by combining fitting lines and correlation coefficients.


```python
import numpy as np
import matplotlib.pyplot as plt
from plotfig import *

np.random.seed(42)
data1 = np.arange(100)
data2 = data1 + np.random.normal(1,50, 100)
# data2 is data1 with added noise.
# Everyone knows data1 and data2 are correlated, but does plotfig know?

ax = plot_correlation_figure(data1,data2)
```


    
![png](correlation_files/correlation_4_0.png)
    


## Parameter Settings

All parameters can be found in the API documentation for [`plot_correlation_figure`](../api/index.md/#plotfig.correlation).


```python
import numpy as np
import matplotlib.pyplot as plt
from plotfig import *

np.random.seed(42)
data1 = np.arange(100)
data2 = data1 + np.random.normal(1,50, 100)
# data2 is data1 with added noise.
# Everyone knows data1 and data2 are correlated, but does plotfig know?

fig, ax = plt.subplots(figsize=(3, 3))
ax = plot_correlation_figure(
    data1,
    data2,
    stats_method="spearman",  # Only "spearman, pearson", default is spearman
    ci=True,  # Show 95% confidence interval
    dots_color="green",
    line_color="pink",
    title_name="Correlation between data1 and data2",
    title_fontsize=10,
    title_pad=20,  # Controls the distance between title and plot, default is 10
    x_label_name="Data1",
    y_label_name="Data2",
)
```


    
![png](correlation_files/correlation_7_0.png)
    


Using `hexbin=True`, we can show the density of a large number of scatter points without having to plot all of them.


```python
import numpy as np
import matplotlib.pyplot as plt
from plotfig import *

np.random.seed(42)
n = 100_000
data1 = np.random.standard_normal(n)
data2 = 2.0 + 3.0 * data1 + 4.0 * np.random.standard_normal(n)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7, 3), layout="constrained")
ax1 = plot_correlation_figure(
    data1,
    data2,
    ax=ax1
)

hb = plot_correlation_figure(
    data1,
    data2,
    ax=ax2,
    hexbin=True,
    hexbin_cmap="Reds",
    hexbin_gridsize=30
)
cb = fig.colorbar(hb, ax=ax2, label='counts')
```


    
![png](correlation_files/correlation_9_0.png)
    

