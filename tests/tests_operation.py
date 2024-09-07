from httpx import AsyncClient
import random

from tests.conftest import client

#
# async def test_add_specific_operations(ac: AsyncClient):
#     response = await ac.post("/operations", json={
#         "id": 0,
#         "quantity": "string",
#         "figi": "string",
#         "instrument_type": "string",
#         "date": "2024-09-04T09:56:32.746",
#         "type": "string"
#     })
#
#     assert response.status_code == 200


def test_add_specific_operations():
    response = client.post("/operations", json={
        "id": 1,
        "quantity": "string",
        "figi": "string",
        "instrument_type": "string",
        "date": "2024-09-04T09:56:32.746",
        "type": "Выплата купонов"
    })

    assert response.status_code == 200


async def test_get_specific_operations():
    response = client.get("/operations", params={
        "operation_type": "Выплата купонов",
    })

    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert len(response.json()["data"]) == 1


# def test_add_random_operations():
#     response = client.post("/operations", json={
#         "id": random.sample(range(1, 100), 1)[0],
#         "quantity": random.choice(spis_random_quantity),
#         "figi": "string",
#         "instrument_type": random.choice(spis_random_instrument_type),
#         "date": "2024-09-04T09:56:32.746",
#         "type": random.choice(spis_random_type)
#     })
#     assert response.status_code == 200
#
#
# spis_random_instrument_type = ["Мобильное приложение", "Брокер", "Посредник", "Браузер"]
# spis_random_quantity = ["Мало", "Хуже среднего", "Лучше среднего", "Много"]
# spis_random_type = ["Выплата купонов", "Оплата счетов", "Погашение кредитов"]
