import csv
import datetime


def format_date(year,month,day):
  date = datetime.date(year, month, day).strftime("%Y%m%d")
  # print(date)
  return date

# station_id = input('What id?')
crop = input('What crop?')
variety = input('What variety?')
year = 2016
month = 1
day = 1
header = True

csvReader = csv.reader(open('file.csv', newline=''), delimiter=',', quotechar='|')
textFileName = "results.txt"
fileHandle = open(textFileName, "w")

for row in csvReader:
  for expectedYield in row:
    if header:
      station_id = expectedYield
      header = False
    elif(month == 12 and day == 23):
      for column in range(0,9):
        string_date = format_date(year,month,day)
        day = day + 1
        fileHandle.write("PercentMeanData.insert({ \n")
        fileHandle.write("\tid: '"+station_id+"', \n")
        fileHandle.write("\tpercentMean: { \n")
        fileHandle.write("\t\tdate: '"+string_date+"', \n")
        fileHandle.write("\t\tcrop: '"+crop+"', \n")
        fileHandle.write("\t\tvariety: '"+variety+"', \n")
        fileHandle.write("\t\texpectedYield: '"+expectedYield+"' \n")        
        fileHandle.write("\t} \n")        
        fileHandle.write("}); \n")
    else:
      for column in range(0,7):
        if(day == 32 and (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10)):
          month = month + 1
          day = 1
        elif(day == 31 and (month == 4 or month == 6 or month == 9 or month == 11)):
          month = month + 1
          day = 1
        elif(day == 30 and month == 2):
          month = month + 1
          day = 1
        string_date = format_date(year,month,day)
        day = day + 1
        fileHandle.write("PercentMeanData.insert({ \n")
        fileHandle.write("\tid: '"+station_id+"', \n")
        fileHandle.write("\tpercentMean: { \n")
        fileHandle.write("\t\tdate: '"+string_date+"', \n")
        fileHandle.write("\t\tcrop: '"+crop+"', \n")
        fileHandle.write("\t\tvariety: '"+variety+"', \n")
        fileHandle.write("\t\texpectedYield: '"+expectedYield+"' \n")        
        fileHandle.write("\t} \n")        
        fileHandle.write("}); \n")
    
fileHandle.close()