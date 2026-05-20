import os

API_BASE_URL = os.environ.get("CODEHOUSE_API_URL", "https://cli.codehouse.cloud/quiz/")  
SESSION_FILE = os.path.expanduser("~/.codehouse_session")

ENDPOINTS = {
    "logo": "sys/logo/",
    "check_email_exists": "jkdioei948938edjckjdoe123",
    "check_phone_exists": "jkdioei948938edjckjdoe124",
    "register": "jkdioei948938edjckjdoe125",
    "verify_email": "jkdioei948938edjckjdoe126",
    "login": "jkdioei948938edjckjdoe127",
    "recover_request": "jkdioei948938edjckjdoe128",            
    "verify_recovery": "jkdioei948938edjckjdoe129",       
    "reset_password": "jkdioei948938edjckjdoe1230",               
    "account_recovery_request": "jkdioei948938edjckjdoe1231",
    "verify_account_recovery": "jkdioei948938edjckjdoe1232",
    "quiy": "jkdioei948938edjckjdoe1233/{sti}/",
    "categories": "jkdioei948938edjckjdoe1234/{sti}/",
    "quiz_access_status": "quiz_access_status/{sti}/",
    "subcategories": "jkdioei948938edjckjdoe1235/{category}/{sti}/",
    "courses": "jkdioei948938edjckjdoe1236/{sti}/{subcategory}/",
    "quiz_status": "jkdioei948938edjckjdoe1237/{course_id}/status/{sti}/",
    "quiz_question": "jkdioei948938edjckjdoe1238/{course_id}/question/{q_index}/{sti}/",
    "pending_quiz": "jkdioei948938edjckjdoe1240/{sti}/",
    "submit_answer": "jkdioei948938edjckjdoe1241/{course_id}/question/{question_id}/submit/{sti}/",
    "global_leaderboard": "jkdioei948938edjckjdoe1242/{sti}/",
    "leaderboard": "jkdioei948938edjckjdoe1243",
    "wallet": "jkdioei948938edjckjdoe1244/{sti}/",
    "bank_detail": "jkdioei948938edjckjdoe1245/{sti}/",
    "announcement": "jkdioei948938edjckjdoe1246/{sti}/",
    "save_bank_detail": "jkdioei948938edjckjdoe1247/{sti}/",
    "wallet_conversion": "jkdioei948938edjckjdoe1248/{sti}/",
    "create_deposit": "jkdioei948938edjckjdoe1249/{sti}/",
    "check_deposit_status": "jkdioei948938edjckjdoe1250/{sti}/{reference}/",
    "withdraw": "jkdioei948938edjckjdoe1251/{sti}/",
    "leaders_top_scorers": "jkdioei948938edjckjdoe1252/{course_id}/top/{sti}/",
    "top_scorers": "jkdioei948938edjckjdoe1253/{course_id}>/{str:sti}/",
    "qz_top_scorers": "leaders/quiz/top-cli/{course_id}>/{str:sti}/",
   
    "finish": "quiz/{course_id}/finish/{sti}/",
    "result_pdf": "results/{result_id}/pdf/",
    "appeal_block": "auth/appeal/"

}
DEFAULT_RETRIES =5
REMOTE_TIMEOUT= 10