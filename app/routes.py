from flask import Flask, render_template, request

app = Flask(__name__)
user_data = []

@app.route('/', methods=['GET', 'POST'])


def index():
    if request.method == 'POST':
        # Получение данных из формы
        name = request.form.get('name')
        city = request.form.get('city')
        hobby = request.form.get('hobby')
        age = request.form.get('age')

        user_data.append({
            'name': name,
            'city': city,
            'hobby': hobby,
            'age': age
        })

    return render_template('blog.html', user_data=user_data)
