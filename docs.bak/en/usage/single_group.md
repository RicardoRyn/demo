# Single-Group Bar Chart

## Quick Plotting

A bar chart is a commonly used graphical tool for displaying numerical comparisons between different categories.
It represents the values of various categories through a set of vertical or horizontal rectangular bars, where the height (or length) of the bars corresponds to the data magnitude.
Bar charts are intuitive and clear, suitable for comparing group means, especially for visualizing discrete categorical data.
In scientific research and data analysis, bar charts are often used to present differences between experimental and control groups.
`plotfig` is developed based on the powerful `matplotlib`, simplifying the plotting process to make multi-group data comparison more intuitive.

For example, we have 3 groups of data (with 9 samples, 10 samples, and 11 samples respectively) displayed through a bar chart to show the differences between them.


```python
import numpy as np
from plotfig import *

data1 = np.random.normal(1, 1, 9)
data2 = np.random.normal(2, 1, 10)
data3 = np.random.normal(3, 1, 11)

ax = plot_one_group_bar_figure([data1, data2, data3])
```


    
![png](single_group_files/single_group_3_0.png)
    


## Multi-Subplots

With the help of `matplotlib`, we can pre-create `figure` and `axes` externally, allowing for flexible drawing of multiple subplots to achieve more complex graphic layouts.
For more advanced subplot layout methods, please see the [tutorial in matplotlib](https://matplotlib.org/stable/users/explain/axes/mosaic.html).


```python
import numpy as np
import matplotlib.pyplot as plt
from plotfig import *

ax1_bar1 = np.random.normal(0, 1, 7)
ax1_bar2 = np.random.normal(0, 1, 8)
ax2_bar1 = np.random.normal(0, 1, 9)
ax2_bar2 = np.random.normal(0, 1, 10)

fig, axes = plt.subplots(1, 2, figsize=(6, 3))
fig.subplots_adjust()

ax1 = plot_one_group_bar_figure([ax1_bar1, ax1_bar2], ax=axes.flatten()[0])
ax2 = plot_one_group_bar_figure([ax2_bar1, ax2_bar2], ax=axes.flatten()[1])
```


    
![png](single_group_files/single_group_6_0.png)
    


More `axes`.


```python
import numpy as np
import matplotlib.pyplot as plt
from plotfig import *

ax1_bar1 = np.random.normal(3, 1, 7)
ax1_bar2 = np.random.normal(3, 1, 8)
ax2_bar1 = np.random.normal(3, 1, 9)
ax2_bar2 = np.random.normal(3, 1, 10)
ax3_bar1 = np.random.normal(3, 1, 9)
ax3_bar2 = np.random.normal(3, 1, 10)
ax4_bar1 = np.random.normal(3, 1, 9)
ax4_bar2 = np.random.normal(3, 1, 10)


fig, axes = plt.subplots(2, 2, figsize=(6, 6))
fig.subplots_adjust(wspace=0.5, hspace=0.5)
ax1 = plot_one_group_bar_figure([ax1_bar1, ax1_bar2], ax=axes[0,0], labels_name=["A", "B"])
ax2 = plot_one_group_bar_figure([ax2_bar1, ax2_bar2], ax=axes[0,1], labels_name=["C", "D"])
ax3 = plot_one_group_bar_figure([ax3_bar1, ax3_bar2], ax=axes[1,0], labels_name=["E", "F"])
ax4 = plot_one_group_bar_figure([ax4_bar1, ax4_bar2], ax=axes[1,1], labels_name=["G", "H"])
```


    
![png](single_group_files/single_group_8_0.png)
    


## Chart Beautification

### Parameter Settings

We can create the `fig` object externally to flexibly control the image size.
`plotfig` provides rich options for customizing chart styles.
The following shows example usage of some common parameters in the `plot_one_group_bar_figure` function.

For complete parameter descriptions, please refer to the API documentation for [`plot_one_group_bar_figure`](../api/index.md/#plotfig.bar.plot_one_group_bar_figure).


```python
import numpy as np
import matplotlib.pyplot as plt
from plotfig import *

data1 = np.random.normal(7, 1, 10)
data2 = np.random.normal(8, 1, 9)

fig, ax = plt.subplots(figsize=(3, 3))
ax = plot_one_group_bar_figure(
    [data1, data2],
    ax=ax,
    labels_name=["A", "B"],
    x_label_name="x",
    y_label_name="y",
    title_name="Title name",
    title_fontsize=15,
    width=0.5,
    dots_size=15,
    colors=["#4573a5", "orange"],
    color_alpha=0.7,
    errorbar_type="sd",
    edgecolor="r",
)
```


    
![png](single_group_files/single_group_12_0.png)
    


`plot_one_group_bar_figure` supports drawing bar charts in gradient color styles, suitable for displaying association results between different objects.

For example, when we calculate the Spearman correlation of structural connections between homologous brain regions (a total of 20) between "human-chimpanzee, human-macaque, chimpanzee-macaque", this method can be considered for visualization.



```python
import numpy as np
import matplotlib.pyplot as plt
from plotfig import *


human_color = "#e38a48"
chimp_color = "#919191"
macaque_color = "#4573a5"

np.random.seed(42)
human_chimp = np.random.normal(7, 1, 20)
human_macaque = np.random.normal(7, 1, 20)
chimp_macaque = np.random.normal(7, 1, 20)

fig, ax = plt.subplots(figsize=(5,5))
ax = plot_one_group_bar_figure(
    [human_chimp, human_macaque, chimp_macaque],
    ax=ax,
    labels_name=["Human-Chimp", "Human-Macaque", "Chimp-Macaque"],
    y_label_name="Spearman correlation",
    width=0.7,
    errorbar_type="sd",
    gradient_color=True,
    colors_start= [human_color, human_color, chimp_color],
    colors_end= [chimp_color, macaque_color, macaque_color]
)
```


    
![png](single_group_files/single_group_14_0.png)
    


### About x-axis

When x-axis labels are long, the rotation angle can be adjusted to avoid overlapping and improve readability.


```python
import numpy as np
import matplotlib.pyplot as plt
from plotfig import *

# 设置中文字体
plt.rcParams['font.family'] = "Microsoft YaHei"  # 微软雅黑
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号

data1 = np.random.normal(3, 1, 10)
data2 = np.random.normal(4, 1, 9)

fig, axes = plt.subplots(1, 2, figsize=(6, 3))
fig.subplots_adjust(wspace=0.5)
ax1 = plot_one_group_bar_figure(
    [data1, data2],
    ax=axes[0],
    labels_name=["AAAAAAAAAAA", "BBBBBBBBBB"],
    y_label_name="y",
    title_name="Long name",
    title_fontsize=15,
)
ax2 = plot_one_group_bar_figure(
    [data1, data2],
    ax=axes[1],
    labels_name=["AAAAAAAAAAA", "BBBBBBBBBB"],
    y_label_name="y",
    title_name="Anchor center rotation",
    title_fontsize=15,
    x_tick_rotation=10,
    x_label_ha="center",
)
```


    
![png](single_group_files/single_group_17_0.png)
    


### About y-axis

`plot_one_group_bar_figure` defaults to automatically calculating the distance between the highest and lowest points, and setting it to 0.618 of the y-axis length (i.e., the golden ratio) to optimize visual effects.
If you want to manually set the y-axis range, you can use the `y_lim` parameter to customize it.


```python
import numpy as np
import matplotlib.pyplot as plt
from plotfig import *

# Set Chinese font
plt.rcParams['font.family'] = "Microsoft YaHei"  # Microsoft YaHei
plt.rcParams['axes.unicode_minus'] = False  # Display minus sign correctly
```


    
![png](single_group_files/single_group_17_0.png)
    


### About y-axis

`plot_one_group_bar_figure` defaults to automatically calculating the distance between the highest and lowest points, and setting it to 0.618 of the y-axis length (i.e., the golden ratio) to optimize visual effects.
If you want to manually set the y-axis range, you can use the `y_lim` parameter to customize it.


```python
import numpy as np
import matplotlib.pyplot as plt
from plotfig import *

# 设置中文字体
plt.rcParams['font.family'] = "Microsoft YaHei"  # 微软雅黑
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号

data1 = np.random.normal(3, 1, 10)
data2 = np.random.normal(4, 1, 9)

fig, axes = plt.subplots(1, 2, figsize=(6, 3))
fig.subplots_adjust(wspace=0.5)
ax1 = plot_one_group_bar_figure(
    [data1, data2],
    ax=axes[0],
    labels_name=["A", "B"],
    y_label_name="y",
    title_name="Golden ratio display",
    title_fontsize=15,
)
ax2 = plot_one_group_bar_figure(
    [data1, data2],
    ax=axes[1],
    labels_name=["A", "B"],
    y_label_name="y",
    title_name="Manually set y-axis",
    title_fontsize=15,
    y_lim=(2, 6)  # Set y-axis range
)
```


    
![png](single_group_files/single_group_20_0.png)
    


Sometimes we want to fix the bottom of the ax to 0, but are unsure of the specific maximum scale value, we can use `ax_bottom_is_0` to set the ax bottom to 0.


```python
import numpy as np
import matplotlib.pyplot as plt
from plotfig import *

# 设置中文字体
plt.rcParams['font.family'] = "Microsoft YaHei"  # 微软雅黑
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号

data1 = np.random.normal(1,  1, 10)
data2 = np.random.normal(2, 1, 9)

fig, axes = plt.subplots(1, 2, figsize=(6, 3))
fig.subplots_adjust(wspace=0.5)
ax1 = plot_one_group_bar_figure(
    [data1, data2],
    ax=axes[0],
    labels_name=["A", "B"],
    y_label_name="y",
    title_name="Golden ratio display",
    title_fontsize=15,
)
ax2 = plot_one_group_bar_figure(
    [data1, data2],
    ax=axes[1],
    labels_name=["A", "B"],
    y_label_name="y",
    title_name="Do not show negative values",
    title_fontsize=15,
    ax_bottom_is_0=True,  # Do not show negative values
)
```


    
![png](single_group_files/single_group_22_0.png)
    


Sometimes we want to limit the maximum tick value of the y-axis to 1, for example when the y-axis represents Fisher z-transformed correlation coefficients, we can set `y_max_tick_is_1` to fix the maximum tick value of the y-axis to 1.


```python
import numpy as np
import matplotlib.pyplot as plt
from plotfig import *

# 设置中文字体
plt.rcParams['font.family'] = "Microsoft YaHei"  # 微软雅黑
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号

data1 = np.random.normal(0.9,  0.1, 10)
data2 = np.random.normal(0.9, 0.1, 9)

fig, axes = plt.subplots(1, 2, figsize=(6, 3))
fig.subplots_adjust(wspace=0.5)
ax1 = plot_one_group_bar_figure(
    [data1, data2],
    ax=axes[0],
    labels_name=["A", "B"],
    y_label_name="y",
    title_name="Golden ratio display",
    title_fontsize=15,
)
ax2 = plot_one_group_bar_figure(
    [data1, data2],
    ax=axes[1],
    labels_name=["A", "B"],
    y_label_name="y",
    title_name="y-axis max tick to 1",
    title_fontsize=15,
    y_max_tick_is_1=True,  # y-axis max tick to 1
)
```


    
![png](single_group_files/single_group_24_0.png)
    


Sometimes we may want to change the display format of the y-axis, for example using scientific notation to present values, we can use the `math_text` parameter to set this.


```python
import numpy as np
import matplotlib.pyplot as plt
from plotfig import *

# 设置中文字体
plt.rcParams['font.family'] = "Microsoft YaHei"  # 微软雅黑
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号

data1 = np.random.normal(10000, 1000, 10)
data2 = np.random.normal(11000, 1000, 9)
data3 = np.random.normal(0.0001, 0.0001, 11)
data4 = np.random.normal(0.0001, 0.0001, 12)

fig, axes = plt.subplots(2, 2, figsize=(6, 6))
fig.subplots_adjust(wspace=0.5, hspace=0.5)
ax1 = plot_one_group_bar_figure(
    [data1, data2],
    ax=axes[0,0],
    labels_name=["A", "B"],
    y_label_name="y",
    title_name="Scientific notation",
    title_fontsize=15,
)  # Default y-axis uses scientific notation
ax2 = plot_one_group_bar_figure(
    [data1, data2],
    ax=axes[0,1],
    labels_name=["A", "B"],
    y_label_name="y",
    title_name="No scientific notation",
    title_fontsize=15,
    math_text=False,  # Manually disable scientific notation
)
ax3 = plot_one_group_bar_figure(
    [data3, data4],
    ax=axes[1,0],
    labels_name=["A", "B"],
    y_label_name="y",
    title_name="Scientific notation",
    title_fontsize=15,
)  # Default y-axis uses scientific notation
ax4 = plot_one_group_bar_figure(
    [data3, data4],
    ax=axes[1,1],
    labels_name=["A", "B"],
    y_label_name="y",
    title_name="No scientific notation",
    title_fontsize=15,
    math_text=False,  # Manually disable scientific notation
)
```


    
![png](single_group_files/single_group_26_0.png)
    


Sometimes we want to display the Y-axis in percentage format.

!!! warning
    The `percentage` format conflicts with `math_text`.
    Since `math_text` is enabled by default, it needs to be explicitly disabled.


```python
import numpy as np
import matplotlib.pyplot as plt
from plotfig import *

# 设置中文字体
plt.rcParams['font.family'] = "Microsoft YaHei"  # 微软雅黑
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号

data1 = np.random.normal(0.5,  0.1, 10)
data2 = np.random.normal(0.5, 0.1, 9)

fig, axes = plt.subplots(1, 2, figsize=(6, 3))
fig.subplots_adjust(wspace=0.5)
ax1 = plot_one_group_bar_figure(
    [data1, data2],
    ax=axes[0],
    labels_name=["A", "B"],
    y_label_name="y",
    title_name="Normal display",
    title_fontsize=15,
)
ax2 = plot_one_group_bar_figure(
    [data1, data2],
    ax=axes[1],
    labels_name=["A", "B"],
    y_label_name="y",
    title_name="Display percentage",
    title_fontsize=15,
    math_text=False,
    percentage=True,
)
```


    
![png](single_group_files/single_group_28_0.png)
    


### About Scatter Points

`plot_one_group_bar_figure` allows assigning colors to each scatter point, commonly used to distinguish data from different sources.


```python
import numpy as np
import matplotlib.pyplot as plt
from plotfig import *

# 设置中文字体
plt.rcParams['font.family'] = "Microsoft YaHei"  # 微软雅黑
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号

data1 = np.random.normal(0.5,  0.1, 10)
data2 = np.random.normal(0.5, 0.1, 9)
dots_color1 = [["blue"]*10, ["red"]*9]
dots_color2 = [["green"]*5+["pink"]*5, ["orange"]*4+["purple"]*5]

fig, axes = plt.subplots(1, 2, figsize=(6, 3))
fig.subplots_adjust(wspace=0.5)
ax1 = plot_one_group_bar_figure(
    [data1, data2],
    ax=axes[0],
    labels_name=["A", "B"],
    y_label_name="y",
    title_name="Scatter points same color",
    title_fontsize=15,
    dots_color=dots_color1,  # Scatter point colors
)
ax2 = plot_one_group_bar_figure(
    [data1, data2],
    ax=axes[1],
    labels_name=["A", "B"],
    y_label_name="y",
    title_name="Scatter points individual colors",
    title_fontsize=15,
    dots_color=dots_color2,  # Scatter point colors
)
```


    
![png](single_group_files/single_group_31_0.png)
    


## Statistics

`plot_one_group_bar_figure` can quickly implement statistical comparisons between bars. Currently supports the following statistical methods:

1. Independent samples t-test (`ttest_ind`)
2. Paired samples t-test (`ttest_rel`)
3. One-sample t-test (`ttest_1samp`)
4. Mann-Whitney U test (`mannwhitneyu`)
5. External statistical test (`external`)

To use, first enable the statistical function through the `statistic` option, and specify the method name in `test_method`.


```python
import numpy as np
import matplotlib.pyplot as plt
from plotfig import *

# 设置中文字体
plt.rcParams['font.family'] = "Microsoft YaHei"  # 微软雅黑
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号

np.random.seed(42)
data1 = np.random.normal(3, 1, 30)
data2 = np.random.normal(4, 1, 31)
data3 = np.random.normal(5, 1, 31)
data4 = np.random.normal(2, 1, 9)
data5 = np.random.normal(4, 1, 10)
data6 = np.random.normal(0, 1, 20)
data7 = np.random.normal(1, 1, 20)

fig, axes = plt.subplots(2, 2, figsize=(6, 6))
fig.subplots_adjust(wspace=0.5, hspace=0.5)
ax1 = plot_one_group_bar_figure(
    [data1, data2],
    ax=axes[0,0],
    labels_name=["A", "B"],
    y_label_name="y",
    title_name="独立样本t检验",
    title_fontsize=15,
    statistic=True, 
    test_method=["ttest_ind"]
)
ax2 = plot_one_group_bar_figure(
    [data2, data3],
    ax=axes[0,1],
    labels_name=["A", "B"],
    y_label_name="y",
    title_name="配对样本t检验",
    title_fontsize=15,
    statistic=True, 
    test_method=["ttest_rel"]
)
ax3 = plot_one_group_bar_figure(
    [data6, data7],
    ax=axes[1,0],
    labels_name=["A", "B"],
    y_label_name="y",
    title_name="单样本t检验",
    title_fontsize=15,
    statistic=True,
    test_method=["ttest_1samp"],
    popmean=0,
)
ax4 = plot_one_group_bar_figure(
    [data4, data5],
    ax=axes[1,1],
    labels_name=["A", "B"],
    y_label_name="y",
    title_name="Mann-Whitney U检验",
    title_fontsize=15,
    statistic=True, 
    test_method=["mannwhitneyu"]
)
```


    
![png](single_group_files/single_group_34_0.png)
    


"External statistical test" (`external`) means users can use other statistical software to complete the test, just pass the calculated p-values to the function.
External statistical tests need to additionally pass in the corresponding p-value list through `p_list`.

!!! note
    When using "external statistical test" and there are multiple bars to compare, the input *p*-values should follow the following order:

    - 1 → 2, 1 → 3, …, 1 → n  
    - 2 → 3, 2 → 4, …, 2 → n  
    - And so on


```python
import numpy as np
import matplotlib.pyplot as plt
from plotfig import *

# 设置中文字体
plt.rcParams['font.family'] = "Microsoft YaHei"  # 微软雅黑
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号

np.random.seed(42)
data1 = np.random.normal(5,  1, 20)
data2 = np.random.normal(7, 1, 20)
data3 = np.random.normal(7, 1, 20)
data4 = np.random.normal(9, 1, 20)

p_list = [0.05, 0.01, 0.001, 1, 0.05, 0.01]

fig, ax = plt.subplots(figsize=(6, 6))
ax = plot_one_group_bar_figure(
    [data1, data2, data3, data4],
    ax=ax,
    y_label_name="y",
    title_name="外部检验",
    title_fontsize=15,
    statistic=True,
    test_method=["external"],
    p_list=p_list,
)
```


    
![png](single_group_files/single_group_36_0.png)
    


# Single-Group Violin Plot

A violin plot is a visualization tool that combines the features of a box plot and a kernel density estimation plot, used to display the distribution of data.
It not only shows statistical information such as the median and quartiles of the data, but also intuitively reflects the distribution shape of data in different value ranges through symmetrical kernel density curves.
Compared to traditional box plots, violin plots can more comprehensively reveal characteristics such as multimodality and skewness of data, making them suitable for comparing distribution differences among multiple groups.
When data distributions are uneven and non-parametric statistical methods are used, violin plots are often more appropriate for display.

In plotfig, the function name for drawing violin plots is `plot_one_group_violin_figure`.
Most of its parameters are similar to `plot_one_group_bar_figure`, here are some demonstrations.

For complete parameter descriptions, please refer to the API documentation for [`plot_one_group_violin_figure`](../api/index.md/#plotfig.bar.plot_one_group_violin_figure).


```python
import numpy as np
import matplotlib.pyplot as plt
from plotfig import *


human_color = "#e38a48"
chimp_color = "#919191"
macaque_color = "#4573a5"

np.random.seed(42)
human_chimp = 1 + np.random.normal(0, 1, 100)
human_macaque = 2 + np.random.normal(0, 1, 100)
chimp_macaque = 3 + np.random.normal(0, 1, 100)

fig, ax = plt.subplots(figsize=(5,5))
ax = plot_one_group_violin_figure(
    [human_chimp, human_macaque, chimp_macaque],
    ax=ax,
    labels_name=["Human-Chimp", "Human-Macaque", "Chimp-Macaque"],
    y_label_name="Spearman correlation",
    width=0.7,
    gradient_color=True,
    colors_start= [human_color, human_color, chimp_color],
    colors_end= [chimp_color, macaque_color, macaque_color],
    show_dots=True,
    dots_size=7,
    statistic=True,
    test_method=["mannwhitneyu"]
)
```


    
![png](single_group_files/single_group_39_0.png)
    

