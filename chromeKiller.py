#!/usr/bin/python

from subprocess import check_output ,call
from time import sleep
from re import sub
from time import sleep
while True:
    output=check_output(["free"]).decode("UTF-8")
    output=output.split("\n")[1]
    output=sub(" +"," ",output).split(" ")
    used=int(output[2])
    total =int(output[1])
    if used /total >=0.75:
        call (["killall","chrome"])
    sleep(5)

