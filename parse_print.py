# -*- coding: utf-8 -*-
#!/usr/bin/env python

# Печать словаря в строку
d = dict(a=2, b=3, complexField={2: 3, 9: 3})
s = "%s" % d
print s

# Разбор XML строки
xml = """<foo>
   <bar>
      <type foobar="1"/>
      <type foobar="2"/>
   </bar>
</foo>"""

import xml.etree.ElementTree as ET

foo = ET.fromstring(xml)
print foo.tag  # foo

for bar in foo:
    print bar.tag  # bar
    for typeElement in bar:
        print typeElement.tag  # type
        print typeElement.attrib['foobar']  # 1 2

# Проверка поведения ElementTree, когда в строке не XML
try:
    res = ET.fromstring("This is test string")
except ET.ParseError:
    print "Это не XML!"


class Result:
    id, code, comment = None, None, None

    def __init__(self, xml):
        """ Разбор XML """
        for child in ET.fromstring(xml):
            setattr(self, child.tag, child.text)


xml = """<?xml version="1.0" encoding="UTF-8"?>
<result>
  <id>0</id>
  <code>NO</code>
  <comment>-3 NO_DOG_NUMBER</comment>
</result>"""
result = Result(xml)
print result.id
print result.code
print result.comment
