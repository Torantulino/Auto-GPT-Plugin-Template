# src/auto_gpt_plugin_template/abstract_singleton.py

class SingletonMeta(type):
    """A metaclass for implementing the Singleton pattern."""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class AbstractSingleton(metaclass=SingletonMeta):
    """Abstract base class for Singleton pattern."""

    def __init__(self):
        if not hasattr(self, '_initialized'):
            self._initialized = True
            self.initialize()

    def initialize(self):
        """Initialize the singleton instance.
        
        This method can be overridden in subclasses to perform custom initialization.
        """
        pass

    @classmethod
    def get_instance(cls):
        """Retrieve the singleton instance.
        
        This method provides access to the singleton instance from outside the class.
        """
        return cls()
