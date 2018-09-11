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

	def createCell(self, sceneCell):
	    """
	    创建cell部分
	    :param sceneCell:场景的cellEntityCall
	    """
	    # API：创建该实体的cell部分
	    self.createCellEntity(sceneCell)

    def hello(self, exposed, content):
        """
        接受客户端hello的指令
        :param exposed: 调用者的id
        :param content: hello的内容
        :return:
        """
        sender_entity = KBEngine.entities[exposed]
        if sender_entity is None:
            ERROR_MSG("FirstEntity[%i]:: can not find sender with exposedvalue=[%i]!" % (self.id, exposed))
            return

        INFO_MSG("FirstEntity[%i]::Hello %s[%i]! I'm in space[%i]. I got your content=%s" % (
            self.id, sender_entity.__class__.__name__, sender_entity.id, self.spaceID, content))


