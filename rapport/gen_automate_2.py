#! /usr/local/bin/python3
# coding: utf-8
from sys import argv
import itertools



if __name__ == '__main__':
    if len(argv)<2:
        print("usage : ./gen_automate_XX.py n_philosophes [n_canaux (si non fourni -> n_canaux = nbr_philos+1)]")
        pass
    nbr_philos = int(argv[1])
    nbr_canaux = nbr_philos
    if len(argv)>2:
        nbr_canaux =int(argv[2])
    cycle = nbr_canaux==nbr_philos+1


    sys_philo="""P = [T,H,E] {
    etat = 3;
    init = 0;
    0=T;
    1=H;
    2=E;
    0 -> 1 [F];
    1 -> 2 [M];
    2 -> 0 [T];

    };;
    """
    sys_canal="""
    C = [P,V] {
    etat = 2;
    init = 1;
    0=P;
    1=V;
    0 -> 1 [V];
    1 -> 0 [P];
    };;
    """

    s=""
    s+=sys_philo+sys_canal
    s += "systeme = <"
    s += ",".join(["P p" + str(i) for i in range(nbr_philos)]) + "," + ",".join(["C c" + str(i) for i in range(nbr_canaux)]) + "> {\n"
    for philo in range(nbr_philos):
        s += "<" + ",".join(["F" if i == philo else "_" for i in range(nbr_philos)])
        s += "," + ",".join(["P" if i == philo  else "_" for i in range(nbr_canaux)])
        s+=">;\n"
        s += "<" + ",".join(["F" if i == philo else "_" for i in range(nbr_philos)])
        s += "," + ",".join(["P" if i - 1 == philo  else "_" for i in range(nbr_canaux)])
        s+=">;\n"

        s += "<" + ",".join(["M" if i == philo else "_" for i in range(nbr_philos)])
        s += "," + ",".join(["P" if i == philo  else "_" for i in range(nbr_canaux)])
        s+=">;\n"
        s += "<" + ",".join(["M" if i == philo else "_" for i in range(nbr_philos)])
        s += "," + ",".join(["P" if i - 1 == philo  else "_" for i in range(nbr_canaux)])
        s+=">;\n"





        s += "<" + ",".join(["T" if i == philo  else "_" for i in range(nbr_philos)])
        s += "," + ",".join(["V" if i == philo  or i-1 == philo else "_" for i in range(nbr_canaux)])
        s+=">;\n"


    s += "};;\n"
    s+="todot verif_test_"+str(nbr_philos)+"_"+str(nbr_canaux)+".dot systeme;;\n"
    print(s)
