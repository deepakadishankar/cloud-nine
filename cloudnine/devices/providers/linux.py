import psutil

from pathlib import Path

from cloudnine.devices.provider import DeviceProvider
from cloudnine.devices.models.device import Device


class LinuxProvider(DeviceProvider):

    def detect(self):

        devices = []

        for partition in psutil.disk_partitions():

            try:

                usage = psutil.disk_usage(partition.mountpoint)

                devices.append(
                    Device(
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