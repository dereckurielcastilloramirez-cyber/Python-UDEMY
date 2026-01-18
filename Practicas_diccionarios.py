cliente = {'nombre':'Peter','apellido':'Linares','peso':68, 'altura':1.70} #las key no se pueden repetir pero los valores si
#consulta = input('Search: ')
#result = cliente[consulta]
#print(result)

dicc ={'c1':44, 'c2':[10,20,30],'c3':{'s1':100,'s2':200}}

#print(dicc['c2'][2]) #imprime un elemento de la lista que tiene el diccionario
print(dicc['c3']['s2']) #imprime el key de un dicc dentro de un dicc 

dic = {'c1':['a','b','c'],'c2':['d','e','f']}

#print(dic['c1'][0].upper())

dic['c3'] = ['g','h','i'] #agregar o sobreescribir elementos

print(dic.keys())
print(dic.values())
print(dic.items())