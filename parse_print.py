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