# app.py
from flask import Flask, render_template, request
from datereturns import dates_return
from append_row import append_row
app = Flask(__name__)
import pandas as pd
payperiod = pd.read_csv('payperiod.csv')

@app.route('/')
def index():
	global period
	dateData = dates_return()
	period = dateData['Period']
	dateList = dateData['Dates']
	print(len(dateList))
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
	
@app.route('/', methods=['POST'])
def indexData():
	lname = (request.form['employee-lname'])
	fname = (request.form['employee-fname'])
	employeeId = (request.form['employee-id'])
	day0 = (request.form['d0'])
	day1 = (request.form['d1'])
	day2 = (request.form['d2'])
	day3 = (request.form['d2'])
	day4 = (request.form['d3'])
	day5 = (request.form['d4'])
	day6 = (request.form['d5'])
	day7 = (request.form['d6'])
	day8 = (request.form['d7'])
	day9 = (request.form['d8'])
	day10 = (request.form['d9'])
	day11 = (request.form['d10'])
	day12 = (request.form['d11'])
	day13 = (request.form['d12'])

	totalHours = (request.form['total-hours'])
	
	tableHead = f"<th>Pay Period</th><th>last name</th><th>first name</th><th>ID</th>"
	for date in dates_return()['Dates']:
		tableHead += f"<th>{date}</th>"
	tableHead += "<th>Total Hours</th>"
	hours = [day0,day1,day2,day3,day4,day5,day6,day7,day8,day9,day10,day11,day12,day13]
	append_row(period,lname,fname,employeeId,hours)
	return (f"""
	<table>
		<thead>
			{tableHead}
		</thead>
		<tbody>
			<tr>
			<td>{period}</td>
			<td>{lname}</td>
			<td>{fname}</td>
			<td>{employeeId}</td>
			<td>{day0}</td>
			<td>{day1}</td>
			<td>{day2}</td>
			<td>{day3}</td>
			<td>{day4}</td>
			<td>{day5}</td>
			<td>{day6}</td>
			<td>{day7}</td>
			<td>{day8}</td>
			<td>{day9}</td>
			<td>{day10}</td>
			<td>{day11}</td>
			<td>{day12}</td>
			<td>{day13}</td>
			<td>{totalHours}</td>
			</tr>
		</tbody>
	</table>
""")

if __name__ == '__main__':
	app.run(debug=True)