import zlib
import argparse

def decompress_zlib(encoded_data):
    try:
        decoded_data = zlib.decompress(encoded_data)
        return decoded_data
    except zlib.error as e:
        print(f"Decompression error: {e}")
        return None

def main(input_file, output_file):
    try:
        # Read the encoded data from the input file
        with open(input_file, 'rb') as f:
            encoded_data = f.read()

        # Decompress the encoded data
        decoded_data = decompress_zlib(encoded_data)

        # If decompression is successful, write the decoded data to the output file
        if decoded_data:
            with open(output_file, 'wb') as f:
                f.write(decoded_data)
            print(f"Decoded data written to {output_file}")
        else:
            print("Failed to decode data.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Setup argument parser to take input and output file names from command line
    parser = argparse.ArgumentParser(description='Decompress zlib-encoded data.')
    parser.add_argument('input_file', help='The file containing zlib-encoded data.')
    parser.add_argument('output_file', help='The file to write the decompressed data to.')
    args = parser.parse_args()

    # Call the main function with parsed arguments
    main(args.input_file, args.output_file)
