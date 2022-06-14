import os
from PIL import Image

# 
root = ''
files = [root + f for f in os.listdir(root) if os.path.isdir(root + f)]

for i in range(len(files)):
    pdf_path = root + files[i].split('/')[-1] + '.pdf'
    print(pdf_path, end='')

    # get file name list sorted
    img_path_list = sorted([
        files[i] + '/' + f
        for f in os.listdir(files[i])
        if '.png' in f  # 이미지 파일이 아닌 파일이 포함되는 것을 방지
    ])

    images = [
        Image.open(img)
        for img in img_path_list
    ]

    # Solve "ValueError: cannot save mode RGBA"
    backgrounds = []
    for image in images:
        image.load()  # required for image.split()
        background = Image.new("RGB", image.size, (255, 255, 255))
        background.paste(image, mask=image.split()[3])
        backgrounds.append(background)

    backgrounds[0].save(
        pdf_path, "PDF", resolution=100.0, save_all=True, append_images=backgrounds[1:])

    print(' saved')
