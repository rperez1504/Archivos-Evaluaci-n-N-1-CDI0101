aclNum = int(input("Ingrese ACL: "))
if aclNum >= 1 and aclNum <= 99:
    print("Esta es una ACL estándar IPv4.")
elif aclNum >=100 and aclNum <= 199:
    print("Esta es una ACL extendida IPv4.")
else:
    print("El valor ingresado no es una ACL IPv4.")
