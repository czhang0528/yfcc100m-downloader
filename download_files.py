#!/usr/bin/env python3

import os
import urllib.request
from xml.dom.minidom import parse

def collect_index_files(path):
    for root, subdirs, files in os.walk(path):
        file_path = os.path.join(root, "index.xml")
        if os.path.exists(file_path):
            yield file_path

def download(path):
    url = "https://multimedia-commons.s3-us-west-2.amazonaws.com/" + path
    print("Download " + url)
    urllib.request.urlretrieve (url, path)

def ensure_file_is_downloaded(path):
    if not os.path.isfile(path):
        download(path)

def ensure_files_are_downloaded(path):
    for path in paths:
        ensure_file_is_downloaded(path)

def extract_image_paths(index_files):
    for index_path in index_files:
        doc = parse_file(index_path)
        for content in doc.getElementsByTagName("Contents"):
            image_path = content.getElementsByTagName("Key")[0].firstChild.data
            yield image_path

def parse_file(path):
    datasource = open(path)
    return parse(datasource)

index_files = collect_index_files("data")
paths = extract_image_paths(index_files)
ensure_files_are_downloaded(paths)
