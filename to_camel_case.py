# Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.

# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"

# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"

# "The_Stealth-Warrior" gets converted to "TheStealthWarrior"

def to_camel_case(text):
    final_string = ''
    capitalize_next = False
    for char in text:
        if char in ['-', '_']:
            capitalize_next = True
        else:
            if capitalize_next:
                final_string += char.upper()
                capitalize_next = False
            else:
                final_string += char
        
    return final_string