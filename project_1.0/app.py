from flask import Flask, render_template, request
import hashlib as h

# print(__name__)

app = Flask(__name__)

def hashing(origin_str, num_char):
    """
    Функция шифрования (хеширования)
    """
    # строка пароли
    # origin_str = pwd.get()

    # кодирование в байт-строку
    byte_str = origin_str.encode()
    # шифрование - пропускание байт-строки через хеш-функция
    hash_str = h.sha256(byte_str)
    # преобразование в строку шестнадцатеричного числа (hex-числа)
    
    if num_char == '-':
        hex_str = hash_str.hexdigest()
    else:
        hex_str = hash_str.hexdigest()[:int(num_char)]

    # # передача хеш-строки
    # pwd_hash.set(hex_str)

    return hex_str

@app.route('/')
def index_page():
    return render_template(
        "index.html",
        the_title="My Site"
    )

# @app.route('/product')
@app.route('/product', methods=['post', 'get'])
def product_page():
    # return render_template(
    #     "product.html",
    #     the_title="My Site"
    # )

    message = ''
    if request.method == 'POST':
        site = request.form.get('site')  # запрос к данным формы
        password = request.form.get('password')
        num_char = request.form.get('num_char')

        message = hashing(password + site, num_char)

    return render_template('product.html', message=message)

@app.route('/contact')
def contact_page():
    return render_template(
        "contact.html",
        the_title="My Site"
    )

if __name__ == "__main__":
    app.run(debug=True)