from .base import Person as BasePerson
# NOTE: it's preferable to not have imports like this because every import will be imported and clutter the namespace, but our file doesn't have any imports only class definitions
from .inherited import *
from .dependency_injection import Signals
# NOTE: a demonstration of aliasing to avoid overwriting namespaced imports and distinctly identify the DI version from the BasePerson class instance
from .dependency_injection import Person as DependencyInjectionPerson