from wtforms import ValidationError


class PhoneNumberValidator:
    def __init__(self, message=None):
        self.message = message

    def __call__(self, form, field):
        try:
            int(field.data)
        except (ValueError, TypeError):
            message = 'Field must have numbers only'
            raise ValidationError(message)

        length = field.data and len(field.data) or 0
        if length != 10:
            message = 'Field must have 10 digits'
            raise ValidationError(message)
