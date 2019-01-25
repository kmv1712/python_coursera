import argparse
import sys
import os
import tempfile
parser = argparse.ArgumentParser()
parser.add_argument("-k", "--key", help="name key")
parser.add_argument("-v", "--val", nargs='+', help="name val")
args = parser.parse_args()
key_name = args.key
value = args.val
f_dict = {}
f_list = []
v_list = []

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
if not os.path.exists(storage_path):
	with open(storage_path, 'w') as f:
		f.write("")

if key_name and value:
	with open(storage_path, 'a') as f:
		f.write(key_name)
		f.write(" | ")
		for item in value:
			f.write(item)
			f.write(" ")
		f.write("\n")

elif key_name:
	with open(storage_path, 'r') as f:
		for line in f:
			file_line = line.split('| ')
			f_dict[file_line[0]] = file_line[1]
			f_list.append(f_dict.copy())
	for item_list in f_list:
		for k, v in item_list.items():
			if k.strip() == key_name.strip():
				v_list.append(v.replace(" \n", ""))
	if v_list:
		print(", ".join(v_list))
else:
	print("")


