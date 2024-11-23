from fastapi import APIRouter, Depends, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from src.Expenses.config import URLPathsConfig, RouterConfig, URLNamesConfig
from src.Expenses.entrypoints.dependancies import get_all_expense_categories, create_expense_category, \
    get_expense_category_by_id
from src.Expenses.domain.models import ExpenseCategoryModel

expense_category_router = APIRouter(
    prefix=RouterConfig.PREFIX,
    tags=RouterConfig.tags_list(),
)

@expense_category_router.get(
    path=URLPathsConfig.LIST,
    response_class=JSONResponse,
    name=URLNamesConfig.LIST,
    status_code=status.HTTP_200_OK
)
async def get_all_categories(expense_categories = Depends(get_all_expense_categories)):
    return [await i.to_dict() for i in expense_categories]


@expense_category_router.post(
    path=URLPathsConfig.CREATE,
    response_class=JSONResponse,
    name=URLNamesConfig.CREATE,
    status_code=status.HTTP_201_CREATED,
    response_model=ExpenseCategoryModel
)
async def create_category(
    category = Depends(create_expense_category)
):
    return category


@expense_category_router.get(
    path=URLPathsConfig.DETAIL,
    response_class=JSONResponse,
    name=URLNamesConfig.DETAIL,
    status_code=status.HTTP_200_OK
)
async def get_category_by_id(
    expense_category = Depends(get_expense_category_by_id)
):
    return await expense_category.to_dict()

#
# @expense_category_router.put(
#     path=URLPathsConfig.UPDATE,
#     response_class=JSONResponse,
#     name=URLNamesConfig.UPDATE,
#     status_code=status.HTTP_200_OK,
#     response_model=ExpenseCategoryModel
# )
# async def update_category(
#     updated_category: ExpenseCategoryResponse = Depends(update_expense_category)
# ):
#     return updated_category
#
#
# @router.delete(
#     path=URLPathsConfig.DELETE,
#     response_class=Response,
#     name=URLNamesConfig.DELETE,
#     status_code=status.HTTP_204_NO_CONTENT
# )
# async def delete_category(category_id: int = Depends(delete_expense_category)):
#     response: Response = Response()
#     response.delete_cookie(
#         key=cookies_config.COOKIES_KEY,
#         secure=cookies_config.SECURE_COOKIES,
#         httponly=cookies_config.HTTP_ONLY,
#         samesite=cookies_config.SAME_SITE
#     )
#     return response
