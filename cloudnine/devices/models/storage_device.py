from dataclasses import dataclass

from cloudnine.devices.enums.transport_type import TransportType
from cloudnine.devices.models.partition import Partition


@dataclass
class StorageDevice:
    id: str
    name: str
    manufacturer: str | None
    model: str | None
    serial_number: str | None
    transport: TransportType
    removable: bool
    capacity: int
    partitions: list[Partition]