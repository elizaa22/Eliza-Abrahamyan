import re

class CircuitParser:
    def init(self):
        self.circuit = []

    def parse_netlist(self, file_path):
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
        except FileNotFoundError:
            print(f"Error: The file {file_path} was not found.")
            return

        sub_circuit = {
            "transistor": [],
            "resistor": []
        }

        for line in lines:
            line = line.strip()

            if line.startswith("*") or not line:
                continue

            if line.startswith("M"):
                parts = line.split()
                name = parts[0]
                parameters = " ".join(parts[1:])
                sub_circuit["transistor"].append({
                    "parameter": name,
                    "value": parameters
                })

            elif line.startswith("R"):
                parts = line.split()
                name = parts[0]
                parameters = " ".join(parts[1:])
                sub_circuit["resistor"].append({
                    "parameter": name,
                    "value": parameters
                })

        self.circuit.append({"sub_circuit": sub_circuit})

    def write_netlist(self, file_path):
        try:
            with open(file_path, 'w') as file:
                for sub in self.circuit:
                    sub_circuit = sub["sub_circuit"]

                    for transistor in sub_circuit["transistor"]:
                        line = f"{transistor['parameter']} {transistor['value']}\n"
                        file.write(line)

                    for resistor in sub_circuit["resistor"]:
                        line = f"{resistor['parameter']} {resistor['value']}\n"
                        file.write(line)
        except IOError:
            print(f"Error: Unable to write to {file_path}.")

parser = CircuitParser()
parser.parse_netlist(“hsp.txt")
print("Parsed Circuit Structure:", parser.circuit)
parser.write_netlist("output_netlist.txt")