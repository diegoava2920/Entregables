def validate_tables(inspector):
    contador = 0
    tables = ["users", "address", "cars"]

    existing = []

    for table in tables:
        if inspector.has_table(table, schema="sqalchemy_test"):
            existing.append(table)
            contador = contador+1

    if existing:
        print("Ya existen:")
        for t in existing:
            print(f" - {t}")
    else:
        print("Ninguna tabla existe")

    if(contador==3):
        return False
    else:
        return True
    
