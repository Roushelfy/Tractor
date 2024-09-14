import os
from lxml import etree

# 指定SVG文件所在的目录
directory = 'img\svg_front'  # 替换为你自己的SVG目录


# 旋转SVG的函数
def rotate_svg(svg_file):
    # 解析SVG文件
    parser = etree.XMLParser(remove_blank_text=True)
    tree = etree.parse(svg_file, parser)
    root = tree.getroot()

    # 为根元素设置旋转变换
    transform = root.attrib.get('transform', '')
    transform += ' rotate(90 0 0)'
    root.attrib['transform'] = transform.strip()

    # 保存修改后的SVG文件，覆盖原文件
    tree.write(svg_file,
               pretty_print=True,
               xml_declaration=True,
               encoding='utf-8')


# 遍历指定目录中的所有SVG文件
for filename in os.listdir(directory):
    if filename.endswith('.svg'):
        svg_path = os.path.join(directory, filename)
        rotate_svg(svg_path)
        print(f'{filename} 已旋转 90 度')

print("所有SVG文件已旋转 90 度")
