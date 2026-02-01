import pytest

from playwright.sync_api import Page

from api.endpoints.user_api import UserAPI
from ui.data.test_data import RegistrationData


@pytest.fixture
def not_authorized_user(page: Page):
    return {'page': page}


@pytest.fixture
def for_registration(not_authorized_user):
    page = not_authorized_user['page']
    reg_data = RegistrationData()
    yield {
        'page': page,
        'name': reg_data.name,
        'email': reg_data.email,
        'password': reg_data.password
    }
    user = UserAPI()
    if user.is_user_exists(reg_data.name, reg_data.email, reg_data.password):
        user.authorization(reg_data.email, reg_data.password)
        user.user_delete()


@pytest.fixture
def for_authorization(for_registration):
    user = UserAPI()
    user.registration(
        for_registration['name'],
        for_registration['email'],
        for_registration['password'])
    return {
        'page': for_registration['page'],
        'name': for_registration['name'],
        'email': for_registration['email'],
        'password': for_registration['password']
    }


@pytest.fixture
def authorized_user(for_authorization):
    user = UserAPI()
    user.authorization(for_authorization['email'], for_authorization['password'])
    return {
        'page': for_authorization['page'],
        'name': for_authorization['name'],
        'email': for_authorization['email'],
        'password': for_authorization['password'],
        'accessToken': user.get_access_token(),
        'refreshToken': user.get_refresh_token()
    }


@pytest.fixture
def deferred_authorization(for_authorization):
    return {
        'page': for_authorization['page'],
        'name': for_authorization['name'],
        'email': for_authorization['email'],
        'password': for_authorization['password'],
    }
