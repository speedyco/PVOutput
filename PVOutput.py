#! /usr/bin/python

from subprocess import call
call('/usr/bin/curl \"http://192.168.2.159/real_time_data.xml\" | grep e-today | sed 's/<.*>\\(.*\\)<\\/.*>/\\1/'')

print("attempt 2")
print(/usr/bin/curl \"http://192.168.2.159/real_time_data.xml\" | grep e-today | sed 's/<.*>\\(.*\\)<\\/.*>/\\1/'+"KW/h")
