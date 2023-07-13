# Carolina González Leal A01284948
# Erick Siller Ojeda A01382929
# Ozner Axel Leyva Mariscal A01742377
# Santiago Martínez Vallejo A00571878
# Valeria Enríquez Limón A00832782

import re


class Node:

  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None


def insert(root, data):
  if root is None:
    return Node(data)
  if data < root.data:
    root.left = insert(root.left, data)
  else:
    root.right = insert(root.right, data)
  return root


def printTree(root, level=0):
  if root is not None:
    printTree(root.right, level + 1)
    print("|   " * level + "|--", root.data)
    printTree(root.left, level + 1)


def buildBinaryTree(numbers):
  root = Node(numbers[0])
  for num in numbers[1:]:
    insert(root, num)
  return root


def readFile(file_path):
  with open(file_path, 'r') as file:
    numbers_str = file.read()
    numbers = readInput(numbers_str)
  return numbers


def readInput(input_str):
  numbers_list = re.findall(r'\d+', input_str)
  numbers = [int(num) for num in numbers_list]
  return numbers


def menu():
  choice = input("Escoja un método: 1 - Terminal, 2 - Archivo: ")

  if choice == "1":
    numbers_str = input("Ingresa los numeros en el formato {1, 2, 3, ...}: ")
    numbers = readInput(numbers_str)
  elif choice == "2":
    file_path = input("Ingresa el nombre del archivo: ")
    numbers = readFile(file_path)
  else:
    print("Opción inválida!")
    return

  root = buildBinaryTree(numbers)
  printTree(root)


menu()