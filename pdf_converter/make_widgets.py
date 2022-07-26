import tkinter as tk
from tkinter import filedialog
from functools import partial
from pdf_generator import pdf_generator
from tkinter import messagebox  # 코드 잘못됐을 때 에러창 띄우려고


def add_path(app, event):
    file_names = list(filedialog.askopenfilenames(initialdir='./png', title='파일선택', filetypes=(
        ('png files', '*.png'), ('jpg files', '*.jpg'), ('all files', '*.*'))))
    for file_name in file_names:
        app.listbox.insert("end", file_name)


def del_path(app, event):
    selected = app.listbox.curselection()
    for checkbox in selected[::-1]:
        app.listbox.delete(checkbox)


def display(app, event):
    try:
        i = app.listbox.curselection()[0]
    except IndexError:
        messagebox.showinfo(title="선택된 이미지가 없음", message="이미지를 먼저 추가해주세요.")
        return -1
    file_name = app.listbox.get(i)
    app.img = tk.PhotoImage(file=file_name)
    app.img = app.img.subsample(8, 8)
    app.img_viewer["image"] = app.img


def to_pdf(app, event):
    images = list(app.listbox.get(0, app.listbox.size() - 1))
    file_name = filedialog.asksaveasfilename(initialdir='', title='파일저장',
                                             filetypes=(('pdf file', '*.pdf'), ('all files', '*.*')))
    return_code = pdf_generator(img_path_list=images, pdf_path=file_name)
    if return_code == 0:
        messagebox.showinfo(title="PDF 변환 성공!", message=f"{file_name} 파일이 저장되었습니다.")
    else:
        messagebox.showinfo(title="PDF 변환 실패", message="파일 저장에 실패했습니다.")


def make(app):
    # 경로 선택 frame
    app.path_frame = tk.LabelFrame(app.sub_fr, text="Images")
    app.path_frame.pack(pady=20)

    # listbox & button 묶는 frame
    app.list_btn_frame = tk.Frame(app.path_frame)
    app.list_btn_frame.pack(side="left")

    # listbox frame
    app.listbox_frame = tk.Frame(app.list_btn_frame)
    app.listbox_frame.pack()

    # button frame
    app.btn_frame = tk.Frame(app.list_btn_frame)
    app.btn_frame.pack()

    # 이미지 미리보기 frame
    app.img_frame = tk.Frame(app.path_frame)
    app.img_frame.pack(side="left")

    # 항목 리스트
    app.listbox = tk.Listbox(app.listbox_frame, selectmode='extended', width=50, height=20)
    app.listbox.pack(side="left", expand=True, padx=10, pady=10, ipady=5)

    # 스크롤바
    app.scrollbar = tk.Scrollbar(app.listbox_frame, orient="vertical")
    app.scrollbar.config(command=app.listbox.yview)
    app.scrollbar.pack(side="left", fill="y")
    app.listbox.config(yscrollcommand=app.scrollbar.set)

    # 이미지 미리보기
    app.img = tk.PhotoImage(file="")
    app.img_viewer = tk.Label(app.img_frame, image=app.img, width=400, height=200)
    app.img_viewer.pack()

    # 항목 추가 버튼
    app.btn_add = tk.Button(app.btn_frame, width=10, font=80, text='이미지 추가')
    app.btn_add.pack(side="left", expand=True, padx=1, pady=5, ipady=5)
    app.btn_add.bind('<Button-1>', partial(add_path, app))

    # 이미지 보기 버튼
    app.btn_img = tk.Button(app.btn_frame, width=10, font=80, text='선택 항목 미리보기')
    app.btn_img.pack(side="left", expand=True, padx=1, pady=5, ipady=5)
    app.btn_img.bind('<Button-1>', partial(display, app))

    # 항목 삭제 버튼
    app.btn_delete = tk.Button(app.btn_frame, width=10, font=80, text='선택 항목 삭제')
    app.btn_delete.pack(side="left", expand=True, padx=1, pady=5, ipady=5)
    app.btn_delete.bind('<Button-1>', partial(del_path, app))

    # PDF 변환 버튼
    app.btn_pdf = tk.Button(app.sub_fr, width=10, font=80, text="PDF 변환")
    app.btn_pdf.pack(side="top", anchor="e", expand=True, padx=10, pady=5, ipady=5)
    app.btn_pdf.bind('<Button-1>', partial(to_pdf, app))
