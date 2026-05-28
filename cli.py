import sys, os, json, time, uuid
from typing import Optional
import requests
from rich import box
import threading
from rich.live import Live
from rich.progress import BarColumn

from rich import box

from .api_client import APIClient
from .utils import format_duration

from .cd4895938593091094850390395094 import ls, ss
from .vendors import (
console,
display,
go_ahead,
framit,
Frame,
in_put,
centralize,
Write,
timing,
create_table,
CDT,
CDPT,
cdb,
cdp,
)

class QuizCLI:
    def __init__(self, z: APIClient):
        self.z = z
        self.d = ls()
        self.start_time = None

    def quiz_d(self, quiz):
        rews =self.z.quiy(quiz)
        if rews.status_code != 200:
            display("[red]Invalid selection[/red]")
        
        quiy_1 =rews.json().get('quiy')
        return quiy_1

    def display_banner(self):

        console.clear()

        try:

            display()

            display(
                centralize(
                    Write(
                        "Starting CODEHOUSE CLOUD",
                        style="bold cyan"
                    )
                )
            )

            display()

            # =====================================================
            # LOAD LOGO
            # =====================================================

            logo_sys = self.z.sys_logo()

            if logo_sys.status_code in (200, 201):

                body = logo_sys.json()

                logo = body.get("logo", "")

                # -------------------------------------------------
                # TYPING EFFECT (CENTERED)
                # -------------------------------------------------

                for line in logo.splitlines():

                    display(
                        centralize(
                            f"[bold cyan]{line}[/bold cyan]"
                        )
                    )

                    timing(0.03)

                display()

            else:

                display(
                    centralize(
                        "[bold cyan]CODEHOUSE CLOUD[/bold cyan]"
                    )
                )

            # =====================================================
            # MAIN PANEL
            # =====================================================

            panel = Frame(

                centralize(

                    Write(
                        "WELCOME TO CDQUIZ: A CODEHOUSE QUIZ SUITE",
                        style="bold bright_white"
                    ),

                    vertical="middle"
                ),

                box=box.HEAVY,

                border_style="bright_cyan",

                padding=(1, 8),

                title=(
                    "[bold bright_white]"
                    "Powered by Applinet Technology (Tel: +234-803-713-7902)"
                    "[/bold bright_white]"
                ),

                subtitle=(
                    "[italic cyan]"
                    "The Ultimate CLI Quiz Arena."
                    "[/italic cyan]"
                ),

                width=80
            )

            display(
                centralize(panel)
            )

            display()

            # =====================================================
            # TERMS / PRIVACY NOTICE
            # =====================================================

            terms_panel = framit(

                "[bold white]"
                "By continuing to use CDQuiz via this Terminal CLI, "
                "you acknowledge and agree to the Terms of Use and "
                "Privacy Policy governing the platform.\n\n"
                "[/bold white]"

                "[cyan]"
                "Press CTRL + Click (Windows/Linux) or CMD + Click (Mac) "
                "on the link below to learn more:\n\n"
                "[/cyan]"

                "[bold bright_blue underline]"
                "https://cli.codehouse.cloud/terms/"
                "[/bold bright_blue underline]",

                title="[bold yellow]NOTICE[/bold yellow]",

                border_style="yellow",

                padding=(1, 3)
            )

            display(
                centralize(terms_panel)
            )

            display()

            # =====================================================
            # CONSENT PANEL
            # =====================================================

            consent_text = Write()

            consent_text.append(
                "Do you agree to the Terms of Use and Privacy Policy?\n\n",
                style="bold white"
            )

            consent_text.append(
                "[1] ",
                style="bold green"
            )

            consent_text.append(
                "Yes\n"
            )

            consent_text.append(
                "[2] ",
                style="bold red"
            )

            consent_text.append(
                "No"
            )

            consent_panel = Frame(

                centralize(consent_text),

                title="[bold cyan]User Agreement[/bold cyan]",

                border_style="bright_cyan",

                padding=(1, 3),

                width=70
            )

            display(
                centralize(consent_panel)
            )

            display()

            # =====================================================
            # USER CONSENT LOOP
            # =====================================================

            while True:

                consent = in_put(

                    "[bold cyan]Select option[/bold cyan]",

                    choices=["1", "2"],

                    default="1"

                ).strip()

                # =================================================
                # ACCEPTED
                # =================================================

                if consent == "1":

                    accepted_panel = Frame(

                        centralize(
                            "[bold green]"
                            "Agreement accepted.\n\n"
                            "Launching CDQuiz..."
                            "[/bold green]"
                        ),

                        border_style="green",

                        padding=(1, 3)
                    )

                    display(
                        centralize(accepted_panel)
                    )

                    timing(1.2)

                    break

                # =================================================
                # DECLINED
                # =================================================

                elif consent == "2":

                    declined_panel = Frame(

                        centralize(
                            "[bold red]"
                            "You declined the agreement.\n\n"
                            "Exiting CDQuiz..."
                            "[/bold red]"
                        ),

                        border_style="red",

                        padding=(1, 3)
                    )

                    display(
                        centralize(declined_panel)
                    )

                    timing(1)

                    sys.exit(0)

            # =====================================================
            # FOOTER
            # =====================================================

            footer = framit(

                "[bold green]"
                "Learn • Compete • Rise"
                "[/bold green]",

                border_style="green"
            )

            display(
                centralize(footer)
            )

            display("\n")

        # =========================================================
        # HANDLE CTRL + C CLEANLY
        # =========================================================

        except KeyboardInterrupt:

            console.print()

            interrupt_panel = Frame(

                centralize(
                    "[bold red]"
                    "CDQuiz closed by user."
                    "[/bold red]"
                ),

                border_style="red",

                padding=(1, 3)
            )

            display(
                centralize(interrupt_panel)
            )

            timing(1)

            # =========================================
            # FORCE CLOSE TERMINAL WINDOW
            # =========================================

            try:

                # Windows CMD / PowerShell
                os.system("taskkill /F /PID %PID% >nul 2>&1")

            except Exception:

                pass

            sys.exit(0)

    # ------------------------
    # Registration
    # ------------------------
    def fi(self):
        display(
            framit(
                "[bold yellow]Create Account[/bold yellow] "
                "[italic cyan]CTRL + C (Windows), Command + C (Mac) to Exit[/italic cyan]"
            )
        )        
        q = in_put("Full name")

        # =========================================================
        # EMAIL INPUT LOOP
        # =========================================================
        while True:

            s = in_put(
                "Email"
            ).strip().lower()

            # =====================================================
            # EMPTY EMAIL
            # =====================================================
            if not s:

                display(
                    "[red]Email field cannot be empty.[/red]"
                )

                continue

            # =====================================================
            # BASIC FORMAT CHECK
            # =====================================================
            if (
                "@" not in s
                or
                "." not in s.split("@")[-1]
            ):

                display(

                    "[red]"
                    "Invalid email format. "
                    "Please enter a valid email address."
                    "[/red]"
                )

                continue

            # =====================================================
            # EXTRA SECURITY CHECKS
            # =====================================================
            if " " in s:

                display(
                    "[red]Email cannot contain spaces.[/red]"
                )

                continue

            if ".." in s:

                display(
                    "[red]Invalid email structure.[/red]"
                )

                continue

            # =====================================================
            # SERVER VALIDATION
            # =====================================================
            zz = self.z.z(s)

            if zz.status_code in (400, 404):

                try:

                    az = zz.json()

                    detail = az.get(
                        "detail",
                        "Invalid email"
                    )

                except Exception:

                    detail = "Unable to validate email"

                display(
                    framit(
                        f"[red]{detail}[/red]"
                    )
                )

                continue

            # =====================================================
            # SUCCESS
            # =====================================================
            break

            



        while True:
            c = in_put("Password", password=True)

            if len(c) < 6:
                display("[red]Password must be at least 6 characters[/red]")
                # return
            else:
                break

        while True:
            c1 = in_put("Confirm password", password=True)
            if c != c1:
                display("[red]Passwords do not match[/red]")
                return
            else:
                break
             # use server to validate password to here 

        while True:
            k = in_put("Phone (e.g. +234...)", default="")
            if not k:

                display(
                    "[red]Phone field cannot be empty.[/red]"
                )
            k1 = self.z.k(k)
            f=k
            if k1.status_code in (400, 404):
                k19 = k1.json()
                k190 = k19.get("detail")
                display(framit(f"[red] {k190} [/red]"))
            
            else:
                break

        t = in_put("Country code (e.g. nga, usa)", default="nga")

        r = self.z.h(q, s, c, f, t)
        x=s
        if r.status_code in (200, 201):
            display(framit("[green]Registration OK — check your email for confirmation token[/green]"))
            z = in_put("Enter confirmation token (from noreply@codehouse.cloud)")
            vr = self.z.y(x, z)            
            if vr.status_code in (200, 201):
                body = vr.json()
                lop = body.get("sti")

                display(
                    framit(
                        f"[bold green]Congratulations! Your email has been successfully verified.[/bold green]\n\n"
                        f"[white]Your STI:[/white] [bold cyan]{lop}[/bold cyan]\n\n"
                        f"[green]You can now continue using CDQuiz seamlessly.[/green]"
                    )
                )

                # Save minimal session
                self.d.update({"email": s, "sti": lop})
                ss(self.d)

                display(
                    framit(
                        "[bold cyan]Redirecting to login...[/bold cyan]"
                    )
                )

                # Automatically go to login
                self.i(prefill_quiz=lop)

            else:
                display(framit(f"[red]Verify failed: {vr.status_code}[/red]"))
            
            

        else:
            try:
                msg = r.json()
            except Exception:
                msg = r.text
            display(framit(f"[red]Registration failed: {msg}[/red]"))

    # ------------------------
    # Login
    # ------------------------
    def i(self, prefill_quiz: Optional[str] = None):
        display(
            framit(
                "[bold yellow]Login [/bold yellow] "
                "[italic cyan]CTRL + C (Windows), Command + C (Mac) to Exit[/italic cyan]"
            )
        )
        i = prefill_quiz or in_put("Enter STI")
        l = in_put("Password", password=True)

        try:
            r = self.z.l(i,l)
        except Exception as e:
            display(framit(f"[red]Network/login error: {e}[/red]"))
            return

        if r.status_code == 200:
            rew = r.json()
            ui = rew.get("token")
            ssk = rew.get("session_key")
            quiz = rew.get("sti") or i
            idw=quiz

            self.z.ui = ui
            self.z.ssk = ssk
            self.z.wo = quiz
            self.d.update({"sti": idw, "token": ui, 'session_key':ssk})
            ss(self.d)

            display(framit("[green]Login successful![/green]"))
            self.o(quiz)
        else:
            try:
                raw = r.json()
                display(framit(f"[red]Login failed: {raw.get('detail') or raw}[/red]"))
            except Exception:
                display(framit(f"[red]Login failed: status {r.status_code}[/red]"))


    def db(self):

        display(
            framit(
                "[bold yellow]Password / STI Recovery[/bold yellow]\n\n"
                "[white]Recover your account using:[/white]\n"
                "• Your STI\n"
                "• Registered email\n"
                "• Registered phone number"
            )
        )

        eu = create_table(expand=True)
        eu.add_column(justify="center")

        eu.add_row(
            "[bold cyan]1[/bold cyan] Recover with STI    "
            "[bold cyan]2[/bold cyan] Recover STI"
        )

        display(
            framit(
                eu,
                title="[bold cyan]Recovery Options[/bold cyan]"
            )
        )

        g = in_put(
            "Select",
            choices=["1", "2"],
            default="1"
        )

        if g == "1":

            w = in_put("Enter your STI", default="")

            if not w:
                display(
                    "[yellow]You must provide STI to request recovery.[/yellow]"
                )
                return

            r = self.z.w(w)

            if r.status_code in (200, 201):

                display(
                    framit(
                        "[green]Recovery token sent to your email.[/green]"
                    )
                )

                v = in_put(
                    "Enter recovery token (from your noreply@codehouse.cloud)"
                )

                vr = self.z.ky(v, w)
                db=w
                if vr.status_code in (200, 201):

                    display(
                        framit(
                            "[green]Recovery token verified. "
                            "Continue to reset password.[/green]"
                        )
                    )

                    ky = in_put(
                        "New password",
                        password=True
                    )

                    up = in_put(
                        "Confirm password",
                        password=True
                    )

                    if ky != up:
                        display(
                            "[red]Passwords do not match[/red]"
                        )
                        return

                    rr = self.z.db(
                        db,
                        v,
                        ky
                    )

                    if rr.status_code in (200, 201):

                        display(
                            framit(
                                "[bold green]Password reset successful![/bold green]\n\n"
                                "[green]Redirecting to login...[/green]"
                            )
                        )

                        self.i(prefill_quiz=db)

                    else:
                        display(
                            f"[red]Reset failed: {rr.text}[/red]"
                        )

                else:
                    display(
                        f"[red]Verification failed: {vr.status_code}[/red]"
                    )

            else:
                display(
                    f"[red]Recovery request failed: {r.status_code}[/red]"
                )

        elif g == "2":
            display(
            framit(
                "[bold yellow]Account / STI Recovery[/bold yellow]\n\n"
                "[white]Recover your STI using your registered email or phone number.[/white]"
            )
        )

            b = in_put(
                "Enter registered email or phone number",
                default=""
            ).strip()



            if not b:
                display(
                    "[red]Email or phone number required.[/red]"
                )
                return

            r = self.z.b(b)


            if r.status_code in (200, 201):

                try:
                    body = r.json()

                    masked_email = body.get(
                        "email",
                        "developers@******il.com"
                    )

                except Exception:
                    masked_email = "developers@******il.com"
                br=b
                display(
                    framit(
                        f"[green]A verification code has been sent to "
                        f"[bold cyan]{masked_email}[/bold cyan][/green]\n\n"
                        "[yellow]If you have issues accessing this email, "
                        "contact CodeHouse Cloud for account recovery assistance.[/yellow]"
                    )
                )

                iz = in_put(
                    "Enter verification token (from email)"
                )

                vr = self.z.ti(br,iz)
                if vr.status_code in (200, 201):

                    try:
                        body = vr.json()

                        quid = body.get("sti")
                        fullname = body.get("fullname", "User")

                    except Exception:
                        quid = None
                        fullname = "User"

                    display(
                        framit(
                            f"[bold green] Account recovery successful![/bold green]\n\n"
                            f"[white]Welcome back:[/white] [bold]{fullname}[/bold]\n"
                            f"[white]Your STI:[/white] [bold cyan]{quid}[/bold cyan]"
                        )
                    )

                    if go_ahead(
                        "Do you want to login now?"
                    ):
                        self.i(prefill_quiz=quid)

                
                else:

                    try:
                        body = vr.json()

                        error_msg = (
                            body.get("detail")
                            or body.get("message")
                            # or vr.text
                        )

                    except Exception:
                        error_msg = vr.status_code

                    display(
                        framit(
                            f"[red] {error_msg}[/red]"
                        )
                    )

            
            else:

                try:
                    body = r.json()

                    error_msg = (
                        body.get("detail")
                        or body.get("message")
                        # or r.text
                    )

                except Exception:
                    error_msg = r.status_code

                display(
                    framit(
                        f"[red] {error_msg}[/red]"
                    )
                )




    def o(self, quiz):

        quiy_1 = self.quiz_d(quiz)

        while True:

            # =================================================
            # QUIZ ACCESS STATUS
            # =================================================
            quiz_access_enabled = True

            quiz_access_message = None

            access_response = self.z.quiz_access_status(quiz)

            if access_response.status_code == 403:

                try:

                    access_data = access_response.json()

                    quiz_access_enabled = False

                    quiz_access_message = access_data.get(
                        "message",
                        "Quiz access restricted."
                    )

                except Exception:

                    quiz_access_enabled = False

                    quiz_access_message = (
                        "Quiz access restricted."
                    )

            elif access_response.status_code == 200:

                try:

                    access_data = access_response.json()

                    quiz_access_enabled = access_data.get(
                        "can_continue_quiz",
                        True
                    )

                    if not quiz_access_enabled:

                        quiz_access_message = access_data.get(
                            "message"
                        )

                except Exception:

                    quiz_access_enabled = True

            # =================================================
            # DASHBOARD
            # =================================================
            display()

            menu = CDT(
                title="CDQuiz Dashboard",
                header_style="bold cyan",
                border_style="cyan"
            )

            menu.add_column(
                "#",
                justify="center",
                style="bold white"
            )

            menu.add_column(
                "Menu",
                style="bold green"
            )

            # =================================================
            # QUIZ MENU STATUS
            # =================================================
            if quiz_access_enabled:

                start_resume_text = (
                    "Start / Resume Quiz"
                )

            else:

                start_resume_text = (
                    "[dim]Start / Resume Quiz "
                    "(Disabled)[/dim]"
                )

            # =================================================
            # MENU ITEMS
            # =================================================
            menu.add_row("1", start_resume_text)

            menu.add_row("2", "View Leaderboard")

            menu.add_row("3", "Wallet")

            menu.add_row("4", "Deposit QuizCoin")

            menu.add_row("5", "Withdraw")

            menu.add_row("6", "Announcements")

            menu.add_row("7", "Logout")

            display(menu)

            # =================================================
            # ACCESS WARNING
            # =================================================
            if not quiz_access_enabled and quiz_access_message:

                display()

                display(

                    framit(

                        f"[bold red]{quiz_access_message}[/bold red]\n\n"
                        f"[bold yellow]Deposit QuizCoin to continue quizzes.[/bold yellow]"
                    )
                )

                display()

            # =================================================
            # USER INPUT
            # =================================================
            choice = in_put(
                "[bold green]Select option[/bold green]",
                default=f"{quiy_1}"
            ).strip()

            # =================================================
            # START / RESUME QUIZ
            # =================================================
            if choice == "1":

                # =============================================
                # BLOCK QUIZ ACCESS
                # =============================================
                if not quiz_access_enabled:

                    display(

                        framit(

                            "[bold red]"
                            "Quiz access currently disabled.\n\n"
                            "Please buy QuizCoin to continue."
                            "[/bold red]"
                        )
                    )

                    continue

                # =============================================
                # CHECK PENDING QUIZZES
                # =============================================
                qz = self.z.quiz(quiz)

                if qz.status_code == 200:

                    data = qz.json()

                    if data.get("has_pending"):

                        pending_list = data.get(
                            "pending",
                            []
                        )

                        if pending_list:

                            table = CDT(
                                title="Pending Quizzes",
                                header_style="bold yellow",
                                border_style="yellow"
                            )

                            table.add_column(
                                "#",
                                justify="center"
                            )

                            table.add_column(
                                "Category",
                                style="magenta"
                            )

                            table.add_column(
                                "Subcategory",
                                style="green"
                            )

                            table.add_column(
                                "Topic",
                                style="cyan"
                            )

                            table.add_column(
                                "Progress",
                                justify="center"
                            )

                            table.add_column(
                                "Next",
                                justify="center"
                            )

                            for idx, item in enumerate(
                                pending_list,
                                start=1
                            ):

                                course = item.get(
                                    "course",
                                    {}
                                )

                                table.add_row(

                                    str(idx),

                                    str(
                                        course.get(
                                            "category",
                                            "-"
                                        )
                                    ),

                                    str(
                                        course.get(
                                            "subcategory",
                                            "-"
                                        )
                                    ),

                                    course.get(
                                        "title",
                                        "Unknown"
                                    ),

                                    item.get(
                                        "progress",
                                        "--"
                                    ),

                                    str(
                                        item.get(
                                            "last_q",
                                            1
                                        )
                                    )
                                )

                            display()
                            display(table)
                            display()

                            if go_ahead(
                                "Resume a pending quiz?"
                            ):

                                pending_choice = in_put(
                                    "Select pending quiz number",
                                    default="1"
                                )

                                try:

                                    selected_pending = pending_list[
                                        int(pending_choice) - 1
                                    ]

                                except Exception:

                                    display(
                                        framit(
                                            "[red]Invalid selection[/red]"
                                        )
                                    )

                                    continue

                                selected_course = (
                                    selected_pending.get(
                                        "course",
                                        {}
                                    )
                                )

                                self.d["selected_course"] = {

                                    "id":
                                        selected_course.get("id"),

                                    "title":
                                        selected_course.get("title"),

                                    "total_questions":
                                        selected_course.get(
                                            "total_questions",
                                            0
                                        ),

                                    "last_q":
                                        selected_pending.get(
                                            "last_q",
                                            1
                                        ),

                                    "has_pending":
                                        True
                                }

                                ss(self.d)

                                self.ghjk(
                                    selected_course.get("id"),
                                    quiz
                                )

                                display(
                                    framit(
                                        "[bold cyan]Resuming quiz...[/bold cyan]"
                                    )
                                )

                                self.asdf(quiz)

                                continue

                # =================================================
                # FETCH CATEGORIES
                # =================================================
                cat_response = self.z.categories(quiz)

                if cat_response.status_code != 200:

                    display(
                        framit(
                            "[red]Failed to fetch categories[/red]"
                        )
                    )

                    continue

                categories = cat_response.json().get(
                    "categories",
                    []
                )

                if not categories:

                    display(
                        framit(
                            "[red]No categories available[/red]"
                        )
                    )

                    continue

                category_table = CDT(
                    title="Quiz Categories",
                    header_style="bold magenta",
                    border_style="magenta"
                )

                category_table.add_column(
                    "#",
                    justify="center"
                )

                category_table.add_column(
                    "Category",
                    style="bold cyan"
                )

                for idx, category in enumerate(
                    categories,
                    start=1
                ):

                    category_table.add_row(

                        str(idx),

                        category.get(
                            "name",
                            "Unknown"
                        )
                    )

                display()
                display(category_table)

                category_choice = in_put(
                    "Select category number "
                    "(or 'b' to go back)",
                    default="1"
                )

                if category_choice.lower() in (
                    "b",
                    "back"
                ):

                    continue

                try:

                    selected_category = categories[
                        int(category_choice) - 1
                    ]

                except Exception:

                    display(
                        framit(
                            "[red]Invalid category selection[/red]"
                        )
                    )

                    continue

                category_id = selected_category.get("id")

                # =================================================
                # FETCH SUBCATEGORIES
                # =================================================
                sub_response = self.z.subcategories(
                    category_id,
                    quiz
                )

                if sub_response.status_code != 200:

                    display(
                        framit(
                            "[red]Failed to fetch subcategories[/red]"
                        )
                    )

                    continue

                subcategories = sub_response.json().get(
                    "subcategories",
                    []
                )

                if not subcategories:

                    display(
                        framit(
                            "[red]No subcategories found[/red]"
                        )
                    )

                    continue

                sub_table = CDT(
                    title=(
                        f"{selected_category.get('name')} "
                        f"Subcategories"
                    ),
                    header_style="bold green",
                    border_style="green"
                )

                sub_table.add_column(
                    "#",
                    justify="center"
                )

                sub_table.add_column(
                    "Subcategory",
                    style="bold cyan"
                )

                for idx, sub in enumerate(
                    subcategories,
                    start=1
                ):

                    sub_table.add_row(

                        str(idx),

                        sub.get(
                            "name",
                            "Unknown"
                        )
                    )

                display()
                display(sub_table)

                sub_choice = in_put(
                    "Select subcategory number "
                    "(or 'b' to go back)",
                    default="1"
                )

                if sub_choice.lower() in (
                    "b",
                    "back"
                ):

                    continue

                try:

                    selected_subcategory = subcategories[
                        int(sub_choice) - 1
                    ]

                except Exception:

                    display(
                        framit(
                            "[red]Invalid subcategory selection[/red]"
                        )
                    )

                    continue

                subcategory_id = (
                    selected_subcategory.get("id")
                )

                # =================================================
                # FETCH COURSES
                # =================================================
                r = self.z.ans(
                    quiz,
                    subcategory_id
                )

                # =================================================
                # ACCESS DENIED
                # =================================================
                if r.status_code == 403:

                    try:

                        denied_data = r.json()

                        display()

                        display(

                            framit(

                                f"[bold red]"
                                f"{denied_data.get('message')}"
                                f"[/bold red]"
                            )
                        )

                        display()

                    except Exception:

                        display(
                            framit(
                                "[red]Quiz access denied[/red]"
                            )
                        )

                    continue

                # =================================================
                # GENERAL FAILURE
                # =================================================
                if r.status_code != 200:

                    display(
                        framit(
                            f"[red]Failed to fetch courses: "
                            f"{r.status_code}[/red]"
                        )
                    )

                    continue

                response_data = r.json()

                hodjn3in008con09ico19048kf = response_data.get(
                    "hodjn3in008con09ico19048kfnoWID9300I030fjjsj193sjfo9402jnabdsoii",
                    []
                )

                if not hodjn3in008con09ico19048kf:

                    display(
                        framit(
                            "[bold red]No courses available.[/bold red]"
                        )
                    )

                    continue

                # =================================================
                # COURSE TABLE
                # =================================================
                table = CDT(
                    title=(
                        f"{selected_subcategory.get('name')} "
                        f"Courses"
                    ),
                    header_style="bold cyan",
                    border_style="cyan"
                )

                table.add_column(
                    "#",
                    justify="center",
                    style="bold white"
                )

                table.add_column(
                    "Status",
                    justify="center"
                )

                table.add_column(
                    "Course ID",
                    justify="center"
                )

                table.add_column(
                    "Title",
                    style="bold"
                )

                table.add_column(
                    "Progress",
                    justify="center"
                )

                table.add_column(
                    "Questions",
                    justify="center"
                )

                table.add_column(
                    "Score",
                    justify="center"
                )

                # =================================================
                # BUILD ROWS
                # =================================================
                for idx, c in enumerate(
                    hodjn3in008con09ico19048kf,
                    start=1
                ):

                    if c.get("has_pending"):

                        status = (
                            "[bold yellow]Pending[/bold yellow]"
                        )

                        row_style = "yellow"

                    elif c.get("not_attempted"):

                        status = (
                            "[bold green]New[/bold green]"
                        )

                        row_style = "green"

                    elif c.get("completed"):

                        status = (
                            "[bold cyan]Completed[/bold cyan]"
                        )

                        row_style = "cyan"

                    else:

                        status = (
                            "[white]Unknown[/white]"
                        )

                        row_style = "white"

                    table.add_row(

                        str(idx),

                        status,

                        str(c.get("id")),

                        c.get(
                            "title",
                            "Untitled"
                        ),

                        c.get(
                            "progress",
                            "--"
                        ),

                        str(
                            c.get(
                                "total_questions",
                                0
                            )
                        ),

                        c.get(
                            "score_text",
                            "--"
                        ),

                        style=row_style
                    )

                display()
                display(table)

                display(
                    "\n"
                    "[bold yellow]Pending[/bold yellow] = Resume unfinished quiz\n"
                    "[bold green]New[/bold green] = New course\n"
                    "[bold cyan]Completed[/bold cyan] = Completed course\n"
                )

                # =================================================
                # COURSE SELECTION
                # =================================================
                selected_choice = in_put(
                    "Choose course number "
                    "(or 'b' to go back dashboard)",
                    default="1"
                )

                if selected_choice.lower() in (
                    "b",
                    "back"
                ):

                    continue

                try:

                    selected = hodjn3in008con09ico19048kf[
                        int(selected_choice) - 1
                    ]

                except Exception:

                    display(
                        framit(
                            "[red]Invalid selection[/red]"
                        )
                    )

                    continue

                # =================================================
                # SAVE SELECTED COURSE
                # =================================================
                self.d["selected_course"] = {

                    "id":
                        selected.get("id"),

                    "title":
                        selected.get("title"),

                    "total_questions":
                        selected.get(
                            "total_questions",
                            0
                        ),

                    "last_q":
                        selected.get(
                            "last_q",
                            quiy_1
                        ),

                    "has_pending":
                        selected.get(
                            "has_pending",
                            False
                        )
                }

                ss(self.d)

                # =================================================
                # ACTIVATE COURSE
                # =================================================
                self.ghjk(
                    selected.get("id"),
                    quiz
                )

                # =================================================
                # START QUIZ
                # =================================================
                display()

                display(
                    framit(
                        "[bold green]Starting quiz...[/bold green]"
                    )
                )

                self.asdf(quiz)

            # =================================================
            # LEADERBOARD
            # =================================================
            elif choice == "2":

                self.bGBwa(quiz)

            # =================================================
            # WALLET
            # =================================================
            elif choice == "3":

                self.quFGa(quiz)

            # =================================================
            # DEPOSIT
            # =================================================
            elif choice == "4":

                self.quFGa3(quiz)

            # =================================================
            # WITHDRAW
            # =================================================
            elif choice == "5":

                self.kjb(quiz)

            # =================================================
            # ANNOUNCEMENTS
            # =================================================
            elif choice == "6":

                self.will(quiz)

            # =================================================
            # LOGOUT
            # =================================================
            elif choice == "7":

                display(
                    framit(
                        "[bold red]Logging out...[/bold red]"
                    )
                )

                self.d.clear()

                ss(self.d)

                return

            # =================================================
            # INVALID OPTION
            # =================================================
            else:

                display(
                    framit(
                        "[red]Invalid menu option[/red]"
                    )
                )
            
            # elif choice == "2":

            #     self.bGBwa(quiz)
    
            
            # elif choice == "3":

            #     self.quFGa(quiz)

            
            # elif choice == "4":

            #     self.quFGa3(quiz)
            
            # elif choice == "5":

            #     self.kjb(quiz)

            
            # elif choice == "6":

            #     self.will(quiz)

            
            # elif choice == "7":

            #     display(
            #         framit(
            #             "[bold red]Logging out...[/bold red]"
            #         )
            #     )

            #     self.d.clear()

            #     ss(self.d)

            #     return

            
            # else:

            #     display(
            #         framit(
            #             "[red]Invalid menu option[/red]"
            #         )
            #     )


    
    def bGBwa(self, sti):

        while True:

            display()

            display(
                framit(
                    "[bold magenta]"
                    "GLOBAL QUIZ LEADERBOARD"
                    "[/bold magenta]\n\n"
                    "[white]"
                    "Top performers across all quizzes"
                    "[/white]",
                    border_style="magenta"
                )
            )

            try:

                
                res = self.z.vtu(sti)

                if res.status_code != 200:

                    display(
                        framit(
                            "[bold red]"
                            "Unable to fetch leaderboard"
                            "[/bold red]"
                        )
                    )

                    return

                response = res.json()

                hodjn3in008con09ico19048kfnoWID9300I030fjjsj193sjfo9402jnabdsoii = response.get(
                    "hodjn3in008con09ico19048kfnoWID9300I030fjjsj193sjfo9402jnabdsoiii2oi0e2",
                    []
                )

                if not hodjn3in008con09ico19048kfnoWID9300I030fjjsj193sjfo9402jnabdsoii:

                    display(
                        framit(
                            "[yellow]"
                            "No leaderboard data yet."
                            "[/yellow]"
                        )
                    )

                    return

                
                table = CDT(

                    title="Top Quiz Champions",

                    header_style="bold cyan",

                    border_style="cyan",

                    show_lines=True
                )

                table.add_column(
                    "No.",
                    justify="center",
                    style="bold yellow"
                )

                table.add_column(
                    "Rank",
                    justify="center",
                    style="bold yellow"
                )

                table.add_column(
                    "Username",
                    style="bold white"
                )

                table.add_column(
                    "Average",
                    justify="center"
                )

                table.add_column(
                    "Accuracy",
                    justify="center"
                )

                table.add_column(
                    "Attempts",
                    justify="center"
                )

                table.add_column(
                    "Best Course",
                    style="cyan"
                )

                table.add_column(
                    "Top Score",
                    justify="center"
                )

                table.add_column(
                    "Avg Speed",
                    justify="center"
                )

                
                for idx, user in enumerate(
                    hodjn3in008con09ico19048kfnoWID9300I030fjjsj193sjfo9402jnabdsoii,
                    start=1
                ):

                    rank = user.get("rank")

                    username = user.get(
                        "username",
                        "Unknown"
                    )

                    avg_score = user.get(
                        "avg_score",
                        0
                    )

                    accuracy = user.get(
                        "accuracy",
                        0
                    )

                    attempts = user.get(
                        "total_attempts",
                        0
                    )

                    avg_speed = user.get(
                        "avg_speed_display",
                        "0s"
                    )

                    speed_remark = user.get(
                        "avg_speed_remark",
                        ""
                    )
                    timing_color = user.get(
                        "timing_color",
                        ""
                    )

                    best_course = (
                        user.get(
                            "best_course",
                            {}
                        ) or {}
                    )

                    course_title = best_course.get(
                        "title",
                        "N/A"
                    )

                    top_score = best_course.get(
                        "score",
                        0
                    )

                    
                    if rank == 1:

                        rank_text = "1st"

                    elif rank == 2:

                        rank_text = "2nd"

                    elif rank == 3:

                        rank_text = "3rd"

                    else:

                        rank_text = str(rank)

                    
                    if avg_score >= 90:

                        avg_text = (
                            f"[bold green]"
                            f"{avg_score}%"
                            f"[/bold green]"
                        )

                    elif avg_score >= 70:

                        avg_text = (
                            f"[yellow]"
                            f"{avg_score}%"
                            f"[/yellow]"
                        )

                    else:

                        avg_text = (
                            f"[red]"
                            f"{avg_score}%"
                            f"[/red]"
                        )

                    
                    if accuracy >= 85:

                        acc_text = (
                            f"[green]"
                            f"{accuracy}%"
                            f"[/green]"
                        )

                    elif accuracy >= 60:

                        acc_text = (
                            f"[yellow]"
                            f"{accuracy}%"
                            f"[/yellow]"
                        )

                    else:

                        acc_text = (
                            f"[red]"
                            f"{accuracy}%"
                            f"[/red]"
                        )

                    
                    speed_text = (
                        f"{avg_speed}\n"
                        
                        f"[{timing_color}]{speed_remark}[/{timing_color}]"
                    )

                    
                    
                    table.add_row(

                        str(idx),

                        rank_text,

                        username,

                        avg_text,

                        acc_text,

                        str(attempts),

                        course_title,

                        f"{top_score}%",

                        speed_text,
                    )

                display()
                display(table)

                
                display()

                display(
                    framit(
                        "[bold green]"
                        "Leaderboard rankings are calculated "
                        "from average scores across all "
                        "completed quiz courses."
                        "[/bold green]\n\n"

                        "[bold cyan]"
                        "Enter a scorer number to view details"
                        "[/bold cyan]\n"

                        "[yellow]R[/yellow] = Refresh leaderboard\n"
                        "[yellow]B[/yellow] = Back to menu",
                        border_style="green"
                    )
                )

                
                choice = in_put(
                    "[bold yellow]Select option[/bold yellow]"
                ).strip().lower()

                
                if choice == "b":

                    return

                
                elif choice == "r":

                    console.clear()

                    continue

                
                try:

                    selected_user = hodjn3in008con09ico19048kfnoWID9300I030fjjsj193sjfo9402jnabdsoii[
                        int(choice) - 1
                    ]

                    self.view_top_scorer_detail(
                        selected_user
                    )

                except Exception:

                    display(
                        framit(
                            "[bold red]"
                            "Invalid scorer selection."
                            "[/bold red]"
                        )
                    )

            except Exception as e:

                display(
                    framit(
                        f"[bold red]"
                        f"Leaderboard error:\n{e}"
                        f"[/bold red]"
                    )
                )

                return


    
    def view_top_scorer_detail(self, user: dict):

        display()

        username = user.get("username", "Unknown")
        avg_score = float(user.get("avg_score", 0))
        accuracy = float(user.get("accuracy", 0))
        attempts = user.get("total_attempts", 0)
        highest_score = float(user.get("highest_score", 0))

        avg_speed = user.get("avg_speed_display", "0s")
        timing_remark = user.get("timing_remark", "Unknown")
        timing_color = user.get("timing_color", "white")

        best_course = user.get("best_course") or {}
        courses = user.get("courses", [])

        current_user = self.d.get("username", "")

        
        is_me = current_user and current_user.lower() == username.lower()

        display(
            framit(
                f"[bold cyan]SCORER PROFILE[/bold cyan]\n\n"
                f"[white]Username:[/white] "
                f"[bold yellow]{username}{' (You)' if is_me else ''}[/bold yellow]\n"
                f"[white]Average Score:[/white] {avg_score}%\n"
                f"[white]Accuracy:[/white] {accuracy}%\n"
                f"[white]Attempts:[/white] {attempts}\n"
                f"[white]Highest Score:[/white] {highest_score}%\n\n"
                f"[white]Avg Speed:[/white] {avg_speed}\n"
                f"[white]Timing:[/white] [{timing_color}]{timing_remark}[/{timing_color}]",
                border_style="cyan"
            )
        )

        
        display(
            framit(
                f"[bold green]Best Course[/bold green]\n\n"
                f"[white]Course:[/white] {best_course.get('title', 'N/A')}\n"
                f"[white]Score:[/white] {best_course.get('score', 0)}%",
                border_style="green"
            )
        )

        
        display()

        display(
            framit(
                "[bold magenta]COURSE PERFORMANCE BREAKDOWN[/bold magenta]",
                border_style="magenta"
            )
        )

        if not courses:

            display(
                framit(
                    "[yellow]No course data available[/yellow]",
                    border_style="yellow"
                )
            )

        else:

            table = CDT(
                title=f"{username} Courses",
                header_style="bold cyan",
                border_style="cyan",
                show_lines=True
            )

            table.add_column("Course", style="cyan")
            table.add_column("Avg", justify="center")
            table.add_column("Accuracy", justify="center")
            table.add_column("Attempts", justify="center")
            table.add_column("Speed", justify="center")
            table.add_column("Timing", justify="center")

            for c in courses:

                c_avg = float(c.get("avg_score", 0))
                c_acc = float(c.get("accuracy", 0))
                c_speed = c.get("avg_speed_display", "0s")
                c_timing = c.get("timing_remark", "Unknown")
                c_color = c.get("timing_color", "white")

                if c_avg >= 90:
                    c_avg_text = f"[bold green]{c_avg}%[/bold green]"
                elif c_avg >= 70:
                    c_avg_text = f"[yellow]{c_avg}%[/yellow]"
                else:
                    c_avg_text = f"[red]{c_avg}%[/red]"

                if c_acc >= 85:
                    c_acc_text = f"[green]{c_acc}%[/green]"
                elif c_acc >= 60:
                    c_acc_text = f"[yellow]{c_acc}%[/yellow]"
                else:
                    c_acc_text = f"[red]{c_acc}%[/red]"

                table.add_row(
                    c.get("course_title", "Unknown"),
                    c_avg_text,
                    c_acc_text,
                    str(c.get("attempts", 0)),
                    f"[{c_color}]{c_speed}[/{c_color}]",
                    f"[{c_color}]{c_timing}[/{c_color}]"
                )

            display(table)

        
        display()

        in_put(
            "[bold cyan]Press ENTER to return[/bold cyan]",
            default=""
        )



    def ghjk(self, course_id, sti):
        display(f"\n[bold magenta]Top 20 Scorers for Course {course_id}[/bold magenta]\n")
        try:
            res = self.z.tlp(course_id, sti)
            if res.status_code == 200:
                data = res.json().get("hodjn3in008con09ico19048kfnoWID9300I030fjjsj193sjfo9402jnabdsoii", [])[:20]
                table = CDT(title="Top Scorers", header_style="bold green")
                table.add_column("#", justify="center")
                table.add_column("Username", justify="left")
                table.add_column("Avg Score", justify="center")
                table.add_column("Accuracy (%)", justify="center")

                for i, s in enumerate(data, 1):
                    uname = s.get("username", "---")
                    avg = s.get("avg_score", 0)
                    acc = s.get("accuracy", 0)
                    style = "bold yellow" if str(s.get("sti") or "").lower() == str(sti).lower() else ""
                    table.add_row(
                        str(i),
                        f"[{style}]{uname}[/{style}]" if style else uname,
                        str(avg),
                        str(acc),
                    )

                display(table)
            else:
                display(f"[red]Unable to fetch leaderboard data. {res.text}[/red]")

        except Exception:
            display(f"[red]Error fetching leaderboard [/red]")


    def ok(
        self,
        yes,
        subcategory_id
    ):
        
        quiy=self.quiz_d(yes)

        
        if not subcategory_id:

            display(
                framit(
                    "[bold red]Invalid subcategory selected.[/bold red]"
                )
            )

            return None

        
        r = self.z.ans(
            yes,
            subcategory_id
        )

        
        if r.status_code != 200:

            display(
                framit(
                    f"[bold red]Failed to load quizzes "
                    f"[/bold red]"
                )
            )

            return None

        response_data = r.json()

        tpk = response_data.get(
            "hodjn3in008con09ico19048kfnoWID9300I030fjjsj193sjfo9402jnabdsoii",
            []
        )

        
        if not tpk:

            display(
                framit(
                    "[bold yellow]No quizzes available yet.[/bold yellow]"
                )
            )

            return None

        
        table = CDT(
            title="Available Quiz Topics",
            show_lines=True,
            border_style="cyan",
            header_style="bold cyan"
        )

        table.add_column(
            "#",
            justify="center",
            style="bold white"
        )

        table.add_column(
            "Status",
            justify="center"
        )

        table.add_column(
            "Topic",
            style="bold white"
        )

        table.add_column(
            "Progress",
            justify="center"
        )

        table.add_column(
            "Questions",
            justify="center"
        )

        table.add_column(
            "Attempts",
            justify="center"
        )

        table.add_column(
            "Score",
            justify="center"
        )

        table.add_column(
            "Difficulty",
            justify="center"
        )

        
        for idx, icx in enumerate(
            tpk,
            start=quiy
        ):

            
            if icx.get("locked"):

                status = (
                    "[bold red]LOCKED[/bold red]"
                )

                row_style = "red"

            elif icx.get("has_pending"):

                status = (
                    "[bold yellow]"
                    "Pending"
                    "[/bold yellow]"
                )

                row_style = "yellow"

            elif icx.get("not_attempted"):

                status = (
                    "[bold green]"
                    "New"
                    "[/bold green]"
                )

                row_style = "green"

            elif icx.get("completed"):

                status = (
                    "[bold cyan]"
                    "Completed"
                    "[/bold cyan]"
                )

                row_style = "cyan"

            else:

                status = (
                    "[white]Unknown[/white]"
                )

                row_style = "white"

           
            attempts_text = (
                f"{icx.get('attempts_used')}"
                f"/"
                f"{icx.get('max_attempts')}"
            )

            
            topic_title = str(
                icx.get(
                    "title",
                    "Untitled"
                )
            )

            
            table.add_row(

                str(idx),

                status,

                topic_title,

                str(
                    icx.get(
                        "progress",
                        "--"
                    )
                ),

                str(
                    icx.get(
                        "total_questions",
                        0
                    )
                ),

                attempts_text,

                str(
                    icx.get(
                        "score_text",
                        "0%"
                    )
                ),

                str(
                    icx.get(
                        "difficulty",
                        "Normal"
                    )
                ),

                style=row_style
            )

        
        display()
        display(table)

        
        display()

        display(
            "[bold yellow]Pending[/bold yellow] "
            "= Resume unfinished quiz"
        )

        display(
            "[bold green]New[/bold green] "
            "= Not attempted yet"
        )

        display(
            "[bold cyan]Completed[/bold cyan] "
            "= Finished course"
        )

        display(
            "[bold red]LOCKED[/bold red] "
            "= Maximum attempts reached"
        )

        display()

        
        while True:

            choice = in_put(
                "[bold green]Select quiz number "
                "or type 'q' to quit[/bold green]"
            ).strip()

            
            if choice.lower() in (
                "q",
                "quit",
                "exit"
            ):

                display(
                    framit(
                        "[yellow]Quiz selection cancelled.[/yellow]"
                    )
                )

                return None

            
            if not choice.isdigit():

                display(
                    "[red]Please enter a valid number.[/red]"
                )

                continue

            u7y = int(choice)
            
            quiy = self.z.quiy(yes)

            if quiy.status_code != 200:
                display(
                    "[red]An error has ocurred.[/red]"
                )


            quit_1 = int(
                        quiy.json().get(
                            "quiy"
                            
                        )
                    )

            
            if (
                u7y < quit_1
                or
                u7y > len(tpk)
            ):

                display(
                    "[red]Invalid quiz selection.[/red]"
                )

                continue

            
            ft45 = tpk[
                u7y - quit_1
            ]
            t=quit_1+1

            
            if ft45.get("locked"):

                display()

                display(
                    framit(
                        "[bold red]"
                        "COURSE LOCKED\n\n"
                        f"You have reached the maximum "
                        f"attempt limit "
                        f"({ft45.get('max_attempts', t)}).\n\n"
                        "This quiz can no longer "
                        "be attempted."
                        "[/bold red]"
                    )
                )

                continue

            
            self.d["selected_course"] = {

                "id":
                    ft45.get("id"),

                "title":
                    ft45.get("title"),

                "total_questions":
                    ft45.get(
                        "total_questions",
                        0
                    ),

                "difficulty":
                    ft45.get(
                        "difficulty",
                        "Normal"
                    ),

                "last_q":
                    ft45.get(
                        "last_q",
                        quit_1
                    ),

                "has_pending":
                    ft45.get(
                        "has_pending",
                        False
                    ),

                "completed":
                    ft45.get(
                        "completed",
                        False
                    ),

                "attempts_used":
                    ft45.get(
                        "attempts_used",
                        0
                    ),

                "remaining_attempts":
                    ft45.get(
                        "remaining_attempts",
                        0
                    ),

                
                "category_id":
                    ft45.get("category_id"),

                "subcategory_id":
                    ft45.get("subcategory_id"),

                "subcategory_name":
                    ft45.get("subcategory_name"),
            }

            ss(self.d)

            display()

            
            if ft45.get("has_pending"):

                display(
                    framit(
                        f"[bold yellow]"
                        f"Resuming pending quiz:\n\n"
                        f"{ft45.get('title')}\n\n"
                        f"Attempts Left: "
                        f"{ft45.get('remaining_attempts')}"
                        f"[/bold yellow]"
                    )
                )

            elif ft45.get("not_attempted"):

                display(
                    framit(
                        f"[bold green]"
                        f"Starting new quiz:\n\n"
                        f"{ft45.get('title')}\n\n"
                        f"Attempts Left: "
                        f"{ft45.get('remaining_attempts')}"
                        f"[/bold green]"
                    )
                )

            else:

                display(
                    framit(
                        f"[bold cyan]"
                        f"Opening completed course:\n\n"
                        f"{ft45.get('title')}\n\n"
                        f"Attempts Left: "
                        f"{ft45.get('remaining_attempts')}"
                        f"[/bold cyan]"
                    )
                )

            return ft45


    def asdf(self, quiz):

        while True:

            # =================================================
            # GLOBAL QUIZ ACCESS CHECK
            # =================================================
            access_response = self.z.quiz_access_status(
                quiz
            )

            if access_response.status_code != 200:

                try:

                    access_data = access_response.json()

                    display()

                    display(

                        framit(

                            f"[bold red]"
                            f"{access_data.get('message', 'Quiz access denied.')}"
                            f"[/bold red]\n\n"

                            f"[bold yellow]"
                            f"Please buy QuizCoin to continue."
                            f"[/bold yellow]"
                        )
                    )

                    display()

                except Exception:

                    display(
                        framit(
                            "[bold red]"
                            "Quiz access denied."
                            "[/bold red]"
                        )
                    )

                return

            try:

                access_data = access_response.json()

                can_continue_quiz = access_data.get(
                    "can_continue_quiz"
                    
                )

                if not can_continue_quiz:

                    display()

                    display(

                        framit(

                            f"[bold red]"
                            f"{access_data.get('message')}"
                            f"[/bold red]\n\n"

                            f"[bold yellow]"
                            f"Please buy QuizCoin to continue."
                            f"[/bold yellow]"
                        )
                    )

                    display()

                    return

            except Exception:

                pass

            # =================================================
            # SELECTED COURSE
            # =================================================
            course = self.d.get(
                "selected_course"
            )

            if not course:

                display(
                    framit(
                        "[bold red]No course selected[/bold red]"
                    )
                )

                return

            course_id = course.get("id")

            if not course_id:

                display(
                    framit(
                        "[bold red]Invalid course selected[/bold red]"
                    )
                )

                return

            # =================================================
            # QUIZ DETAILS
            # =================================================
            current_q = self.quiz_d(quiz)

            total_questions = int(
                course.get(
                    "total_questions",
                    0
                )
            )

            is_resuming = False

            # =================================================
            # CHECK PENDING QUIZZES
            # =================================================
            pqz = self.z.quiz(quiz)

            if pqz.status_code == 200:

                pqzd = pqz.json()

                if pqzd.get("has_pending"):

                    pending_list = pqzd.get(
                        "pending",
                        []
                    )

                    matched_pending = None

                    for pending in pending_list:

                        pending_course = pending.get(
                            "course",
                            {}
                        )

                        if (
                            pending_course.get("id")
                            ==
                            course_id
                        ):

                            matched_pending = pending

                            break

                    if matched_pending:

                        is_resuming = True

                        current_q = int(
                            matched_pending.get(
                                "last_q",
                                1
                            )
                        )

                        current_q = max(
                            current_q,
                            1
                        )

                        if total_questions > 0:

                            current_q = min(
                                current_q,
                                total_questions
                            )

                        display(
                            framit(
                                f"[bold yellow]"
                                f"Resuming quiz:\n\n"
                                f"{course.get('title')}"
                                f"[/bold yellow]\n\n"

                                f"[cyan]Progress:[/cyan] "
                                f"{matched_pending.get('progress', '--')}"
                            )
                        )

            # =================================================
            # NEW QUIZ
            # =================================================
            if not is_resuming:

                quiy = self.z.quiy(quiz)

                if quiy.status_code == 200:

                    current_q = int(
                        quiy.json().get(
                            "quiy",
                            1
                        )
                    )

                else:

                    current_q = 1

                display(
                    framit(
                        f"[bold green]"
                        f"Starting new quiz:\n\n"
                        f"{course.get('title')}"
                        f"[/bold green]"
                    )
                )

            # =================================================
            # NO QUESTIONS
            # =================================================
            if total_questions <= 0:

                display(
                    framit(
                        "[bold red]"
                        "This course has no questions yet."
                        "[/bold red]"
                    )
                )

                return

            # =================================================
            # QUIZ STARTED
            # =================================================
            display()

            display(
                framit(
                    f"[bold cyan]QUIZ STARTED[/bold cyan]\n\n"

                    f"[white]{course.get('title')}[/white]\n\n"

                    f"[green]Questions:[/green] "
                    f"{total_questions}",

                    title="QUIZ MODE"
                )
            )

            # =================================================
            # LOAD QUESTION
            # =================================================
            q_r = self.z.d(
                course_id,
                current_q,
                quiz
            )

            # =================================================
            # ACCESS DENIED / TRIAL ENDED
            # =================================================
            if q_r.status_code == 403:

                try:

                    denied_data = q_r.json()

                    display()

                    display(

                        framit(

                            f"[bold red]"
                            f"{denied_data.get('message', 'Quiz access denied.')}"
                            f"[/bold red]\n\n"

                            f"[bold yellow]"
                            f"Please buy QuizCoin to continue."
                            f"[/bold yellow]"
                        )
                    )

                    display()

                except Exception:

                    display(
                        framit(
                            "[bold red]"
                            "Quiz access denied."
                            "[/bold red]"
                        )
                    )

                return

            # =================================================
            # GENERAL FAILURE
            # =================================================
            if q_r.status_code != 200:

                display(
                    framit(
                        f"[bold red]"
                        f"Failed to load question\n\n"
                        f"{q_r.text}"
                        f"[/bold red]"
                    )
                )

                return

            current_question = q_r.json()

            # =================================================
            # QUESTION LOOP
            # =================================================
            while True:

                # =============================================
                # QUIZ COMPLETED
                # =============================================
                if current_question.get("completed"):

                    display(
                        framit(
                            "[bold green]"
                            "Quiz completed"
                            "[/bold green]"
                        )
                    )

                    break

                # =============================================
                # ACCESS BLOCKED MID-QUIZ
                # =============================================
                if (
                    current_question.get("trial_exhausted")
                    or
                    current_question.get("access_denied")
                ):

                    display()

                    display(

                        framit(

                            f"[bold red]"
                            f"{current_question.get('message')}"
                            f"[/bold red]\n\n"

                            f"[bold yellow]"
                            f"Please buy QuizCoin to continue."
                            f"[/bold yellow]"
                        )
                    )

                    display()

                    return

                q_id = current_question.get("id")

                question_text = current_question.get(
                    "text"
                )

                options = current_question.get(
                    "options",
                    []
                )

                # =============================================
                # INVALID QUESTION
                # =============================================
                if not q_id:

                    display(
                        framit(
                            "[bold red]"
                            "Invalid question received"
                            "[/bold red]"
                        )
                    )

                    break

                if not options:

                    display(
                        framit(
                            "[bold red]"
                            "Question has no options"
                            "[/bold red]"
                        )
                    )

                    break

                # =============================================
                # DISPLAY QUESTION
                # =============================================
                display()

                display(
                    Frame(
                        Write(
                            question_text,
                            style="bold white"
                        ),
                        title=(
                            f"Question "
                            f"{current_q} "
                            f"of "
                            f"{total_questions}"
                        ),
                        border_style="cyan"
                    )
                )

                # =============================================
                # DISPLAY OPTIONS
                # =============================================
                for i, option in enumerate(
                    options,
                    start=1
                ):

                    display(
                        f"[cyan]{i}.[/cyan] {option}"
                    )

                display()

                display(
                    "[yellow]"
                    "Enter option number "
                    "or type 'e' to exit."
                    "[/yellow]"
                )

                # =============================================
                # ANSWER TIMER
                # =============================================
                q_start = time.time()

                ans = in_put(
                    "[bold green]Your answer[/bold green]"
                ).strip()

                time_spent = int(
                    time.time() - q_start
                )

                # =============================================
                # EXIT QUIZ
                # =============================================
                if ans.lower() in (
                    "e",
                    "exit",
                    "quit",
                    "end"
                ):

                    should_exit = go_ahead(
                        "Quit and save progress?"
                    )

                    if should_exit:

                        self.d["last_q"] = current_q

                        ss(self.d)

                        display(
                            framit(
                                "[cyan]"
                                "Progress saved successfully."
                                "[/cyan]"
                            )
                        )

                        display(
                            framit(
                                "[bold yellow]"
                                "Returning to dashboard..."
                                "[/bold yellow]"
                            )
                        )

                        timing(1)

                        return

                    continue

                # =============================================
                # INVALID INPUT
                # =============================================
                if not ans.isdigit():

                    display(
                        "[red]"
                        "Please enter a valid number."
                        "[/red]"
                    )

                    continue

                selected_index = int(ans)

                if (
                    selected_index < 1
                    or
                    selected_index > len(options)
                ):

                    display(
                        "[red]"
                        "Selected option does not exist."
                        "[/red]"
                    )

                    continue

                selected_text = options[
                    selected_index - 1
                ]

                # =============================================
                # SUBMIT ANSWER
                # =============================================
                sub_r = self.z.sa(
                    course_id=course_id,
                    q_index=q_id,
                    selected=selected_text,
                    time_spent=time_spent,
                    source="cli",
                    quiz=quiz
                )

                # =============================================
                # SUBMIT FAILURE
                # =============================================
                if sub_r.status_code not in (
                    200,
                    201
                ):

                    display(
                        framit(
                            f"[bold red]"
                            f"Failed to submit answer\n\n"
                            f"{sub_r.text}"
                            f"[/bold red]"
                        )
                    )

                    continue

                sub = sub_r.json()

                # =============================================
                # ANSWER RESULT
                # =============================================
                correct = sub.get(
                    "correct",
                    False
                )

                result_text = (
                    "Correct!"
                    if correct
                    else "Incorrect!"
                )

                result_style = (
                    "green"
                    if correct
                    else "red"
                )

                display()

                display(
                    framit(
                        f"{result_text}\n\n"

                        f"Time: "
                        f"{cdp(time_spent)}",

                        border_style=result_style
                    )
                )

                # =============================================
                # PERFORMANCE
                # =============================================
                display(
                    framit(
                        f"[bold yellow]Progress:[/bold yellow] "
                        f"{sub.get('progress', '--')}\n\n"

                        f"[bold cyan]Score:[/bold cyan] "
                        f"{sub.get('score', 0)}%\n\n"

                        f"[bold magenta]Rank:[/bold magenta] "
                        f"#{sub.get('rank', '--')}\n\n"

                        f"[bold green]"
                        f"{sub.get('motivation', '')}"
                        f"[/bold green]",

                        title="Performance Update"
                    )
                )

                # =============================================
                # QUIZ FINISHED
                # =============================================
                if sub.get("completed"):

                    display()

                    display(
                        framit(
                            f"[bold green]"
                            f"Quiz Finished!"
                            f"[/bold green]\n\n"

                            f"Final Score: "
                            f"{sub.get('final_score', 0)}%\n\n"

                            f"Accuracy: "
                            f"{sub.get('accuracy', 0)}%\n\n"

                            f"Rank: "
                            f"#{sub.get('rank', '--')}\n\n"

                            f"[cyan]"
                            f"{sub.get('motivation', 'Well done!')}"
                            f"[/cyan]",

                            title="Final Result"
                        )
                    )

                    self.d["selected_course"] = None

                    ss(self.d)

                    another = go_ahead(
                        "Do you want another quiz?"
                    )

                    if another:

                        return

                    display(
                        framit(
                            "[bold cyan]"
                            "Thanks for participating!"
                            "[/bold cyan]"
                        )
                    )

                    return

                # =============================================
                # NEXT QUESTION
                # =============================================
                next_question = sub.get(
                    "next_question"
                )

                if not next_question:

                    display(
                        framit(
                            "[yellow]"
                            "No next question found."
                            "[/yellow]"
                        )
                    )

                    break

                current_q += 1

                current_question = next_question

                timing(1)

            # =================================================
            # CLEANUP
            # =================================================
            self.d["selected_course"] = None

            ss(self.d)

            return    

    # def asdf(self, quiz):

    #     while True:

            
    #         course = self.d.get(
    #             "selected_course"
    #         )

    #         if not course:

    #             display(
    #                 framit(
    #                     "[bold red]No course selected[/bold red]"
    #                 )
    #             )

    #             return

    #         course_id = course.get("id")

    #         if not course_id:

    #             display(
    #                 framit(
    #                     "[bold red]Invalid course selected[/bold red]"
    #                 )
    #             )

    #             return

            
    #         current_q = self.quiz_d

    #         total_questions = int(
    #             course.get(
    #                 "total_questions",
    #                 0
    #             )
    #         )

    #         is_resuming = False

            
    #         pqz = self.z.quiz(quiz)

    #         if pqz.status_code == 200:

    #             pqzd = pqz.json()

    #             if pqzd.get("has_pending"):

    #                 pending_list = pqzd.get(
    #                     "pending",
    #                     []
    #                 )

    #                 matched_pending = None

                    
    #                 for pending in pending_list:

    #                     pending_course = pending.get(
    #                         "course",
    #                         {}
    #                     )

    #                     if (
    #                         pending_course.get("id")
    #                         ==
    #                         course_id
    #                     ):

    #                         matched_pending = pending
    #                         break

                    
    #                 if matched_pending:

    #                     is_resuming = True

    #                     current_q = int(
    #                         matched_pending.get(
    #                             "last_q",
    #                             1
    #                         )
    #                     )

    #                     current_q = max(
    #                         current_q,
    #                         1
    #                     )

    #                     if total_questions > 0:

    #                         current_q = min(
    #                             current_q,
    #                             total_questions
    #                         )

    #                     display(
    #                         framit(
    #                             f"[bold yellow]"
    #                             f"Resuming quiz:\n\n"
    #                             f"{course.get('title')}"
    #                             f"[/bold yellow]\n\n"

    #                             f"[cyan]Progress:[/cyan] "
    #                             f"{matched_pending.get('progress', '--')}"
    #                         )
    #                     )

            
    #         h=0
    #         if not is_resuming:

    #             quiy = self.z.quiy(quiz)

    #             if quiy.status_code == 200:

    #                 current_q = int(
    #                     quiy.json().get(
    #                         "quiy"
                            
    #                     )
    #                 )

    #             else:

    #                 current_q = 1

    #             display(
    #                 framit(
    #                     f"[bold green]"
    #                     f"Starting new quiz:\n\n"
    #                     f"{course.get('title')}"
    #                     f"[/bold green]"
    #                 )
    #             )

            
    #         if total_questions <= h:

    #             display(
    #                 framit(
    #                     "[bold red]"
    #                     "This course has no questions yet."
    #                     "[/bold red]"
    #                 )
    #             )

    #             return

            
    #         display()

    #         display(
    #             framit(
    #                 f"[bold cyan]QUIZ STARTED[/bold cyan]\n\n"

    #                 f"[white]{course.get('title')}[/white]\n\n"

    #                 f"[green]Questions:[/green] "
    #                 f"{total_questions}",

    #                 title="QUIZ MODE"
    #             )
    #         )

           
    #         q_r = self.z.d(
    #             course_id,
    #             current_q,
    #             quiz
    #         )

    #         if q_r.status_code != 200:

    #             display(
    #                 framit(
    #                     f"[bold red]"
    #                     f"Failed to load question\n\n"
    #                     f"{q_r.text}"
    #                     f"[/bold red]"
    #                 )
    #             )

    #             return

    #         current_question = q_r.json()

            
    #         while True:

                
    #             if current_question.get("completed"):

    #                 display(
    #                     framit(
    #                         "[bold green]"
    #                         "Quiz completed"
    #                         "[/bold green]"
    #                     )
    #                 )

    #                 break

    #             q_id = current_question.get("id")

    #             question_text = current_question.get(
    #                 "text"
    #             )

    #             options = current_question.get(
    #                 "options",
    #                 []
    #             )

                
    #             if not q_id:

    #                 display(
    #                     framit(
    #                         "[bold red]"
    #                         "Invalid question received"
    #                         "[/bold red]"
    #                     )
    #                 )

    #                 break

    #             if not options:

    #                 display(
    #                     framit(
    #                         "[bold red]"
    #                         "Question has no options"
    #                         "[/bold red]"
    #                     )
    #                 )

    #                 break

                
    #             display()

    #             display(
    #                 Frame(
    #                     Write(
    #                         question_text,
    #                         style="bold white"
    #                     ),
    #                     title=(
    #                         f"Question "
    #                         f"{current_q} "
    #                         f"of "
    #                         f"{total_questions}"
    #                     ),
    #                     border_style="cyan"
    #                 )
    #             )

               
    #             for i, option in enumerate(
    #                 options,
    #                 start=1
    #             ):

    #                 display(
    #                     f"[cyan]{i}.[/cyan] {option}"
    #                 )

    #             display()

    #             display(
    #                 "[yellow]"
    #                 "Enter option number "
    #                 "or type 'e' to exit."
    #                 "[/yellow]"
    #             )

                
    #             q_start = time.time()

    #             ans = in_put(
    #                 "[bold green]Your answer[/bold green]"
    #             ).strip()

    #             time_spent = int(
    #                 time.time() - q_start
    #             )

                
    #             if ans.lower() in (
    #                 "e",
    #                 "exit",
    #                 "quit",
    #                 "end"
    #             ):

    #                 should_exit = go_ahead(
    #                     "Quit and save progress?"
    #                 )

    #                 if should_exit:

    #                     self.d["last_q"] = current_q

    #                     ss(self.d)

    #                     display(
    #                         framit(
    #                             "[cyan]"
    #                             "Progress saved successfully."
    #                             "[/cyan]"
    #                         )
    #                     )

    #                     display(
    #                         framit(
    #                             "[bold yellow]"
    #                             "Returning to dashboard..."
    #                             "[/bold yellow]"
    #                         )
    #                     )

    #                     timing(1)

    #                     return

    #                 continue

                
    #             if not ans.isdigit():

    #                 display(
    #                     "[red]"
    #                     "Please enter a valid number."
    #                     "[/red]"
    #                 )

    #                 continue

    #             selected_index = int(ans)

    #             if (
    #                 selected_index < 1
    #                 or
    #                 selected_index > len(options)
    #             ):

    #                 display(
    #                     "[red]"
    #                     "Selected option does not exist."
    #                     "[/red]"
    #                 )

    #                 continue

    #             selected_text = options[
    #                 selected_index - 1
    #             ]

                
    #             sub_r = self.z.sa(
    #                 course_id=course_id,
    #                 q_index=q_id,
    #                 selected=selected_text,
    #                 time_spent=time_spent,
    #                 source="cli",
    #                 quiz=quiz
    #             )

            
    #             if sub_r.status_code not in (
    #                 200,
    #                 201
    #             ):

    #                 display(
    #                     framit(
    #                         f"[bold red]"
    #                         f"Failed to submit answer\n\n"
    #                         f"{sub_r.text}"
    #                         f"[/bold red]"
    #                     )
    #                 )

    #                 continue

    #             sub = sub_r.json()

                
    #             correct = sub.get(
    #                 "correct",
    #                 False
    #             )

    #             result_text = (
    #                 "Correct!"
    #                 if correct
    #                 else "Incorrect!"
    #             )

    #             result_style = (
    #                 "green"
    #                 if correct
    #                 else "red"
    #             )

    #             display()

    #             display(
    #                 framit(
    #                     f"{result_text}\n\n"

    #                     f"Time: "
    #                     f"{cdp(time_spent)}",

    #                     border_style=result_style
    #                 )
    #             )

                
    #             display(
    #                 framit(
    #                     f"[bold yellow]Progress:[/bold yellow] "
    #                     f"{sub.get('progress', '--')}\n\n"

    #                     f"[bold cyan]Score:[/bold cyan] "
    #                     f"{sub.get('score', 0)}%\n\n"

    #                     f"[bold magenta]Rank:[/bold magenta] "
    #                     f"#{sub.get('rank', '--')}\n\n"

    #                     f"[bold green]"
    #                     f"{sub.get('motivation', '')}"
    #                     f"[/bold green]",

    #                     title="Performance Update"
    #                 )
    #             )

    #             b=1
                
    #             if sub.get("completed"):

    #                 display()

    #                 display(
    #                     framit(
    #                         f"[bold green]"
    #                         f"Quiz Finished!"
    #                         f"[/bold green]\n\n"

    #                         f"Final Score: "
    #                         f"{sub.get('final_score', 0)}%\n\n"

    #                         f"Accuracy: "
    #                         f"{sub.get('accuracy', 0)}%\n\n"

    #                         f"Rank: "
    #                         f"#{sub.get('rank', '--')}\n\n"

    #                         f"[cyan]"
    #                         f"{sub.get('motivation', 'Well done!')}"
    #                         f"[/cyan]",

    #                         title="Final Result"
    #                     )
    #                 )

                    
    #                 self.d["selected_course"] = None

    #                 ss(self.d)

    #                 another = go_ahead(
    #                     "Do you want another quiz?"
    #                 )

    #                 if another:

    #                     return

    #                 display(
    #                     framit(
    #                         "[bold cyan]"
    #                         "Thanks for participating!"
    #                         "[/bold cyan]"
    #                     )
    #                 )

    #                 return

                
    #             next_question = sub.get(
    #                 "next_question"
    #             )

    #             if not next_question:

    #                 display(
    #                     framit(
    #                         "[yellow]"
    #                         "No next question found."
    #                         "[/yellow]"
    #                     )
    #                 )

    #                 break



    #             current_q += b

    #             current_question = next_question

    #             timing(1)

            
    #         self.d["selected_course"] = None

    #         ss(self.d)

    #         return



    def quFGa(self, check):

        
        r = self.z.vm(check)

         
        if r.status_code != 200:

            display(
                framit(
                    f"[bold red]Failed to load wallet "
                    f"({r.status_code}) "
                    f"({r.text})[/bold red]"
                )
            )

            return

       
        data = r.json()
        
        user_data = data.get("user", {})

        wallet = data.get("AG2Hueyjdh874jfj94ifkfu489djporfj3MnBGHjj9O0O21120394IIFJVadjfjrifjv", {})

        quiz_stats = data.get(
            "quiz_stats",
            {}
        )

        earnings = data.get(
            "earnings",
            {}
        )

        withdrawals = data.get(
            "withdrawals",
            {}
        )

        withdrawal_history = data.get(
            "withdrawal_history",
            []
        )

        transactions = data.get(
            "recent_transactions",
            []
        )


        
        console.clear()

        
        display()

        display(
            centralize(
                framit(
                    f"[bold cyan]CDQUIZ WALLET DASHBOARD[/bold cyan]\n\n"

                    f"[white]User:[/white] "
                    f"[bold green]{user_data.get('username', 'Unknown')}[/bold green]\n"

                    f"[white]Email:[/white] "
                    f"{user_data.get('email', 'N/A')}",

                    border_style="cyan"
                )
            )
        )


        
        tx_table = CDT(
            title="Recent Transactions",
            header_style="bold white",
            border_style="white",
            show_lines=True
        )

        tx_table.add_column(
            "Type",
            style="cyan"
        )

        tx_table.add_column(
            "Amount",
            justify="right"
        )

        tx_table.add_column(
            "Date"
        )

        if transactions:

            for tx in transactions:

                tx_type = tx.get(
                    "type",
                    "unknown"
                )

                amount = tx.get(
                    "amount",
                    0
                )

                created_at = str(
                    tx.get(
                        "created_at",
                        ""
                    )
                )[:19]

                
                if tx_type in (
                    "deposit",
                    "challenge_reward",
                    "reward_correct_answer",
                ):

                    amount_text = (
                        f"[green]+{amount}[/green]"
                    )

                elif tx_type in (
                    "withdraw",
                    "quiz_timing_penalty",
                    "penalty_wrong_answer",
                    "penalty_policy_issues",
                    "withdraw_request",
                ):

                    amount_text = (
                        f"[red]-{amount}[/red]"
                    )

                else:

                    amount_text = str(amount)

                tx_table.add_row(
                    tx_type,
                    amount_text,
                    created_at
                )

        else:

            tx_table.add_row(
                "No transactions",
                "-",
                "-"
            )

        display()
        display(centralize(tx_table))






        
        wallet_table = CDT(
            title="Wallet Overview",
            border_style="green",
            header_style="bold green",
            show_lines=True
        )

        wallet_table.add_column(
            "Balance Type",
            style="bold white"
        )

        wallet_table.add_column(
            "Value",
            justify="right"
        )

        wallet_table.add_row(
            "QuizCoins",
            f"[bold yellow]{wallet.get('quizcoin_balance', 0)}[/bold yellow]"
        )

        wallet_table.add_row(
            "Points",
            f"[bold cyan]{wallet.get('points_balance', 0)}[/bold cyan]"
        )

        wallet_table.add_row(
            "Estimated NGN",
            f"[bold green]{wallet.get('estimated_ngn', '₦0')}[/bold green]"
        )

        wallet_table.add_row(
            "Withdrawable NGN",
            f"[bold bright_green]{wallet.get('withdrawable_ngn', '₦0')}[/bold bright_green]"
        )

        wallet_table.add_row(
            "Reserved QuizCoin",
            f"[red]{wallet.get('reserved_quizcoin', 0)}[/red]"
        )

        wallet_table.add_row(
            "Withdrawable QuizCoin",
            f"[green]{wallet.get('withdrawable_quizcoin', 0)}[/green]"
        )

        display()
        display(centralize(wallet_table))

        
        stats_table = CDT(
            title="Quiz Performance",
            border_style="cyan",
            header_style="bold cyan",
            show_lines=True
        )

        stats_table.add_column(
            "Metric",
            style="bold white"
        )

        stats_table.add_column(
            "Value",
            justify="right"
        )

        avg_score = float(
            quiz_stats.get(
                "average_score",
                0
            )
        )

        
        if avg_score >= 80:

            avg_score_text = (
                f"[bold green]{avg_score}%[/bold green]"
            )

        elif avg_score >= 50:

            avg_score_text = (
                f"[bold yellow]{avg_score}%[/bold yellow]"
            )

        else:

            avg_score_text = (
                f"[bold red]{avg_score}%[/bold red]"
            )

        stats_table.add_row(
            "Total Quizzes",
            str(
                quiz_stats.get(
                    "total_quizzes_taken",
                    0
                )
            )
        )

        stats_table.add_row(
            "Completed",
            str(
                quiz_stats.get(
                    "completed_quizzes",
                    0
                )
            )
        )

        stats_table.add_row(
            "Correct Answers",
            str(
                quiz_stats.get(
                    "total_correct_answers",
                    0
                )
            )
        )

        stats_table.add_row(
            "Questions Answered",
            str(
                quiz_stats.get(
                    "total_questions_answered",
                    0
                )
            )
        )

        stats_table.add_row(
            "Average Score",
            avg_score_text
        )

        display()
        display(centralize(stats_table))

        
        earnings_table = CDT(
            title="Today's Earnings",
            border_style="magenta",
            header_style="bold magenta",
            show_lines=True
        )

        earnings_table.add_column(
            "Type",
            style="bold white"
        )

        earnings_table.add_column(
            "Amount",
            justify="right"
        )

        earnings_table.add_row(
            "Earned Today",
            f"[green]+{earnings.get('today_earned_quizcoin', 0)} QC[/green]"
        )

        earnings_table.add_row(
            "Penalties",
            f"[red]-{earnings.get('today_penalties', 0)} QC[/red]"
        )

        display()
        display(centralize(earnings_table))

        
        withdrawal_table = CDT(
            title="Withdrawal Summary",
            border_style="blue",
            header_style="bold blue",
            show_lines=True
        )

        withdrawal_table.add_column(
            "Metric",
            style="bold white"
        )

        withdrawal_table.add_column(
            "Value",
            justify="right"
        )

        withdrawal_table.add_row(
            "📤 Total Requests",
            str(
                withdrawals.get(
                    "total_requests",
                    0
                )
            )
        )

        withdrawal_table.add_row(
            "Completed",
            f"[green]{withdrawals.get('completed_requests', 0)}[/green]"
        )

        withdrawal_table.add_row(
            "Pending",
            f"[yellow]{withdrawals.get('pending_requests', 0)}[/yellow]"
        )

        withdrawal_table.add_row(
            "Rejected",
            f"[red]{withdrawals.get('rejected_requests', 0)}[/red]"
        )

        withdrawal_table.add_row(
            "Total Withdrawn",
            f"[green]₦{withdrawals.get('total_withdrawn_ngn', 0):,.2f}[/green]"
        )

        withdrawal_table.add_row(
            "Pending NGN",
            f"[yellow]₦{withdrawals.get('pending_ngn', 0):,.2f}[/yellow]"
        )

        display()
        display(centralize(withdrawal_table))

        
        history_table = CDT(
            title="Withdrawal History",
            border_style="yellow",
            header_style="bold yellow",
            show_lines=True
        )

        history_table.add_column(
            "Status",
            justify="center"
        )

        history_table.add_column(
            "QuizCoin",
            justify="right"
        )

        history_table.add_column(
            "NGN",
            justify="right"
        )

        history_table.add_column(
            "Requested"
        )

        history_table.add_column(
            "Withdrawal ID"
        )

        
        if withdrawal_history:

            for wd in withdrawal_history[:10]:

                status = str(
                    wd.get(
                        "status",
                        ""
                    )
                ).lower()

                
                if status == "completed":

                    status_text = (
                        "[bold green]COMPLETED[/bold green]"
                    )

                elif status == "pending":

                    status_text = (
                        "[bold yellow]PENDING[/bold yellow]"
                    )

                elif status == "rejected":

                    status_text = (
                        "[bold red]REJECTED[/bold red]"
                    )

                else:

                    status_text = status.upper()

                
                history_table.add_row(

                    status_text,

                    str(
                        wd.get(
                            "quizcoin",
                            0
                        )
                    ),

                    str(
                        wd.get(
                            "formatted_ngn",
                            "₦0"
                        )
                    ),

                    str(
                        wd.get(
                            "created_at",
                            "-"
                        )
                    ),

                    

                    str(
                        wd.get(
                            "reference",
                            "-"
                        )
                    )
                )

        
        else:

            history_table.add_row(
                "-",
                "-",
                "-",
                "No withdrawal history",
                "-",
            )
        display()
        display(centralize(history_table))
        
        display()

        display(
            centralize(
                framit(
                    "[bold green]"
                    "Wallet dashboard loaded successfully."
                    "[/bold green]",
                    border_style="green"
                )
            )
        )

        display()

    def kjb(self, wid):

        
        r = self.z.vm(wid)

        if r.status_code != 200:
            display(
                framit(
                    f"[bold red]Failed to load wallet ({r.text})[/bold red]"
                )
            )
            return

        data = r.json()
        wallet = data.get("AG2Hueyjdh874jfj94ifkfu489djporfj3MnBGHjj9O0O21120394IIFJVadjfjrifjv", {})

        quizcoin_balance = float(wallet.get("quizcoin_balance", 0))
        withdrawable = float(wallet.get("withdrawable_quizcoin", 0))

        
        display(
            framit(
                "[bold cyan]WITHDRAWAL DASHBOARD[/bold cyan]\n\n"
                f"[bold white]QuizCoin Balance:[/bold white] {quizcoin_balance}\n"
                f"[bold green]Withdrawable QuizCoin:[/bold green] {withdrawable}\n\n"
                "[yellow]All withdrawals are processed in QuizCoin[/yellow]",
                border_style="cyan"
            )
        )

        if withdrawable <= 0:
            display("[bold red]No withdrawable balance available[/bold red]")
            return

        
        bank_res = self.z.fqtyu(wid)

        if bank_res.status_code != 200:
            display("[red]Unable to fetch bank details[/red]")
            return

        bank = bank_res.json().get("bank", {})

        
        if not bank:

            display(
                framit(
                    "[bold yellow]No Bank Account Found[/bold yellow]\n\n"
                    "You need a bank account to withdraw QuizCoin earnings.",
                    border_style="yellow"
                )
            )

            if not go_ahead("Create bank account now?"):
                return

            display(
                framit(
                    "[bold cyan]Create Bank Account[/bold cyan]",
                    border_style="cyan"
                )
            )

            bank_name = in_put("Bank name")
            account_number = in_put("Account number")
            account_name = in_put("Account name")

            save_res = self.z.chunj(
                wid,
                bank_name=bank_name,
                account_number=account_number,
                account_name=account_name
            )

            if save_res.status_code not in (200, 201):
                display("[red]Failed to save bank details[/red]")
                return

            bank = {
                "bank_name": bank_name,
                "account_number": account_number,
                "account_name": account_name
            }

        
        display(
            framit(
                f"[bold green]Bank Details[/bold green]\n\n"
                f"{bank.get('bank_name')}\n"
                f"{bank.get('account_number')}\n"
                f"{bank.get('account_name')}",
                border_style="green"
            )
        )

        
        display(
            framit(
                "[bold cyan]Choose Withdrawal Mode[/bold cyan]\n\n"
                "[1] Withdraw QuizCoin (Recommended)\n"
                "[2] View NGN Equivalent Only",
                border_style="cyan"
            )
        )

        mode = in_put("Select option", choices=["1", "2"], default="1")
        

        
        amount_input = in_put(
            "Enter QuizCoin amount to withdraw",
            default=str(withdrawable)
        )

        # server base


        try:
            amount = float(amount_input)
        except:
            display("[red]Invalid amount[/red]")
            return

        if amount <= 0:
            display("[red]Amount must be greater than 0[/red]")
            return

        if amount > withdrawable:
            display("[red]Exceeds withdrawable balance[/red]")
            return
        
        
        conv_res = self.z.plojt5(wid, amount)


        if conv_res.status_code != 200:
            display("[red]Failed run conversion [/red]")
            return

            
       
        conv_data = conv_res.json()

        constants = conv_data.get('constants')

        if mode == "2":

            display(
                framit(
                    f"[bold yellow]Conversion Preview Only[/bold yellow]\n\n"
                    "[cyan]You are still withdrawing QuizCoin, not NGN[/cyan]",
                    border_style="yellow"
                )
            )

            if not go_ahead("Proceed with QuizCoin withdrawal?"):
                return

        else:

            display(
                framit(
                    f"[bold green]Confirm Withdrawal[/bold green]\n\n"
                    f"QuizCoin: {amount}\n"
                    f"Bank: {bank.get('bank_name')}",
                    border_style="green"
                )
            )

            if not go_ahead("Proceed?"):
                return

        

        
        r = self.z.qputf3(
            sti=wid,
            quizcoin_amount=amount,
            bank_name=bank.get("bank_name"),
            account_number=bank.get("account_number"),
        )


        if r.status_code not in (200, 201):
            print(r.text)
            display(
                framit(
                    f"[bold red]Withdrawal failed ({r.status_code}): {r.json().get('detail')}[/bold red]"
                )
            )
            return

        res = r.json()

        
        display(
            framit(
                "[bold green]Withdrawal Submitted![/bold green]\n\n"
                f"{amount} QuizCoin\n"
                "Status: Pending Approval\n\n"
                "[cyan]QuizCoin remains your primary currency[/cyan]",
                border_style="green"
            )
        )

        if res.get("withdrawal_id"):
            display(f"[cyan]Transaction ID:[/cyan] {res['withdrawal_id']}")




    def quFGa3(self, sti):

        
        display()

        display(
             centralize(
                framit(
                    "[bold cyan]QUIZCOIN DEPOSIT CENTER[/bold cyan]\n\n"
                    "Fund your CDQuiz wallet securely using Paystack.\n"
                    "Instant QuizCoin delivery after payment confirmation.\n\n"
                    "[bold yellow]Minimum Deposit:[/bold yellow] ₦1,500",
                    border_style="cyan"
                )
             )
        )

        
        amount_input = in_put(
            "[bold green]Enter amount in Naira (₦)[/bold green]"
        ).strip()

        
        try:

            amount_ngn = float(amount_input)

        except Exception:

            display()

            display(
                framit(
                    "[bold red]Invalid amount entered.[/bold red]\n\n"
                    "Please enter a valid numeric amount.",
                    border_style="red"
                )
            )

            return

        
        if amount_ngn <= 1500:

            display()

            display(
                framit(
                    "[bold red]Deposit too low.[/bold red]\n\n"
                    "Minimum deposit is ₦1,500.",
                    border_style="red"
                )
            )

            return

        
        display()

        display(
            "[cyan]Initializing secure payment gateway...[/cyan]"
        )

        
        try:

            r = self.z.m(

                sti=sti,

                amount_ngn=amount_ngn
            )

        except Exception as e:

            display()

            display(
                framit(
                    "[bold red]Connection Error[/bold red]\n\n"
                    f"{str(e)}",
                    border_style="red"
                )
            )

            return

        
        if r.status_code != 200:

            try:

                error_data = r.json()

                detail = error_data.get(
                    "detail",
                    "Failed to initialize deposit"
                )

            except Exception:

                detail = "Server error occurred"
                

            display()

            display(
                framit(
                    f"[bold red]{detail}[/bold red]",
                    border_style="red"
                )
            )

            return

        
        data = r.json()

        success = data.get("success")

        if not success:

            display()

            display(
                framit(
                    "[bold red]Deposit initialization failed.[/bold red]",
                    border_style="red"
                )
            )

            return

        
        reference = data.get("reference")

        payment_url = data.get("payment_url")

        provider = data.get(
            "provider",
            "paystack"
        )

        status = data.get(
            "status",
            "pending"
        )

        formatted = data.get(
            "formatted",
            {}
        )

        user_data = data.get(
            "user",
            {}
        )

        conversion_rates = data.get(
            "conversion_rates",
            {}
        )

        
        formatted_ngn = formatted.get(
            "ngn",
            f"₦{amount_ngn:,.2f}"
        )

        formatted_usd = formatted.get(
            "usd",
            "$0.00"
        )

        formatted_quizcoin = formatted.get(
            "quizcoin",
            "0 QC"
        )

        formatted_points = formatted.get(
            "points",
            "0 pts"
        )

        
        display()

        display(
            centralize(
                framit(

                    "[bold green]DEPOSIT INITIALIZED[/bold green]\n\n"

                    f"[white]Reference:[/white]\n"
                    f"{reference}\n\n"

                    f"[white]Gateway:[/white]\n"
                    f"{provider.upper()}\n\n"

                    f"[white]Account:[/white]\n"
                    f"{user_data.get('email', 'N/A')}\n\n"

                    f"[white]Amount:[/white]\n"
                    f"{formatted_ngn}\n\n"

                    f"[white]USD Equivalent:[/white]\n"
                    f"{formatted_usd}\n\n"

                    f"[white]QuizCoin Reward:[/white]\n"
                    f"{formatted_quizcoin}\n\n"

                    f"[white]Points Reward:[/white]\n"
                    f"{formatted_points}\n\n"

                    f"[white]Rate:[/white]\n"
                    f"1 USD = ₦"
                    f"{conversion_rates.get('usd_to_ngn')}\n\n"

                    "[bold cyan]"
                    "Opening secure browser payment..."
                    "[/bold cyan]",

                    border_style="green"
                )
            )
        )

        
        try:

            cdb.open(payment_url)

        except Exception:

            display()

            display(
                framit(
                    "[bold red]Unable to open browser automatically.[/bold red]\n\n"
                    "Open this URL manually:\n\n"
                    f"{payment_url}",
                    border_style="red"
                )
            )

        
        display()

        display(
            "[bold yellow]"
            "Waiting for payment confirmation..."
            "[/bold yellow]"
        )

        display(
            "[cyan]"
            "Do not close this terminal."
            "[/cyan]"
        )

        
        with CDPT() as progress:

            task = progress.add_task(

                "[cyan]Monitoring payment status...[/cyan]",

                total=None
            )

            completed = False

            retries = 0

            max_retries = 300

            while not completed:

                timing(3)

                retries += 1

                
                if retries >= max_retries:

                    progress.stop()

                    display()

                    display(
                        framit(
                            "[bold red]Payment session timed out.[/bold red]\n\n"
                            "If payment was deducted, "
                            "it will reflect shortly.",
                            border_style="red"
                        )
                    )

                    return

                
                try:

                    check = self.z.cx(
                        sti,
                        reference
                    )

                except Exception:

                    progress.update(

                        task,

                        description=
                            "[yellow]"
                            "Reconnecting to server..."
                            "[/yellow]"
                    )

                    continue

                
                if check.status_code != 200:

                    progress.update(

                        task,

                        description=
                            "[yellow]"
                            "Retrying payment verification..."
                            "[/yellow]"
                    )

                    continue

               
                status_data = check.json()

                payment_status = status_data.get(
                    "status",
                    "pending"
                )

                
                if payment_status == "success":

                    completed = True

                    progress.stop()

                    wallet = status_data.get(
                        "wallet",
                        {}
                    )

                    deposit = status_data.get(
                        "deposit",
                        {}
                    )

                    display()

                    display(
                        centralize(
                            framit(

                                "[bold green]"
                                "PAYMENT SUCCESSFUL"
                                "[/bold green]\n\n"

                                f"[white]Reference:[/white]\n"
                                f"{reference}\n\n"

                                f"[white]Amount Paid:[/white]\n"
                                f"{deposit.get('formatted_ngn', formatted_ngn)}\n\n"

                                f"[white]QuizCoin Added:[/white]\n"
                                f"{deposit.get('formatted_quizcoin', formatted_quizcoin)}\n\n"

                                f"[white]Points Added:[/white]\n"
                                f"{deposit.get('formatted_points', formatted_points)}\n\n"

                               

                                "[bold cyan]"
                                "Wallet updated successfully. Select 3, to view wallet."
                                "[/bold cyan]",

                                border_style="green"
                            )
                        )
                    )

                    return

                
                elif payment_status in (

                    "failed",
                    "cancelled"

                ):

                    progress.stop()

                    display()

                    display(
                        framit(

                            "[bold red]"
                            "PAYMENT FAILED"
                            "[/bold red]\n\n"

                            f"Reference:\n"
                            f"{reference}\n\n"

                            "Your transaction was not completed.\n\n"

                            "You can retry again safely.",

                            border_style="red"
                        )
                    )

                    return

                
                elif payment_status == "processing":

                    progress.update(

                        task,

                        description=
                            "[cyan]"
                            "Payment received. "
                            "Finalizing transaction..."
                            "[/cyan]"
                    )

                
                else:

                    progress.update(

                        task,

                        description=
                            "[yellow]"
                            "Waiting for Paystack confirmation..."
                            "[/yellow]"
                    )

                    

    def will(self, sti):

        
        r = self.z.p(sti)

        if r.status_code != 200:

            display(
                framit(
                    "[bold red]Failed to load announcements[/bold red]",
                    border_style="red"
                )
            )
            return

        data = r.json()
        hodjn3in008con09ico19048kfno = data.get("hodjn3in008con09ico19048kfno6769083858274", [])

        if not hodjn3in008con09ico19048kfno:

            display(
                framit(
                    "[yellow]No announcements available[/yellow]",
                    border_style="yellow"
                )
            )
            return

        
        display()
        display(
            framit(
                "[bold cyan]LIVE ANNOUNCEMENTS[/bold cyan]\n"
                "[white]Updates • Leaders • Motivation • System News[/white]",
                border_style="cyan"
            )
        )

        
        for item in hodjn3in008con09ico19048kfno:

            a_type = item.get("type", "announcement")
            title = item.get("title") or "Announcement"
            message = item.get("message", "")
            priority = item.get("priority", 1)

            
            if a_type == "top_scorer":

                style = "bold yellow"
                border = "yellow"
                icon = ""


            elif a_type == "motivation":

                style = "bold magenta"
                border = "magenta"
                icon = ""

            else:

                style = "bold cyan"
                border = "cyan"
                icon = ""

            
            display(
                framit(
                    f"[{style}]{title}[/{style}]\n\n{message}",
                    title=f"{icon} Priority {priority}",
                    border_style=border
                )
            )

            timing(0.3)

        
        display(
            framit(
                "[bold green]✔ All announcements loaded successfully[/bold green]",
                border_style="green"
            )
        )

    
            
        
    
    def run(self):
        while True:
            try:
                menu = create_table(expand=True)
                menu.add_column(justify="center")
                menu.add_row(
                     
                    "[bold cyan]1[/bold cyan] Login    "
                    "[bold cyan]2[/bold cyan] Register    "
                    "[bold cyan]3[/bold cyan] Recover    "
                    "[bold cyan]CTRL + C (Windows), Command + C (Mac) to [/bold cyan] Exit"
                )
                display(framit(menu, title="[bold cyan]CDQUIZ[/bold cyan]"))
                choice = in_put("Select", choices=["1", "2", "3"], default="1")

                if choice == "1":
                    self.i()
                elif choice == "2":
                    self.fi()
                elif choice == "3":
                    self.db()
                else:
                    # self.db()
                    display("[bold]Goodbye![/bold]\n[dim cyan]Powered by Applinet Technology[/dim cyan]")
                    display("To restart cdquiz on terminal, run: python -m cdquiz.start ", style="green")
                    sys.exit(0)
            except KeyboardInterrupt:
                display()
                if go_ahead("Exit application?"):
                    display("To restart cdquiz on terminal, run: python -m cdquiz.start ", style="green")
                    display("Goodbye!", style="blue")
                    sys.exit(0)
