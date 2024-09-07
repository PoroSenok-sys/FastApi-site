from fastapi import APIRouter, BackgroundTasks, Depends

from src.auth.base_config import current_user
from src.tasks.tasks import send_email_report_dashboard

router = APIRouter(
    prefix="/report",
    tags=["Report"])


@router.get("/dashboard")
async def get_dashboard_report(background_tasks: BackgroundTasks, user=Depends(current_user)):
    # 1400 ms - Это базовый и самый плохой подход, клиент должен дождаться выполнения задачи:
    # send_email_report_dashboard(user.username)

    # 500 ms - Хороший вариант, пользователь не обязан ждать завершения задачи, т.к.
    # она выполняется на фоне FastAPI в event loop'е или в другом треде:
    # background_tasks.add_task(send_email_report_dashboard, user.username)

    # 600 ms - Лучший способ. Задача выполняется воркером Celery в отдельном процессе,
    # с возможностью мониторить выполняемые процессы через Flower,
    # повторным выполнением не завершенных задачи и многое другое:
    send_email_report_dashboard.delay(user.username)

    return {
        "status": 200,
        "data": "Письмо отправлено",
        "details": None
    }
