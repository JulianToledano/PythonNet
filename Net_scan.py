import sys # Argumentos por linea de comandos
import whois
import os
# whois de la maquina objetivo
def who_is(name_domain):
    u = whois.whois(name_domain)
    print u # Imprime toda la informacion

# Ping
def ping(name_domain):
    response = os.system("ping -c 1 " + name_domain)
    if response == 0:
        print name_domain, 'is up!'
    else:
        print name_domain, 'is down!'

def main():
    print "Bienvenido a net scan:"
    name = sys.argv[1]
    ping(name)

if __name__ == "__main__":
    main()
