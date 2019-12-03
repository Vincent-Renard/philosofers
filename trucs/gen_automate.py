#! /usr/bin/env pypy3
# coding: utf-8

from sys import argv
import itertools

if __name__ == '__main__':

    nbr_philos = 4  # argv[1]

    state_HUNGRY = 'HUNGRY'
    state_THINK = 'THINK'
    state_EAT = 'EAT'

    s = "systeme = <"
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

    s += "};;"
    print(s)
