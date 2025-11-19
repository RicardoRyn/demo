# Brain Connectivity Plot

Transparent brain plot that can display connections between brain regions.
You need to prepare surface files for the left and right hemispheres, nii.gz files related to brain regions, and a connectivity matrix.


```python
import numpy as np
from plotfig import *

# Generate a 31x31 connectivity matrix (symmetric weighted matrix, diagonal is 0)
matrix = np.zeros((31, 31))
matrix[0, 1] = 1
matrix[0, 2] = 2
matrix[0, 3] = 3
matrix[4, 1] = -1
matrix[4, 2] = -2
matrix[4, 3] = -3
matrix = (matrix + matrix.T) / 2  # Matrix symmetry

connectome = matrix

output_file = "./figures/brain_connection.html"

lh_surfgii_file = r"e:\6_Self\plot_self_brain_connectivity\103818.L.midthickness.32k_fs_LR.surf.gii"
rh_surfgii_file = r"e:\6_Self\plot_self_brain_connectivity\103818.R.midthickness.32k_fs_LR.surf.gii"
niigz_file = rf"e:\6_Self\plot_self_brain_connectivity\human_Self_processing_network.nii.gz"

fig = plot_brain_connection_figure(
    connectome,
    lh_surfgii_file=lh_surfgii_file,
    rh_surfgii_file=rh_surfgii_file,
    niigz_file=niigz_file,
    output_file=output_file,
    scale_method="width",
    line_width=10,
)
```


    
![png](brain_connectivity_files/human.gif)
    


HTML files can be interacted with in a browser. You can take screenshots manually, or use the following command to generate images.


```python
from pathlib import Path


Path(f"./figures/brain_connection").mkdir(parents=True, exist_ok=True)  # Create new folder to save frames
save_brain_connection_frames(fig, output_dir=rf"./figures/brain_connection", n_frames=36)
```

    100%|██████████| 36/36 [02:01<00:00,  3.37s/it]

    Saved 36 images in ./figures/brain_connection
    

    
    
