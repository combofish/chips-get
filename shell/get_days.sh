#!/bin/sh

read -p "Enter year, month, day:" year month day
if [ $month -le 0 -o $month -gt 12 ]
then
    echo "month is illegal!!!"
    exit
fi
#####
array_days=(31 28 31 30 31 30 31 31 30 31 30 31)

####
if [ `expr $year % 4` -eq 0 -a `expr $year % 100` -ne 0 -o `expr $year % 400` -eq 0 ]
then
    array_days[1]=29
else
    array_days[1]=28
fi
#####
use_month=`expr $month - 1`
if [ ${array_days[ $use_month ]} -lt $day ]
then
    echo "day is illegal(maybe too large!"
    exit
fi
####
if [ $year -lt 0 ] 
then
    echo "year is less then illegal"
fi
if [ $day -lt 0 ]
then
    echo "day is less then illegal"
fi
#####
sum_day=$day

number=`expr $month - 1`
while(($number>0))
do
    let "number--"
    sum_day=`expr $sum_day + ${array_days[ $number ]}`
    echo "-----------add :$sum_day"
done
#####
echo "the year:(${year}-${month}-${day}) has the number of days: ${sum_day}. "

    




