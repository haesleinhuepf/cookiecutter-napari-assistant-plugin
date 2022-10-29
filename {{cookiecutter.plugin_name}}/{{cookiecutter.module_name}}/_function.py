from napari_plugin_engine import napari_hook_implementation
from napari_tools_menu import register_function
from napari_time_slicer import time_slicer

@napari_hook_implementation
def napari_experimental_provide_function():
    return [process_image]

@register_function(menu="{{cookiecutter.tools_menu}} > {{cookiecutter.menu_name}}")
@time_slicer
def process_image({{cookiecutter.python_parameters}}) -> {{cookiecutter.output_type}}:
    """
    {{cookiecutter.short_description}}
    
    # TODO: Provide more detailed documentation here. E.g. specify the parameters and what values users should enter.
    """
    # TODO: Check the list of parameters of the function definition above. 
    # If there are parameters that should not be editable by the end user, move their definition and values here instead.
    
    {{cookiecutter.python_code}}
