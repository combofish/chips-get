#!/bin/sh
read -p "please enter a word :" -n 50 line
if [ ! "${line}" ]
then
    echo "empty string!!!"
    exit
fi
num_space=0
num_number=0
num_other=0
num_char=0
for r in `echo "${line}" | tr -d "\n" | od -An -t dC `
do
    echo $r
    if [ $r -ge 65 -a $r -le 90 -o $r -ge 97 -a $r -le 122 ] 
    then
        num_char=`expr $num_char + 1`
    elif [ $r -ge 48 -a $r -le 57 ]
    then
        num_number=`expr $num_number + 1`
    elif [ $r -eq 32 ]
    then
        num_space=`expr $num_space + 1`
    else
        num_other=`expr $num_other + 1`
    fi
done
length=${#line}
echo "空格个数为：${num_space}/${length}."
echo "数字个数为：${num_number}/${length}."
echo "其他字符个数为： ${num_other}/${length}."
echo "字母个数为： ${num_char}/${length}."         
        
      



    
