import os
from PIL import Image


def pdf_generator(img_folder_path, pdf_path):
    print(pdf_path)
    img_path_list = sorted([
        img_folder_path + '/' + f
        for f in os.listdir(img_folder_path)
    ])

    # 이미지 불러오기
    images = []
    for img in img_path_list:
        # 이미지 파일이 아닌 파일이 포함되는 것을 방지
        try:
            images.append(Image.open(img))
        except Exception as e:
            continue

    try:
        images[0].save(pdf_path, "PDF", resolution=100.0, save_all=True, append_images=images[1:])
    except Exception as e:
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
