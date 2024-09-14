import os
from PIL import Image

# 指定图片目录
directory = 'img/back'  # 替换为你的图片所在目录

# 遍历目录中的所有文件
for filename in os.listdir(directory):
    if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):  # 支持的图片格式
        img_path = os.path.join(directory, filename)
        # 打开图片
        with Image.open(img_path) as img:
            # 旋转图片 90 度
            rotated_img = img.rotate(-90, expand=True)
            # 保存旋转后的图片，覆盖原文件
            rotated_img.save(img_path)

        print(f'{filename} 已旋转 90 度')

print("图片旋转完成！")
