from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class BlogForm(FlaskForm):
    blogTitle = StringField('Blog Title',validators=[DataRequired(),Length(min=5,max=50)])
    auther = StringField('Auther Name',validators=[DataRequired()])
    blogContent = TextAreaField('Blog Content',validators=[DataRequired(),Length(min=50)])
    tags = StringField('Tags',validators=[DataRequired()])
    submit = SubmitField('Submit',validators=[DataRequired(),])