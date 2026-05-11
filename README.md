Battle Sim: Python POO Edition
Un simulador de combate por turnos desarrollado en Python para demostrar la implementación práctica de conceptos avanzados de Programación Orientada a Objetos (POO).

🚀 Descripción
El proyecto consiste en un motor de batalla donde diferentes clases de personajes (Guerreros, Magos y Arqueros) se enfrentan en un duelo a muerte. Cada personaje tiene atributos únicos y habilidades especiales que se activan de forma probabilística durante el combate.

🏗️ Arquitectura y Principios Aplicados
El código se estructura bajo los siguientes pilares:

Abstracción: Uso de la clase base Personaje (ABC) para definir la estructura obligatoria de cualquier luchador.

Encapsulamiento: Atributos de salud, ataque y defensa privados (__) con validación mediante @property y @setter.

Herencia: Clases especializadas (Guerrero, Mago, Arquero) que heredan de la clase base.

Polimorfismo: Cada clase hija implementa su propio método atacar(), permitiendo que el motor de batalla maneje cualquier personaje de forma genérica.

Clase       ,                                       Habilidad Especial,                                                                               Probabilidad
Guerrero,Furia:                            Incrementa el daño base en un 20%.                                                                            30%
Mago,Hechizo:                             Ignora completamente la defensa del oponente.                                                                  40%
Arquero,                                  Tiro Crítico: Duplica el daño si el ataque supera la defensa.                                                  30%
