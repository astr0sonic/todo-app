from fastapi import APIRouter, Depends

from src.models.other import MyOtherParams

other_router = APIRouter(prefix="/other")


@other_router.get("")
async def get_other(my_other_params: MyOtherParams = Depends()) -> str:
    return "ok"
