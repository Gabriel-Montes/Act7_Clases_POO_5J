print("Programacion POO")

class Perro:
    nombre="BOB"
    ed=4
    def m(self):
        print("Muerde")
    def d_p(self,nombre,ed):
        print(f"Nombre: {nombre} edad:{ed}")

los=Perro()

los.d_p("bob",5)
los.m()

# python claseperro.py