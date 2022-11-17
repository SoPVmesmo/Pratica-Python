#se tiver em outra pasta basta colocar . EX:pasta.arquivo
#metodo 01 chama so uma função mas não precisa colocar o nome do arquivo antes
from funçoes02 import soma,ano
soma()

#medoto 02 chama geral preciso declarar o nome do arquivo antes do nome da função
import funçoes02
funçoes02.ano()

#metodo 03 puxa todas mas n precisa declarar o nodo do arquivo antes
from funçoes02 import *
soma()