import random
from abc import ABC, abstractmethod

## 1. Clase Abstracta Base (
class Personaje(ABC):
    def __init__(self, nombre, vida, ataque, defensa):
        self.nombre = nombre
        # Atributos privados para cumplir con el Encapsulamiento 
        self.__vida = vida
        self.__ataque = ataque
        self.__defensa = defensa

    # Getters y Setters con validación 
    @property
    def vida(self):
        return self.__vida

    @vida.setter
    def vida(self, valor):
        if valor < 0:
            self.__vida = 0
        elif valor > 100:
            self.__vida = 100
        else:
            self.__vida = valor

    @property
    def ataque(self):
        return self.__ataque

    @property
    def defensa(self):
        return self.__defensa

    def esta_vivo(self):
        return self.vida > 0

    # Método Abstracto para aplicar Polimorfismo 
    @abstractmethod
    def atacar(self, objetivo):
        pass

## 2. Clases Derivadas con Habilidades Aleatorias

class Guerrero(Personaje):
    def atacar(self, objetivo):
        danio = self.ataque
        # Habilidad aleatoria (30% de probabilidad): 20% incremento de daño 
        if random.random() < 0.3:
            danio *= 1.20 
            print(f"⚔️ ¡FURIA! {self.nombre} incrementa su daño.")
        
        danio_final = max(0, danio - objetivo.defensa)
        objetivo.vida -= danio_final
        print(f"{self.nombre} golpea a {objetivo.nombre} causando {danio_final:.1f} de daño.")

class Mago(Personaje):
    def atacar(self, objetivo):
        # Habilidad aleatoria (40% de probabilidad): Ignora defensa 
        if random.random() < 0.4:
            danio_final = self.ataque
            print(f"🔮 ¡HECHIZO! {self.nombre} ignora la defensa.")
        else:
            danio_final = max(0, self.ataque - objetivo.defensa)
            
        objetivo.vida -= danio_final
        print(f"{self.nombre} lanza magia a {objetivo.nombre} causando {danio_final} de daño.")

class Arquero(Personaje):
    def atacar(self, objetivo):
        danio_base = self.ataque
        # Habilidad aleatoria (30% de prob.): Doble daño si supera defensa 
        if random.random() < 0.3 and danio_base > objetivo.defensa:
            danio_final = danio_base * 2
            print(f"🏹 ¡TIRO CRÍTICO! {self.nombre} duplica su daño.")
        else:
            danio_final = max(0, danio_base - objetivo.defensa)
            
        objetivo.vida -= danio_final
        print(f"{self.nombre} dispara a {objetivo.nombre} causando {danio_final} de daño.")

## 3. Clase de Control de Batalla
class Batalla:
    def __init__(self, p1, p2):
        self.personaje1 = p1
        self.personaje2 = p2

    def mostrar_estado(self):
        # Muestra vida restante después de cada ataque 
        print(f" {self.personaje1.nombre}: {self.personaje1.vida} HP | {self.personaje2.nombre}: {self.personaje2.vida} HP")

    def iniciar(self):
        print(f" LA BATALLA COMIENZA: {self.personaje1.nombre} vs {self.personaje2.nombre} \n")
        
        # Ciclo de enfrentamiento por turnos 
        while self.personaje1.esta_vivo() and self.personaje2.esta_vivo():
            # Ataque del Personaje 1
            self.personaje1.atacar(self.personaje2)
            if not self.personaje2.esta_vivo(): break
            
            # Ataque del Personaje 2
            self.personaje2.atacar(self.personaje1)
            
            self.mostrar_estado()
            print("-" * 40)

        ganador = self.personaje1.nombre if self.personaje1.esta_vivo() else self.personaje2.nombre
        print(f"\n💀 ¡BATALLA TERMINADA! El ganador es: {ganador} 🏆")

# --- EJECUCIÓN ---
if __name__ == "__main__":
    # Configuración de personajes [cite: 28, 29]
    roronoa = Guerrero("Roronoa-Zoro", 100, 30, 20)
    merlin  = Mago("Merlin", 80, 40, 10)

    arena = Batalla(roronoa, merlin)
    arena.iniciar()