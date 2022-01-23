from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea
# Create a Posts Form. So users can create post and submit onto website. - MN


class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    image = StringField('Image URL', validators=[DataRequired(), ])
    content = StringField("Content", validators=[
                          DataRequired()], widget=TextArea())
    submit = SubmitField("Submit")


class UpdatePostForm(FlaskForm):
    title = StringField('Title')
    image = StringField('Image URL')
    content = StringField('Post Content')
    submit = SubmitField()
