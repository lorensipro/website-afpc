#!/bin/sh

## Build the pattern using the lastnames provided as command line arguments
if [ $# -eq 1 ] ; then
    PEOPLE=$1
elif [ $# -ge 1 ] ; then
    PEOPLE="("$1
    shift 1
    for i in $* ; do
        PEOPLE=$PEOPLE" OR "$i
    done
    PEOPLE=$PEOPLE")"
fi

## Create the HAL request
REQUEST="https://api.archives-ouvertes.fr/search/tel?q=authLastName_s:"$PEOPLE"&indent=true&wt=xml"
#echo $REQUEST

## Execute the request and display the response on the stand output
wget -q -O /dev/stdout "$REQUEST"
