from cryptography.fernet import Fernet

def generar_clave():
    clave = Fernet.generate_key()
    with open("clave.key", "wb") as archivo_clave:
        archivo_clave.write(clave)
    print("Clave generada y guardada en clave.key")

if __name__ == "__main__":
    generar_clave()