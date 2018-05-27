"""
I'm expecting you have openCV, numpy, and pandas
since you're about to run some ML algorithms that requires most of them.

If you've run this script before, then I will be producing a script to look
through all the subdirectories and restore the files to their original location.
"""
from cv2 import imread
from lxml import etree, objectify
from os import path, mkdir, remove,system
import os
from shutil import rmtree, copyfile

from file_helper import read_lines, safe_remove, write_line, read_content


def label2xml(list_path, category_id, ANN_DIR='data/Annotations/', IMG_DIR='data/images/', SET_DIR='data/ImageSets/',
              train=True, start_img_cnt=0):
    set_file_list = [SET_DIR + 'train.txt', SET_DIR + 'minival.txt', SET_DIR + 'testdev.txt', SET_DIR + 'test.txt']
    TYPEPREFIX = 'train' if train else 'val'
    lines = read_lines(list_path)
    line_i = 0
    last_name = ''
    E = None
    img_annotation = None
    image_file = None
    while line_i < len(lines):
        line = lines[line_i]
        infos = line.split()
        image_path = infos[0]
        box = infos[1:]
        imagename = int(image_path.split('.')[0].split('/')[-1])
        dir_num = int(image_path.split('.')[0].split('/')[-2][-5:])
        target_name = '%05d%04d' % (dir_num, imagename)

        print('last_path: %s, image_path: %s' % (last_name, image_path))
        if last_name != target_name:
            if train:
                write_line(set_file_list[0], "%s.jpg %s.xml" % (target_name, target_name))
            else:
                for i in range(1, 4):
                    write_line(set_file_list[i], "%s.jpg %s.xml" % (target_name, target_name))
            if last_name != '':
                xml_pretty = etree.tostring(img_annotation, pretty_print=True)
                with open(ANN_DIR + last_name + ".xml", 'wb') as ann_file:
                    ann_file.write(xml_pretty)
            image_file = imread(image_path)
            copyfile(image_path, IMG_DIR + '%s.jpg' % target_name)
            if path.exists(ANN_DIR + "%s.xml" % target_name):
                E = objectify.ElementMaker(annotate=False)
                img_annotation = objectify.fromstring(read_content(ANN_DIR + target_name + ".xml"))
            else:
                E = objectify.ElementMaker(annotate=False)
                img_annotation = E.annotation(
                    E.folder(TYPEPREFIX),
                    E.filename(target_name),
                    E.source(
                        E.database('coco_cattle'),
                    ),
                    E.size(
                        E.width(image_file.shape[1]),
                        E.height(image_file.shape[0]),
                        E.depth(3),
                    ),
                    E.segmented(0)
                )

            last_name = target_name
        objectNode = E.object(
            E.name(str(category_id)),
            E.pose("Unspecified"),
            E.truncated("0"),
            E.difficult("0"),
            E.bndbox(
                E.xmin(str(int(float(box[0]) * image_file.shape[1]))),
                E.ymin(str(int(float(box[1]) * image_file.shape[0]))),
                E.xmax(str(int(float(box[2]) * image_file.shape[1]))),
                E.ymax(str(int(float(box[3]) * image_file.shape[0]))),
            ),
        )
        img_annotation.append(objectNode)
        line_i += 1


def cattle_ssd_prepare(ANN_DIR='data/Annotations/', IMG_DIR='data/images', SET_DIR='data/ImageSets/', force=True):
    set_file_list = [SET_DIR + 'train.txt', SET_DIR + 'minival.txt', SET_DIR + 'testdev.txt', SET_DIR + 'test.txt']
    if force:
        if os.path.exists(IMG_DIR):
            rmtree(IMG_DIR)
            mkdir(IMG_DIR)
        else:
            mkdir(IMG_DIR)
        if os.path.exists(ANN_DIR):
            rmtree(ANN_DIR)
            mkdir(ANN_DIR)
        else:
            mkdir(ANN_DIR)
        if os.path.exists(SET_DIR):
            rmtree(SET_DIR)
            mkdir(SET_DIR)
        else:
            mkdir(SET_DIR)

        for set_file in set_file_list:
            safe_remove(set_file)
    label2xml('data/animal_box.txt', 21, train=True)
    label2xml('data/hard_body.txt', 19, train=True)
    label2xml('data/hard_body_part.txt', 19, train=True)
    label2xml('data/hard_head.txt', 21, train=True)
    label2xml('data/hard_head_part.txt', 21, train=True)
    label2xml('data/oid_cattle.txt', 21, train=True)
    # label2xml('data/oid_cattle_full.txt', 21, train=True)
    label2xml('data/oid_cattle.txt', 21, train=False)
    # system('./data2example.sh')


if __name__ == '__main__':
    cattle_ssd_prepare(force=True)
