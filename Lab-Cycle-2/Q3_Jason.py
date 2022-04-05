import json

with open('iris.json') as f:
	data=json.load(f)

p_area=1000
s_area=0
for i in data:
	petalarea=i['petalLength']*i['petalWidth']
	sepalarea=i['sepalLength']*i['sepalWidth']
	if i['species']=='setosa':
		print(i)
		if (sepalarea)>s_area:
			s_area=sepalarea
		if p_area>petalarea:
			p_area=petalarea
print("\nMinimum petal area of the species 'Setosa'\t: ",p_area)
print("Maximum sepal area of the species 'Setosa'\t: ",s_area)
p_area=1000
s_area=0
for i in data:
	petalarea=i['petalLength']*i['petalWidth']
	sepalarea=i['sepalLength']*i['sepalWidth']
	if i['species']=='versicolor':
		if (sepalarea)>s_area:
			s_area=sepalarea
		if p_area>(petalarea):
			p_area=petalarea
print("Minimum petal area of the species 'Versicolor'\t: ",p_area)
print("Maximum sepal area of the species 'Versicolor'\t: ",s_area)
p_area=1000
s_area=0
for i in data:
	petalarea=i['petalLength']*i['petalWidth']
	sepalarea=i['sepalLength']*i['sepalWidth']
	if i['species']=='virginica':
		if (sepalarea)>s_area:
			s_area=sepalarea
		if p_area>(petalarea):
			p_area=petalarea
print("Minimum petal area of the species 'Virginica'\t: ",p_area)
print("Maximum sepal area of the species 'Virginica'\t: ",s_area)

for i in data:
	petalarea=i['petalLength']*i['petalWidth']
	sepalarea=i['sepalLength']*i['sepalWidth']
	totalarea=sepalarea+petalarea
	i.update({'totalarea':totalarea})

sort_data=sorted(data, key = lambda i:i['totalarea'])
print("\nSorted dictionary\t: \n")
for i in sort_data:
	print(i)