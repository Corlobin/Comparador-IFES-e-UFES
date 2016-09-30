import requests
from lxml import html

class Pagina(object):
	def __init__(self):
		print('ok')
	def set_object(self, list):
		for i in range(0, len(list)):
			if list[i] == 'gs_rt': # titulo
				print(list[i].getchildren())
		
		
def main():
	# Apenas cursos de ciencia e sistemas
	pag = 0
	
	pagina = requests.get('https://scholar.google.com.br/scholar?start=0&q=jaccard+cosine+similarity&hl=pt-BR&as_sdt=0,5')
	tree = html.fromstring(pagina.content)
	#lista = [a for a in tree.xpath('//div[@class="gs_r"]//div[@class="gs_fl"]//a') ]
	lista = [a for a in tree.xpath('//div[@class="gs_ri"]') ]
	pagina = Pagina()
	for i in range(0, len(lista)):
		pagina.set_object(lista[i].getchildren())
		#print (str(i) + "----------->\t\t")
		#for filho in lista[i].getchildren():
			#print(filho.items())
		#print("\n")
		
		
main()
    



