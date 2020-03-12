import os
from os import path
from wordcloud import WordCloud
# from matplotlib import pyplot as plt

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

# 获取当前文件路径
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
for i in len(file_pth):
    # 获取文本text
    text = open(path.join(d,file_pth[i])).read()
    # 生成词云
    wc = WordCloud(scale=2,max_font_size = 100)
    wc.generate_from_text(text)
    # 显示图像
    plt.imshow(wc,interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout()
    # 存储图像
    wc.to_file(str(i) + '.png')
# or
# plt.savefig('1900_basic.png',dpi=200)
# plt.show()