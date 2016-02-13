#!/usr/bin/python

import cv2
import cv2.face as cv2face
import numpy
import sys
import random
import math
import csv

def create_and_train_model_from_dict(label_matrix):
    """ Create eigenface model from dict of labels and images """
    model = cv2.createEigenFaceRecognizer()
    model.train(label_matrix.values(), numpy.array(label_matrix.keys()))
    return model


def split_test_training_data(data, ratio=0.2):
    """ Split a list of image files by ratio of training:test data """
    test_size = int(math.floor(ratio*len(data)))
    random.shuffle(data)
    return data[test_size:], data[:test_size]

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Enter a <training_csv> that has a list of faces in the format 'file_path, id'")
        print("Enter the number of faces you want to be taken out randomly and test against")
        print("usage: {} <training_csv> <ratio>".format(sys.argv[0]))
        sys.exit(1)

    print("Running on " + cv2.__version__)
    training_csv = sys.argv[1]
    #testing_csv = sys.argv[2]
    ratio = sys.argv[2]

    ## Read in the images into a dictionarhy that is 'id -> gray scale image data'
    ## Separate some images, to be used for testing. Do not train on them.
    facedict = {}
    with open(training_csv, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for csvrow in csvreader:
            img = cv2.imread(csvrow['path'], cv2.IMREAD_GRAYSCALE)
            facedict[int(csvrow['id'])] = img

    ## Train Eigenfaces, by feeding it the bulk of the faces. But not all of them
    model = cv2face.createEigenFaceRecognizer()
    model.train(facedict.values(), numpy.array(label_matrix.keys()))

    ## Test our model and see how accurate we are
    #for line in testing_csv:
    #    filename, label =  line.strip().split(';')
    #    image = read_matrix_from_file(filename)
    #    prediction = model.predict(image)
    #    print 'Predicted: %(predicted)s  Actual: %(actual)s' %  {"predicted": predicted_label[0], "actual": label}
