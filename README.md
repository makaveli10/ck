[![PyPI version](https://badge.fury.io/py/cmind.svg)](https://pepy.tech/project/cmind)
[![Python Version](https://img.shields.io/badge/python-3+-blue.svg)](https://github.com/mlcommons/ck/tree/master/cm/cmind)
[![License](https://img.shields.io/badge/License-Apache%202.0-green)](LICENSE.md)

[![CM test](https://github.com/mlcommons/ck/actions/workflows/test-cm.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cm.yml)
[![CM script automation features test](https://github.com/mlcommons/ck/actions/workflows/test-cm-script-features.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cm-script-features.yml)

### Documentation

* [Table of contents](docs/README.md)

### About

We deeply believe in the power of open science and open source to solve the world's most challenging problems.

Following our [tedious experience reproducing 150 research papers and validating them in the real world](https://learning.acm.org/techtalks/reproducibility),
we started developing Collective Knowledge technology to provide a common interface to access and reuse
any shared knowledge (research projects, experiments, AI/ML models, code, data and automation scripts), 
facilitate reproducible research, and simplify transfer to production across rapidly evolving models, software, hardware and data.

Collective Knowledge technology consists of the following sub-projects:
* Non-intrusive and technology-agnostic [Collective Mind automation language (CM)](https://doi.org/10.5281/zenodo.8105339) 
  helps to convert any project, code or data
  into a collection of portable and reusable components 
  with a unified interaface. 
  CM language allows users to run various automation workflows and applications in the same way either inside automatically generated container snapshots
  or the latest software/hardware stacks (that may fail and then collaboratively improved by the community).
  CM is intended to be always backward compatible and continously extended by the community via Python automation recipes and JSON/YAML meta descriptions:
  * [Common CM automations](https://github.com/mlcommons/ck/tree/master/cm-mlops/automation) 
  * [Portable and reusable CM scripts](https://github.com/mlcommons/ck/tree/master/cm-mlops/script)
  CM provides the same interface 
* [Collective Knowledge Platform (CK Playground)](https://access.cKnowledge.org) provides a user-friendly GUI 
  to help the community explore, reproduce, understand, optimize and reuse the state-of-the-art AI/ML Systems.


The first practical use case for CM language and CK platform is to let everyone participate in collaborative benchmarking,
optimization and validation of the state-of-the-art AI/ML applications across rapidly evolving models, data, software and hardware 
from different vendors - see our [reproducibility and optimization challenges](https://access.cknowledge.org/playground/?action=challenges), 
[shared benchmarking and optimization results for ML Systems (performance, accuracy, power consumption, costs)](https://access.cknowledge.org/playground/?action=experiments) 
and the [leaderboard](https://access.cknowledge.org/playground/?action=contributors).

Read [our documentation](docs/README.md) to learn about how our open-source technology can help you.

Join our [Discord server](https://discord.gg/JjWNWXKxwT) to ask questions, provide feedback and participate in collaborative developments.

### Copyright

2021-2023 [MLCommons](https://mlcommons.org)

### License

[Apache 2.0](LICENSE.md)

### Acknowledgments

This project is supported by [MLCommons](https://mlcommons.org), 
[cKnowledge.org](https://cKnowledge.org),
[cTuning.org](https://cTuning.org),
and [individual contributors](https://github.com/mlcommons/ck/blob/master/CONTRIBUTING.md).
We thank [HiPEAC](https://hipeac.net) and [OctoML](https://octoml.ai) for sponsoring initial development.
