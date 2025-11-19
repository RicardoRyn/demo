# Brain Surface Plot

Brain surface plot is a chart used to visualize numerical data on the surface of the cerebral cortex.
It can map numerical values of different brain regions to the corresponding areas of the cerebral cortex and display the distribution of these values in a color-coded manner.
This type of chart is commonly used to display various brain region indicators in neuroscience research, such as BOLD signal intensity, myelination degree, volume or thickness, or other numerical brain characteristics.

The `plot_brain_surface_figure` function is developed based on the `surfplot` library, providing a unified and simplified interface for drawing brain surface plots of human, macaque, and chimpanzee brains.
Currently, it supports multiple brain atlases, including:

1. Human Glasser (HCP-MMP) Atlas[^1]. [Atlas CSV file](../assets/atlas_csv/human_glasser.csv).
1. Human BNA Atlas[^2]. [Atlas CSV file](../assets/atlas_csv/human_bna.csv).
1. Chimpanzee BNA Atlas[^3]. [Atlas CSV file](../assets/atlas_csv/chimpanzee_bna.csv).
1. Macaque CHARM 5-level [^4]. [Atlas CSV file](../assets/atlas_csv/macaque_charm5.csv).
1. Macaque CHARM 6-level [^4]. [Atlas CSV file](../assets/atlas_csv/macaque_charm6.csv).
1. Macaque BNA Atlas[^5]. [Atlas CSV file](../assets/atlas_csv/macaque_bna.csv).
1. Macaque D99 Atlas[^6]. [Atlas CSV file](../assets/atlas_csv/macaque_d99.csv).

[^1]:
    Glasser, M. F., Coalson, T. S., Robinson, E. C., Hacker, C. D., Harwell, J., Yacoub, E., Ugurbil, K., Andersson, J., Beckmann, C. F., Jenkinson, M., Smith, S. M., & Van Essen, D. C. (2016). A multi-modal parcellation of human cerebral cortex. Nature, 536(7615), Article 7615. https://doi.org/10.1038/nature18933
[^2]:
    Fan, L., Li, H., Zhuo, J., Zhang, Y., Wang, J., Chen, L., Yang, Z., Chu, C., Xie, S., Laird, A. R., Fox, P. T., Eickhoff, S. B., Yu, C., & Jiang, T. (2016). The Human Brainnetome Atlas: A New Brain Atlas Based on Connectional Architecture. Cerebral Cortex (New York, N.Y.: 1991), 26(8), 3508–3526. https://doi.org/10.1093/cercor/bhw157
[^3]:
    Wang, Y., Cheng, L., Li, D., Lu, Y., Wang, C., Wang, Y., Gao, C., Wang, H., Erichsen, C. T., Vanduffel, W., Hopkins, W. D., Sherwood, C. C., Jiang, T., Chu, C., & Fan, L. (2025). The Chimpanzee Brainnetome Atlas reveals distinct connectivity and gene expression profiles relative to humans. The Innovation, 0(0). https://doi.org/10.1016/j.xinn.2024.100755
[^4]:
    Jung, B., Taylor, P. A., Seidlitz, J., Sponheim, C., Perkins, P., Ungerleider, L. G., Glen, D., & Messinger, A. (2021). A comprehensive macaque fMRI pipeline and hierarchical atlas. NeuroImage, 235, 117997. https://doi.org/10.1016/j.neuroimage.2021.117997
[^5]:
    Lu, Y., Cui, Y., Cao, L., Dong, Z., Cheng, L., Wu, W., Wang, C., Liu, X., Liu, Y., Zhang, B., Li, D., Zhao, B., Wang, H., Li, K., Ma, L., Shi, W., Li, W., Ma, Y., Du, Z., … Jiang, T. (2024). Macaque Brainnetome Atlas: A multifaceted brain map with parcellation, connection, and histology. Science Bulletin, 69(14), 2241–2259. https://doi.org/10.1016/j.scib.2024.03.031
[^6]:
    Reveley, C., Gruslys, A., Ye, F. Q., Glen, D., Samaha, J., E. Russ, B., Saad, Z., K. Seth, A., Leopold, D. A., & Saleem, K. S. (2017). Three-Dimensional Digital Template Atlas of the Macaque Brain. Cerebral Cortex, 27(9), 4463–4477. https://doi.org/10.1093/cercor/bhw248

## Whole Brain

### Quick Plotting

!!! info
    Please ensure brain region names are correct before plotting.


```python
from plotfig import *

data = {"lh_V1": 1, "rh_MT": 1.5}

ax = plot_brain_surface_figure(data, species="human", atlas="glasser")
```


    
![png](brain_surface_files/brain_surface_5_0.png)
    



```python
import matplotlib.pyplot as plt
from plotfig import *

macaque_data = {"lh_V1": 1}
chimpanzee_data = {"lh_MVOcC.rv": 1}

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

ax1 = plot_brain_surface_figure(
    chimpanzee_data, species="chimpanzee", atlas="bna", ax=ax1, title_name="Chimpanzee"
)
ax2 = plot_brain_surface_figure(
    macaque_data, species="macaque", atlas="charm5", ax=ax2, title_name="Macaque"
)
```


    
![png](brain_surface_files/brain_surface_6_0.png)
    


### Parameter Settings

All parameters can be found in the API documentation for [`plot_brain_surface_figure`](../api/index.md/#plotfig.brain_surface.plot_brain_surface_figure).


```python
from plotfig import *

data = {"lh_V1": 1, "rh_MT": 1.5, "rh_V1": -1}

ax = plot_brain_surface_figure(
    data,
    species="human",
    atlas="glasser",
    surf="inflated",
    cmap="bwr",
    vmin=-1,
    vmax=1,
    colorbar=True,
    colorbar_label_name="AAA"
)
```


    
![png](brain_surface_files/brain_surface_9_0.png)
    

