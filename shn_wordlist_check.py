#!/usr/bin/env python3
import sys

if len(sys.argv) < 2:
    exit(f"Usage {sys.argv[0]} input.txt")

file = sys.argv[1]

file_base = file.split(".txt")[0]

charset = set()

number = '0123456789႐႑႒႓႔႕႖႗႘႙'
symbol = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ €"
lang_char ='ငတထပမယရလဝသဢိီုူေဵံး်ျြွ၊။ၢၵၶၷၸၺၻၼၽၾၿႁႂႃႄႅႆႇႈႉႊꧠꧡꧢꧣꧤꩡꩦꩧꩨꩩꩪꩮ'

# all_shn_char = number + symbol + lang_char
check_char = set([c for c in lang_char])

with open(file, 'r', encoding='utf-8') as f:
    for line in f:
        for c in line.strip():
            code = ord(c)
            if (
                (0x1000 <= code and code <= 0x109f) or
                (0xaa60 <= code and code <= 0xaa7f) or
                (0xa9e0 <= code and code <= 0xa9fe)
            ):
                charset.add(c)

print(f"Total charsets {len(charset)} in {file}")
charset = sorted(charset)
print(charset)

# Remaining charset
if len(set(lang_char) - set(charset)) !=0:
    print("Charset Remaining:")
    print(set(lang_char) - set(charset))
else:
    print("Great! no charset remaining")