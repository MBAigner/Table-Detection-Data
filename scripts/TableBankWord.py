import pandas as pd
import urllib
import os
import signal

gt_subset = pd.read_csv("../data/tablebank/Detection_data/gt_5000.csv", sep=";", index_col=0)


def get_file_name(url):
    parts = url.split("/")
    return parts[len(parts)-1]


def conv_url(link):
    p = link.split("/")
    return p[len(p) - 1]


def replace_file_type(file_name, new_type):
    file_name_parts = file_name.split(".")
    return file_name.replace(file_name_parts[len(file_name_parts) - 1], new_type)


def handler(signum, frame):
    raise Exception("failed")


def get_files_word3(url_row):
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(5)
    name_w = conv_url(url_row["url"])
    file_w = "../data/tablebank/Detection_data/Word/word/" + name_w
    try:
        if not os.path.exists(file_w):
            data = urllib.request.urlretrieve(url_row["url"], file_w)
        print(file_w + " done")
    except Exception as e:
        print(file_w + " failed")
        print(e)


word_links = pd.read_csv("../data/tablebank/Detection_data/Word/url.csv", sep=",")
word_links = word_links[word_links["image_name"].isin(gt_subset["file"].apply(lambda x: get_file_name(x)))]
word_links.apply(lambda x: get_files_word3(x), axis=1)
