from flask import flash


def flash_exception(e):
        flash_error(str(e))


def flash_error(msg):
        flash(msg, category='error')


def flash_message(msg):
        flash(msg, category='message')
