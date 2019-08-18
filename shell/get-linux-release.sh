#!/bin/env zsh

release_name=`uname -r | cut -d '-' -f 2`
echo $release_name

if test $release_name = 'gentoo'; then
    echo "Gentoo Linux"
fi

