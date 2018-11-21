def show_magicians(magicians):##打印名字
	for magician in magicians:
		mes=magician.title()
		print(mes)
def make_great(magicians,current_magicians):##导入空列表
	for magician in magicians:
		mes_1=("theGreat"+magician.title())
		print(mes_1)
		current_magicians.append(mes_1)
		current_magicians.sort()
		
magicians=['david','coop','red']
current_magicians=[]

show_magicians(magicians)
make_great(magicians[:],current_magicians)

show_magicians(current_magicians)
show_magicians(magicians)
 

