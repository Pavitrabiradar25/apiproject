import requests
import json

BASE_URL='http://127.0.0.1:8000/'
END_POINT='api/'

def get_single_data():
	id=input('enter the id : \t')
	data={}
	if id is not None:
		data={'id':id}
	response=requests.get(BASE_URL+END_POINT,data=json.dumps(data))
	print(response.json())
	print(response.status_code)



def get_total_data(id=None):

	data={}
	if id is not None:
		data={'id':id}
	response=requests.get(BASE_URL+END_POINT,data=json.dumps(data))
	print(response.json())
	print(response.status_code)


def create_data():
	eno=int(input('enter the employee number :\t'))
	ename=input('enter the employee name : ')
	esalary=int(input('enter the employee salary :\t'))
	eaddress=input('enter the employee address : \t')
	created_data={'eno':eno,'ename':ename,'esalary':esalary,'eaddress':eaddress}

	response=requests.post(BASE_URL+END_POINT,data=json.dumps(created_data))
	print(response.json())
	print(response.status_code)



def update_partial_data():
	id=input('enter the id : \t')
	update_data = {'id':id ,'esalary':350000,'eaddress':'bihar'}
	response = requests.put(BASE_URL+END_POINT,data=json.dumps(update_data))
	print(response.json())
	print(response.status_code)



def update_total_data():
	id=input('enter the id : \t')

	eno=int(input('enter the employee number :\t'))
	ename=input('enter the employee name : ')
	esalary=int(input('enter the employee salary :\t'))
	eaddress=input('enter the employee address : \t')
	updated_data={'id':id,'eno':eno,'ename':ename,'esalary':esalary,'eaddress':eaddress}

	response = requests.put(BASE_URL+END_POINT,data=json.dumps(updated_data))
	print(response.json())
	print(response.status_code)



def delete_data():
	id=input('enter the id : \t')
	emp_data={'id':id}	

	response=requests.delete(BASE_URL+END_POINT,data=json.dumps(emp_data))
	print(response.json())
	print(response.status_code)





def invalidOption():
	print('please provide valid option')
	

if __name__ == '__main__':

	while(1):
		print(''' 
			Please Select the below operation.
			1. select single data .
			2. Select total data.
			3. create resource.
			4. Update partially.
			5. Update Completely.
			6. Delete the resource.
			(id = 1 is deleted ,please enter other id)

			
			 ''')

		choice = int(input('Enter your choice:'))

		options = {
			1: get_single_data,2: get_total_data,
			3: create_data,4: update_partial_data,
			5: update_total_data,6: delete_data,
			
		}
		options.get(choice, invalidOption)()


























