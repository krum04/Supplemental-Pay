# app.py
from flask import Flask, render_template, request
from datereturns import dates_return
from append_row import append_row
from datetime import datetime

app = Flask(__name__)
period = ''
@app.route('/')
def index():
	global period
	dateData = dates_return() # set dateData to dictionary returned from dates_return() containing pay period and dates
	period = dateData['Period'] # set period to the current pay period
	dateList = dateData['Dates'] # set dateList to list of dates in pay period
	
	# set each date in dateList to a variable
	date1 = dateList[0]
	date2 = dateList[1]
	date3 = dateList[2]
	date4 = dateList[3]
	date5 = dateList[4]
	date6 = dateList[5]
	date7 = dateList[6]
	date8 = dateList[7]
	date9 = dateList[8]
	date10 = dateList[9]
	date11 = dateList[10]
	date12 = dateList[11]
	date13 = dateList[12]
	date14 = dateList[13]
	return render_template('index.html', period=period,d0=date1, d1=date2, d2=date3, d3=date4, d4=date5, d5=date6, d6=date7, d7=date8, d8=date9, d9=date10, d10=date11, d11=date12, d12=date13, d13=date14)
	
# @app.route('/', methods=['POST'])
# def indexData():
# 	# grab data from form
# 	lname = (request.form['employee-lname'])
# 	fname = (request.form['employee-fname'])
# 	employeeId = (request.form['employee-id'])

# 	day0 = (request.form['d0'])
# 	d0start = (request.form['d0start'])
# 	d0stop = (request.form['d0stop'])

# 	day1 = (request.form['d1'])
# 	d1start = (request.form['d1start'])
# 	d1stop = (request.form['d1stop'])

# 	day2 = (request.form['d2'])
# 	d2start = (request.form['d2start'])
# 	d2stop = (request.form['d2stop'])

# 	day3 = (request.form['d3'])
# 	d3start = (request.form['d3start'])
# 	d3stop = (request.form['d3stop'])

# 	day4 = (request.form['d4'])
# 	d4start = (request.form['d4start'])
# 	d4stop = (request.form['d4stop'])
	
# 	day5 = (request.form['d5'])
# 	d5start = (request.form['d5start'])
# 	d5stop = (request.form['d5stop'])

# 	day6 = (request.form['d6'])
# 	d6start = (request.form['d6start'])
# 	d6stop = (request.form['d6stop'])

# 	day7 = (request.form['d7'])
# 	d7start = (request.form['d7start'])
# 	d7stop = (request.form['d7stop'])

# 	day8 = (request.form['d8'])
# 	d8start = (request.form['d8start'])
# 	d8stop = (request.form['d8stop'])

# 	day9 = (request.form['d9'])
# 	d9start = (request.form['d9start'])
# 	d9stop = (request.form['d9stop'])

# 	day10 = (request.form['d10'])
# 	d10start = (request.form['d10start'])
# 	d10stop = (request.form['d10stop'])

# 	day11 = (request.form['d11'])
# 	d11start = (request.form['d11start'])
# 	d11stop = (request.form['d11stop'])

# 	day12 = (request.form['d12'])
# 	d12start = (request.form['d12start'])
# 	d12stop = (request.form['d12stop'])

# 	day13 = (request.form['d13'])
# 	d13start = (request.form['d13start'])
# 	d13stop = (request.form['d13stop'])

# 	totalHours = (request.form['total-hours'])
# 	tableHead = f"<th>Pay Period</th><th>last name</th><th>first name</th><th>ID</th>"
	
# 	for date in dates_return()['Dates']:
# 		tableHead += f"<th>{date}</th>"
# 	tableHead += "<th>Total Hours</th>"

# 	hours=[]
	
# 	for i in range(14):
# 		var_name = f"day{i}"
# 		if eval(var_name) != "0:00":
# 			hours.append(f"{eval(var_name)} {eval('d' + str(i) + 'start')} - {eval('d' + str(i) + 'stop')}")
# 		else:
# 			hours.append("")
	
# 	# hours = [day0,day1,day2,day3,day4,day5,day6,day7,day8,day9,day10,day11,day12,day13]
# 	print(f" Pay Period {period}")
# 	input()
# 	append_row(period,lname,fname,employeeId,hours)
# 	return (f"""
# 	<table>
# 		<thead>
# 			{tableHead}
# 		</thead>
# 		<tbody>
# 			<tr>
# 			<td>{period}</td>
# 			<td>{lname}</td>
# 			<td>{fname}</td>
# 			<td>{employeeId}</td>
# 			<td>{day0}</td>
# 			<td>{day1}</td>
# 			<td>{day2}</td>
# 			<td>{day3}</td>
# 			<td>{day4}</td>
# 			<td>{day5}</td>
# 			<td>{day6}</td>
# 			<td>{day7}</td>
# 			<td>{day8}</td>
# 			<td>{day9}</td>
# 			<td>{day10}</td>
# 			<td>{day11}</td>
# 			<td>{day12}</td>
# 			<td>{day13}</td>
# 			<td>{totalHours}</td>
# 			</tr>
# 		</tbody>
# 	</table>
# """)

	
@app.route('/', methods=['POST'])
def indexData():
	date = datetime.now().strftime("%m/%d/%Y %#I:%M %p")
	# grab data from form
	lname = (request.form['employee-lname'])
	fname = (request.form['employee-fname'])
	employeeId = (request.form['employee-id'])

	day0 = (request.form['d0'])
	d0start = (request.form['d0start'])
	d0stop = (request.form['d0stop'])

	day1 = (request.form['d1'])
	d1start = (request.form['d1start'])
	d1stop = (request.form['d1stop'])

	day2 = (request.form['d2'])
	d2start = (request.form['d2start'])
	d2stop = (request.form['d2stop'])

	day3 = (request.form['d3'])
	d3start = (request.form['d3start'])
	d3stop = (request.form['d3stop'])

	day4 = (request.form['d4'])
	d4start = (request.form['d4start'])
	d4stop = (request.form['d4stop'])
	
	day5 = (request.form['d5'])
	d5start = (request.form['d5start'])
	d5stop = (request.form['d5stop'])

	day6 = (request.form['d6'])
	d6start = (request.form['d6start'])
	d6stop = (request.form['d6stop'])

	day7 = (request.form['d7'])
	d7start = (request.form['d7start'])
	d7stop = (request.form['d7stop'])

	day8 = (request.form['d8'])
	d8start = (request.form['d8start'])
	d8stop = (request.form['d8stop'])

	day9 = (request.form['d9'])
	d9start = (request.form['d9start'])
	d9stop = (request.form['d9stop'])

	day10 = (request.form['d10'])
	d10start = (request.form['d10start'])
	d10stop = (request.form['d10stop'])

	day11 = (request.form['d11'])
	d11start = (request.form['d11start'])
	d11stop = (request.form['d11stop'])

	day12 = (request.form['d12'])
	d12start = (request.form['d12start'])
	d12stop = (request.form['d12stop'])

	day13 = (request.form['d13'])
	d13start = (request.form['d13start'])
	d13stop = (request.form['d13stop'])

	totalHours = (request.form['total-hours'])
	tableHead = f"<th>Pay Period</th><th>last name</th><th>first name</th><th>ID</th>"
	
	dateList = dates_return()
	dateData = dateList['Dates']
	print(dateData)

	hours=[]
	
	for i in range(14):
		var_name = f"day{i}"
		if eval(var_name) != "0:00":
			hours.append(f"{eval(var_name)} {eval('d' + str(i) + 'start')} - {eval('d' + str(i) + 'stop')}")
		else:
			hours.append("")
	
	append_row(period,lname,fname,employeeId,hours)

	return render_template('receipt.html',fname=fname, lname=lname, period=period, date=date, day0=dateData[0], 
	day1=dateData[1], day2=dateData[2], day3=dateData[3], day4=dateData[4], day5=dateData[5], day6=dateData[6], 
	day7=dateData[7], day8=dateData[8], day9=dateData[9], day10=dateData[10], day11=dateData[11], day12=dateData[12], 
	day13=dateData[13], d0start=d0start,d1start=d1start, d2start=d2start, d3start=d3start, d4start=d4start, d5start=d5start,
	d6start=d6start,d7start=d7start,d8start=d8start,d9start=d9start,d10start=d10start,d11start=d11start,d12start=d12start,
	d13start=d13start,d0stop=d0stop,d1stop=d1stop,d2stop=d2stop,d3stop=d3stop,d4stop=d4stop,d5stop=d5stop,d6stop=d6stop,
	d7stop=d7stop,d8stop=d8stop,d9stop=d9stop,d10stop=d10stop,d11stop=d11stop,d12stop=d12stop,d13stop=d13stop,day0total=day0,
	day1total=day1,day2total=day2,day3total=day3,day4total=day4,day5total=day5,day6total=day6,day7total=day7,day8total=day8,day9total=day9,day10total=day10,day11total=day11,
	day12total=day12,day13total=day13, total= totalHours
	)
	
# 	return (f"""
# 	<table>
# 		<thead>
# 			{tableHead}
# 		</thead>
# 		<tbody>
# 			<tr>
# 			<td>{period}</td>
# 			<td>{lname}</td>
# 			<td>{fname}</td>
# 			<td>{employeeId}</td>
# 			<td>{day0}</td>
# 			<td>{day1}</td>
# 			<td>{day2}</td>
# 			<td>{day3}</td>
# 			<td>{day4}</td>
# 			<td>{day5}</td>
# 			<td>{day6}</td>
# 			<td>{day7}</td>
# 			<td>{day8}</td>
# 			<td>{day9}</td>
# 			<td>{day10}</td>
# 			<td>{day11}</td>
# 			<td>{day12}</td>
# 			<td>{day13}</td>
# 			<td>{totalHours}</td>
# 			</tr>
# 		</tbody>
# 	</table>
# """)

if __name__ == '__main__':
	app.run(debug=True, port=8081)