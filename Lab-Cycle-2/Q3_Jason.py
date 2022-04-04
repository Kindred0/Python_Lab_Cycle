import json

with open('iris.json') as f:
	data=json.load(f)

p_area=1000
s_area=0
for i in data:
	if i['species']=='setosa':
		print(i)
		if (i['sepalLength']*i['sepalWidth'])>s_area:
			s_area=i['sepalLength']*i['sepalWidth']
		if p_area>(i['petalLength']*i['petalWidth']):
			p_area=i['petalLength']*i['petalWidth']
print("Minimum petal area of the species 'Setosa'\t: ",p_area)
print("Maximum sepal area of the species 'Setosa'\t: ",s_area)
p_area=1000
s_area=0
for i in data:
	if i['species']=='versicolor':
		if (i['sepalLength']*i['sepalWidth'])>s_area:
			s_area=i['sepalLength']*i['sepalWidth']
		if p_area>(i['petalLength']*i['petalWidth']):
			p_area=i['petalLength']*i['petalWidth']
print("Minimum petal area of the species 'Versicolor'\t: ",p_area)
print("Maximum sepal area of the species 'Versicolor'\t: ",s_area)
p_area=1000
s_area=0
for i in data:
	if i['species']=='virginica':
		if (i['sepalLength']*i['sepalWidth'])>s_area:
			s_area=i['sepalLength']*i['sepalWidth']
		if p_area>(i['petalLength']*i['petalWidth']):
			p_area=i['petalLength']*i['petalWidth']
print("Minimum petal area of the species 'Virginica'\t: ",p_area)
print("Maximum sepal area of the species 'Virginica'\t: ",s_area)


