from flask import Flask, render_template
from env import JUN09TOOl
from proctitle import setproctitle

setproctitle.setproctitle(JUN09TOOl.PROC_NAME)

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def main():
    nav_item = (
        "장원툴", "대리점", "온라인 스토어", "매장위치", "문의하기"
    )
    return render_template('index.html', nav_item=nav_item)

@app.route('/volunteer_jang')
def volunteerjang():
    return render_template('volunteerjang.html')


if __name__ == '__main__':
    app.run('0.0.0.0', debug=JUN09TOOl.DEBUG, port=JUN09TOOl.PORT)
