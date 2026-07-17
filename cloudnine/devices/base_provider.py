from abc import ABC, abstractmethod
from typing import List

from cloudnine.devices.models.device_passport import DevicePassport


class BaseProvider(ABC):
    """Base class for all device providers."""

    @abstractmethod
    def detect(self) -> List[Device]:
        """Return a list of detected devices."""
        pass