import sys

def reverse_bits_in_file(input_path, output_path):
    # Lookup table to instantly reverse the bits of any 8-bit byte on the fly
    bit_reverse_table = bytes([
        int('{:08b}'.format(i)[::-1], 2) for i in range(256)
    ])
    
    try:
        with open(input_path, 'rb') as f_in:
            data = f_in.read()
            
        # Translate every single byte using the flipped bit lookup table
        reversed_data = data.translate(bit_reverse_table)
        
        with open(output_path, 'wb') as f_out:
            f_out.write(reversed_data)
            
        print(f"Successfully flipped bits! Created: {output_path}")
    except FileNotFoundError:
        print(f"Error: Could not find the file '{input_path}'. Make sure Quartus generated it first.")

# Execute the conversion
if __name__ == "__main__":
    # Change "output_file.rbf" to whatever your local Quartus output name is!
    reverse_bits_in_file("../src/fpga/output_files/ap_core.rbf", "../dist/Cores/dave18.ZXSpectrum/bitstream.rbf_r")
