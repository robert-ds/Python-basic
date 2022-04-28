f = open('/etc/passwd', 'r')
datos = f.read(21)
f.close()

print(datos)
