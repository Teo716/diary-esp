from argon2 import PasswordHasher

from argon2.exceptions import VerifyMismatchError
# Inicializa el hasheador de contraseñas de Argon2

ph = PasswordHasher()

def hashear_contrasena(contrasena_plana):

    """Hashea una contraseña usando Argon2."""

    return ph.hash(contrasena_plana)

def verificar_contrasena(contrasena_plana, hash_guardado):

    """Verifica si una contraseña plana coincide con un hash guardado."""

    try:

        ph.verify(hash_guardado, contrasena_plana)

        return True

    except VerifyMismatchError:

        return False

    except Exception as e: # Captura otros posibles errores de verificación

        print(f"Error durante la verificación: {e}")

        return False