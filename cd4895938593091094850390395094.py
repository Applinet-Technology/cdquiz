import os
import json
import uuid

from pathlib import Path

from rich.console import Console


console = Console()


CONFIG_DIR = Path.home() / ".cdquiz"

CONFIG_DIR.mkdir(
    exist_ok=True
)


SESSION_FILE = (
    CONFIG_DIR / "session.json"
)


FINGERPRINT_FILE = (
    CONFIG_DIR / "fingerprint.json"
)


def sf(path):

    try:

        os.chmod(
            path,
            0o600
        )

    except Exception:
        pass


def gcf():

    try:

        
        if FINGERPRINT_FILE.exists():

            with open(

                FINGERPRINT_FILE,

                "r",

                encoding="utf-8"

            ) as f:

                data = json.load(f)

            fingerprint = data.get(
                "fingerprint"
            )

            if fingerprint:

                return fingerprint

        
        fingerprint = (
            f"cdq_{uuid.uuid4().hex}"
        )

        payload = {

            "fingerprint":
                fingerprint
        }

        with open(

            FINGERPRINT_FILE,

            "w",

            encoding="utf-8"

        ) as f:

            json.dump(

                payload,

                f,

                indent=4
            )

        sf(
            FINGERPRINT_FILE
        )

        return fingerprint

    except Exception as e:

        console.log(

            "[red]Fingerprint Error:[/red] "
            f"{e}"
        )

        return (
            f"cdq_{uuid.uuid4().hex}"
        )


def ls():

    try:

        if not SESSION_FILE.exists():

            return {}

        with open(

            SESSION_FILE,

            "r",

            encoding="utf-8"

        ) as f:

            data = json.load(f)

        if not isinstance(data, dict):

            return {}

        return data

    except Exception as e:

        console.log(

            "[yellow]Session Load Warning:[/yellow] "
            f"{e}"
        )

        return {}

def ss(obj):

    try:

        if not isinstance(obj, dict):

            raise ValueError(
                "Session object msft be a dictionary."
            )

        with open(

            SESSION_FILE,

            "w",

            encoding="utf-8"

        ) as f:

            json.dump(

                obj,

                f,

                indent=4
            )

        sf(
            SESSION_FILE
        )

    except Exception as e:

        console.log(

            "[yellow]Warning saving session:[/yellow] "
            f"{e}"
        )


def cs():

    try:

        if SESSION_FILE.exists():

            SESSION_FILE.unlink()

    except Exception as e:

        console.log(

            "[yellow]Warning clearing session:[/yellow] "
            f"{e}"
        )


def us(**kwargs):

    try:

        session = ls()

        session.update(kwargs)

        ss(session)

        return session

    except Exception as e:

        console.log(

            "[yellow]Session Update Warning:[/yellow] "
            f"{e}"
        )

        return {}


def gsv(

    key,

    default=None
):

    session = ls()

    return session.get(
        key,
        default
    )


def rsk(key):

    try:

        session = ls()

        if key in session:

            del session[key]

            ss(session)

    except Exception as e:

        console.log(

            "[yellow]Session Remove Warning:[/yellow] "
            f"{e}"
        )


