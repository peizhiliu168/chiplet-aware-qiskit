import json
import copy

#Specify the connections required here
connections = [[0,12],[1,13],[2,14]]


def parse_json(file_name):
    f = open(file_name)

    data = json.load(f)

    for keys in data:
        print(keys)
        if keys == "qubits":
            data[keys] = insert_qubit(len(connections), data[keys])
        
        if keys == "gates":
            data[keys] = insert_gates(data[keys])
    
    out_file = open("modified_props_chiplet.json", "w")
  
    json.dump(data, out_file, indent=4)
  
    out_file.close()
        
        
# This function modifies the "qubits" field
def insert_qubit(num, array):
    c = copy.copy(array)
    for i in range(num):
        c.append(array[0])
    
    return c


# This function modifies the "gates" field
def insert_gates(array):
    c = copy.copy(array)

    fake_time = array[0]["parameters"][0]["date"]
    fake_delay = array[0]["parameters"][1]["value"]

    gate_error = {"date": fake_time, "name": "gate_error", "unit": "", "value": 0.0}
    gate_delay = {"date": fake_time, "name": "gate_length", "unit": "ns", "value": fake_delay}
        

    for ele in connections:
        tmp = {}
        tmp["qubits"] = ele
        tmp["gate"] = "swap"
        tmp["parameters"] = [gate_error, gate_delay]
        tmp["name"] = "swap" + str(ele[0]) + "_" + str(ele[1])
        c.append(copy.copy(tmp))

        tmp = {}
        tmp["qubits"] = [ele[1],ele[0]]
        tmp["gate"] = "swap"
        tmp["parameters"] = [gate_error, gate_delay]
        tmp["name"] = "swap" + str(ele[1]) + "_" + str(ele[0])
        c.append(copy.copy(tmp))
    
    return c
        

def main():
    parse_json("props_chiplet.json")


if __name__=="__main__":
    main()