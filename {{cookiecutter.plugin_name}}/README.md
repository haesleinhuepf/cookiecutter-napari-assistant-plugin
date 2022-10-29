# {{cookiecutter.plugin_name}}

[![License](https://img.shields.io/pypi/l/{{cookiecutter.plugin_name}}.svg?color=green)](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.plugin_name}}/raw/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/{{cookiecutter.plugin_name}}.svg?color=green)](https://pypi.org/project/{{cookiecutter.plugin_name}})
[![Python Version](https://img.shields.io/pypi/pyversions/{{cookiecutter.plugin_name}}.svg?color=green)](https://python.org)
[![tests](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.plugin_name}}/workflows/tests/badge.svg)](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.plugin_name}}/actions)
[![codecov](https://codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.plugin_name}}/branch/master/graph/badge.svg)](https://codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.plugin_name}})
[![Development Status](https://img.shields.io/pypi/status/{{cookiecutter.plugin_name}}.svg)](https://en.wikipedia.org/wiki/Software_release_life_cycle#Alpha)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/{{cookiecutter.plugin_name}})](https://napari-hub.org/plugins/{{cookiecutter.plugin_name}})

{{cookiecutter.short_description}}

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using with haesleinhuepfs modified napari [cookiecutter-napari-plugin] template.

## Usage

This plugin can be started from the menu `Tools > {{cookiecutter.tools_menu}} > {{cookiecutter.menu_name}} `.

TODO: Explain the parameters of your plugin.
* Tell the user what values to enter and why. E.g. "if the resulting segmentation shows too large objects, enter a smaller sigma value."
* Tell the user how they can validate that your plugin processed their data properly
* Provide a link to example data (e.g. on https://zenodo.org) so that new users can apply your plugin to data it has been developed for.
Please put a screenshot here, e.g. a `screenshot.png` in a sub-folder called `docs`.

![image](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.plugin_name}}//raw/main/docs/screenshot.png)

<!-- TODO: uncomment this as soon as your plugin has been deployed to pypi (see instructions below)
## Installation

You can install `{{cookiecutter.plugin_name}}` via [pip]:

    pip install {{cookiecutter.plugin_name}}
-->

## Similar and related plugins

TODO: Use this section to list/link other napari plugins that have similar functionality or are compatible with yours.
* Think of users who wonder what functions to use to convert their data so that it is compatible to this plugin.
* Think of users who wonder what to do with the output of your plugin.
* Think of plugins that do similar things but work in different contexts.

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## Deployment to collaborators

You can package your plugin as zip file and send it via email to collaborators. They can then install it using pip:

```
pip install {{cookiecutter.plugin_name}}.zip
```

## Deployment to pypi (instructions for developers)

For deploying the plugin to the python package index (pypi), one needs a [pypi user account](https://pypi.org/account/register/) 
first. For deploying the plugin to pypi, one needs to install some tools:

```
python -m pip install --user --upgrade setuptools wheel
python -m pip install --user --upgrade twine
```

The following command allows us to package the souce code as a python wheel. Make sure that the 'dist' and 'build' folders are deleted before doing this:

```
python setup.py sdist bdist_wheel
```

This command ships the just generated package to pypi:

```
python -m twine upload --repository pypi dist/*
```

[Read more about distributing your python package via pypi](https://realpython.com/pypi-publish-python-package/#publishing-to-pypi).


## License

Distributed under the terms of the [{{cookiecutter.license}}] license,
"{{cookiecutter.plugin_name}}" is free and open source software

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

[napari]: https://github.com/napari/napari
[Cookiecutter]: https://github.com/audreyr/cookiecutter
[@napari]: https://github.com/napari
[MIT]: http://opensource.org/licenses/MIT
[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[GNU GPL v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
[GNU LGPL v3.0]: http://www.gnu.org/licenses/lgpl-3.0.txt
[Apache Software License 2.0]: http://www.apache.org/licenses/LICENSE-2.0
[Mozilla Public License 2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
[cookiecutter-napari-plugin]: https://github.com/haesleinhuepf/cookiecutter-napari-plugin
[file an issue]: https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.plugin_name}}/issues
[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
