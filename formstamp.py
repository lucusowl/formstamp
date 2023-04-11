from datetime import datetime, date

class Stamp:
	def __init__(self, obj = None):
		self.set_template(obj)

	def __deepcopy(self, ele):
		if ele == None:
			return None

		elif type(ele) in (str, int, float, complex, bool, datetime, date):
			self.__cnt += 1
			if (self.__vars == None) or (self.__vars[self.__cnt-1] == None):
				# 타입 기본값
				if type(ele)   is str:      return ''
				elif type(ele) is int:      return 0
				elif type(ele) is float:    return 0.0
				elif type(ele) is complex:  return 0+1j
				elif type(ele) is bool:     return True
				elif type(ele) is datetime: return datetime.min
				elif type(ele) is date:     return date.min
				else: return ele
			else:
				# 변수 지정값
				# 자동 형변환?
				return self.__vars[self.__cnt-1]

		elif type(ele) is list:
			new_ele = []
			for i in ele:
				new_ele.append(self.__deepcopy(i))
		elif type(ele) is dict:
			new_ele = {}
			for i in ele:
				new_ele[i] = self.__deepcopy(ele[i])

		return new_ele

	def get_template_num_var(self) -> int:
		return self.num_var

	def get_template(self):
		return self.__template

	def is_valid_var(self, vars: tuple|list|None) -> bool:
		if vars == None: return True
		return len(vars) == self.num_var

	def set_template(self, obj = None) -> None:
		self.__cnt = 0
		self.__vars = None
		self.__template = self.__deepcopy(obj) # 원본과 분리
		self.num_var = self.__cnt

	def get_instance(self, vars: tuple|list|None = None):
		self.__cnt = 0
		if not self.is_valid_var(vars):
			raise ValueError(f'The number of variables is incorrect, There should be {self.num_var} not {len(vars)}')
		self.__vars = vars
		return self.__deepcopy(self.__template)