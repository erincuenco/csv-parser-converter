import csv
import datetime


def format_date_utc(year,month,day):
  date = datetime.date(year, month, day).strftime("%Y-%m-%d")
  date = date+"T16::00:00.000Z"
  print(date)
  return date

year = 2016
month = 1
day = 1
header = True

csvReader = csv.reader(open('file2.csv', newline=''), delimiter=',', quotechar='|')
textFileName = "results_daily_rainfall.txt"
fileHandle = open(textFileName, "w")

for row in csvReader:
  year = 2016
  month = 1
  day = 1
  header = True
  for rainfall in row:
    if header:
      station_id = rainfall
      header = False
    else:
      if(day == 32 and (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10)):
        month = month + 1
        day = 1
      elif(day == 31 and (month == 4 or month == 6 or month == 9 or month == 11)):
        month = month + 1
        day = 1
      elif(day == 30 and month == 2):
        month = month + 1
        day = 1
      elif(day == 32 and month == 12):
        break
      string_date = format_date_utc(year,month,day)
      day = day + 1
      fileHandle.write("HistoricalDailyRainData.insert({ \n")
      fileHandle.write("\tid: '"+station_id+"', \n")
      fileHandle.write("\tdailyRain: { \n")
      fileHandle.write("\t\tdateUTC: new Date('"+string_date+"'), \n")
      fileHandle.write("\t\trainfall: '"+rainfall+"', \n")      
      fileHandle.write("\t} \n")        
      fileHandle.write("}); \n")
    
fileHandle.close()