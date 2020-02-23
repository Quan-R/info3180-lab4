from flask_wtf import FlaskForm, CSRFProtect
from flask_wtf.file import FileField, FileRequired, FileAllowed

csrf = CSRFProtect()

class UploadForm(FlaskForm):
    image =  FileField('image', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])