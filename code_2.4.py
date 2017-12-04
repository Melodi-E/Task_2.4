import os

def search_substring_in_file(original_file_list):
	new_file_list = [] 

	string_to_search = input('Введите строку для поиска:')
	for file_name in original_file_list: 
		with open(file_name) as current_file:
			file_content = current_file.read() 
			if string_to_search in file_content: 
				new_file_list.append(file_name) 
				print(file_name)
	print('Всего: ', len(new_file_list))
	return new_file_list 

def find_files():
	migrations = 'Migrations'
	current_dir = os.path.dirname(os.path.abspath(__file__)) 
	os.chdir(os.path.join(current_dir, migrations)) 

	file_list = []
	files = os.listdir()      
	for file in files:
		filename, file_extension = os.path.splitext(file)
		if file_extension == ".sql":
		    file_list.append(file) 
	print('Осторожно, бесконечный цикл. Для выхода нажмите Ctrl + C')
	while True:
		file_list = search_substring_in_file(file_list)
		if len(file_list) == 0:
			print('Ничего не нашли, выходим из цикла')
			break
		elif len(file_list) == 1:
			print('Файл найден')
			break

find_files()