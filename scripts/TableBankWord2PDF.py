import os

import docx2pdf
from shutil import copyfile
from util import StorageUtil

f = []
for dirpath, subdirs, files in os.walk("../data/tablebank/Detection_data/Word/word/"):
    for x in files:
        file_w = "../data/tablebank/Detection_data/Word/word/" + x
        file_p = "../data/tablebank/Detection_data/Word/pdf_complete/" + StorageUtil.cut_file_type(x) + ".pdf"
        print(file_p)
        if not os.path.exists(file_p):
            copyfile(file_w, "test.docx")
            docx2pdf.convert("test.docx", file_p)