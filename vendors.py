

import sys, os, json, time, uuid
from typing import Optional
import requests
from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich.table import Table
from rich.text import Text
from rich.align import Align
from rich.progress import BarColumn, Progress
from rich.text import Text

import threading
import time
from rich.table import Table
from rich.panel import Panel
from rich.live import Live


import time
import webbrowser

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.progress import Progress
from rich.spinner import Spinner

from .utils import pretty_time, format_duration




console = Console()
display=console.print
go_ahead=Confirm.ask
framit=Panel.fit
Frame =Panel
in_put=Prompt.ask
centralize= Align.center
Layout= Align
Write = Text
timing=time.sleep
create_table=Table.grid
CDT=Table
CDPT=Progress

cdb =webbrowser
cdp = pretty_time