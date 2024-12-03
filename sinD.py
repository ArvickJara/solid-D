# Sin Principio de Inversión de Dependencias
class ReproductorMP3:
    def reproducir_mp3(self):
        print("Reproduciendo música MP3")


class ReproductorCD:
    def reproducir_cd(self):
        print("Reproduciendo CD de música")

# Clase de alto nivel DEPENDE de implementaciones concretas


class SistemaMusica:
    def __init__(self):
        self.reproductor_mp3 = ReproductorMP3()
        self.reproductor_cd = ReproductorCD()

    def reproducir_mp3(self):
        self.reproductor_mp3.reproducir_mp3()

    def reproducir_cd(self):
        self.reproductor_cd.reproducir_cd()

# Uso


def main():
    sistema = SistemaMusica()
    sistema.reproducir_mp3()
    sistema.reproducir_cd()


if __name__ == "__main__":
    main()
