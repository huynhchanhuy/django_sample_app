from base import *

try:
	from local import *
except:
	pass

try:
	from production import *
except Exception as e:
	print e
pass