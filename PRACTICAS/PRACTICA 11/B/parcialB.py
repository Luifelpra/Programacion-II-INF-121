class Anuncio:
    def __init__(self, numero, precio):
        self.numero = numero
        self.precio = precio

    def incrementar_precio(self, monto):
        self.precio += monto

    def __str__(self):
        return f"Anuncio #{self.numero} - Precio: {self.precio}"

class Artista:
    def __init__(self, nombre, ci, anios_experiencia):
        self.nombre = nombre
        self.ci = ci
        self.anios_experiencia = anios_experiencia

    def __str__(self):
        return f"{self.nombre} ({self.anios_experiencia} años de experiencia)"


class Obra:
    def __init__(self, titulo, material, datos_artista1, datos_artista2, anuncio=None):
        self.titulo = titulo
        self.material = material
        self.artista1 = Artista(*datos_artista1)
        self.artista2 = Artista(*datos_artista2)
        self.anuncio = anuncio


class Pintura(Obra):
    def __init__(self, titulo, material, datos_artista1, datos_artista2, genero, anuncio=None):
        super().__init__(titulo, material, datos_artista1, datos_artista2, anuncio)
        self.genero = genero

    def agregar_anuncio(self, anuncio):
        self.anuncio = anuncio

    def monto_venta(self):
        return self.anuncio.precio if self.anuncio else 0

    def artista_mas_experto(self):
        return self.artista1 if self.artista1.anios_experiencia >= self.artista2.anios_experiencia else self.artista2

    def artistas(self):
        return [self.artista1, self.artista2]

anuncio2 = Anuncio(103, 1200.0)
anuncio3 = Anuncio(104, 1700.0)

pintura1_b = Pintura(
    "Amanecer", "acuarela",
    ("Lucía Rojas", "2223334", 10),
    ("Marco Gutiérrez", "3332221", 7),
    "abstracto",
    anuncio2
)

pintura2_b = Pintura(
    "Reflejos", "óleo",
    ("Elena Vargas", "5551112", 6),
    ("Pedro Salas", "6668889", 9),
    "surrealismo",
    anuncio3
)

total_anios = 0
contador_artistas = 0
for pintura in [pintura1_b, pintura2_b]:
    for artista in pintura.artistas():
        total_anios += artista.anios_experiencia
        contador_artistas += 1

promedio_experiencia = total_anios / contador_artistas
print("\n Promedio de años de experiencia:", promedio_experiencia)

nombre_objetivo = "Elena Vargas"
incremento = 500.0
for pintura in [pintura1_b, pintura2_b]:
    for artista in pintura.artistas():
        if artista.nombre == nombre_objetivo:
            pintura.anuncio.incrementar_precio(incremento)
            print(f"\n Se incrementó el precio de la pintura de {nombre_objetivo}:")
            print(f"Título: {pintura.titulo}, Nuevo precio: {pintura.anuncio.precio}")
