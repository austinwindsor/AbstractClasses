import sys
from importlib import import_module
from collections import OrderedDict

"""
Loads in modules with a run submodule with a Run class that inherits from
the abstract_classes.run.AbstractRun class
"""
module_name = sys.argv[1]
module = import_module(module_name+".run")

"""
Refers to the Run class's run() method to find which parameters are used
Creates an a argparse.Namespace object from a argparse.ArgumentParser
Must include a positional argument 'module_name' to deal with the first argument
that's used in the block above

'module_name' is deleted after being used, and only leaves the module_name.run.Run.run()
method's key word arguments in the dictionary
"""
run_obj = module.Run()
args = run_obj.get_argparser(run_method='run')
kwargs = OrderedDict(args._get_kwargs())
del kwargs['module_name']
run_obj.run(**kwargs)
