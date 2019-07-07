


def custom_jwt_response_handler(token, user=None, request=None):
    """
    自定义obtain_jwt_token视图返回的数据
    :param token: obtain_jwt_token视图生成token
    :param user: 经过身份校验之后的用户对象
    :param request: 请求对象
    :return: 响应数据
    """

    return {
        "username": user.username,
        "user_id": user.id,
        "token": token
    }