from flask import render_template, url_for, flash, redirect, request
from app import app, db, bcrypt
from app.forms import RegistrationForm, LoginForm, LoginFormAdmin, NoticiaForm
from app.models import User, Post
from flask_login import login_user, current_user,logout_user, login_required


@app.route("/")
@app.route("/home")
def home():
    noticias = Post.query.all()
    return render_template("home.html", noticias=noticias)


@app.route("/homeadmin")
def homeadmin():
    noticias = Post.query.all()
    return render_template("homeadmin.html", noticias=noticias)


@app.route("/loginadmin", methods=['GET', 'POST'])
def loginadmin():
    form = LoginFormAdmin()
    if form.validate_on_submit():
        if form.emailadmin.data == 'admin@spacenews.com' and form.passwordadmin.data == 'fabricio':
            flash('Você está logado, Admin!', 'success')
            return redirect(url_for('homeadmin'))
        else:
            flash('Credenciais inválidas, verifique usuário e senha', 'danger')
    return render_template('loginadmin.html', title='Login', form=form)


@app.route("/logoutadmin")
def logoutadmin():
    logout_user()
    return redirect(url_for('home'))


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home_assinante'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home_assinante'))
        else:
            flash('Credenciais inválidas!', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/cadastro", methods=['GET', 'POST'])
def cadastro():
    if current_user.is_authenticated:
        return redirect(url_for('home_assinante'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Conta criada! Você já pode fazer login', 'success')
        return redirect(url_for('login'))
    return render_template('cadastro.html', title='Cadastro', form=form)


@app.route("/assinante")
@login_required
def home_assinante():
    noticias = Post.query.all()
    return render_template("assinante.html", noticias=noticias)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/conta")
@login_required
def account():
    return render_template('account.html', title='Conta')


@app.route("/noticia/nova", methods=['GET', 'POST'])
def criar_noticia():
    form = NoticiaForm()
    autor = "AdminSpaceNews"
    if form.validate_on_submit():
        post = Post(titulo=form.titulo.data, conteudo=form.conteudo.data, autor=autor)
        db.session.add(post)
        db.session.commit()
        flash('Notícia postada!', 'success')
        return redirect(url_for('homeadmin'))
    return render_template('nova_noticia.html', title='Criar Notícia', form=form, autor=autor)
