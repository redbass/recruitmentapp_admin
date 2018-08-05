from wtforms import StringField
from wtforms.widgets import TextArea


class LongStringField(StringField):

    widget = TextArea()
