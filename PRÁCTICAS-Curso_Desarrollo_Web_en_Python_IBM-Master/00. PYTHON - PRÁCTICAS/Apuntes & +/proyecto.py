# Definición de la clase Libro
class Libro:
    def __init__(self, titulo, autor, isbn, disponible):
        # Inicializa los atributos del libro
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible

    def descripcion(self):
        # Devuelve una descripción del libro
        return f"{self.titulo} por {self.autor} con ISBN: {self.isbn} {'Estado del libro: disponible' if self.disponible else 'Estado del libro: no disponible'}"

    def estado(self):
        # Devuelve el estado de disponibilidad del libro
        return f"Estado del libro: {'disponible' if self.disponible else 'no disponible'}"

# Funciones
def menu_principal():
    # Muestra el menú principal y devuelve la opción seleccionada por el usuario
    print("Menú principal")
    print("1. Agregar libro")
    print("2. Prestar libro")
    print("3. Devolver libro")
    print("4. Mostrar libros")
    print("5. Buscar libro")
    print("0. Salir")
    return input("Seleccione una opción: ")

def agregar(libros):
    # Agrega un nuevo libro a la lista de libros
    print("Introduce un título")
    titulo = input()
    print("Introduce un autor")
    autor = input()
    print("Introduce un ISBN")
    isbn = input()
    print("¿Está disponible? (s/n)")
    disponible = input().lower()
    if disponible == "s":
        disponible = True
    else:
        disponible = False

    libro = Libro(titulo, autor, isbn, disponible)
    libros.append(libro)  # Añade el libro a la lista de libros
    print("Libro añadido")

def mostrar(libros):
    # Muestra todos los libros en la lista
    if not libros:
        print("No hay libros para mostrar.")
    for libro in libros:
        print(libro.descripcion())

def prestar(libros):
    # Presta un libro si está disponible
    print("Introduce el ISBN del libro que deseas prestar")
    isbn = input()
    
    if not isbn:
        print("ISBN no encontrado")
        return
    try:
        encontrado = False
        for libro in libros:
            if libro.isbn == isbn:
                encontrado = True
                if libro.disponible:
                    libro.disponible = False  # Cambia el estado a no disponible
                    print("El libro ha sido prestado con éxito")
                else:
                    print("El libro no está disponible")
                break
        if not encontrado:
            print("Error al buscar el ISBN: no existe")
    except Exception as e:
        print(f"Error al buscar el ISBN: {e}")

def devolver(libros):
    # Devuelve un libro prestado
    print("Introduce el ISBN del libro que deseas devolver")
    isbn = input()
    if not isbn:
        print("ISBN no encontrado")
        return
    try:
        encontrado = False
        for libro in libros:
            if libro.isbn == isbn:
                encontrado = True
                if not libro.disponible:
                    libro.disponible = True  # Cambia el estado a disponible
                    print("El libro ha sido devuelto")
                else:
                    print("El libro ya está disponible")
                break
        if not encontrado:
            print("Error al buscar el ISBN: no existe")
    except Exception as e:
        print(f"Error al buscar el ISBN: {e}")

def buscar(libros):
    # Busca un libro por su ISBN y muestra su descripción
    print("Introduce el ISBN del libro que deseas buscar")
    isbn = input()
    if not isbn:
        print("ISBN no encontrado")
        return
    try:
        encontrado = False
        for libro in libros:
            if libro.isbn == isbn:
                encontrado = True
                print("El libro está disponible: " + libro.descripcion())
                break
        if not encontrado:
            print("Error al buscar el ISBN: no existe")
    except Exception as e:
        print(f"Error al buscar el ISBN: {e}")

# Función principal
def main():
    libros = []  # Inicializa una lista vacía para almacenar los libros
    while True:
        menu = menu_principal()
        if menu == '0':
            break
        if menu not in ['0', '1', '2', '3', '4', '5']:
            print("Opción no válida")
            continue
        try:
            if menu == '1':
                agregar(libros)
            elif menu == '2':
                prestar(libros)
            elif menu == '3':
                devolver(libros)
            elif menu == '4':
                mostrar(libros)
            elif menu == '5':
                buscar(libros)
        except (ValueError, IndexError):
            print("Error desconocido")

if __name__ == "__main__":
    main()
    input("Presiona enter para salir...")