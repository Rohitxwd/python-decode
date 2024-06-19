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
        with open(input_file, 'rb') as f:
            encoded_data = f.read()

        decoded_data = decompress_zlib(encoded_data)

        if decoded_data:
            with open(output_file, 'wb') as f:
                f.write(decoded_data)
            print(f"Decoded data written to {output_file}")
        else:
            print("Failed to decode data.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Decompress zlib-encoded data.')
    parser.add_argument('input_file', help='The file containing zlib-encoded data.')
    parser.add_argument('output_file', help='The file to write the decompressed data to.')
    args = parser.parse_args()

    main(args.input_file, args.output_file)
