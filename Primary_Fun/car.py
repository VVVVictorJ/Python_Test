def make_car(Type,size,**makein):
	some={}
	some['Type']=Type
	some['size']=size
	for key,value in makein.items():
		some[key]=value
	return some

car=make_car('subaru','outback',color='blue',two_package=True)
print(car)	
