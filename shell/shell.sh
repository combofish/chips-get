#!/bin/sh
echo "helloworld"
your_name="rubb.com"
for file in `ls /etc`;do
    echo $file
done    
echo $(ls -la ~)
echo ${your_name}
for skill in Ada coddi action java;do
    echo "i am good at ${skill}script"
done
your_name=haha
echo $your_name
readonly your_name
#your_name="http://hahah"
unset your_name
echo $your_name
str='haha'
echo $str
geeting1="hello,${your_name}!"
echo $geeting1
echo ${#geeting1}
string="runoob is a great site."
echo ${string:1:4}
echo `expr index "$string" io`
array_name=(
    value
    value1
    value2
)
value=${array_name[2]}
echo $value
:<<EOF
jsdf
jlsf
EOF
echo "canshu1$0"
echo "canshu2$1"
echo "$#"
echo $*
echo "pid:$$"
echo "$@"
echo $@
echo "---"
echo $*
echo "$*"
echo "----"
for i in $*;do
    echo $i
done
for i in $@;do
    echo $i
done    
if [ -n "$1" ];then
    echo "baohan first par"
else
    echo "don't have"
fi    
array=(a b c "d")
echo ${array[1]}
echo ${array[3]}
echo "----"
echo "the all ${array[*]}"
echo "the all ${array[@]}"
echo "the number of the array is ${#array[*]}!"
val=`expr 2 + 2`
echo "sum = $val"
a=2
b=3
echo "`expr $a + $b`"
if [ $b == $a ];then
    echo "$a"
fi
if [ $a -ne $b ]
then
    echo "hahah -ne"
fi    
if [ !false ]
then
    echo "true"
fi
d=50
if [ $d -ge 40 -a $d -le 1000  ]
then
    echo "hahah -ge -le"
fi    
echo "[ "jjj" = "jjj" ]"
if [ "hh" = "hh" ]
then
    echo "true"
fi
if [ -z '' ]
then
    echo "is 0"
fi
if [ -n "hhha" ]
then
    echo "not zero"
fi
file="/var/log/wtmp"
if [ -r $file ];then
    echo "can read:${file}"
fi
if [ -w $file ];then
    echo "can w"
else
    echo "can not write!"
fi
if [ -e $file ];then
    echo "exeist $file"
fi
if [ -f $file ];then
    echo "file $file"
fi
echo "string"
echo I am learning
echo "\" i am learning!\""
##read name
echo "${name} is hahah"
echo -e "OK!\n"
echo "it is a test!"
echo -e "haha\c"
echo "no line:"
echo "echo >>file" >> use.txt
echo "name\""
echo -e "name\""
echo `date`
##read firstStr secondStr
echo "first :$firstStr,secondStr :$secondStr"
##read -p "please enter a word:" -n 10 -t 4 -s passwd
echo -e "\npassword is $passwd"
printf "d %s\n" 1 "abc"
printf '%d%s\n' 1 "abc"
a=5
b=6
result=$[a+b]
echo $result
for loop in 1 2 3 4 5
do
    echo "haha,the value is $loop"
done
for str in "this is a string"
do
    echo $str
done
int=1
while(($int<=5))
do
    echo $int
    let 'int++'
done
a=0
until [ ! $a -lt 10 ]
do
    echo $a
    a=`expr $a + 1`
done
echo [$a + 1]
let "a++"
echo $a
echo -n "jh"
echo "jsj"
#read -p "jhh" hah
echo $hah
for((i=1;i<=5;i++));do
    echo "haha"
done
a=2
case $a in
    1)
        echo "jaja"
    ;;
    2)
        echo "jiji"
    ;;
    esac

#read -p "please enter a word: " -n 50 line
for l in ${line[@]}
do
    echo -e "${l}"
done
echo "---"
echo ${line[0]}
int=0
while(($int<50))
do
#    echo $int
    echo "${int}:---:${line:$int:1}"
    let "int++"
done
echo ${#line}              

a="a"
b="b"
#diff $a $b
echo $?
if [ ! "$a" = "$b" ]
then
    echo "jaj"
    echo "ha"
fi
for r in `echo "azazaz" | tr -d "\n" | od -An -t dC `
do
    echo $r
done

