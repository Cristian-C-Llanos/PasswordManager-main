from flask import Flask, render_template, request, redirect
from business_layer import BusinessLayer

app = Flask(__name__)
business_layer = BusinessLayer()

@app.route('/')
def index():
    passwords = business_layer.get_passwords()
    return render_template('index.html', passwords=passwords)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        service = request.form['service']
        username = request.form['username']
        password = request.form['password']
        business_layer.add_password(service, username, password)
        return redirect('/')
    return render_template('add_password.html')

@app.route('/update/<int:password_id>', methods=['GET', 'POST'])
def update(password_id):
    if request.method == 'POST':
        new_password = request.form['password']  # Nueva contraseña
        business_layer.update_password(password_id, new_password)  # Actualiza en la base de datos
        return redirect('/')
    else:
        # Obtiene la contraseña actual para mostrar en el formulario
        passwords = business_layer.get_passwords()
        password = next((p for p in passwords if p['id'] == password_id), None)
        return render_template('update.html', password=password)

@app.route('/delete/<int:password_id>')
def delete(password_id):
    business_layer.delete_password(password_id)
    return redirect('/')
