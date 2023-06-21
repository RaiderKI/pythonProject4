import functions


data_list = functions.read_json('operations.json')

operations = functions.get_executed_operations(data_list)

for operation in operations:
    print(functions.get_message(operation))