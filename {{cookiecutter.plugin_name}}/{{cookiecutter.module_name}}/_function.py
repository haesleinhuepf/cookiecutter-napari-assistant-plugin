"""
This module is an example of a barebones function plugin for napari

It implements the ``napari_experimental_provide_function`` hook specification.
see: https://napari.org/docs/dev/plugins/hook_specifications.html

Replace code below according to your needs.
"""
from typing import TYPE_CHECKING

from enum import Enum
import numpy as np
from napari_plugin_engine import napari_hook_implementation

if TYPE_CHECKING:
    from napari.types import ImageData, LabelsData, LayerDataTuple


# This is the actual plugin function, where we export our function
# (The functions themselves are defined below)
@napari_hook_implementation
def napari_experimental_provide_function():
    # we can return a single function
    # or a tuple of (function, magicgui_options)
    # or a list of multiple functions with or without options, as shown here:
    return [process_image]


# 1.  First example, a simple function that thresholds an image and creates a labels layer
def process_image(data: "ImageData", {{cookiecutter.python_parameters}}) -> "LabelsData":
    
	{{cookiecutter.python_code}}
