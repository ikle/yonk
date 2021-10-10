#!/usr/bin/python3

class Point:
	def __init__ (o, name, title):
		o.name  = name
		o.title = title

class Typed (Point):
	def __init__ (o, name, title, types = None):
		super ().__init__ (name, title)
		o.types = types if types != None else ["string"]


class Group (Point):
	def __init__ (o, name, title):
		super ().__init__ (name, title)

class Node (Typed):
	def __init__ (o, name, title, types = None):
		super ().__init__ (name, title, types)

class Attr (Typed):
	def __init__ (o, name, title, types = None):
		super ().__init__ (name, title, types)

