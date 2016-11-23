import sys              # Argumentos por linea de comandos
import whois
import os
import dns.resolver     # MS y NX

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

# Clasificacion de sistemas NS y MX
def MX_NS(name_domain):
    #NS
    answers = dns.resolver.query(name_domain, 'NS')
    for rdata in answers:
        print 'Nss: ', rdata.target
    #MX
    answers = dns.resolver.query(name_domain, 'MX')
    for rdata in answers:
        print 'Hosts: ', rdata.exchange, 'con preferencia', rdata.preference

def main():
    print "Bienvenido a net scan:"
    name = sys.argv[1]
    ping(name)
    MX_NS(name)
    
if __name__ == "__main__":
    main()
