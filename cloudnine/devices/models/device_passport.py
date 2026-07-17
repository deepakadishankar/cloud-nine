from dataclasses import dataclass
from datetime import datetime


@dataclass
class DevicePassport:
    """
    Cloud Nine's persistent identity for a storage device.
    """

    c9_id: str

    fingerprint: str

    nickname: str | None

    first_seen: datetime

    last_seen: datetime

    import_count: int = 0

    favorite: bool = False