# Collective Knowledge

Collective Knowledge (CK) is an open-source meta-framework
to manage, connect and reuse artifacts, scripts and workflows 
on any platform with any software stack.

CK helps researchers and developers turn their scripts and artifacts
into a database of [portable, reusable, customizable and deterministic components](https://arxiv.org/pdf/2011.01149.pdf)
with minimal effort and no changes to their projects.

All such components have a simple, human-friendly and platform-independent CLI, Python API,
JSON/YAML meta description, tags, and Unique ID automatically generated by CK.

This approach allows users to automatically plug any ad-hoc scripts and artifacts 
from the community into their projects, build systems, CI/CD tools,
containers, Jupyter/Colab notebooks and any other technology.

CK runtime system also helps users interconnect any scripts and artifacts 
into portable workflows, applications and web-services.
They can run natively or inside containers while automatically 
adapting to any given software and hardware.

Any output of CK components and workflows (CSV/XLS/JSON/YAML files,
pre-processed data set, notes and optimized code) can be also stored 
as CK components with all related CM dependencies.
Such database-like organization of projects makes it easier
for the community to re-run, reproduce and reuse research results.

We have donated CK to the [MLCommons foundation](https://mlcommons.org) 
to benefit everyone after it was successfully validated by Qualcomm, Arm, General Motors,
OctoML, Krai, HPE, Dell, Lenovo and other organizations.

We continue improving and enhancing CK based on your feedback and requirements - 
feel free to join our [open workgroup](docs/mlperf-education-workgroup.md) 
to provide your feedback and participate in further developments!


&copy; 2021-2022 [MLCommons](https://mlcommons.org)<br>

Apache 2.0 license



# Getting Started

### Collective Mind meta-framework

Collective Mind (CM) is the second generation of the CK meta-framework
being developed by the [open workgroup](docs/mlperf-education-workgroup.md)
to modularize complex AI systems and automate their co-design, benchmarking, 
optimization and deployment across continuously changing software, hardware and data.

[![PyPI version](https://badge.fury.io/py/cmind.svg)](https://pepy.tech/project/cmind)
[![Python Version](https://img.shields.io/badge/python-3+-blue.svg)](https://github.com/mlcommons/ck/tree/master/cm)
[![License](https://img.shields.io/badge/License-Apache%202.0-green)](https://github.com/mlcommons/ck/tree/master/cm)
[![CM(CK2) test](https://github.com/mlcommons/ck/actions/workflows/test-cm.yml/badge.svg)](https://github.com/mlcommons/ck/actions/workflows/test-cm.yml)



### Installation

CM meta-framework is implemented as a small Python class with a CLI and minimal dependencies 
(Python 3+, PIP and Git client). It can be installed on any platform using PIP:

```bash
pip install cmind

cm version
```
```
1.0.1

```

Please check the [CM installation guide](cm/docs/installation.md) 
to install system dependencies and CM on Linux, Windows, MacOS 
and other operating systems. 

If you encounter any problems, just open a ticket [here](https://github.com/mlcommons/ck/issues)
and we will get back to you!



### Repositories with reusable and cross-platform scripts

CM allows users to add simple database-like interface to their existing Git repositories
to make it easier for the community to reuse their artifacts and automation scripts.

We are working with the community to assemble various artifacts and scripts 
from [reproduced ML and Systems papers](https://cknowledge.io/reproduced-papers) 
and [MLPerf benchmarks](https://github.com/mlcommons)
as cross-platform CM components in this [GitHub repository](https://github.com/mlcommons/ck/tree/master/cm-mlops).
 
These components provide a unified API, CLI and meta to automatically download, install, build and interconnect
ML applications, models, data sets, engines, libraries, SDKs and tools
for different platforms and operating systems.

You can install this repository (or any other repository with the "CM-compatible logo") as follows:
```bash
cm pull repo --url=https://github.com/mlcommons/ck
```

or

```bash
cm pull repo mlcommons@ck
```

You can then use the CM database interface to list, find, add, remove, update and load any CM component
with a native user artifact or script:
```bash
cm list script

cm find script --tags=app,image-classification
```

You can also run any shared script on any platform via the CM runtime natively or inside a container as follows:
```bash
cm run script --tags=detect,os --out
```

You can run the same script similar to a unified micro-service or standalone app using CM Python API as follows:
```python
import cmind
r=cmind.access({'action':'run', 'automation':'script', 'tags':'get,os'})
print (r)
```

### Image classification example

Users can pull multiple public and private repositories compatible with the CM
and automatically interconnect shared CM components into portable applications and workflows.

The following example demonstrates how to run a modular image classification workflow using CM. 
CM workflow is also a unified CM component that chains other [cross-platform CM components](https://github.com/mlcommons/ck/blob/master/cm-mlops/script) 
using a [simple and human friendly JSON/YAML description](https://github.com/mlcommons/ck/blob/master/cm-mlops/script/app-image-classification-onnx-py/_cm.json).

These components update global environments and a CM "state" dictionary similar to native scripts
while automatically detecting, downloading, installing and building all related artifacts
and tools to adapt this workflow to any user platform:

```bash
cm run script --tags=app,image-classification,onnx,python --quiet
cm run script --tags=app,image-classification,onnx,python --input=my-image.jpg
```

or using Python scripting:
```python
import cmind
r=cmind.access({'action':'run', 'automation':'script'
                'tags':'app,image-classification,onnx,python',
                'quiet':True})
print (r)
```


It may take a few minutes to run this workflow for the first time and adapt it to your platform depending on the Internet speed.
Note that all the subsequent runs will be much faster because CM automatically caches the output of all components to be quickly reused
in this and other CM workflows.



### Tutorials


* [Digging into image classification CM workflow](cm/docs/example-modular-image-classification.md)
* [Understanding CM database and runtime interface](cm/docs/tutorial-concept.md)
* [Understanding cross-platform CM scripts](cm/docs/tutorial-scripts.md)
* [Running and reproducing MLPerf inference benchmarks](docs/mlperf-cm-automation-demo.md)
* [Adding new artifacts, scripts and workflows to CM](cm/docs/tutorial-scripts.md#adding-new-artifacts-scripts-and-workflows-to-cm) 

### Documentation

* [Internal diagram](cm/docs/structure.md)
* [High-level specification with common CM commands](cm/docs/specification.md)
* [Conventions](cm/docs/conventions.md)



### Contributing

Please check this [guide](cm/docs/tutorial-scripts.md#adding-new-artifacts-scripts-and-workflows-to-cm) 
to plug your own artifacts, scripts and workflows into CM.

You can then share CM components in your Git repository for your own scripts and artifacts 
to help the community reuse and build upon them (similar to this [CM repository](https://github.com/mlcommons/ck/tree/master/cm-mlops)).

You can join our [open workgroup](docs/mlperf-education-workgroup.md)
and/or contribute your own CM components [here](https://github.com/mlcommons/ck/tree/master/cm-mlops/script).

These components must automatically download, install, build and preprocess different applications, models,
data sets, frameworks, compilers, SDKs and tools across different platforms and operating systems
to help the community modularize, simplify, co-design, benchmark, optimize and deploy efficient AI/ML systems.

You are very welcome to provide feedback and report bugs [here](https://github.com/mlcommons/ck/issues).

Thank you for your support and looking forward to collaborating with you!



### Legacy Collective Knowledge framework (CK)

Please check [this page](ck1) to get the legacy CK framework v2.6.1.
Note that we are gradually converting old CK components and workflows
to the new CM format - please open a [ticket](https://github.com/mlcommons/ck/issues) if you need help!



# On-going community projects

* [Open workgroup to automate co-design, benchmarking, optimization and deployment of ML Systems](docs/mlperf-education-workgroup.md)
* [Artifact evaluation and reproducibility initiatives at conferences](https://cTuning.org/ae)


# Resources and references

* [Our motivation](cm/docs/motivation.md)
* [Journal article describing our concept](https://arxiv.org/pdf/2011.01149.pdf)
* ["Reproducing 150 Research Papers and Testing Them in the Real World" (ACM TechTalk; Feb 2021)](https://learning.acm.org/techtalks/reproducibility)
* ["MLOps Is a Mess But That's to be Expected" (March 2022)](https://www.mihaileric.com/posts/mlops-is-a-mess)
* ["Automating MLPerf design space exploration and production deployment" (HPCA'22)](https://doi.org/10.5281/zenodo.6475385)
* ["Collaboratively Benchmarking and Optimizing Deep Learning Implementations" (General Motors; Jun 2017)]( https://youtu.be/1ldgVZ64hEI )
* [MLOps projects, articles and tools](https://github.com/mlcommons/ck/tree/master/cm/docs/KB/MLOps.md)


# Maintainers

* [Grigori Fursin](https://cKnowledge.io@gfursin) and [Arjun Suresh](https://www.linkedin.com/in/arjunsuresh) 
  ([OctoML](https://octoml.ai) and [MLCommons](https://mlcommons.org))

