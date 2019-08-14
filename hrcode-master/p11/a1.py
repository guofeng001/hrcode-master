import xml.etree.ElementTree as ET

tree = ET.parse('../p11/data.xml')
print(tree)
root = tree.getroot()
print(root[0])  # 标签为L的元素 <Element 'L' at 0x02639360>
for i in range(len(root[0])):
    data = root[0][i]
    print(data)  # 输出元素 <Element 'd' at 0x020B94B0>
    onedict = data.attrib  # {'name': 'Mike', 'age': '10'}
    name = onedict['name']  # 姓名
    age = onedict['age']  # 年龄
    print(name, age)
