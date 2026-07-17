from dataclasses import dataclass

@dataclass
class Partition:
    id: str
    filesystem: str
    mount_point: Path
    label: str | None
    uuid: str | None
    total_space: int
    free_space: int