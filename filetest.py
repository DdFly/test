
#encoding:utf-8
import csv
product_dict = {}
list=[]
n=20
i=1
cvs_file = csv.reader(open('order_products__prior.csv','r'))
# print(cvs_file)
for abc in cvs_file:
	if abc[0]=='order_id':
		continue
	if abc[0] in product_dict:
		product_dict[abc[0]].append(abc[1])
	else:
		product_dict.setdefault(abc[0],[]).append(abc[1])
	i+=1
	if(i>n):
		break
for l in product_dict:
	list.append(product_dict[l])
print(list)
