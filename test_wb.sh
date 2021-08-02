#!/bin/bash
key=$1
mess=$2
python3 Get_room.py "$key" > test_room.txt
sleep 1

cat test_room.txt | while read line1

do

file1="test_email_"+$i1+"_.txt"


python3 Get_list_of_email.py "$key" "$line1" > "test_mail_room$line1"
sleep 1
python3 Send_mess.py "$key" "$line1" "$mess for room $line1" 
 
done

