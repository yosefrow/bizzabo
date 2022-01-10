#!/bin/bash -eu

VERSION=$1

docker run --rm --env-file .env -it bizzabo:$VERSION
