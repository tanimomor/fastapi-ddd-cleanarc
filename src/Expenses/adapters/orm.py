from sqlalchemy import Table, Column, Integer, String, Boolean

from src.Expenses.domain.models import ExpenseCategoryModel
from src.core.database.metadata import mapper_registry

# Define the table
expense_categories_table = Table(
    'expense_categories',
    mapper_registry.metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),  # Primary Key
    Column('name', String, nullable=False),  # Required category
    Column('code', String, nullable=False, unique=True),  # Required code
    Column('type', String, nullable=False),  # Required type
    Column('icon', String, nullable=True),  # Optional icon
    Column('is_active', Boolean),  # Boolean flag for active status
)

def start_mappers():
    # Map the ExpenseCategoryModel to the expense_categories_table
    mapper_registry.map_imperatively(
        class_=ExpenseCategoryModel,
        local_table=expense_categories_table,
        properties={
            '_id': expense_categories_table.c.id,
            '_name': expense_categories_table.c.name,  # Map the column `name` to the property `_name`
            '_code': expense_categories_table.c.code,  # Map the column `code` to the property `_code`
            '_type': expense_categories_table.c.type,  # Map the column `type` to the property `_type`
            '_icon': expense_categories_table.c.icon,  # Map the column `icon` to the property `_icon`
            '_is_active': expense_categories_table.c.is_active,  # Map the column `is_active` to the property `_is_active`
        }
    )