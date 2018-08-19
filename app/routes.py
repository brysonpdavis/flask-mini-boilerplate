from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import InputForm


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = InputForm()
    if form.validate_on_submit():
        flash('Requested for handles {} {}'.format(
            form.fst_handle.data, form.snd_handle.data))
        return redirect(url_for('index'))
    return render_template('index.html', title='Home', form=form)