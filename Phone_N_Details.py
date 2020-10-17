# Get Details Of Phone Number
import phonenumbers
from phonenumbers import geocoder , carrier

print(phonenumbers.parse("+919220467408"))
print(carrier.name_for_number(phonenumbers.parse("+918928322500"),'en'))
print(geocoder.description_for_number(phonenumbers.parse("+918928322500"),'en'))
print(phonenumbers.is_valid_number(phonenumbers.parse("+918928322500")))
print(phonenumbers.is_possible_number(phonenumbers.parse("+918928322500")))
