from flask import flash


def flash_exception(e):
        flash(str(e), category='error')
