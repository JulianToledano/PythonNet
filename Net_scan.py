import sys              # Argumentos por linea de comandos
import whois
import os
import dns.resolver     # MS y NX. pip install dnspython
import nmap             # nmap. pip install python-namp

# whois de la maquina objetivo
def who_is(name_domain):
    print 'Realizando whois a', name_domain
    u = whois.whois(name_domain)
    print u # Imprime toda la informacion

# Ping
def ping(name_domain):
    print 'Enviando ping a', name_domain
    response = os.system("ping -c 1 " + name_domain)
    if response == 0:
        print name_domain, 'is up!'
    else:
        print name_domain, 'is down!'

# Clasificacion de sistemas NS y MX
def MX_NS(name_domain):
    print 'Clasificando los sistemas NS y MX de', name_domain
    #NS
    answers = dns.resolver.query(name_domain, 'NS')
    for rdata in answers:
        print 'Nss: ', rdata.target
    print '\n'
    #MX
    answers = dns.resolver.query(name_domain, 'MX')
    for rdata in answers:
        print 'Hosts: ', rdata.exchange, 'con preferencia', rdata.preference

# Deteccion de puertos
def ports_detection(name_domain):
    print 'Detectando los 100 puertos mas comunes en', name_domain
    nm = nmap.PortScanner()
    nm.scan(name_domain, arguments = '-F')
    print nm.csv()

def helpp(name):
    print 'Bienvenido a net Scan:'
    print '[argumento] [nombre dominio, IP]'
    print '-w para realizar un whois'
    print '-p para realizar un ping'
    print '-sx para clasificar sistemas NS y MX'
    print '-n para analizar los 100 puertos mas utilizados'
    print '-h para obtener informacion'
    print 'Ejemplo: -p google.com'

def main():

    options = {
        '-w' : who_is,
        '-p' : ping,
        '-sx' : MX_NS,
        '-n' : ports_detection,
        '-h' : helpp,
    }
    # Comprobamos que el numero de argumentos pasados por la linea de comandos
    # son los necesarios y que ademas son validos
    try:
        argument = sys.argv[1]
        name = sys.argv[2]
        options[argument](name)
    except:
        helpp(-1)


if __name__ == "__main__":
    main()
