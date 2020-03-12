import os
from os import path
import xlwt

file_pth = ['./cloudmap_doc_pre/hairDryer_mid_content_text.txt',\
            './cloudmap_doc_pre/hairDryer_mid_title_text.txt',\
            './cloudmap_doc_pre/hairDryer_neg_title_text.txt',\
            './cloudmap_doc_pre/hairDryer_pos_content_text.txt',\
            './cloudmap_doc_pre/hairDryer_pos_title_text.txt',\
           './cloudmap_doc_pre/microwave_mid_content_text.txt',\
            './cloudmap_doc_pre/microwave_mid_title_text.txt',\
            './cloudmap_doc_pre/microwave_neg_title_text.txt',\
            './cloudmap_doc_pre/microwave_pos_content_text.txt',\
            './cloudmap_doc_pre/microwave_pos_title_text.txt',\
            './cloudmap_doc_pre/pacifier_mid_content_text.txt',\
            './cloudmap_doc_pre/pacifier_mid_title_text.txt',\
            './cloudmap_doc_pre/pacifier_neg_title_text.txt',\
            './cloudmap_doc_pre/pacifier_pos_content_text.txt',\
            './cloudmap_doc_pre/pacifier_pos_title_text.txt']

workbook = xlwt.Workbook()
# 获取当前文件路径
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
for i in range(len(file_pth)):
    # 获取文本text
    text = open(path.join(d,file_pth[i])).read()
    text = text.split()
#     print(len(text))
    count = {}
    for word in text:
        count[word] = count.get(word, 0) + 1
    iteams = list(count.items())
#     print(iteams) # iteams - list
#     print(len(iteams))
    sheet = workbook.add_sheet(str(i), cell_overwrite_ok=True)
    for word in range(len(iteams)):
        sheet.write(word, 0, iteams[word][0])
        sheet.write(word, 1, iteams[word][1])

file_name = 'word_freq.xls'
workbook.save(file_name)
        