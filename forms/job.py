from flask_wtf import FlaskForm
from wtforms import PasswordField, EmailField, BooleanField, SubmitField, StringField, TextAreaField, IntegerField, DateField
from wtforms.validators import DataRequired


class AddJob(FlaskForm):
    job_title = StringField('Название работы', validators=[DataRequired()])
    team_leader = StringField('Ответственнный за выполнение работы', validators=[DataRequired()])
    work_size = IntegerField('Длительность', validators=[DataRequired()])
    collaborators = StringField('Соучастники')
    start_date = DateField('Дата начала')
    is_finished = BooleanField('Работа окончена?')
    submit = SubmitField('Создать')
