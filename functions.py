def find_first_difference(file1, file2):
    with open(file1, "rb") as f1, open(file2, "rb") as f2:
        line_number = 1
        while True:
            line1 = f1.readline()
            line2 = f2.readline()
            if line1 != line2:
                return line_number
            if not line1:
                break  # End of file reached for both files
            line_number += 1
    return None  # Files are identical