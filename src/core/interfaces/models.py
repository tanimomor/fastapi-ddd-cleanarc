from dataclasses import dataclass, asdict
from abc import ABC
from typing import Optional, Any, Dict, Set


@dataclass
class AbstractModel(ABC):
    """
    Base model, from which any domain model should be inherited.
    """

    async def to_dict(
            self,
            exclude: Optional[Set[str]] = None,
            include: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:

        data: Dict[str, Any] = asdict(self)

        data = {key.lstrip('_'): value for key, value in data.items()}

        if exclude:
            for key in exclude:
                try:
                    del data[key]
                except KeyError:
                    pass

        if include:
            data.update(include)

        return data
