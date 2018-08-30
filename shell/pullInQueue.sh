#!/bin/sh
arr_num1=(10 9 8 7 6 5 4 3 2 1)
arr_num=(1 2 3  5 6 7 8 9 10)
read -p "Enter a number: " num
echo "you Enter a ${num}."
if [ ${arr_num[0]} -gt ${arr_num[1]} ]
then
    qu=1
else
    qu=0
fi
#####---------未检测输入--------

length=${#arr_num[@]}
echo "Length is :`expr ${length} + 1`"
i=0
j=0

if [ $qu -eq 0 ];then
    echo "up>>"
    while [ $i -lt ${length} ]
    do
        if [ $num -lt ${arr_num[ $i ]} ]
        then
            arr[ $j ]=$num
            let "j++"
        fi
        
        arr[ $j ]=${arr_num[ $i ]}
        let "j++"
        let "i++"
    done
    arr[ $j ]=$num
    
else
    echo "down>>"
fi
echo ${arr[*]}
         
