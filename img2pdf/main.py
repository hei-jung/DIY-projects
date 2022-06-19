from pdf_generator import pdf_generator

if __name__ == '__main__':
    img_path = input('변환할 이미지 폴더 경로\n>> ')
    pdf_path = input('저장할 파일명\n>> ')
    if not pdf_path.endswith('.pdf'):
        pdf_path += '.pdf'
    pdf_generator(img_path, pdf_path)
