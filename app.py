from flask import Flask, render_template, abort, request, flash, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import SelectField, SelectMultipleField, SubmitField, RadioField, widgets
from wtforms.validators import DataRequired

from data_process import DATA, ITEM_ID, FIELDS, LONG_FIELDS, SPLIT_FIELDS, results, left_data, result_fields

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = '1234'
bootstrap = Bootstrap(app)

saved = True

class ItemForm(FlaskForm):
    pass

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()
    

for field in result_fields:
    if field['mutiple']:
        setattr(ItemForm, field['field'], SelectMultipleField(field['field'],
        choices=list((opt['label'],opt['value']) for opt in field['options']), validators=[DataRequired()]))
    else:
        setattr(ItemForm, field['field'], SelectField(field['field'],
        choices=list((opt['label'],opt['value']) for opt in field['options']), validators=[DataRequired()]))
        
setattr(ItemForm, 'submit', SubmitField('Submit!'))


@app.route('/')
def index():
    pass

@app.route('/item/<item_id>', methods=['GET','POST'])
def item(item_id):
    if item_id not in DATA:
        abort(404)

    item = DATA[item_id]
    form = ItemForm()
    long_fields = {f:item[f].replace('\n','<br>') for f in LONG_FIELDS}
    split_fields = {}
    for field in SPLIT_FIELDS:
        split_tag = field['split']
        field_name = field['field']
        split_fields[field_name] = item[field_name].split(split_tag)

    if form.validate_on_submit():
        result = {}
        form_data = form.data
        for field in result_fields:
            result[field['field']] = form_data.get(field['field'])
        results[item_id] = result
        flash('item has already been classified!')
        if left_data[0]==item_id:
            left_data.pop(0)
        else:
            try:
                left_data.remove(item_id)
            except ValueError:
                flash('modified a bug which is classified!')    
        next_id = left_data[0]
        return redirect(url_for('item',item_id=next_id))       
    return render_template('item.html',item=item,form=form,long_fields=long_fields,split_fields=split_fields)


@app.context_processor
def inject_fields():
    return {
        'FIELDS': FIELDS,
        'LONG_FIELDS': LONG_FIELDS,
        'SPLIT_FIELDS': SPLIT_FIELDS,  
        'ITEM_ID': ITEM_ID      
    }


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
