def convert_temp(unit_in, unit_out, temp):
  temp = float(temp)
  if unit_in == "c":
    if unit_out == "f":
        return (temp*1.8) + 32
    elif unit_out == "c":
        return temp
    else:
        return "Invalid unit " + unit_out
  elif unit_in == "f":
    if unit_out == "c":
        return (temp-32) / 1.8
    elif unit_out == "f":
        return temp
    else:
        return "Invalid unit " + unit_out
  else: 
    return "Invalid unit " + unit_in
print("CONVERT")
print("c", "f", 0, convert_temp("c", "f", 0), "should be 32.0")
print("f", "c", 212, convert_temp("f", "c", 212), "should be 100.0")
print("z", "f", 32, convert_temp("z", "f", 32), "should be Invalid unit z")
print("c", "z", 32, convert_temp("c", "z", 32), "should be Invalid unit z")
print("f", "f", 75.5, convert_temp("f", "f", 75.5), "should be 75.5")

