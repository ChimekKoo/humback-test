# Humback Test 0.1
# Copyright (c) 2020 Joachim Kołodziejski
# https://github.com/chimekkoo/humback-test

from sys import argv
from webbrowser import open as open_browser

__version__ = "0.1"

# import click
#
#
# @click.command
# @click.option("--gui", "-g", is_flag=True)
# def command(gui):
#     if gui:
#         from gui import webgui as flaskapp
#         flaskapp.run(host="localhost", port="5555")
#         open_browser("http://localhost:5555/")
#     else:
#         pass


if __name__ == "__main__":
    if "--gui" in argv:
        from webgui import app as flaskapp
        open_browser("http://localhost:5555/")
        flaskapp.run(host="localhost", port="5000")
