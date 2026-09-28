
# Task 1: Create raw_logs.txt with encrypted dummy data
raw_file = open("raw_logs.txt", "w")

raw_file.write("2026-09-21 02:14 EUHDFK ghwhfwhg rq vhuyhu GE-07\n")
raw_file.write("2026-09-21 03:05 Xvhu orjlq vxffhvvixo iurp 10.0.0.15\n")
raw_file.write("2026-09-21 04:47 Iluhzdoo uxoh xsgdwhg eb Dgplq Crh\n")
raw_file.write("2026-09-21 06:30 EUHDFK dohuw uhtxluhv uhylhz: srvvleoh gdwd hailowudwlrq\n")
raw_file.write("2026-09-21 08:12 Edfnxs frpsohwhg zlwkrxw huuruv\n")
raw_file.write(" 2026-09-21 09:55 Bhduob vbvwhp pdlqwhqdqfh ilqlvkhg \n")

raw_file.close()


# Task 2: Open the input file and two output files


input_file = open("raw_logs.txt", "r")
master_file = open("decrypted_master.txt", "w")
alert_file = open("security_alerts.txt", "w")


# Task 3: Process every line and every character


for line in input_file:

    decrypted_line = ""

    for character in line:

        # Uppercase letter
        if character >= "A" and character <= "Z":

            code = ord(character) - 3

            # Wrap around from A to Z
            if code < ord("A"):
                code = code + 26

            decrypted_line = decrypted_line + chr(code)

        # Lowercase letter
        elif character >= "a" and character <= "z":

            code = ord(character) - 3

            # Wrap around from a to z
            if code < ord("a"):
                code = code + 26

            decrypted_line = decrypted_line + chr(code)

        # Keep spaces, numbers, punctuation, and newline unchanged
        else:

            decrypted_line = decrypted_line + character



    # Task 4: Clean the decrypted line
    clean_line = decrypted_line.strip()


    # Task 5: Save every decrypted line
    master_file.write(clean_line + "\n")


   
    # Task 6: Find BREACH and save matching lines
    upper_line = clean_line.upper()

    if "BREACH" in upper_line:

        alert_file.write(clean_line + "\n")


# Task 7: Close all files
input_file.close()
master_file.close()
alert_file.close()

# Task 8: Display completion messages
print("Decryption completed successfully.")
print("Decrypted logs saved to decrypted_master.txt")
print("Security alerts saved to security_alerts.txt")