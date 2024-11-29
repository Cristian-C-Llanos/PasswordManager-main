from flask import Flask, render_template, request, redirect, url_for
from business_layer import BusinessLayer

app = Flask(__name__, template_folder="templates")
business_layer = BusinessLayer()

@app.route('/')
def index():
    passwords = business_layer.get_passwords()
    return render_template('index.html', passwords=passwords)

@app.route('/add', methods=['GET', 'POST'])
def add_password():
    if request.method == 'POST':
        service = request.form['service']
        username = request.form['username']
        password = request.form['password']
        business_layer.add_password(service, username, password)
        return redirect(url_for('index'))
    return render_template('add_password.html')

@app.route('/delete/<int:password_id>')
def delete_password(password_id):
    business_layer.delete_password(password_id)
    return redirect(url_for('index'))

@app.route('/update/<int:password_id>', methods=['GET', 'POST'])
def update_password(password_id):
    if request.method == 'POST':
        new_password = request.form['password']
        business_layer.update_password(password_id, new_password)
        return redirect(url_for('index'))
    return render_template('update_password.html', password_id=password_id)

if __name__ == '__main__':
    app.run(debug=True)
