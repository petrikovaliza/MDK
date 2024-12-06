def meters_to_centimeters(lengths):
    for length in lengths:
        yield {"meter": length, "centimeter": length * 100}

lengths_in_meters = [2, 5, 6.5]
for item in meters_to_centimeters(lengths_in_meters):
  print(item)