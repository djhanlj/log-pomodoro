#!/usr/bin/python 

# Coloque o arquivo sheets.py na mesma pasta desse script
import sheets

from datetime import datetime
import easygui

# Substitua pelo ID da sua planilha
SPREADSHEET='1e88rVqeexmhdQATK28UepXzf5GKoRBJXetx-gQYBGhg'

total = int(sheets.read_spreadsheet(SPREADSHEET, "Summary!G3:G3")[0][0])

row = total + 3
now = datetime.now()

current_date = now.strftime("%d/%m/%Y")
current_time = now.strftime("%H:%M")

try:
    previous_task = sheets.read_spreadsheet(SPREADSHEET, "Log!D" + str(row-1) + ":D" + str(row-1))[0][0]
except:
    previous_task = ""

task = easygui.enterbox(msg="What is your current task?", default=previous_task)

sheets.write_spreadsheet(SPREADSHEET, "Log!B" + str(row) + ":D" + str(row), list([[current_date, current_time, task]]))