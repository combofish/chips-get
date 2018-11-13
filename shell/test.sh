#!/bin/env sh
use(){
	echo $1
}
use `uname -r`
read -p "enter a number" -t 5 name
echo $name
