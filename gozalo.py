class producto:
    def __init__(self,nombre,precio,cantstock,idproveedor):
        self.nombre=nombre
        self.precio=precio
        self.cantstock=cantstock
        self.idproveedor=idproveedor
    def mostrar (self):
            print("producto:", self.nombre)
            print("precio:", self.precio)
            print("cantstock", self.cantstock)
            print("idproveedor", self.idproveedor)
while True:
     op=int(input("Menu:\n 1-Agregar producto\n 2-mostrar producto \n 3-salir"))
     if op==1:
         objeto=input("ingrese nombre de objeto a crear:")
         ip=int(input("ingrese codigo de producto: "))
         nom=input("ingrese nombre del producto: ")
         stock=int(input("ingrese stock: "))
         prec=float(input("ingrese precio: "))
         iprov=int(input("ingrese el codigo del proveedor: "))
         objeto1=producto(ip,nom,s,p,iprov)
     elif op=="S" or "s":
         objeto=input("ingrese nombre de objeto a crear:")
         ip=int(input("ingrese codigo de producto: "))
         nom=input("ingrese nombre del producto: ")
         stock=int(input("ingrese stock: "))
         prec=float(input("ingrese precio: "))
         iprov=int(input("ingrese el codigo del proveedor: "))
         objeto2=producto(ip,nom,s,p,iprov)
     elif op=="N" or "n":
         
     elif op==2:
         objeto.mostrar()
         objeto.mostrar()
     elif op==3:
        print("cerrado") 
        break       