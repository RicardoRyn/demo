# Introduction

`plotfig` is a Python library designed specifically for scientific data visualization, dedicated to providing cognitive neuroscience researchers with efficient, user-friendly, and aesthetically pleasing graphing tools.
This project is developed based on industry-leading visualization libraries such as `matplotlib`, `surfplot`, and `plotly`, integrating the powerful features of all three to meet complex plotting requirements in various scenarios of neuroscience and brain connectomics.

![plotfig](./assets/plotfig.png)

## Project Structure

The project adopts a modular design, containing the following main functional modules:

- `bar.py`: Bar chart plotting, suitable for comparative display of grouped data.
- `correlation.py`: Correlation matrix visualization, facilitating analysis of correlation distributions between variables.
- `matrix.py`: General matrix visualization, supporting multiple color schemes and annotation methods.
- `brain_surface.py`: Brain surface visualization, implementing the drawing of 3D brain surface atlas structures.
- `circos.py`: Circos diagram visualization, suitable for planar display of connections between brain regions.
- `brain_connection.py`: Glass brain connection visualization, supporting the display of complex brain network structures.

## Features

- `plotfig` has a simple API design with flexible parameters, suitable for researchers and data analysts to quickly integrate into their own data analysis workflows.
- Its modular architecture facilitates subsequent feature expansion and custom development.
- Combined with `matplotlib`, it supports vector graphics or high-resolution bitmap and interactive HTML output, suitable for paper publication and academic presentations.

---

Fun fact: All the elements on a figure[^1].
![Parts of a Figure](https://matplotlib.org/stable/_images/anatomy.png)

[^1]: [Quick start guide of matplotlib.](https://matplotlib.org/stable/tutorials/introductory/usage.html#parts-of-a-figure)
