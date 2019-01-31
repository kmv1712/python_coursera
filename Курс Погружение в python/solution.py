class FileReader:
	def __init__(self, file_path):
		self.file_path = file_path

	def read(self):
		"""Возвращает содержимое файла в виде строки"""
		try:
			f = open(self.file_path, "r")
			file_content = f.read()
			f.close()
			file_content = file_content.replace("\n", "")
			return file_content
		except IOError:
			return "" 

reader = FileReader("example.txt")
print(reader.read())
