#!/usr/bin/env bash

# This file might change for different assignments.
# This file is stored in the assignemnt repo.

# Set up autograder files

# List the files you expect the student to submit. Only these
# will be copied from the student submission into the space where the assignment is graded.
# The student submission is a collection of files in a particular folder structure.
# The EXPECTED_FILES should be be in $SUBMISSION_SOURCE (often /autograder/submission).
# QUESTION: Can the expected files be of the form: src/labxx.py, for example?

# Install utilities that allow the creation of results.json and allow decorators
#if [ -d pytest_utils ]; then
#    cd pytest_utils
#    git pull origin master
#else
#    git clone https://github.com/ucsb-gradescope-tools/pytest_utils.git
#    cd pytest_utils
#fi

cd pytest_utils
pip3 install -e .
cd ..


SUBMISSION_SOURCE=/autograder/submission

if [ -d $SUBMISSION_SOURCE ]; then
   echo "Checking submission from $SUBMISSION_SOURCE"
else
   echo "ERROR: $SUBMISSION_SOURCE does not exist"
   exit
fi

list_files_from_dir () {
    echo "\n==> list_files_from_dir $1"
    echo `ls -R $1`
}

copy_files_from_dir_if_it_exists () {
    echo "\n==> copy_files_from_dirs $1"
    if [ -d $1 ]; then
        cp -rv $1/* .
    else
    echo "   Folder does not exist"
    fi
}


echo "==> pwd"; echo `pwd`
echo ""; echo "pwd(.): `pwd`"; list_files_from_dir .
echo "";                       list_files_from_dir ..
echo ""; list_files_from_dir /autograder/submission
echo ""; list_files_from_dir /autograder/git-repo

echo""; echo "before rm MAKE-STUDENT-OUTPUT"
/bin/rm -rf /autograder/MAKE-STUDENT-OUTPUT

# -p is used to prevent errors if the folder already exists
echo ""; echo "before mkdir -p  MAKE-STUDENT-OUTPUT"
mkdir -p /autograder/MAKE-STUDENT-OUTPUT
echo ""; echo "after mkdir -p  MAKE-STUDENT-OUTPUT, ls: `ls`"

mkdir /autograder/MAKE-STUDENT-OUTPUT/CODE
mkdir /autograder/MAKE-STUDENT-OUTPUT/TEST

cd /autograder/MAKE-STUDENT-OUTPUT

echo ""; echo "==> SUBMISSION_SOURCE:" ; echo "$SUBMISSION_SOURCE";
list_files_from_dir $SUBMISSION_SOURCE;  echo " "


# mv all the files to .
# Not sure about the purpose of $f
cp -v -r $SUBMISSION_SOURCE/* /autograder/MAKE-STUDENT-OUTPUT/CODE
# git-repo contains a single folder: the grading repository. 
# Perhaps do a 'mv' instead of 'cp' for efficiency?
# cp allowed for better debugging. I can repeat run_autograde multiple times
cp -v -r /autograder/git-repo/*/*   /autograder/MAKE-STUDENT-OUTPUT/TEST
cd /autograder/MAKE-STUDENT-OUTPUT/TEST


# What if I have multiple files to run?
rm -f results.json

# Run as many tests as necessary
#python3 -m pytest test_structure.py
#python3 test_structure.py

# There is only one folder in git-repo
#cd /autograder/git-repo/*
chmod 755 ./run_tests.x
./run_tests.x

# Copy appropriate files from folder MAKE-STUDENT-OUTPUT/submission/ to 
# to folder MAKE-STUDENT-OUTPUT/git-repo/CAP-5777-s24-grading-1/
# ISSUE: make sure there are no files with conflicting names. 
# Perhaps test.x should make sure there are no conflicts. 

# These three lines should be reinstated 2023-11-25
if [ -d /autograder/results ]; then
    cp -v results.json /autograder/results
fi

#----------------------------------------------------------------------
