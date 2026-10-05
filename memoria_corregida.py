import random
import time


class Memoria:
    def __init__(self, tamanio: int):
        self.tamanio: int = tamanio
        self.memoria: list[str | None] = [None] * tamanio

    def compactar(self) -> None:
        """Junta todos los bloques ocupados al inicio para eliminar huecos"""
        print("-> Compactando memoria para eliminar fragmentación...")
        bloques_ocupados = [bloque for bloque in self.memoria if bloque is not None]
        bloques_libres = [None] * (self.tamanio - len(bloques_ocupados))
        self.memoria = bloques_ocupados + bloques_libres

    def asignar(self, proceso: str, tamanio_requerido: int) -> bool:
        # Primero intenta asignar normal
        for i in range(self.tamanio - tamanio_requerido + 1):
            if all(self.memoria[i + j] is None for j in range(tamanio_requerido)):
                for j in range(tamanio_requerido):
                    self.memoria[i + j] = proceso
                print(f"Proceso {proceso} asignó {tamanio_requerido} bloques en posición {i}.")
                return True

        # Si no hay espacio contiguo, intenta compactar y volver a intentar
        print(f"Proceso {proceso} NO encontró espacio contiguo. Hay fragmentación externa.")
        self.compactar()
        self.mostrar_memoria()

        # Segundo intento después de compactar
        for i in range(self.tamanio - tamanio_requerido + 1):
            if all(self.memoria[i + j] is None for j in range(tamanio_requerido)):
                for j in range(tamanio_requerido):
                    self.memoria[i + j] = proceso
                print(f"Proceso {proceso} asignó {tamanio_requerido} bloques DESPUÉS de compactar.")
                return True

        print(f"Proceso {proceso} no pudo asignar memoria. Memoria realmente llena.")
        return False

    def liberar(self, proceso: str) -> None:
        for i in range(self.tamanio):
            if self.memoria[i] == proceso:
                self.memoria[i] = None
        print(f"Proceso {proceso} ha liberado su memoria.")

    def mostrar_memoria(self) -> None:
        print(f"Estado actual: {self.memoria}\n")


def proceso(nombre: str, memoria: Memoria) -> None:
    tamanio_requerido = random.randint(1, 5)
    print(f"{nombre} pide {tamanio_requerido} bloques.")
    if memoria.asignar(nombre, tamanio_requerido):
        time.sleep(0.5)
        memoria.liberar(nombre)
    time.sleep(0.5)


def gestionar_memoria() -> None:
    memoria = Memoria(10)
    procesos = ['Proceso-A', 'Proceso-B', 'Proceso-C', 'Proceso-D', 'Proceso-E']
    print("=== SIMULACIÓN CON CÓDIGO CORREGIDO (CON COMPACTACIÓN) ===\n")
    for _ in range(8):
        proceso_nombre = random.choice(procesos)
        proceso(proceso_nombre, memoria)
        memoria.mostrar_memoria()


if __name__ == "__main__":
    gestionar_memoria()