# Matrix Plot

A matrix plot is a visualization method used to show pairwise relationships between multiple variables, commonly in the form of a symmetric two-dimensional grid where each cell represents the statistical relationship between a pair of variables.
It is commonly used to explore the correlation structure between multiple variables in a dataset, serving as a common tool in data analysis and scientific plotting.

`plot_matrix_figure` supports automatic generation of matrix plots.

## Quick Plotting

We can generate a 10 × 19 matrix plot to show the pairwise relationships between 10 elements and another 19 elements.


```python
import numpy as np
from plotfig import *

data = np.random.rand(10, 19)

ax = plot_matrix_figure(data)
```


    
![png](matrix_files/matrix_4_0.png)
    


## Parameter Settings

All parameters can be found in the API documentation for [`plot_matrix_figure`](../api/index.md/#plotfig.matrix.plot_matrix_figure).


```python
import numpy as np
import matplotlib.pyplot as plt
from plotfig import *

data = np.random.rand(4,4)

fig, ax = plt.subplots(figsize=(3,3))
ax = plot_matrix_figure(
    data,
    row_labels_name=["A", "B", "C", "D"],
    col_labels_name=["E", "F", "G", "H"],
    cmap="viridis",
    title_name="Matrix Figure",
    title_fontsize=10,
    colorbar=True,
    colorbar_label_name="Colorbar",
)
```


    
![png](matrix_files/matrix_7_0.png)
    

