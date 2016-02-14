#!/bin/bash

tens=`find . -name "10.pgm"`
for f in $tens
do
	newfile=`sha256sum ${f} | awk '{print $1}'`
	echo $newfile
	cp $f ./10th_face_of_all/$newfile
done

