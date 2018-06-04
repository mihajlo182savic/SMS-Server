from flask import Flask, render_template, request, redirect
import RPi.GPIO as GPIO
import time as t
import os 

os.system("sudo service start motion")


ad = Flask(__name__)




if __name__ == '__main__':
	

	ad.run(debug=True,threaded=True, host='192.168.44.15')