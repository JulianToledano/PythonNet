import sys # Argumentos por linea de comandos
import whois
# whois de la maquina objetivo
def who_is(domains):
    u = whois.whois(domains)
    print u.name

def main():
    print "Bienvenido a net scan:"
    domains = sys.argv[1]
    who_is(domains)

if __name__ == "__main__":
    main()
