# "строка с %спецификаторами" % значения

name = "Mikhail"
city = "Almaty"

print("Hello, i'm {0} from {1}"
      .format(name, city))

print("Hello, i'm {1} from {0}"
      .format(name, city))

print("Hello, i'm {0} from {1}"
      .format(city, city))

print("Hello, i'm {name} from {city}"
      .format(name=name, city=city))

print("Hello, i'm {name} from {town}"
      .format(name=name, town=city))

print()

number = 7
print("%05d" % number)
print("%-5d" % number)

float_number = 7.3430
print("Your height: %f m" % float_number)
print("Your height: %.2f my height %s" % (float_number, float_number + 5))