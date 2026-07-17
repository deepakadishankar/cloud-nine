import platform

from cloudnine.devices.providers.linux.detector import LinuxProvider


class DeviceManager:

    def __init__(self):

        self.provider = self._provider()

    def _provider(self):

        system = platform.system()

        if system == "Linux":

            return LinuxProvider()

        raise RuntimeError(f"{system} not supported yet")

    def detect(self):

        return self.provider.detect()