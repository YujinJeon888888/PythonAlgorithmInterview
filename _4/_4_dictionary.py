person= {'name': 'Alice','age': 30,'city': 'New York'}
print("name: ",person['name'])
print("Age: ",person['age'])
print("City: ",person['city'])
#딕셔너리 값 변경
person['age']=31

print("Updated Age: ",person['age'])

#딕셔너리에 새로운 키, 값 추가
person['job']='Engineer'

print("job: ",person['job'])

#딕셔너리 순회
for key, value in person.items():
    print(f"{key}: {value}")

#딕셔너리 요소 삭제
del person['city']

print(person)

#딕셔너리에 특정 키 있나 확인
if 'name' in person:
    print("Name is in the dictionary")
else: 
    print("Name isn't in the dictionary")

