from dataclasses import dataclass, field, asdict
from typing import Optional, Set, Dict, Any

from src.core.interfaces import AbstractModel

@dataclass
class ExpenseCategoryModel(AbstractModel):
    id: int = 0
    _name: str = field(default="", repr=False, init=False)
    _code: str = field(default="", repr=False, init=False)
    _type: str = field(default="", repr=False, init=False)
    _icon: str = field(default="", repr=False, init=False)
    _is_active: bool = field(default="", repr=False, init=False)

    def __init__(self, name: str, code: str, type: str, icon: str = None, is_active: bool = True):
        self._name = name
        self._code = code
        self._type = type
        self._icon = icon
        self._is_active = is_active

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value: str):
        self._code = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value: str):
        self._type = value

    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, value: str):
        self._icon = value

    @property
    def is_active(self):
        return self._is_active

    # @is_active.setter
    # def is_active(self, value: bool):
    #     self._is_active = value
    #
    # @property
    # def id(self):
    #     return self._id
