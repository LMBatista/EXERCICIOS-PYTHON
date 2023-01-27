class veiculo:
    def __init__(self,nome,velocidade_maxima,quilometros_percorridos_por_litro):
        self.nome=nome
        self.velocidade_maxima=velocidade_maxima
        self.quilometros_percorridos_por_litro=quilometros_percorridos_por_litro
     
    def tostr(self):
      print(f'nome={self.nome}')
      print(f'velocidade_maxima={self.velocidade_maxima}')
      print(f'quilometros_percorridos_por_litro={self.quilometros_percorridos_por_litro}')
  
modelo_carro = veiculo ("Camaro",300,5)
modelo_carro.tostr()

class onibus(veiculo):
    pass
onibus_escolar=onibus("Volksvagem",180,15)
onibus_escolar.tostr()
        
