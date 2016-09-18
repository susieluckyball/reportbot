import subprocess

def call_df():
	return subprocess.check_call(["df", "-h"])