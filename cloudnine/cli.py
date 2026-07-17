import typer
from cloudnine.ui import welcome, show_devices
from cloudnine.devices.manager import DeviceManager

app = typer.Typer(
    help="☁ Cloud Nine Protocol"
)


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    """
    Launch Cloud Nine.
    """
    if ctx.invoked_subcommand is None:
        welcome()

        manager = DeviceManager()
        devices = manager.detect()

        show_devices(devices)


@app.command()
def devices():
    print("Listing devices...")


@app.command()
def doctor():
    print("Checking device health...")


@app.command()
def sync():
    print("Starting sync...")


if __name__ == "__main__":
    app()