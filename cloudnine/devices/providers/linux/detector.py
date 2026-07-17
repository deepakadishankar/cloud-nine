import psutil

from pathlib import Path

from cloudnine.devices.base_provider import BaseProvider
from cloudnine.devices.models.storage_device import StorageDevice


class LinuxProvider(BaseProvider):

    def detect(self):

        devices = []

        for partition in psutil.disk_partitions():

            try:

                usage = psutil.disk_usage(partition.mountpoint)

                devices.append(
                    StorageDevice(
                        name=partition.device,
                        mount_point=Path(partition.mountpoint),
                        filesystem=partition.fstype,
                        total_bytes=usage.total,
                        used_bytes=usage.used,
                        free_bytes=usage.free,
                        removable=False,
                    )
                )

            except PermissionError:

                pass

        return devices