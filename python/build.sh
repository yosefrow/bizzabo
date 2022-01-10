#!/bin/bash -eu

VERSION=$1

docker build ./src -t bizzabo:$VERSION
