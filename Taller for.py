class For: 
    def __init__(self):
        self.numero=0
    
    def usoFor(self):
       nombre = "Fernanda"
       datos=["Fernanda",20,True]
       numeros=(2,5,6,4,1)
       docente = {"nombre": "Fernanda","edad":20,"fac": "faci"}
       listanotas = [(30,40),(20,40,50),(50,40)]
       listaalumnos = [{"nombre":"maria","fianl":70},{"nombre":"Yessenia","fianl":60},{"nombre":"Fabian","fianl":90}] 
       for i in range(5):
           print("i={}".format(i))   
bucle = For()
bucle.usoFor()
print(bucle.nombre)      
