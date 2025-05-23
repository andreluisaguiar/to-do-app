from flask import Blueprint, render_template, redirect, url_for, flash, request
from app import db
from app.forms import LoginForm, RegistrationForm, TaskForm
from app.models import User, Task
from flask_login import current_user, login_user, logout_user, login_required
from urllib.parse import urlparse, urljoin
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint('main', __name__)

def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc

@bp.route('/')
def index():
    if current_user.is_authenticated:
        tasks = current_user.tasks.order_by(Task.id.desc()).all()
        total = len(tasks)
        concluidas = len([t for t in tasks if t.done])
        pendentes = len([t for t in tasks if not t.done])
        return render_template('index.html', tasks=tasks, total=total, concluidas=concluidas, pendentes=pendentes)
    return render_template('index.html')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            nome=form.nome.data,
            sobrenome=form.sobrenome.data,
            email=form.email.data.lower(),
            password_hash=generate_password_hash(form.password.data)
        )
        db.session.add(user)
        db.session.commit()
        flash('Cadastro realizado com sucesso! Faça login.')
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.lower()).first()
        if user is None or not check_password_hash(user.password_hash, form.password.data):
            flash('Email ou senha inválidos')
            return redirect(url_for('main.login'))
        login_user(user)
        return redirect(url_for('main.dashboard'))
    return render_template('login.html', form=form)

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@bp.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(title=form.title.data, description=form.description.data, user=current_user)
        db.session.add(task)
        db.session.commit()
        flash('Task added!')
        return redirect(url_for('main.dashboard'))
    tasks = current_user.tasks.order_by(Task.id.desc()).all()
    return render_template('dashboard.html', form=form, tasks=tasks)

@bp.route('/task/<int:task_id>/done')
@login_required
def mark_done(task_id):
    task = Task.query.get_or_404(task_id)
    if task.user != current_user:
        flash('You do not have permission to modify this task.')
        return redirect(url_for('main.dashboard'))
    task.done = not task.done
    db.session.commit()
    return redirect(url_for('main.dashboard'))

@bp.route('/task/<int:task_id>/delete')
@login_required
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    if task.user != current_user:
        flash('You do not have permission to delete this task.')
        return redirect(url_for('main.dashboard'))
    db.session.delete(task)
    db.session.commit()
    flash('Task deleted.')
    return redirect(url_for('main.dashboard'))

