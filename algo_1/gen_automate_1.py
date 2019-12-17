#! /usr/local/bin/python3
# coding: utf-8

from sys import argv
import itertools

if __name__ == '__main__':
    nbr_philos = int(argv[1]) #TODO metre mode d'emploi si l'argument n'est pas fourni
    nbr_canaux = nbr_philos - 1

    GO_H = "Faim"
    GO_E = "Repas"
    GO_T = "Reflexion"
    REMAIN_T = "remainT"
    REMAIN_HE = "remainHE"
    ADD_L = "addL"
    ADD_R = "addR"
    DEL_L = "delL"
    DEL_R = "delR"
    REMAIN_NL = "remainNL"
    REMAIN_NR = "remainNR"

    sys_philo=f"""
P = [T,H,E] {{
etat = 3;
init = 0;
0=T;
1=H;
2=E;
0 -> 1 [{GO_H}];
1 -> 2 [{GO_E}];
2 -> 0 [{GO_T}];
0 -> 0 [{REMAIN_T}];
1 -> 1 [{REMAIN_HE}];
2 -> 2 [{REMAIN_HE}];
}};;
"""
    sys_canal=f"""
C = [N,L,R] {{
etat = 3;
init = 0;
0=N;
1=L;
2=R;
0 -> 1 [{ADD_L}];
0 -> 2 [{ADD_R}];
0 -> 0 [{DEL_L}];
1 -> 0 [{DEL_L}];
0 -> 0 [{DEL_R}];
2 -> 0 [{DEL_R}];
0 -> 0 [{REMAIN_NL}];
1 -> 1 [{REMAIN_NL}];
0 -> 0 [{REMAIN_NR}];
2 -> 2 [{REMAIN_NR}];
}};;
"""
    s=""
    s+=sys_philo+sys_canal
    s += "systeme = <"
    s += ",".join(["P p" + str(i) for i in range(nbr_philos)]) + "," + ",".join(
        ["C c" + str(i) for i in range(nbr_canaux)]) + "> {\n"
    for philo in range(nbr_philos):
        s += "<" + ",".join([GO_H if i == philo else REMAIN_T if (i - 1) % nbr_philos == philo or (i + 1) % nbr_philos == philo else "_" for i in range(nbr_philos)])
        s += "," + ",".join(["_" for i in range(nbr_canaux)]) + ">;\n"

        s += "<" + ",".join([GO_H if i == philo else REMAIN_HE if (i - 1) % nbr_philos == philo else REMAIN_T if (i + 1) % nbr_philos == philo else "_" for i in range(nbr_philos)])
        s += "," + ",".join([ADD_L if i == philo else "_" for i in range(nbr_canaux)]) + ">;\n"

        s += "<" + ",".join([GO_H if i == philo else REMAIN_T if (i - 1) % nbr_philos == philo else REMAIN_HE if (i + 1) % nbr_philos == philo else "_" for i in range(nbr_philos)])
        s += "," + ",".join([ADD_R if (i + 1) % nbr_canaux == philo else "_" for i in range(nbr_canaux)]) + ">;\n"

        s += "<" + ",".join([GO_H if i == philo else REMAIN_HE if (i - 1) % nbr_philos == philo or (i + 1) % nbr_philos == philo else "_" for i in range(nbr_philos)])

        s += "," + ",".join([ADD_L if i == philo else ADD_R if (i + 1) % nbr_canaux == philo else "_" for i in range(nbr_canaux)]) + ">;\n"
        s += "\n"
    for i in range(nbr_philos):
        s += "<" + ",".join([GO_E if j == i else "_" for j in range(nbr_philos)])
        s += "," + ",".join([REMAIN_NL if (i - 1) % nbr_canaux == j else REMAIN_NR if i == j else "_" for j in range(nbr_canaux)]) + ">;\n"
    s += "\n"
    for i in range(nbr_philos):
        s += "<" + ",".join([GO_T if j == i else "_" for j in range(nbr_philos)])
        s += "," + ",".join([DEL_L if (i - 1) % nbr_canaux == j else DEL_R if i == j else "_" for j in range(nbr_canaux)]) + ">;\n"

    s += "};;\n"
    s+="todot verif_test_"+str(nbr_philos)+"_"+str(nbr_canaux)+".dot systeme;;\n"
    print(s)
