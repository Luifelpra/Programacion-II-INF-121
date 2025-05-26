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


anuncio1 = Anuncio(101, 1500.0)


pintura_con_anuncio = Pintura(
    "El Alba", "óleo",
    ("Juan Pérez", "1234567", 8),
    ("María López", "7654321", 12),
    "realismo",
    anuncio1
)

pintura_sin_anuncio = Pintura(
    "La Tormenta", "acrílico",
    ("Carlos Díaz", "9876543", 15),
    ("Ana Torres", "4567890", 5),
    "impresionismo"
)

print("Artistas con más experiencia:")
print("Con anuncio:", pintura_con_anuncio.artista_mas_experto())
print("Sin anuncio:", pintura_sin_anuncio.artista_mas_experto())

nuevo_anuncio = Anuncio(102, 1800.0)
pintura_sin_anuncio.agregar_anuncio(nuevo_anuncio)

total_venta = pintura_con_anuncio.monto_venta() + pintura_sin_anuncio.monto_venta()
print("\nMonto total de venta:", total_venta)
