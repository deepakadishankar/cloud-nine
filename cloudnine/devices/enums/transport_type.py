from enum import Enum

class TransportType(Enum):

    USB = "usb"

    SD = "sd"

    NVME = "nvme"

    SATA = "sata"

    MTP = "mtp"

    NETWORK = "network"

    UNKNOWN = "unknown"