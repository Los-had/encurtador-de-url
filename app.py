from flask import Flask, url_for, redirect, request, render_template
import pyshorteners


app = Flask(__name__)

'''
link_teste = 'https://pypi.org/project/names/'
encurtador = pyshorteners.Shortener()
nova_url = encurtador.tinyurl.short(link_teste)
print(f'\n{nova_url}')
'''

@app.route('/', methods=['GET'])
def index():
    try:
        return render_template('index.html')
    except:
        return redirect('/error')

@app.route('/error')
def error():
    return render_template('error.html')

@app.route('/resultado', methods=['GET', 'POST'])
def resultado():
    try:
        if request.method == 'POST':
            link_do_usuário = request.form['url']
            encurtador = pyshorteners.Shortener()
            nova_url = encurtador.tinyurl.short(link_do_usuário)
            return render_template('resultado.html', nova_url=nova_url) 
        else:
            return redirect('/error')
    except:
        return redirect('/error')

if __name__ == '__main__':
    app.run(debug=True)