from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index.html')
def index():
    mensaje = "Bienvenido"
    return render_template('index.html', mensaje=mensaje)


@app.route('/admin.html')
def admin():
    mensaje = "Bienvenido Admin"
    return render_template('admin.html', mensaje=mensaje)



if __name__ == '__main__':
    app.run(debug=True)