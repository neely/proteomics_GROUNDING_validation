import csv
import struct
import os

def convert_proteomics_csv_to_binary(input_csv_path, output_binary_path):
    """
    Reads proteomics data from a custom CSV format and writes results to a proprietary binary format.

    Expected CSV columns: protein_id, peptide_sequence, modification, intensity
    Binary format:
        - 4-byte unsigned integer: number of records
        For each record:
            - 4-byte unsigned integer: length of protein_id string, followed by the string bytes
            - 4-byte unsigned integer: length of peptide_sequence string, followed by the string bytes
            - 4-byte unsigned integer: length of modification string, followed by the string bytes
            - 4-byte float: intensity value

    Args:
        input_csv_path (str): Path to the input CSV file
        output_binary_path (str): Path to the output binary file
    """
    # Read the CSV file
    records = []
    with open(input_csv_path, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Extract the required fields
            protein_id = row['protein_id']
            peptide_sequence = row['peptide_sequence']
            modification = row['modification']
            intensity = float(row['intensity'])
            records.append((protein_id, peptide_sequence, modification, intensity))

    # Write to binary file
    with open(output_binary_path, 'wb') as binfile:
        # Write number of records
        binfile.write(struct.pack('<I', len(records)))

        for protein_id, peptide_sequence, modification, intensity in records:
            # Write each string as length-prefixed UTF-8
            pid_bytes = protein_id.encode('utf-8')
            pseq_bytes = peptide_sequence.encode('utf-8')
            mod_bytes = modification.encode('utf-8')

            binfile.write(struct.pack('<I', len(pid_bytes)))
            binfile.write(pid_bytes)

            binfile.write(struct.pack('<I', len(pseq_bytes)))
            binfile.write(pseq_bytes)

            binfile.write(struct.pack('<I', len(mod_bytes)))
            binfile.write(mod_bytes)

            binfile.write(struct.pack('<f', intensity))

    print(f"Converted {len(records)} records from {input_csv_path} to {output_binary_path}")

# Example usage (if run as a script)
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python proteomics_converter.py <input_csv> <output_binary>")
        sys.exit(1)
    convert_proteomics_csv_to_binary(sys.argv[1], sys.argv[2])