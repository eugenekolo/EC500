#!/usr/bin/python
"""
Predicts to whom a face image belongs to using Eigenfaces algorithm.
Call the script with "--help" for help.
The csv's you feed it must be properly set up. Use the script faces_to_csv.py for this.
Or take a look at /assets/all_faces.csv for an idea of what it's supposed to look like.

Example1: ./eigenface_recognizer.py --training_csv ../assets/all_faces.csv --ratio .5
[*] TRAINING: 200 images from 200 IDs.
[*] TESTING: 200 images from 200 IDs.
[*] We matched 90% correctly

Example2:
./eigenface_recognizer.py --training_csv ../assets/all_faces.csv --ratio .9
[*] TRAINING: 40 images from 40 IDs.
[*] TESTING: 360 images from 360 IDs.
[*] We matched 42% correctly
"""

import cv2
import cv2.face as cv2face
import numpy
import sys
import random
import math
import csv
import pprint
import argparse
from collections import defaultdict
from PIL import Image

def ascii_art(f):
    ASCII_CHARS = [ '#', '?', '%', '.', 'S', '+', '.', '*', ':', ',', '@']
    WIDTH = 50
    QUANT = 25

    ## Open, scale, convert to grayscale
    img = Image.open(f)
    (original_width, original_height) = img.size
    aspect_ratio = original_height/float(original_width)
    new_height = int(aspect_ratio * WIDTH)
    img = img.resize((WIDTH, new_height))
    img = img.convert('L')

    ## Convert the pixels to ASCII quantizations
    pixels_in_image = list(img.getdata())
    pixels_to_chars = [ASCII_CHARS[pixel_value/QUANT] for pixel_value in pixels_in_image]
    pixels_to_chars = "".join(pixels_to_chars)
    len_pixels_to_chars = len(pixels_to_chars)
    image_ascii = [pixels_to_chars[index: index + WIDTH] for index in xrange(0, len_pixels_to_chars, WIDTH)]

    return image_ascii

def print_results(ascii=False):
    fmt = '{:<50}{:<10}{:<50}'
    for (predicted, actual) in zip(ascii_art(csvrow['path']), ascii_art(csvrow['path'])):
        print(fmt.format(left, '', right))


def split_test_training_data(data, ratio=0.2):
    """ Split a list of image files by ratio of training:test data """
    test_size = int(math.floor(ratio*len(data)))
    random.shuffle(data)
    return data[test_size:], data[:test_size]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--training_csv', required=True,
        help='Input CSV to train face recognition on. Required.')
    parser.add_argument('--testing_csv', default=None,
        help='Testing CSV to test the face recognition model on. Either this xor ratio is required.')
    parser.add_argument('--ratio', default=None, type=float,
        help='Take random faces based on the ratio from the training_csv to be used for testing and not training.'
        'Either this xor testing_csv is required.')
    parser.add_argument('--ascii', default=False, action='store_true',
        help='Print ascii images of the results!.')
    args = parser.parse_args()

    if not (args.testing_csv or args.ratio):
        parser.error('No clue how to test, add --ratio or --testing_csv')
    if (args.testing_csv != None and args.ratio != None):
        parser.error('Choose one, either --ratio or --testing_csv')

    training_csv = args.training_csv
    testing_csv = args.testing_csv
    ratio = args.ratio
    yesascii = args.ascii

    ## Read in the images into a dict that is: path -> img, id
    trainingdict = {}
    with open(training_csv, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for csvrow in csvreader:
            img = cv2.imread(csvrow['path'], cv2.IMREAD_GRAYSCALE)
            trainingdict[csvrow['path']] = (img, int(csvrow['id']))

    TOTAL_IMAGES = len(trainingdict)

    ## Read in the testing data into a dict that is: path -> img, id
    testingdict = defaultdict(list)
    if testing_csv:
        with open(testing_csv, 'r') as csvfile:
            csvreader = csv.DictReader(csvfile)
            for csvrow in csvreader:
                img = cv2.imread(csvrow['path'], cv2.IMREAD_GRAYSCALE)
                testingdict[csvrow['path']] = (img, int(csvrow['id']))
    elif ratio:
        ## Separate some images, to be used for testing. Do not train on them.
        testsize = int(math.floor(ratio*TOTAL_IMAGES))
        for i in range(testsize):
            randpath = random.choice(trainingdict.keys())
            randimage = trainingdict[randpath][0]
            randid = trainingdict[randpath][1]  
            testingdict[randpath] = (randimage, randid)
            trainingdict.pop(randpath, None)


    ## Train Eigenfaces, by feeding it face data
    trainingimgs, trainingids = zip(*trainingdict.values()) 
    testingimgs, testingids = zip(*testingdict.values()) 
    model = cv2face.createEigenFaceRecognizer()
    model.train(numpy.array(trainingimgs), numpy.array(trainingids))

    ## Test our model and see how accurate we are
    correct = 0
    iscorrect = False
    for path,x in testingdict.iteritems():
        img = x[0]
        actualid = x[1]
        predictionid = model.predict(numpy.array(img))
        if predictionid == actualid: # We got it!
            correct += 1
            iscorrect = True
        else: # Dang it!
            predictionpath = "" # BUG: If no id is found, cause they all went into testing, this will fail.
            for path2,x2 in trainingdict.iteritems():
                if x2[1] == actualid:
                    predictionpath = path2
                    break
            if yesascii:
                fmt = '{:<50}{:<10}{:<50}'
                print(fmt.format("Predicted " + str(predictionid) + " " + predictionpath, "", "Actual " + str(actualid) + " " + path))
                for (predictionimg, actualimg) in zip(ascii_art(predictionpath), ascii_art(path)):
                    print(fmt.format(predictionimg, '', actualimg))
                print("\n\n")
            else:
                pass
               # TODO
               # Python imaging is uuuuugh

    ## Print some data
    TRAINING_IMAGES = len(trainingimgs)
    TRAINING_IDS = len(trainingids)
    TESTING_IMAGES = len(testingimgs)
    TESTING_IDS = len(testingids)
    print("[*] TRAINING: {} images from {} IDs.".format(TRAINING_IMAGES, TRAINING_IDS))
    print("[*] TESTING: {} images from {} IDs.".format(TESTING_IMAGES, TESTING_IDS))
    print("[*] We matched {}% correctly".format(100*correct/(TESTING_IMAGES)))

