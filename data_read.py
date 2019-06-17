# Uses python 3.x compatible backw


# Required libraries

# for accessing spreadsheets
import xlrd
# for pymongo, interface for mongodb
from pymongo import MongoClient
import datetime

# db connection
#no need to specify as its the default port
client = MongoClient('10.56.133.21',27017)
# enter the name of the db within quotes
db = client['Phones']
# enter the name of the collection in quotes
col = db['charging']
# note above db and collection will be created if they are not present

# reading from the spreadsheet
# opening the workbook
workbook = xlrd.open_workbook('7966a52e9dc91019.xls')
# accessing the first sheet by index also by name etc
worksheet = workbook.sheet_by_index(0)
# getting the count of row, starts from 0

def read():
    for val in range(2,worksheet.nrows):
        userid = str((worksheet.cell(val,1)).value)
        date = str()


def update_date():






# Function to convert the time format
def update_time(str1):

	# Checking if last two elements of time
	# is AM and first two elements are 12
	if str1[-2:] == "AM" and str1[:2] == "12":
		return "00" + str1[2:-2]

	# remove the AM
	elif str1[-2:] == "AM":
		return str1[:-2]

	# Checking if last two elements of time
	# is PM and first two elements are 12
	elif str1[-2:] == "PM" and str1[:2] == "12":
		tom = str1[:-2]
	else:
		# add 12 to hours and remove PM
		tom = str(int(str1[:2]) + 12) + str1[2:8]



if __name__ == '__main__':
    read()
