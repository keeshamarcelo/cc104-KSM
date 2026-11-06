flag_register = 0b10101010
the_mask = 0b00001000

if flag_register & the_mask:
    print("My bit is set.")
else:
    print("My bit is reset.")

