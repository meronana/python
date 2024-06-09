#needed because we are in a sub folder = module
"""
The __init__.py files are required to make 
Python treat directories containing the files as packages.
THis prevents directories with a common name, such as string,
ununtentuanally hiding valid modules that occur later on the module search path.
In the simplest case, __init__.py can just be an empty file
but it can also execute initialization code for the package.
"""

from .test import * #go and have every content of it


#. current
#.. parent
