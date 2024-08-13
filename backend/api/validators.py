from django.core.validators import RegexValidator

username_validator = RegexValidator(
    regex='^[\w.@+-]+\z',
    message='Недопустимые символы в имени',
    code='invalid_username',
)