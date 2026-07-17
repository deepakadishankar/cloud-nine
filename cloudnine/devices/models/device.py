from dataclasses import dataclass
from pathlib import Path


@dataclass
class Device:
    """Represents a storage device."""

    name: str
    mount_point: Path
    filesystem: str

    total_bytes: int
    used_bytes: int
    free_bytes: int

    removable: bool

    def total_gb(self):
        return round(self.total_bytes / (1024**3), 2)

    def used_gb(self):
        return round(self.used_bytes / (1024**3), 2)

    def free_gb(self):
        return round(self.free_bytes / (1024**3), 2)