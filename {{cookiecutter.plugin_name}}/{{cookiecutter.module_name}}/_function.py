"""
This module is an example of a barebones function plugin for napari

It implements the ``napari_experimental_provide_function`` hook specification.
see: https://napari.org/docs/dev/plugins/hook_specifications.html

Replace code below according to your needs.
"""

from enum import Enum
import numpy as np
from napari_plugin_engine import napari_hook_implementation

from napari.types import ImageData, LabelsData, LayerDataTuple
from napari_tools_menu import register_function
from napari_time_slicer import time_slicer

# This is the actual plugin function, where we export our function
# (The functions themselves are defined below)
@napari_hook_implementation
def napari_experimental_provide_function():
    # we can return a single function
    # or a tuple of (function, magicgui_options)
    # or a list of multiple functions with or without options, as shown here:
    return [process_image]


# 1.  First example, a simple function that processes an image and creates a labels or image layer
@register_function("{{cookiecutter.tools_menu}} > {{cookiecutter.menu_name}}")
@time_slicer
def process_image({{cookiecutter.python_parameters}}) -> {{cookiecutter.output_type}}:
    
	{{cookiecutter.python_code}}
