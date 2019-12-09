#! /usr/local/bin/python3
# coding: utf-8
from sys import argv
import itertools
if __name__ == '__main__':
    if len(argv)<2:
        print("usage : ./gen_automate_XX.py n_philosophes [n_canaux (si non fourni -> n_canaux = nbr_philos)]")
    nbr_philos = int(argv[1]) #TODO metre mode d'emploi si l'argument n'est pas fourni
    nbr_canaux = nbr_philos-1

    if len(argv)>2:
        nbr_canaux =int(argv[2])


    sys_philo=
"""
P = [T,,E] {
etat = 3;
init = 0;
0=T;
1=H;
2=E;
0 -> 1 [T];
1 -> 2 [H];
2 -> 3 [E];
3 -> 0 [T];
};;
"""
    sys_canal=
"""
C = [P,V] {
etat = 2;
init = 0;
0=P;
1=V;
0 -> 1 [V];
1 -> 0 [P];
};;
"""
"""

<T,H,E,P,V,P>


"""

    s=""
    s+=sys_philo+sys_canal
    s += "systeme = <"
    s += ",".join(["P p" + str(i) for i in range(nbr_philos)]) + "," + ",".join(["C c" + str(i) for i in range(nbr_canaux)]) + "> {\n"
    for philo in range(nbr_philos):
        s += "<" + ",".join(["H" if i == philo else "_" for i in range(nbr_philos)])
        s += "," + ",".join(["V" if i == philo else "_" for i in range(nbr_canaux)])

        s += "<" + ",".join(["E" if i == philo else "_" if (i - 1) == philo or (i + 1) == philo else "_" for i in range(nbr_philos)])
        s += "," + ",".join(["_" for i in range(nbr_canaux)]) + ">;\n"
        s += "<" + ",".join(["E" if i == philo else "remainHE" if (i - 1) == philo else "_" if (i + 1) == philo else "_" for i in range(nbr_philos)])
        s += "," + ",".join(["T" if i == philo else "_" for i in range(nbr_canaux)]) + ">;\n"
        s += "<" + ",".join(["E" if i == philo else "_" if (i - 1) == philo else "remainHE" if (i + 1) == philo else "_" for i in range(nbr_philos)])
        s += "," + ",".join(["addR" if (i + 1) == philo else "_" for i in range(nbr_canaux)]) + ">;\n"
        s += "<" + ",".join(["E" if i == philo else "remainHE" if (i - 1) == philo or (i + 1) == philo else "_" for i in range(nbr_philos)])
        s += "," + ",".join(["T" if i == philo else "addR" if (i + 1) == philo else "_" for i in range(nbr_canaux)]) + ">;\n"
        s += "\n"
    for i in range(nbr_philos):
        s += "<" + ",".join(["goE" if j == i else "_" for j in range(nbr_philos)])
        s += "," + ",".join(["remainNL" if (i - 1) == j else "remainNR" if i == j else "_" for j in range(nbr_canaux)]) + ">;\n"
    s += "\n"
    for i in range(nbr_philos):
        s += "<" + ",".join(["goT" if j == i else "_" for j in range(nbr_philos)])
        s += "," + ",".join(["delL" if (i - 1) == j else "delR" if i == j else "_" for j in range(nbr_canaux)]) + ">;\n"
    s += "};;\n"
    s+="todot verif_test_"+str(nbr_philos)+"_"+str(nbr_canaux)+".dot systeme;;\n"
    print(s)
