import os
import uuid
import json
import hmac
import time
import socket
import hashlib
import platform
import secrets

import requests

from rich.console import Console

from .cd4895938593091094850390395094 import (
    ls,
    gcf,
)

from .network import NetworkHelper

from .config import (
    API_BASE_URL,
    ENDPOINTS,
    REMOTE_TIMEOUT,
)


# =========================================================
# CONSOLE
# =========================================================
console = Console()


# =========================================================
# CLIENT VERSION
# =========================================================
CLIENT_VERSION = "2.0.0"


# =========================================================
# GLOBAL FINGERPRINT
# =========================================================
fingerprint = gcf()


class APIClient:
    

    def __init__(

        self,

        base_url=None,

        endpoints=None
    ):

        # =================================================
        # BASE URL
        # =================================================
        self.base_url = (

            (base_url or API_BASE_URL)
            .rstrip("/")

            + "/"
        )

        # =================================================
        # ENDPOINTS
        # =================================================
        self.endpoints = (
            endpoints or ENDPOINTS
        )

        # =================================================
        # SESSION
        # =================================================
        self.session = ls()

        self.ui = self.session.get(
            "token"
        )

        self.wo = self.session.get(
            "sti"
        )

        # -------------------------------------------------
        # SESSION SIGNING KEY
        # -------------------------------------------------
        self.ssk = self.session.get(
            "session_key"
        )

        # =================================================
        # NETWORK
        # =================================================
        self.net = NetworkHelper(
            console
        )

        # =================================================
        # DEVICE FINGERPRINT
        # =================================================
        self.fingerprint = fingerprint

        # =================================================
        # INSTALLATION SECURITY
        # =================================================
        self.installation_id = (
            self.get_installation_id()
        )

        self.device_id = (
            self.generate_device_id()
        )

        self.device_signature = (
            self.generate_device_signature()
        )

    
    def generate_nonce(self):

        return secrets.token_hex(32)
    
    def generate_timestamp(self):

        return str(int(time.time()))

    # =====================================================
    # INSTALLATION ID
    # =====================================================
    def get_installation_id(self):

        path = ".cdquiz_installation"

        if os.path.exists(path):

            try:

                with open(

                    path,

                    "r",

                    encoding="utf-8"

                ) as f:

                    return f.read().strip()

            except Exception:
                pass

        install_id = str(
            uuid.uuid4()
        )

        with open(

            path,

            "w",

            encoding="utf-8"

        ) as f:

            f.write(
                install_id
            )

        return install_id

    # =====================================================
    # DEVICE ID
    # =====================================================
    def generate_device_id(self):

        raw = (

            f"{platform.node()}|"

            f"{platform.system()}|"

            f"{platform.machine()}|"

            f"{socket.gethostname()}|"

            f"{uuid.getnode()}"
        )

        return hashlib.sha256(

            raw.encode()

        ).hexdigest()

    # =====================================================
    # DEVICE SIGNATURE
    # =====================================================
    def generate_device_signature(self):

        raw = (

            f"{self.device_id}|"

            f"{self.fingerprint}|"

            f"{platform.platform()}|"

            f"{self.installation_id}"
        )

        return hashlib.sha512(

            raw.encode()

        ).hexdigest()

    # =====================================================
    # BODY HASH
    # =====================================================
    def generate_body_hash(

        self,

        payload=None
    ):

        if not payload:

            payload = {}

        encoded = json.dumps(

            payload,

            sort_keys=True,

            separators=(",", ":")

        ).encode()

        return hashlib.sha256(

            encoded

        ).hexdigest()

    # =====================================================
    # REQUEST SIGNATURE
    # =====================================================
    def generate_request_signature(

        self,

        sti,

        endpoint,

        method,

        timestamp,

        nonce,

        body_hash="",
    ):

        # -------------------------------------------------
        # REQUIRE SESSION KEY
        # -------------------------------------------------
        if not self.ssk:

            # raise Exception(
            #     "Missing secure session key."
            # )
            # if not self.ssk:

            # BEFORE LOGIN → skip signing
            return None

        hostname = socket.gethostname()

        device_name = platform.node()

        payload = (

            f"{sti}|"

            f"{self.fingerprint}|"

            f"{self.device_id}|"

            f"{timestamp}|"

            f"{nonce}|"

            f"{endpoint}|"

            f"{method}|"

            f"{hostname}|"

            f"{device_name}|"

            f"{body_hash}|"

            f"{self.installation_id}"
        )

        return hmac.new(

            self.ssk.encode(),

            payload.encode(),

            hashlib.sha512

        ).hexdigest()

    # =====================================================
    # URL RESOLVER
    # =====================================================
    def _url(

        self,

        key,

        **kwargs
    ):

        ep = self.endpoints.get(
            key
        )

        if not ep:

            raise KeyError(
                f"Unknown endpoint: {key}"
            )

        return self.base_url + ep.format(
            **kwargs
        )

    # =====================================================
    # SECURE HEADERS
    # =====================================================
    def _headers(

        self,

        sti=None,

        endpoint="unknown",

        method="GET",

        payload=None,
    ):

        sti = sti or self.wo

        # -------------------------------------------------
        # TIMESTAMP
        # -------------------------------------------------
        timestamp = str(
            int(time.time())
        )

        # -------------------------------------------------
        # NONCE
        # -------------------------------------------------
        nonce = uuid.uuid4().hex

        # -------------------------------------------------
        # BODY HASH
        # -------------------------------------------------
        body_hash = self.generate_body_hash(
            payload
        )

        # -------------------------------------------------
        # REQUEST SIGNATURE
        # -------------------------------------------------
        signature = None

        if self.ssk:

            signature = self.generate_request_signature(

                sti=sti,
                endpoint=endpoint,
                method=method,
                timestamp=timestamp,
                nonce=nonce,
                body_hash=body_hash,
            )
        # signature = (
        #     self.generate_request_signature(

        #         sti=sti,

        #         endpoint=endpoint,

        #         method=method,

        #         timestamp=timestamp,

        #         nonce=nonce,

        #         body_hash=body_hash,
        #     )
        # )

        # -------------------------------------------------
        # PLATFORM INFO
        # -------------------------------------------------
        hostname = socket.gethostname()

        device_name = platform.node()

        os_name = platform.system()

        os_release = platform.release()

        machine = platform.machine()

        # -------------------------------------------------
        # HEADERS
        # -------------------------------------------------
        headers = {

            # ---------------------------------------------
            # CONTENT
            # ---------------------------------------------
            "Content-Type":
                "application/json",

            # ---------------------------------------------
            # AUTH
            # ---------------------------------------------
            "Authorization":
                str(self.ui or ""),

            "STI":
                str(sti or ""),

            # ---------------------------------------------
            # CLIENT
            # ---------------------------------------------
            "X-Client-Version":
                CLIENT_VERSION,

            "X-Request-Source":
                "cdquiz-cli",

            # ---------------------------------------------
            # DEVICE
            # ---------------------------------------------
            "X-Device-ID":
                self.device_id,

            "X-Device-Fingerprint":
                self.fingerprint,

            "X-Device-Signature":
                self.device_signature,

            "X-Installation-ID":
                self.installation_id,

            # ---------------------------------------------
            # PLATFORM
            # ---------------------------------------------
            "X-Hostname":
                hostname,

            "X-Device-Name":
                device_name,

            "X-OS":
                os_name,

            "X-OS-Release":
                os_release,

            "X-Machine":
                machine,

            # ---------------------------------------------
            # REQUEST
            # ---------------------------------------------
            "X-Timestamp":
                timestamp,

            "X-Nonce":
                nonce,

            "X-Endpoint":
                endpoint,

            "X-Request-Method":
                method,

            "X-Body-Hash":
                body_hash,

            # "X-Request-Signature":
            #     signature,

            "X-Request-Signature": signature or "",

            # ---------------------------------------------
            # USER AGENT
            # ---------------------------------------------
            "User-Agent":
                (
                    f"CDQuizSecureCLI/"
                    f"{CLIENT_VERSION} "
                    f"({platform.system()})"
                ),
        }

        return headers

    # =====================================================
    # REGISTER
    # =====================================================
    def h(self, q, s, c, f, t):

        payload = {

            "fullname": q,

            "email": s,

            "password": c,

            "phone": f,

            "country": t,

            "fingerprint": self.fingerprint,
        }

        return self.net.request(

            lambda: requests.post(

                self._url("register"),

                json=payload,

                headers=self._headers(

                    endpoint="register",

                    method="POST",

                    payload=payload,
                ),

                timeout=REMOTE_TIMEOUT,
            ),

            spinner_text="Registering",
        )


    # =====================================================
    # CHECK EMAIL
    # =====================================================
    def z(self, s):

        payload = {
            "email": s
        }

        return self.net.request(

            lambda: requests.post(

                self._url("check_email_exists"),

                json=payload,

                headers=self._headers(

                    endpoint="check_email_exists",

                    method="POST",

                    payload=payload,
                ),

                timeout=REMOTE_TIMEOUT,
            ),

            spinner_text="Checking if Account Exist",
        )


    # =====================================================
    # CHECK PHONE
    # =====================================================
    def k(self, k):

        payload = {
            "phone": k
        }

        return self.net.request(

            lambda: requests.post(

                self._url("check_phone_exists"),

                json=payload,

                headers=self._headers(

                    endpoint="check_phone_exists",

                    method="POST",

                    payload=payload,
                ),

                timeout=REMOTE_TIMEOUT,
            ),

            spinner_text="Checking phone number...",
        )



    # =====================================================
    # VERIFY EMAIL
    # =====================================================
    def y(self, x, z):

        payload = {

            "email": x,

            "token": z,
        }

        return self.net.request(

            lambda: requests.post(

                self._url("verify_email"),

                json=payload,

                headers=self._headers(

                    endpoint="verify_email",

                    method="POST",

                    payload=payload,
                ),

                timeout=REMOTE_TIMEOUT,
            ),

            spinner_text="Verifying email",
        )

    # =====================================================
    # SYSTEM LOGO
    # =====================================================
    def sys_logo(self):

        return self.net.request(

            lambda: requests.get(

                self._url("logo"),

                headers=self._headers(

                    endpoint="logo",

                    method="GET",
                ),

                timeout=REMOTE_TIMEOUT,
            ),

            spinner_text="Loading CodeHouse Cloud...",
        )


    # =====================================================
    # LOGIN
    # =====================================================
    def l(self, im, lm):

        payload = {

            "sti": im,

            "password": lm,

            "fingerprint": self.fingerprint,
        }

        return self.net.request(

            lambda: requests.post(

                self._url("login"),

                json=payload,

                headers=self._headers(

                    endpoint="login",

                    method="POST",

                    payload=payload,
                ),

                timeout=REMOTE_TIMEOUT,
            ),

            spinner_text="Logging in",
        )

    # =====================================================
    # ACCOUNT RECOVERY REQUEST
    # =====================================================
    def b(self, b):

        payload = {
            "identity": b
        }

        return self.net.request(

            lambda: requests.post(

                self._url("account_recovery_request"),

                json=payload,

                headers=self._headers(

                    endpoint="account_recovery_request",

                    method="POST",

                    payload=payload,
                ),

                timeout=REMOTE_TIMEOUT,
            ),

            spinner_text="Requesting account recovery token",
        )


    # =====================================================
    # VERIFY ACCOUNT RECOVERY
    # =====================================================
    def ti(self, br, iz):

        payload = {

            "identity": br,

            "token": iz,
        }

        return self.net.request(

            lambda: requests.post(

                self._url("verify_account_recovery"),

                json=payload,

                headers=self._headers(

                    endpoint="verify_account_recovery",

                    method="POST",

                    payload=payload,
                ),

                timeout=REMOTE_TIMEOUT,
            ),

            spinner_text="Verifying token...",
        )
    



    # =====================================================
    # RECOVERY REQUEST
    # =====================================================
    def w(self, w):

        payload = {
            "sti": w
        }

        return self.net.request(

            lambda: requests.post(

                self._url("recover_request"),

                json=payload,

                headers=self._headers(

                    endpoint="recover_request",

                    method="POST",

                    payload=payload,
                ),

                timeout=REMOTE_TIMEOUT,
            ),

            spinner_text="Requesting recovery token",
        )

    # =====================================================
    # VERIFY RECOVERY
    # =====================================================
    def ky(self, v, w):

        payload = {

            "sti": w,

            "recovery_token": v,
        }

        return self.net.request(

            lambda: requests.post(

                self._url("verify_recovery"),

                json=payload,

                headers=self._headers(

                    endpoint="verify_recovery",

                    method="POST",

                    payload=payload,
                ),

                timeout=REMOTE_TIMEOUT,
            ),

            spinner_text="Verifying recovery token",
        )

    # =====================================================
    # RESET PASSWORD
    # =====================================================
    def db(self, db, v, ky):

        payload = {

            "sti": db,

            "recovery_token": v,

            "new_password": ky,
        }

        return self.net.request(

            lambda: requests.post(

                self._url("reset_password"),

                json=payload,

                headers=self._headers(

                    endpoint="reset_password",

                    method="POST",

                    payload=payload,
                ),

                timeout=REMOTE_TIMEOUT,
            ),

            spinner_text="Resetting password",
        )



    def quiy(self,quiz):
        return self.net.request(

            lambda: requests.get(

                self._url(

                    "quiy",

                    sti=quiz
                ),

                headers=self._headers(

                    sti=quiz,

                    endpoint="quiy",

                    method="GET",
                ),

                timeout=REMOTE_TIMEOUT,
            ),

            spinner_text="Checking...",
        )

    # =====================================================
    # PENDING QUIZ
    # =====================================================
    def quiz(self, quiz):

        return self.net.request(

            lambda: requests.get(

                self._url(

                    "pending_quiz",

                    sti=quiz
                ),

                headers=self._headers(

                    sti=quiz,

                    endpoint="pending_quiz",

                    method="GET",
                ),

                timeout=REMOTE_TIMEOUT,
            ),

            spinner_text="Checking pending quiz...",
        )
    
    # =====================================================
    # CATEGORY
    # =====================================================
    def categories(self, quiz):

        return self.net.request(

            lambda: requests.get(

                self._url(

                    "categories",

                    sti=quiz
                ),

                headers=self._headers(

                    sti=quiz,

                    endpoint="categories",

                    method="GET",
                ),

                timeout=REMOTE_TIMEOUT,
            ),

            spinner_text="Fetching categories",
        )
    # =====================================================
    # SUBCATEGORIES
    # =====================================================
    def subcategories(self, category, quiz):

        return self.net.request(

            lambda: requests.get(

                self._url(

                    "subcategories",
                    category=category,
                    sti=quiz
                ),

                headers=self._headers(

                    sti=quiz,

                    endpoint="subcategories",

                    method="GET",
                ),

                timeout=REMOTE_TIMEOUT,
            ),

            spinner_text="Fetching subcategories",
        )
    # =====================================================
    # COURSES
    # =====================================================

    def quiz_access_status(self, quiz):

        return self.net.request(

            lambda: requests.get(

                self._url(

                    "quiz_access_status",

                    sti=quiz,
                ),

                headers=self._headers(

                    sti=quiz,

                    endpoint="quiz_access_status",

                    method="GET",
                ),

                timeout=REMOTE_TIMEOUT,
            ),

            spinner_text="Checking quiz access status...",
        )


    def ans(self, quiz, subcategory_id):

        return self.net.request(

            lambda: requests.get(

                self._url(

                    "courses",

                    sti=quiz,
                    subcategory=subcategory_id,
                ),

                headers=self._headers(

                    sti=quiz,

                    endpoint="courses",

                    method="GET",
                ),

                timeout=REMOTE_TIMEOUT,
            ),

            spinner_text="Fetching courses",
        )

    # =====================================================
    # QUIZ STATUS
    # =====================================================
    def get_status(self, course_id, sti):

        return self.net.request(

            lambda: requests.get(

                self._url(

                    "quiz_status",

                    course_id=course_id,

                    sti=sti
                ),

                headers=self._headers(

                    sti=sti,

                    endpoint="quiz_status",

                    method="GET",
                ),

                timeout=REMOTE_TIMEOUT,
            ),

            spinner_text="Checking quiz status",
        )



    # =====================================================
    # QUIZ QUESTION
    # =====================================================
    def d(self, course_id, q_index, sti):

        return self.net.request(

            lambda: requests.get(

                self._url(

                    "quiz_question",

                    course_id=course_id,

                    q_index=q_index,

                    sti=sti
                ),

                headers=self._headers(

                    sti=sti,

                    endpoint="quiz_question",

                    method="GET",
                ),

                timeout=REMOTE_TIMEOUT,
            ),

            spinner_text="Loading question",
        )


    # =====================================================
    # SUBMIT ANSWER
    # =====================================================
    def sa(

        self,
        course_id,
        q_index,
        selected,
        time_spent,
        source="cli",
        quiz=None,
    ):

        payload = {

            "q_index": q_index,

            "answer": selected,

            "sti": quiz,

            "time_spent": time_spent,

            "source": source,
        }

        return self.net.request(

            lambda: requests.post(

                self._url(

                    "submit_answer",

                    course_id=course_id,

                    question_id=q_index,

                    sti=quiz
                ),

                headers=self._headers(

                    sti=quiz,

                    endpoint="submit_answer",

                    method="POST",

                    payload=payload,
                ),

                json=payload,

                timeout=REMOTE_TIMEOUT,
            ),

            spinner_text="Submitting answer",
        )


    # =====================================================
    # FINISH QUIZ
    # =====================================================
    def finish(self, course_id, sti):

        payload = {}

        return self.net.request(

            lambda: requests.post(

                self._url(

                    "finish",

                    course_id=course_id,

                    sti=sti
                ),

                headers=self._headers(

                    sti=sti,

                    endpoint="finish",

                    method="POST",

                    payload=payload,
                ),

                timeout=REMOTE_TIMEOUT,
            ),

            spinner_text="Finalizing quiz",
        )


    # =====================================================
    # TOP SCORERS
    # =====================================================
    def get_top(self, course_id, sti):

        return self.net.request(

            lambda: requests.get(

                self._url(

                    "top_scorers",

                    course_id=course_id,

                    sti=sti
                ),

                headers=self._headers(

                    sti=sti,

                    endpoint="top_scorers",

                    method="GET",
                ),

                timeout=REMOTE_TIMEOUT,
            ),

            spinner_text="Loading leaderboard",
        )

    # =====================================================
    # GLOBAL LEADERBOARD
    # =====================================================
    def vtu(self, quiz):

        return self.net.request(

            lambda: requests.get(

                self._url(

                    "global_leaderboard",

                    sti=quiz
                ),

                headers=self._headers(

                    sti=quiz,

                    endpoint="global_leaderboard",

                    method="GET",
                ),

                timeout=REMOTE_TIMEOUT,
            ),

            spinner_text="Loading leaderboard",
        )


    # =====================================================
    # LEADERS TOP SCORERS
    # =====================================================
    def tlp(self, course_id, sti):

        return self.net.request(

            lambda: requests.get(

                self._url(

                    "leaders_top_scorers",

                    course_id=course_id,

                    sti=sti
                ),

                headers=self._headers(

                    sti=sti,

                    endpoint="leaders_top_scorers",

                    method="GET",
                ),

                timeout=REMOTE_TIMEOUT,
            ),

            spinner_text="Loading leaderboard",
        )

    # =====================================================
    # RESULT PDF
    # =====================================================
    def get_result_pdf(self, result_id, sti):

        return self.net.request(

            lambda: requests.get(

                self._url(

                    "result_pdf",

                    result_id=result_id
                ),

                headers=self._headers(

                    sti=sti,

                    endpoint="result_pdf",

                    method="GET",
                ),

                timeout=REMOTE_TIMEOUT,
            ),

            spinner_text="Preparing your result PDF",
        )



    # # =====================================================
    # # WALLET
    # # =====================================================
    # def vm(self, sti):

    #     return self.net.request(

    #         lambda: requests.get(

    #             self._url(
    #                 "wallet",
    #                 sti=sti
    #             ),

    #             headers=self._headers(

    #                 sti=sti,

    #                 endpoint="wallet_view",

    #                 method="GET",
    #             ),

    #             timeout=REMOTE_TIMEOUT,
    #         ),

    #         spinner_text="Fetching wallet...",
    #     )
    
    
    
    # =====================================================
    # WALLET
    # =====================================================
    def vm(self, sti):

        return self.net.request(

            lambda: requests.get(

                self._url(

                    "wallet",

                    sti=sti
                ),

                headers=self._headers(

                    sti=sti,

                    endpoint="wallet",

                    method="GET",
                ),

                timeout=REMOTE_TIMEOUT,
            ),

            spinner_text="Fetching wallet",
        )
    

    # =====================================================
    # WALLET CONVERSION
    # =====================================================
    def plojt5(self, sti, quizcoin):

        payload = {

            "quizcoin": quizcoin,
        }

        return self.net.request(

            lambda: requests.post(

                self._url(

                    "wallet_conversion",

                    sti=sti
                ),

                headers=self._headers(

                    sti=sti,

                    endpoint="wallet_conversion",

                    method="POST",

                    payload=payload,
                ),

                json=payload,

                timeout=REMOTE_TIMEOUT,
            ),

            spinner_text="Checking wallet conversion",
        )
    

    # =====================================================
    # BANK DETAIL
    # =====================================================
    def fqtyu(self, sti):

        return self.net.request(

            lambda: requests.get(

                self._url(

                    "bank_detail",

                    sti=sti
                ),

                headers=self._headers(

                    sti=sti,

                    endpoint="bank_detail",

                    method="GET",
                ),

                timeout=REMOTE_TIMEOUT,
            ),

            spinner_text="Fetching bank",
        )
    


    # =====================================================
    # ANNOUNCEMENTS
    # =====================================================
    def p(self, sti):

        return self.net.request(

            lambda: requests.get(

                self._url(

                    "announcement",

                    sti=sti
                ),

                headers=self._headers(

                    sti=sti,

                    endpoint="announcement",

                    method="GET",
                ),

                timeout=REMOTE_TIMEOUT,
            ),

            spinner_text="Fetching announcements",
        )
    


    # =====================================================
    # SAVE BANK DETAIL
    # =====================================================
    def chunj(

        self,
        sti,
        bank_name,
        account_number,
        account_name
    ):

        payload = {

            "bank_name": bank_name,

            "account_number": account_number,

            "account_name": account_name,
        }

        return self.net.request(

            lambda: requests.post(

                self._url(

                    "save_bank_detail",

                    sti=sti
                ),

                headers=self._headers(

                    sti=sti,

                    endpoint="save_bank_detail",

                    method="POST",

                    payload=payload,
                ),

                json=payload,

                timeout=REMOTE_TIMEOUT,
            ),

            spinner_text="Saving bank",
        )
    


    # =====================================================
    # CREATE DEPOSIT
    # =====================================================
    def m(self, sti, amount_ngn):

        payload = {

            "amount_ngn": amount_ngn,
        }

        return self.net.request(

            lambda: requests.post(

                self._url(

                    "create_deposit",

                    sti=sti
                ),

                headers=self._headers(

                    sti=sti,

                    endpoint="create_deposit",

                    method="POST",

                    payload=payload,
                ),

                json=payload,

                timeout=REMOTE_TIMEOUT,
            ),

            spinner_text="Making Deposit",
        )
    

    # =====================================================
    # CHECK DEPOSIT STATUS
    # =====================================================
    def cx(self, sti, reference):

        return self.net.request(

            lambda: requests.get(

                self._url(

                    "check_deposit_status",

                    sti=sti,

                    reference=reference
                ),

                headers=self._headers(

                    sti=sti,

                    endpoint="check_deposit_status",

                    method="GET",
                ),

                timeout=REMOTE_TIMEOUT,
            ),

            spinner_text="Checking Deposit Status...",
        )
    

    # =====================================================
    # WITHDRAW
    # =====================================================
    def qputf3(

        self,
        sti,
        quizcoin_amount,
        bank_name,
        account_number
    ):

        payload = {

            "quizcoin_amount": quizcoin_amount,

            "bank_name": bank_name,

            "account_number": account_number,
        }

        return self.net.request(

            lambda: requests.post(

                self._url(

                    "withdraw",

                    sti=sti
                ),

                headers=self._headers(

                    sti=sti,

                    endpoint="withdraw",

                    method="POST",

                    payload=payload,
                ),

                json=payload,

                timeout=REMOTE_TIMEOUT,
            ),

            spinner_text="Requesting withdrawal",
        )
    


    # =====================================================
    # APPEAL BLOCK
    # =====================================================
    def appeal_block(self):

        payload = {}

        return self.net.request(

            lambda: requests.post(

                self._url("appeal_block"),

                headers=self._headers(

                    endpoint="appeal_block",

                    method="POST",

                    payload=payload,
                ),

                timeout=REMOTE_TIMEOUT,
            ),

            spinner_text="Submitting appeal",
        )