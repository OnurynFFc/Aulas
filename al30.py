'''
CONSTANTE = "variaveis" que não mudam
Muitas condições do IF(ruim)
    <- Contagem de complexidade (ruim)
'''
velocidade = 50 #velocidade atual do carro
local_carro = 101 #local em que o caari está na estrada

RADAR_1 = 60 
LOCAL_1 = 100
RADAR_RANGE = 1

vel_car_radar = velocidade > RADAR_1
carro_multado = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro  <= (LOCAL_1+RADAR_1)

carro_multado_radar1=carro_multado and vel_car_radar

if vel_car_radar:
    print("multa")

if carro_multado:
    print('carro passou pelo radar 1')

if carro_multado and vel_car_radar:
    print('multa')