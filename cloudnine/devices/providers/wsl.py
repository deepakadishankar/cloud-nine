from abc import ABC, abstractmethod
from typing import List

from cloudnine.devices.device import Device


class DeviceProvider(ABC):
    """
    Base class for every device provider.
    """

    @abstractmethod
    def detect(self) -> List[Device]:
        """
        Return all devices discovered by this provider.
        """
        raise NotImplementedError