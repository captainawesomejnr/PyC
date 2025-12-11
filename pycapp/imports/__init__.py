import pkgutil
import importlib

__all__ = []

# Discover all modules inside this package
for module in pkgutil.iter_modules(__path__):
    name = module.name
    __all__.append(name)
    importlib.import_module(f"{__name__}.{name}")
