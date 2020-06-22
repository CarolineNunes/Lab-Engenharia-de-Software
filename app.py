from flask import Flask, request, render_template, url_for, flash, redirect, request, abort
from flask_login import login_user, current_user, logout_user, login_required
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'b843c6cf3ef9cedcd0fbd635b84f17ae'


noticias = [
    {
        'autor': 'Caroline F Nunes',
        'titulo': 'Nasa SpaceX launch: Who are the astronauts?',
        'conteudo': '''Doug Hurley and Bob Behnken have broken a nine-year
         hiatus for Nasa, becoming the first astronauts to launch from US 
         soil since the retirement of the space shuttle in 2011.
        In the intervening years, Nasa bought seats for its astronauts
         - at a cost of tens of millions of dollars per flight - on the Russian Soyuz.
        But officials have also worked with Elon Musk's company SpaceX and aerospace
         giant Boeing to develop new, American spacecraft capable of ferrying humans 
         to and from the ISS - under the space agency's Commercial Crew Program.
        Musk's vehicle was first to fly; Hurley and Behnken travelled to the ISS in the sleek Crew Dragon spacecraft.''',
        'data_postagem': '12/04/2020'
    },
    {
        'autor': 'Caroline F Nunes',
        'titulo': 'New NASA human spaceflight leader acknowledges challenge of 2024 lunar landing',
        'conteudo':
        '''The new head of NASA’s human spaceflight programs says she’s excited by
         the opportunity to lead efforts to return astronauts to the moon, but cautioned
          she could not guarantee that could be accomplished by the end of 2024.
        In a June 18 call with reporters, her first since being named associate 
        administrator for human exploration and operations (HEO) June 12,
         Kathy Lueders said she was “very grateful” for the opportunity to 
         lead the directorate responsible for NASA’s exploration programs, 
         the International Space Station, and commercial crew, the program 
         she managed for several years before being tapped as associate administrator.''',
        'data_postagem': '13/04/2020'
    },
{
        'autor': 'Joe Rao',
        'titulo': 'Ring of fire solar eclipse 2020: Here is how it works (and what to expect)',
        'conteudo':
        '''The first full day of summer in the Northern Hemisphere will bring with it one of nature's 
        great sky shows: an annular solar eclipse. On Sunday (June 21), the new moon will orbit between 
        the sun and Earth and will pass squarely across the face of the sun for viewers along a very narrow path that 
        will run through central and northeast Africa, Saudi Arabia, Pakistan, northern India, and southern China
         including Taiwan. But instead of completely blocking the sun, it will leave a "ring of fire" from the sun when it peaks. ''',
        'data_postagem': '13/04/2020'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", noticias=noticias)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@spacenews.com' and form.password.data == 'fabricio':
            flash('Você está logado!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Credenciais inválidas, verifique usuário e senha', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/cadastro", methods=['GET', 'POST'])
def cadastro():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Conta criada para {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('cadastro.html', title='Cadastro', form=form)


@app.route("/assinante")
def home_assinante():
    return render_template("assinante.html", noticias=noticias)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
