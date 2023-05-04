---
title: libGL swrast and iris errors
categories:
- Graphics issues
feature_image: "https://picsum.photos/2560/600?image=872"
---

When running the game through the `main.py` file, you may briefly see the GUI flash up before disappearing. When you check the terminal, there is a chance that you will be met with an issue along the lines of:

```bash
libGL error: MESA-LOADER: failed to open iris: /usr/lib/dri/iris_dri.so: cannot open shared object file: No such file or directory (search paths /usr/lib/x86_64-linux-gnu/dri:\$${ORIGIN}/dri:/usr/lib/dri)
libGL error: failed to load driver: iris
libGL error: MESA-LOADER: failed to open swrast: /usr/lib/dri/swrast_dri.so: cannot open shared object file: No such file or directory (search paths /usr/lib/x86_64-linux-gnu/dri:\$${ORIGIN}/dri:/usr/lib/dri)
libGL error: failed to load driver: swrast
```

As is natural with errors in Linux, there are many reasons why you may be seeing this. One is that the software was built on an older version of the GCC compiler than what is currently on your system, which essentially means that any aspects of the compiler that have now become outdated will cause random issues.

To fix this, we can install an implementation of libstdcxx-ng using the conda environment which should resolve any compatibility errors.

`conda install -c conda-forge libstdcxx-ng`

The `-c` flag tells conda to install from the `conda-forge` channel, which is a community-led channel that provides updated and verifiable packages for software. If you want to verify the contents of the package for safety yourself, that can be done [here](https://anaconda.org/conda-forge/libstdcxx-ng).

After installing the package, run the game again in a new instance of the terminal (restart VS Code) and run the game.