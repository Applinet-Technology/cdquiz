import time
import traceback
import requests
from requests import RequestException
from rich.console import Console
from rich.panel import Panel

from .config import DEFAULT_RETRIES

console = Console()


class NetworkHelper:
    def __init__(
        self,
        console: Console = console,
        retries: int = DEFAULT_RETRIES,
    ):
        self.console = console
        self.retries = retries

    def request(self, func, spinner_text=None):
        last_exc = None

        for attempt in range(max(1, self.retries)):
            try:
                if spinner_text:
                    with self.console.status(
                        f"[cyan]{spinner_text}[/cyan]",
                        spinner="dots",
                    ):
                        r = func()
                else:
                    r = func()

                return r

            except RequestException as exc:
                last_exc = exc

                self.console.print(
                    f"[yellow]Network error "
                    f"(attempt {attempt + 1}/{self.retries})[/yellow]"
                )

                time.sleep(0.6 + attempt * 0.5)

        if last_exc:
            tb = traceback.format_exception_only(
                type(last_exc),
                last_exc,
            )

            error_message = "".join(tb).strip()

            self.console.print()
            self.console.print(
                Panel(
                    f"[bold red]{error_message}[/bold red]",
                    title="[red]Connection Failed[/red]",
                    border_style="red",
                    padding=(1, 2),
                )
            )
            self.console.print()

            raise SystemExit(1)

        raise RuntimeError("NetworkHelper.request failed without exception")