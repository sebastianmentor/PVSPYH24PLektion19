something = True
something_else = True
something_finaly = True

if something and something_else and something_finaly:
    print(f"{something=}")
    print(f"{something_else=}")
    print(f"{something_finaly=}")

elif something:
    print(f"{something=}")
elif something_else:
    print(f"{something_else=}")
elif something_finaly:
    print(f"{something_finaly=}")
else:
    print(f"Else world is on fire!!")