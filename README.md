# py-webprinter-demo

用到的打印机是GP-58系列,使用了pyusb 和 python-escpos 库
网页端还是flask
缺什么自己装

## 还是写下安装说明吧
### 树莓派
```
sudo pip3 install python-escpos pyusb
```
即可

### 香橙派
```
apt-get install python3-pip
pip3 install flask
pip3 install pyserial
pip3 install qrcode
apt-get install python3-pil
```

默认图片搜索目录为 /home/pi/print,请自行修改或创建该目录

### 安装完成后运行python3 print.py即可
