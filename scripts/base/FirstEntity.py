# -*- coding: utf-8 -*-

import KBEngine
from KBEDebug import *

class FirstEntity(KBEngine.Entity):
	"""
	第一个实体的base部分的实现
	"""
	def __init__(self):
		KBEngine.Entity.__init__(self)


	def hello(self, content):
		"""
		hello 方法
		"""
		INFO_MSG("Hello ComblockEngine! I'm %s. I got your content=%s" % (self.name, content))
		