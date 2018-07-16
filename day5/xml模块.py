# !/usr/bin/env python
# _*_ coding:utf-8 _*_

# import xml.etree.ElementTree as ET
# tree = ET.parse("xmltest.xml")
# root = tree.getroot()
# print(root.tag)
#
# for child in root:
#     print(child.tag, child.attrib)
#
# for node in root.iter("year"):
#     print(node.tag, node.text)

#
# import xml.etree.ElementTree as ET
# tree = ET.parse("xmltest.xml")
# root = tree.getroot()
# 修改内容
# for node in root.iter("year"):
#     node_year = int(node.text) + 1
#     node.text = str(node_year)
#     node.set("node.text", "yes")
#
# tree.write("xmltest.xml")

# 删除内容
# for country in root.findall("country"):
#     rank = int(country.find("rank").text)
#     if rank > 50:
#        root.remove(country)
#
# tree.write("xmltest.xml")

# 创建xml
import xml.etree.ElementTree as ET

new_xml = ET.Element("namelist")
person_info = ET.SubElement(new_xml, "person_info", attrib = {"enrolled":"yes"})
name = ET.SubElement(person_info, "name")
name.text = "yanzhuang"
age = ET.SubElement(person_info, "age", attrib = {"checked":"no"})

sex = ET.SubElement(person_info, "sex")

sex.text = "33"

person_info2 = ET.SubElement(new_xml,"person_info", attrib={"enrolled":"no"})
name = ET.SubElement(person_info2, "name")
name.text = "lvsixian"
age = ET.SubElement(person_info2, "age")
age.text = "19"

et = ET.ElementTree(new_xml)
et.write("test.xml", encoding="utf-8", xml_declaration=True)

ET.dump(new_xml)
