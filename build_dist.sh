# This attempts to build a distribution directory for the workshop.
#
# This creates a directory and populates it with code, exercises, solutions, and
# presentations. It works from a git clone of this directory, so make sure
# you've committed everything you want before running the script.
#
# Before you run this, make sure the PDFs have been generated for the
# presentations. The script will fail if there are no PDFs in the presentations
# directory; this is on purpose.
#
# To run it:
#
#   ./build_dist.sh
#
# This will put a zip file in the `dist` directory.

function abs_path {
    local dir=`dirname "$1"`
    local file=`basename "$1"`
    pushd "$dir" &>/dev/null || return $? # On error, return error code
    echo "`pwd -P`/$file" # output full, link-resolved path with filename
    popd &> /dev/null
}

function cleanup_venv() {
    # Deactivate the virtualenv
    deactivate
}

# The name of the workshop. This will be used to name the output zip file.
WORKSHOP_NAME=sixty-north-introduction-to-python

GIT_ORIGIN=$(abs_path .)
PRESENTATION_DIR=$(abs_path presentation)
WORK_DIR=$(abs_path dist)

# Clear and re-create the work dir
mkdir -p $WORK_DIR
rm -Rf $WORK_DIR/*

# Set up a temporary virtual env
if which pyenv > /dev/null; then eval "$(pyenv init -)"; fi
# Make a venv to work from
if which pyenv > /dev/null;
then
    pyenv virtualenvwrapper
else
    source `which virtualenvwrapper.sh`
fi

mktmpenv -c --python=python3.6

trap cleanup_venv INT EXIT TERM

# Clone the repo
GIT_CLONE=$WORK_DIR/repo

IFS=$'\n'
set -e

git clone $GIT_ORIGIN $GIT_CLONE

# Install Python dependencies
pip install -r $GIT_CLONE/exercises/requirements.txt

# First, build HTML from sphinx
pushd $GIT_CLONE/exercises
make html
popd

# Copy exercises and solutions from git repo
DIST_DIR=$WORK_DIR/$WORKSHOP_NAME
mkdir -p $DIST_DIR/exercises
cp -R $GIT_CLONE/exercises/build/html $DIST_DIR/exercises
cp -R $GIT_CLONE/exercises/solutions $DIST_DIR/exercises


# Copy student materials from git repo
# cp -R $GIT_CLONE/materials $DIST_DIR

# Copy presentations
# echo `pwd`
# mkdir -p $DIST_DIR/presentation
# cp $PRESENTATION_DIR/*pdf $DIST_DIR/presentation

# Create zip file
pushd $WORK_DIR
zip -r $WORKSHOP_NAME.zip $WORKSHOP_NAME
popd
