from wtforms import StringField, SelectField, SelectMultipleField
from wtforms.widgets import TextArea
from wtforms.compat import text_type


class LongStringField(StringField):

    widget = TextArea()


class SelectFieldAsync(SelectField):

    def __init__(self, label=None, validators=None, coerce=text_type,
                 choices_fn=None, **kwargs):

        choices = choices_fn()

        super().__init__(label, validators, coerce, choices, **kwargs)


class SelectMultipleFieldAsync(SelectMultipleField):

    def __init__(self, label=None, validators=None, coerce=text_type,
                 choices_fn=None, **kwargs):

        choices = choices_fn()

        super().__init__(label, validators, coerce, choices, **kwargs)
