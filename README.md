[![Gitter](https://badges.gitter.im/pyModEA/configuring-cmaes.svg)](https://gitter.im/pyModEA/configuring-cmaes?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

# Summary #
This repository contains the configurable CMA-ES experiments code that uses the Modular EA framework. The framework is available separately as [ModEA](https://github.com/sjvrijn/ModEA).

Most experiments are programmed in the `main.py` file, while the configurable CMA-ES setup is defined in `EvolvingES.py`.


# Example Usage #

## main.py ##
This file is setup mostly to run either an optimizer (currently a MIES, but still labeled as 'GA') or a brute-force enumeration run over all available structure configurations.

The current behavior of executing the file depends on the number of arguments given:
* 0: executes the 'default' option, currently set to a 5D brute-force enumeration over the Sphere function F1.
* 2 (`ndim fid`): executes the 'optimization' option (currently MIES) on the given BBOB function `fid` in `ndim` dimensions
* 3 (`ndim fid run`): executes the 'optimization' option (currently MIES) on the given BBOB function `fid` in `ndim` dimensions, but with an added `run` parameter that is used to log multiple runs without overwriting.
* 4 (`ndim fid parallel part`): executes the 'brute-force enumeration' option on the given BBOB function `fid` in `ndim` dimensions, while explicitly running `parallel` configurations in parallel. Also, to prevent some memory issues, `part` specifies which part out of 4 of the entire list of possible configurations should executed. An external script (e.g. the included `BF_experiment.sh` file) should be used to iterate over parts 1...4.


## EvolvingES.py ##
The most important function in `EvolvingES.py` is`runCustomizedES(representation, iid, rep, ndim, fid, budget)`. This function takes a `representation` from {0,1}^9 X {0,1,2}^2 (optionally extended with a set of parameter values), combined with some BBOB parameters: instance ID `iid`, repetition number `rep`, dimensionality `ndim`, function ID `fid`, and the total available budget in evaluations `budget`. This function takes the representation, splits it into <configuration>, lambda, mu, <other parameters> and passes them on accordingly to the customizedES in [ModEA](https://github.com/sjvrijn/ModEA).

To simplify large runs of experiments, the `evaluateCustomizedESs(...):` function also exists, which tries to automatically parallelize the running of multiple representations over multiple instance ID's of a fixed `fid` and `ndim`.

# Citation #
To cite this work, please use the following reference:
* [Evolving the Structure of Evolution Strategies. Sander van Rijn, Hao Wang, Matthijs van Leeuwen, Thomas Bäck. IEEE SSCI December 6-9 2016, Athens, Greece.](https://ieeexplore.ieee.org/document/7850138)
```
@INPROCEEDINGS{vanrijn2016,
    author={S. {van Rijn} and H. {Wang} and M. {van Leeuwen} and T. {Bäck}},
    booktitle={2016 IEEE Symposium Series on Computational Intelligence (SSCI)}, 
    title={Evolving the structure of Evolution Strategies}, 
    year={2016},
    doi={10.1109/SSCI.2016.7850138},
}
```


# References #
 * [Evolving the Structure of Evolution Strategies. Sander van Rijn, Hao Wang, Matthijs van Leeuwen, Thomas Bäck. IEEE SSCI December 6-9 2016, Athens, Greece.](https://ieeexplore.ieee.org/document/7850138)
 * [Algorithm Configuration Data Mining for CMA Evolution Strategies. Sander van Rijn, Hao Wang, Bas van Stein, Thomas Bäck. GECCO July 15-19 2017, Berlin, Germany.](https://dl.acm.org/citation.cfm?id=3071205) -- Analysis code is published [here](https://github.com/sjvrijn/cma-es-configuration-data-mining).
 * [Towards an Adaptive CMA-ES Configurator. Sander van Rijn, Carola Doerr, Thomas Bäck. PPSN XV September 8-12 2018, Coimbra, Portugal.](https://link.springer.com/chapter/10.1007/978-3-319-99253-2_5)
