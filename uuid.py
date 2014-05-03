#!/usr/bin env python
#-*- encoding gb2312 -*-

import uuid

print uuid.uuid1()
print uuid.uuid3(uuid.NAMESPACE_DNS,'testme')
print uuid.uuid4()
print uuid.uuid5(uuid.NAMESPACE_DNS,'testme')

