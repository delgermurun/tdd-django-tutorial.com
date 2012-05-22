#! /bin/bash

tag_me()
{
  tag_name=$1
  message=$2
  TIME='date +%Y-%m-%d-%H-%M'
  git tag -d $tag_name
  git tag -a -f -m "$message" $tag_name-$TIME
  git push origin tag $tag_name-$TIME
}

if [ $# -ne 2 ] ;then
  echo 1>&2 Usage: $0 tag_name message
  exit 127
fi

tag_me $1 $2
