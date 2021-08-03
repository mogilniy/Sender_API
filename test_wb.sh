#!/bin/bash
key="OTUzMDhiNTItMTZlNC00ZjdlLTk1YWMtZjViYmE3MWJjMjQ2YzIwZDdlZWEtNmZk_PE93_bed4d195-92fc-4dd3-946a-c5b317a8386e"
mess="autotest from git action"
python3 Get_room.py "$key" > test_room.txt
sleep 1
echo "==========================list all room"
cat test_room.txt
echo "==========================list all room"

cat test_room.txt | while read line1

do

file1="test_email_"+$i1+"_.txt"


python3 Get_list_of_email.py "$key" "$line1" > "test_mail_room$line1"
echo "==========================list E-mail"
cat "test_mail_room$line1"
echo "==========================end list E-mail"
sleep 1
python3 Send_mess.py "$key" "$line1" "$mess for room $line1" 
 
done

