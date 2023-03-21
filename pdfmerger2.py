import PyPDF2

merger = PyPDF2.PdfMerger()

while True:
    # Prompt user for input file path
    input_file_path = input("Enter path to PDF file (or type 'done' to stop): ")
    if input_file_path.lower() == "done":
        break
    else:
        try:
            # Append the input file to the merger
            merger.append(input_file_path)
        except PyPDF2._utils.PdfStreamError:
            print(f"{input_file_path} is not a valid PDF file.")

# Prompt user for output file path
output_file_path = input("Enter path to output file: ")

# Write the merged PDF to the output file
with open(output_file_path, "wb") as output_file:
    merger.write(output_file)