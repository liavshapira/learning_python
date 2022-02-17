given_temp_to_check=input("Insert the temperature you would like to convert:")
temp_type=given_temp_to_check[-1:].upper()
temp_value=float(given_temp_to_check[:-1])
if ( (isinstance(temp_value,float)) ):
    if   ( temp_type == 'F' ):
        C = ( ( 5 * temp_value ) - 160 ) / 9
        print(str(C)+"C")
    elif ( temp_type == 'C' ):
        F = ( ( 9 * temp_value ) + ( 32 * 5 ) ) / 5
        print(str(F)+"F")
    else:
        print("Wrong temp input")
else:
    print(temp_type)
    print(temp_value)
    print("Wrong number input")

