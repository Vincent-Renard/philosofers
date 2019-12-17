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
    sys_canal="""
C = [N,L,R] {
etat = 3;
init = 0;
0=N;
1=L;
2=R;
0 -> 1 [addL];
0 -> 2 [addR];
0 -> 0 [delL];
1 -> 0 [delL];
0 -> 0 [delR];
2 -> 0 [delR];
0 -> 0 [remainNL];
1 -> 1 [remainNL];
0 -> 0 [remainNR];
2 -> 2 [remainNR];
};;
"""
    state_HUNGRY = 'HUNGRY'
    state_THINK = 'THINK'
    state_EAT = 'EAT'
    s=""
    s+=sys_philo+sys_canal
    s += "systeme = <"
    s += ",".join(["P p" + str(i) for i in range(nbr_philos)]) + "," + ",".join(
        ["C c" + str(i) for i in range(nbr_canaux)]) + "> {\n"
    for philo in range(nbr_philos):
        s += "<" + ",".join(["goH" if i == philo else "remainT" if (i - 1) == philo or (i + 1) == philo else "_" for i in range(nbr_philos)])
        s += "," + ",".join(["_" for i in range(nbr_canaux)]) + ">;\n"
        s += "<" + ",".join(["goH" if i == philo else "remainHE" if (i - 1) == philo else "remainT" if (i + 1) == philo else "_" for i in range(nbr_philos)])
        s += "," + ",".join(["addL" if i == philo else "_" for i in range(nbr_canaux)]) + ">;\n"
        s += "<" + ",".join(["goH" if i == philo else "remainT" if (i - 1) == philo else "remainHE" if (i + 1) == philo else "_" for i in range(nbr_philos)])
        s += "," + ",".join(["addR" if (i + 1) == philo else "_" for i in range(nbr_canaux)]) + ">;\n"
        s += "<" + ",".join(["goH" if i == philo else "remainHE" if (i - 1) == philo or (i + 1) == philo else "_" for i in range(nbr_philos)])
        s += "," + ",".join(["addL" if i == philo else "addR" if (i + 1) == philo else "_" for i in range(nbr_canaux)]) + ">;\n"
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
