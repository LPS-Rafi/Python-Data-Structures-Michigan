"""Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below.
Convert the extracted value to a floating point number and print it out."""
text = "X-DSPAM-Confidence:    0.8475"
pos_start = text.find(':') + 1  # Find the position of ':' and move one character forward
number_str = text[pos_start:].strip()  # Slice from the position and strip whitespace
number = float(number_str)  # Convert the extracted value to a floating point number
print(number)  # Print the floating point number