#! /usr/bin/env pypy3
# coding: utf-8

from sys import argv
import itertools

if __name__ == '__main__':

    nbr_philos = 4  # argv[1]
    sys_philo="P = [T,H,E] {\netat = 3;\ninit = 0;\n0=T;\n1=H;\n2=E;\n0 -> 1 [goH];\n1 -> 2 [goE];\n2 -> 0 [goT];\n0 -> 0 [remainT];\n1 -> 1 [remainHE];\n2 -> 2 [remainHE];\n};;\n"
    sys_canal="C = [N,L,R] {\netat = 3;\ninit = 0;\n0=N;\n1=L;\n2=R;\n0 -> 1 [addL];\n0 -> 2 [addR];\n0 -> 0 [delL];\n1 -> 0 [delL];\n0 -> 0 [delR];\n2 -> 0 [delR];\n0 -> 0 [remainNL];\n1 -> 1 [remainNL];\n0 -> 0 [remainNR];\n2 -> 2 [remainNR];\n};;\n"
    state_HUNGRY = 'HUNGRY'
    state_THINK = 'THINK'
    state_EAT = 'EAT'
    s=""
    s+=sys_philo+sys_canal
    s += "systeme = <"
    s += ",".join(["P p" + str(i) for i in range(nbr_philos)]) + "," + ",".join(
        ["C c" + str(i) for i in range(nbr_philos)]) + "> {\n"

    for philo in range(nbr_philos):
        s += "<" + ",".join(["goH" if i == philo else "remainT" if (i - 1) % nbr_philos == philo or (i + 1) % nbr_philos == philo else "_" for i in range(nbr_philos)])
        s += "," + ",".join(["_" for i in range(nbr_philos)]) + ">;\n"

        s += "<" + ",".join(["goH" if i == philo else "remainHE" if (i - 1) % nbr_philos == philo else "remainT" if (i + 1) % nbr_philos == philo else "_" for i in range(nbr_philos)])
        s += "," + ",".join(["addL" if i == philo else "_" for i in range(nbr_philos)]) + ">;\n"

        s += "<" + ",".join(["goH" if i == philo else "remainT" if (i - 1) % nbr_philos == philo else "remainHE" if (i + 1) % nbr_philos == philo else "_" for i in range(nbr_philos)])
        s += "," + ",".join(["addR" if (i + 1) % nbr_philos == philo else "_" for i in range(nbr_philos)]) + ">;\n"

        s += "<" + ",".join(["goH" if i == philo else "remainHE" if (i - 1) % nbr_philos == philo or (i + 1) % nbr_philos == philo else "_" for i in range(nbr_philos)])
        s += "," + ",".join(["addL" if i == philo else "addR" if (i + 1) % nbr_philos == philo else "_" for i in range(nbr_philos)]) + ">;\n"
        s += "\n"

    for i in range(nbr_philos):
        s += "<" + ",".join(["goE" if j == i else "_" for j in range(nbr_philos)])
        s += "," + ",".join(["remainNL" if (i - 1) % nbr_philos == j else "remainNR" if i == j else "_" for j in range(nbr_philos)]) + ">;\n"
    s += "\n"

    for i in range(nbr_philos):
        s += "<" + ",".join(["goT" if j == i else "_" for j in range(nbr_philos)])
        s += "," + ",".join(["delL" if (i - 1) % nbr_philos == j else "delR" if i == j else "_" for j in range(nbr_philos)]) + ">;\n"

    s += "};;\n"

    s+="todot verif_test.dot systeme;;\n"


    print(s)
