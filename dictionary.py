def myfun(text, *line, **header):
    for data in header.keys():
        print(data+ ":" +header[data])
    print()
    print(text)
    for l in line:
        print(l)

myfun('TAFS','subroto park', 'delhi cantt', phy='SJT', chem='MNG',comp='PKC')