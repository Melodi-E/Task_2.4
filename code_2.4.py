import glob
import os.path

def search_substring_in_file(original_file_list):
	new_file_list = [] 

	string_to_search = input('Введите строку для поиска:')

	for file_name in original_file_list: 
		current_file = open(file_name) 
		file_content = current_file.read() 
		if string_to_search in file_content: 
			new_file_list.append(file_name) 
			print(file_name) 
	print('Всего: ', len(new_file_list))
	return new_file_list 

def find_files():
	migrations = 'Migrations'
	file_list = []
	files = glob.glob(os.path.join(migrations, "*.sql"))
	for file in files:
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