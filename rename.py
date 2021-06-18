import os

input_path = input('请输入文件夹路径:')
find_content = input('待替换内容:')
replace_content = input('替换内容(默认不输入为空字符串):')
for path,dir_list,file_list in os.walk(input_path):
	for file_name in file_list:
		file_path = os.path.join(path, file_name)
		new_path = file_path.replace(find_content, replace_content)
		os.rename(file_path, new_path)
		print(new_path)
