from common import commonUnit
from common import configHttp
import readConfig as readConfig

localReadConfig = readConfig.ReadConfig()
localConfigHttp = configHttp.ConfigHttp()
localLogin_xls = commonUnit.get_xls("userCase.xlsx", "login")
localAddAddress_xls = commonUnit.get_xls("userCase.xlsx", "addAddress")


# login
def login():
    """
    login
    :return: token
    """
    # set url
    url = commonUnit.get_url_from_xml('login')
    localConfigHttp.set_url(url)

    # set header
    # token = localReadConfig.get_headers("token_v")
    # header = {"app_key": token}
    # localConfigHttp.set_headers(header)

    # set param
    data = {"username": localLogin_xls[0][3],
            "password": localLogin_xls[0][4],
            "app_key":"0F8CBF490DD3AB06C6DE0F9E9617FF71"}

    localConfigHttp.set_data(data)

    params = {}
    # login
    response = localConfigHttp.post().json()
    params['token'] = commonUnit.get_value_from_return_json(response, "data", "token")
    params['uuid'] = commonUnit.get_value_from_return_json(response, "data", "uuid")
    return params


# logout
def logout(token):
    """
    logout
    :param token: login token
    :return:
    """
    # set url
    url = commonUnit.get_url_from_xml('logout')
    localConfigHttp.set_url(url)

    # set header
    header = {'token': token}
    localConfigHttp.set_headers(header)

    # logout
    localConfigHttp.get()


if __name__ == '__main__':
    login()

