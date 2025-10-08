from fastapi import APIRouter

lists_router = APIRouter(prefix="/lists", tags=["Processing todo lists"])


@lists_router.post("/lists")
async def create_list():
    return "create_list"


@lists_router.get("")
async def get_lists():
    return "get_lists"


@lists_router.get("/{list_id}")
async def get_list(list_id: int):
    return "get_list"


@lists_router.put("/{list_id}")
async def update_list(list_id: int):
    return "update_list"


@lists_router.delete("/{list_id}")
async def delete_list(list_id: int):
    return "delete_list"
