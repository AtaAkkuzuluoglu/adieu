Names = []
while True: 
    try:     
        GetNames = str(input(""))
        Names.append(GetNames)
    except EOFError:
            if len(Names) == 2:
                Names.insert(1, "and")
                print("Adieu, adieu, to " + ' '.join(Names))
            elif len(Names) < 2:
                print("Adieu, adieu, to " + ' '.join(Names))
            elif len(Names) > 2:
                Names.insert(-1, "and")
                print("Adieu, adieu, to " + ", ".join(Names[:-1]) + " " + Names[-1])
            break
