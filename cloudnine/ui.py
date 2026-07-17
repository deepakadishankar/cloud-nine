from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.table import Table

console = Console()


def welcome():

    title = """
██████╗  ██╗      ██████╗  ██╗   ██╗ ██████╗ 9
██╔════╝ ██║     ██╔═══██╗ ██║   ██║ ██╔══██╗
██║      ██║     ██║   ██║ ██║   ██║ ██║  ██║
██║      ██║     ██║   ██║ ██║   ██║ ██║  ██║
╚██████╗ ███████╗╚██████╔╝ ╚██████╔╝ ██████╔╝
 ╚═════╝ ╚══════╝ ╚═════╝   ╚═════╝  ╚═════╝
"""

    panel = Panel(
        Align.center(title),
        title="☁  Cloud Nine Protocol",
        subtitle="Intelligent Media Transfer",
        border_style="cyan"
    )

    console.print(panel)

def show_devices(devices):

    table = Table(title="Connected Storage Devices")

    table.add_column("Name")
    table.add_column("Filesystem")
    table.add_column("Capacity")
    table.add_column("Free")
    table.add_column("Removable")

    for device in devices:

        table.add_row(

            device.name,

            device.filesystem,

            f"{device.total_gb()} GB",

            f"{device.free_gb()} GB",

            "✅" if device.removable else "❌"

        )

    console.print(table)