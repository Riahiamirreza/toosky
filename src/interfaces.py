import abc


class BaseDBWrapper(abc.ABC):
    def fetch(id_): ...
    def delete(id_): ...
    def insert(*args, **kwargs): ...
    def filter(*args, **kwargs): ...
    def update(*args, **kwargs): ...
