#encoding:utf-8
from flask import Flask
from flask import request
from flask import render_template,redirect,url_for
from escpos import printer 
from escpos.printer import Dummy
import os

app = Flask(__name__)

pic_dir = '/home/pi/print'
filter = ['.png','.jpg','jpeg','.JPG','.PNG','JPEG','.bmp','.BMP','.gif','.GIF']

def get_items(dir,filter):
	result = []
	files = os.listdir(dir)
	for file in files:
		if os.path.isdir(dir + '/' + file):
			temp=get_items(dir + '/' + file,filter)
			if temp:	result.extend(temp)
		elif file[-4:] in filter :       
			result.append(dir + '/' + file)
	result.sort()
	return result

def get_pictures():
	global filter
	return get_items(pic_dir,filter)

def pr(content,type):
	p = printer.File("/dev/usb/lp0")
	d = Dummy()
	endl = bytes('\n','ascii')
	d.set(align=u'left', font=u'a', text_type=u'normal', width=2, height=2, density=9, invert=False, smooth=False, flip=False)
	if type == 'text':
		d._raw(bytes(content,'gbk'))
#	p.device.flush()
	if type == 'qr':
		d.qr(content, ec=0, size=7, model=2, native=False)
	if type == 'file':
		if content[-4:] in filter:
			d.image(content)
	if type == 'barcode':
		d.barcode(content,'EAN13',64,2,'','') 
	p._raw(d.output+endl)
@app.route('/')
def index():
#	return "hello"
	imgs = get_pictures()
	return render_template('printer.html',imgs = imgs)

@app.route('/print')
def printing():
	print(request.form)
	content = request.args.get('content')
	type = request.args.get('cmd')
	print( content + type)
	if content and type:
		pr(content,type)
	imgs = get_pictures()
	msg = '已发出打印请求'
	return redirect(url_for('index')) 
#pr('测试','text')
if __name__ == '__main__':
    app.run("0.0.0.0",debug=True)

