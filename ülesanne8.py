class auto:

    mark = 'teadmata'
    aasta = 0
    hind = 0
    kiirus = 0
    varv = 'teadmata'
    
    def lisamark(self,a):
        self.mark = a
        
    def lisaaasta(self,a):
        self.aasta = a
        
    def lisahind(self,a):
        self.hind = a
    
    def lisavarv(self,a):
        self.varv = a
        
    def lisakiirus(self,a):
        self.kiirus = a
        
        
    def kuva(self):
        print(f'mark: {self.mark} \nAasta: {self.aasta} \nHind {self.hind}€ \nkiirus {self.kiirus} km/h \nvärv {self.varv}')

auto1 = auto()
auto1.lisamark('auto1')
auto1.lisaaasta(1992)
auto1.lisahind(2000)
auto1.lisakiirus(69)
auto1.lisavarv('must')
auto1.kuva()

print()

auto2 = auto()
auto2.lisamark('auto1')
auto2.lisaaasta(1969)
auto2.lisahind(42000)
auto2.lisakiirus(420)
auto2.lisavarv('valge')
auto2.kuva()