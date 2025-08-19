#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Módulo 1: Ejemplos Básicos de POO en Python
Docente: Alejandro Salgar Marín
ITM 2025-2
"""

print("MÓDULO 1: INTRODUCCIÓN A POO EN PYTHON")
print("=" * 50)

# ============================================================================
# 1. CREACIÓN DE UNA CLASE Y OBJETOS
# ============================================================================
print("\n1. CREACIÓN DE UNA CLASE Y OBJETOS")
print("-" * 40)

class Persona:
    def __init__(self, nombre: str, edad: int):
        self.nombre: str = nombre
        self.edad: int = edad

    def saludar(self) -> str:
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."

# Crear objetos
persona1: Persona = Persona("Alejandro", 25)
persona2: Persona = Persona("Laura", 30)

print(f"Persona 1: {persona1.saludar()}")
print(f"Persona 2: {persona2.saludar()}")

# ============================================================================
# 2. ENCAPSULACIÓN
# ============================================================================
print("\n2. ENCAPSULACIÓN")
print("-" * 40)

class CuentaBancaria:
    def __init__(self, titular: str, saldo: float):
        self.titular: str = titular
        self.__saldo: float = saldo  # Atributo privado

    def depositar(self, cantidad: float) -> None:
        self.__saldo += cantidad

    def retirar(self, cantidad: float) -> str:
        if cantidad <= self.__saldo:
            self.__saldo -= cantidad
            return f"Retiro exitoso de ${cantidad}"
        else:
            return "Fondos insuficientes"

    def mostrar_saldo(self) -> str:
        return f"Saldo actual: ${self.__saldo}"

# Crear y usar cuenta bancaria
cuenta: CuentaBancaria = CuentaBancaria("Alejandro", 1000)
print(f"Titular: {cuenta.titular}")
print(f"Saldo inicial: {cuenta.mostrar_saldo()}")

print(f"{cuenta.depositar(500)}")
print(f"{cuenta.retirar(200)}")
print(f"{cuenta.mostrar_saldo()}")

# ============================================================================
# 3. HERENCIA
# ============================================================================
print("\n3. HERENCIA")
print("-" * 40)

class Animal:
    def __init__(self, nombre: str) -> None:
        self.nombre: str = nombre

    def hacer_sonido(self) -> str:
        return "Hace un sonido."

class Perro(Animal):
    def hacer_sonido(self) -> str:
        return "Guau 🐶"

class Gato(Animal):
    def hacer_sonido(self) -> str:
        return "Miau 🐱"

# Crear instancias
perro: Perro = Perro("Firulais")
gato: Gato = Gato("Mishito")

print(f"{perro.nombre}: {perro.hacer_sonido()}")
print(f"{gato.nombre}: {gato.hacer_sonido()}")

# ============================================================================
# 4. POLIMORFISMO
# ============================================================================
print("\n4. POLIMORFISMO")
print("-" * 40)

animales: list[Animal] = [Perro("Boby"), Gato("Luna"), Animal("Criatura")]

print("Demostrando polimorfismo:")
for animal in animales:
    print(f"{animal.nombre}: {animal.hacer_sonido()}")

# ============================================================================
# 5. EJEMPLO COMPLETO - SISTEMA DE VEHÍCULOS
# ============================================================================
print("\n5. SISTEMA COMPLETO DE VEHÍCULOS")
print("-" * 40)

class Vehiculo:
    def __init__(self, marca: str, modelo: str) -> None:
        self.marca: str = marca
        self.modelo: str = modelo

    def descripcion(self) -> str:
        return f"{self.marca} {self.modelo}"

class Carro(Vehiculo):
    def descripcion(self) -> str:
        return f"Carro: {self.marca} {self.modelo}"

class Moto(Vehiculo):
    def descripcion(self) -> str:
        return f"Moto: {self.marca} {self.modelo}"

# Crear vehículos
vehiculos: list[Vehiculo] = [Carro("Toyota", "Corolla"), Moto("Yamaha", "MT-07")]

print("Descripción de vehículos:")
for v in vehiculos:
    print(f"  {v.descripcion()}")

print("\n¡Ejemplos completados exitosamente!")
print("=" * 50)
