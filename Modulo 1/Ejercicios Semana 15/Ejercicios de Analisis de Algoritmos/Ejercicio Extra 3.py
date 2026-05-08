def print_all_pairs(my_dict):
    for key1 in my_dict:#0(n)
        for key2 in my_dict:#0(n^2)
            print(f"{key1}-{key2}")#0(1)

#0(n^2)

#Con 1 millon de claves el programa hubiera corrido un millon a la potencia y hubiera tardado mucho en correr