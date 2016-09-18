import argparse 
from reportbot import call_df

def report_run():
	parser = argparse.ArgumentParser()
	parser.add_argument("-r", "--report", 
		help="Input the report name to run.")
	args = parser.parse_args()
	
	if args.report == "df":
		call_df()

report_run()