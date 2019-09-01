#/usr/bin/env python3.5
#-*- coding:utf-8 -*- 

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>Hello World!</h1><img src="https://ww.namu.la/s/1d7681d48a6e825f33a7589000651705a33b4b06f3322735474f5278b1fae7ce1a4180e3deda02e70e428c0c34f03b6c071522e08f1022998a369ed41a08aa952341a473f76e8ec3e20d4f7563c7c74797c9dd0be050e140e334978bef5f8022">'

if __name__ == "__main__":
	app.run()

