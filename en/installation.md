# Installation

## Installation Methods

`plotfig` supports installation via `pip` or from source code, requiring Python 3.11 or higher.

### Install using pip (Recommended)

```bash
pip install plotfig
```

### Install from GitHub source code

```bash
git clone --depth 1 https://github.com/RicardoRyn/plotfig.git
cd plotfig
pip install .
```

## Dependency Requirements

`plotfig` depends on several core libraries, which will be automatically handled during the installation process, but please note:

- [surfplot](https://github.com/danjgale/surfplot) must use the latest version from its GitHub repository, not the PyPI version, as the latter does not yet contain the required functionality.

!!! warning "Specify `surfplot` version"

    Due to the outdated `surfplot` version on PyPI, which lacks the functionality required by `plotfig`, it is recommended to install the latest version from its GitHub repository using the following steps.

    If you don't need to draw `brain surface` plots, you can skip this step.

    ```bash
    # Uninstall old version
    pip uninstall surfplot

    # Clone source code and install
    git clone --depth 1 https://github.com/danjgale/surfplot.git
    cd surfplot
    pip install .

    # After installation, return to the parent directory and delete the source code folder
    cd ..
    rm -rf surfplot
    ```

## Contribution Guidelines

**_The `dev` branch usually contains the latest features and fixes not yet merged into `main`._**

If you wish to experience these features or participate in `plotfig` development, you can choose to install the project in development mode (editable mode).

This installation method allows modifications to your local source code to take effect immediately, making it ideal for debugging, development, and code contributions.

It is recommended to first fork the repository, then clone your own fork and install the `dev` branch:

```bash
git clone -b dev https://github.com/<your-username>/plotfig.git
cd plotfig
pip install -e .
```

---

**Welcome to submit Issues or PRs!**

Whether it's bug reports, feature suggestions, or documentation improvements.

They are all very welcome to be proposed in [Issue](https://github.com/RicardoRyn/plotfig/issues).

You can also directly submit [PRs](https://github.com/RicardoRyn/plotfig/pulls) to make it better together 💪！
