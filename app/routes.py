from app import app, db
from app.models import Admin, Inventory, Components
from app.forms import LoginForm, NewComponent, NewItem
from flask_login import current_user, login_user, login_required
from werkzeug.security import check_password_hash, generate_password_hash
from flask import render_template, redirect, flash, url_for, get_flashed_messages


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        admin = Admin.query.filter_by(name=form.name.data).first()
        if admin is None or not admin.check_password(form.password.data):
            flash('Invalid login credentials..')
            return redirect(url_for('login'))
        login_user(admin)
        return redirect('/index')
    return render_template('login.html', title='Login', form=form)

@app.route('/new_item', methods=['POST'])
@app.route('/index', methods=['GET'])
@login_required
def index():
    form = NewItem()
    if form.validate_on_submit():
        item = Inventory(
            device = form.device.data,
            model = form.model.data,
            brand = form.brand.data,
            price = form.price.data,
            quantity = form.quantity.data,
            notes = form.notes.data
        )
        db.session.add(item)
        db.session.commit()
        flash('Item has been added!')
        redirect(url_for('index'))
    inventory = Inventory.query.all()
    return render_template('index.html', title='Inventory', inventory=inventory, form=form)

@app.route('/remove_item/<itemid>', methods=['GET'])
@login_required
def remove_item(itemid):
    item = Inventory.query.filter_by(id=itemid).first()
    component = Components.query.filter_by(item_id=itemid).all()
    for c in component:
        db.session.delete(c)
    db.session.delete(item)
    db.session.commit()
    flash('Item has been deleted!')
    return redirect(url_for('index'))

@app.route('/remove_component/<itemid>/<component_id>', methods=['GET'])
@login_required
def remove_component(itemid, component_id):
    component = Components.query.filter_by(id=component_id).first()
    db.session.delete(component)
    db.session.commit()
    flash('Component has been deleted!')
    return redirect(url_for('item', itemid=itemid))

@app.route('/item/<itemid>', methods=['GET', 'POST'])
@login_required
def item(itemid):
    form = NewComponent()
    item = Inventory.query.filter_by(id=itemid).first()
    if form.validate_on_submit():
        component = Components(
            item_id = itemid,
            part = form.part.data,
            model = form.model.data,
            brand = form.brand.data,
            price = form.price.data,
            quantity = form.quantity.data
        )
        db.session.add(component)
        db.session.commit()
        flash('Component has been added!')
        return redirect(url_for('item', itemid=itemid))
    components = Components.query.all()
    return render_template('item.html', form=form, item=item, components=components)