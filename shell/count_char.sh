#!/bin/sh
read -p "please enter a word: " -n 50 line
if [ -z "${line}" ]
then
    echo "empty string!!!"
    exit
fi
length=${#line}
int=0
space=" "
num_space=0
num_number=0
num_other=0
num_char=0
a="a"
z="z"
while(($int<$length))
do
    char=${line:$int:1}
    if [ "$char" = "$space" ]
    then
        num_space=`expr $num_space + 1`
    elif [ $char -ge 0 -a $char -le 9 ]
    then
        num_number=`expr $num_number + 1`
    elif [ "${char}" -ge "97" -a "${char}" -le "122" ]
    then
        num_char=`expr $num_char + 1`
    else
        num_other=`expr $num_other + 1`
    fi
    let "int++"
done
echo "空格个数为：${num_space}/${length}."
echo "数字个数为：${num_number}/${length}."
echo "其他字符个数为： ${num_other}/${length}."
echo "字母个数为： ${num_char}/${length}."
