from pytest_factoryboy import register
from tests.factory import AdFactory, UserFactory, CategoryFactory, SelectionFactory

pytest_plugins = "tests.fixtures"

register(UserFactory)
register(CategoryFactory)
register(AdFactory)
register(SelectionFactory)

