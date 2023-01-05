from deta import Deta
from os import getenv

deta = Deta(getenv("a04kvnlj_1dq5jVzsBHoF8FPq6ceaXWWopJzWheSj"))


def client_db():
    return deta.Base("client")


def notification_db():
    return deta.Base("notification")


def command_db():
    return deta.Base("command")


def auth_db():
    return deta.Base("auth")


async def tear_drive():
    return deta.Drive("teardroid")
