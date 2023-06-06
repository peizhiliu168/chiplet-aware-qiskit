import json
import copy

#Specify the connections required here
connections = [[0,12],[1,13],[2,14]]


def parse_json(file_name):
    f = open(file_name)

    data = json.load(f)

    for keys in data:
        print(keys)
        if keys == "n_qubits":
            data[keys] = data[keys] + len(connections)
                    
        if keys == "gates":
            data[keys] = insert_gates(data[keys])
        
        if keys == "coupling_map":
            for con in connections:
                data[keys].append(con)
                data[keys].append([con[1], con[0]])
        if keys == "supported_instructions" and "swap" not in data[keys]:
            data[keys].append("swap")
    
    out_file = open("modified_conf_chiplet.json", "w")
  
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
    swap_exist = False

    for i in range(len(array)):
        if c[i]["name"] == "swap":
            swap_exist = True
            for con in connections:
                c[i]["coupling_map"].append(con)
                c[i]["coupling_map"].append([con[1], con[0]])
    
    if not swap_exist:
        tmp = {}
        tmp["name"] = "swap"
        tmp["parameters"] = []
        tmp["qasm_def"] = "gate swap q0, q1 { SWAP q0, q1; }"
        for con in connections:
            tmp["coupling_map"].append(con)
            tmp["coupling_map"].append([con[1], con[0]])
        c.append(tmp)

    
    return c
        

def main():
    parse_json("conf_chiplet.json")


if __name__=="__main__":
    main()