from abc import ABC, abstractmethod

# Abstracción (interfaz)


class Reproductor(ABC):
    @abstractmethod
    def reproducir(self):
        pass

# Implementaciones concretas


class ReproductorMP3(Reproductor):
    def reproducir(self):
        print("Reproduciendo música MP3")


class ReproductorCD(Reproductor):
    def reproducir(self):
        print("Reproduciendo CD de música")

# Clase de alto nivel DEPENDE de una abstracción


class SistemaMusica:
    def __init__(self, reproductor: Reproductor):
        self.reproductor = reproductor

    def iniciar_reproduccion(self):
        self.reproductor.reproducir()

# Uso


def main():
    # Flexibilidad para cambiar el reproductor
    reproductor_mp3 = ReproductorMP3()
    sistema_mp3 = SistemaMusica(reproductor_mp3)
    sistema_mp3.iniciar_reproduccion()

    reproductor_cd = ReproductorCD()
    sistema_cd = SistemaMusica(reproductor_cd)
    sistema_cd.iniciar_reproduccion()


if __name__ == "__main__":
    main()
