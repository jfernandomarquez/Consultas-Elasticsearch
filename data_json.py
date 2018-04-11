import json

#print('\033[91m' + "False"+ '\033[0m' )
#print('\033[92m' + "True"+ '\033[0m' )


data = json.load(open("data.json"))
#print "El tipo es:", type(data)

for key, value in data.iteritems():
		print('\033[92m')
                print key
                print('\033[0m')
                print('\033[91m')
                print  value
                print ('\033[0m')
		for k, v in value.iteritems():
			print('\033[93m')
			print k
			print('\033[0m')
			print('\033[94m')
			print  v
			print ('\033[0m')
			if k == "GlossDiv":
				for ke, va in v.iteritems():
                        		print('\033[95m')
                        		print ke
                        		print('\033[0m')
                        		print('\033[96m')
                        		print  va
                        		print ('\033[0m')


print "--------------------------------------------------------"
print data['glossary']['GlossDiv']['GlossList'] 


#data2={ "name":"John", "age":30}
#print "el tipo es", type(data2)

#for key, value in data2.iteritems():
#	print "la llave ", key, "el valor " ,value

