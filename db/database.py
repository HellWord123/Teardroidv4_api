from deta import Deta
from os import getenv

deta = Deta(getenv("e0e0rp25_jLoKmyUSgvR4nexY1BPJW3MZncZR7ueh"))


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
