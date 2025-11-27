#### Fonctions secondaires

# imports
from plotly.graph_objects import Scatter, Figure

### NEPASMODIFIER ###
def syr_plot(lsyr):
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({  'layout':   { 'title': {'text': title},
                                'xaxis': {'title': {'text':"x"}},
                                'yaxis': {'title': {'text':"y"}},
                                }
                }
    )

    x = [ i for i in range(len(lsyr)) ]
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color = "blue")
    fig.add_trace(t)
    fig.show()
    return None
#######################

def syracuse_l(n):
    """retourne la suite de Syracuse de source n"""
    
    l = [n]  # on commence par la source

    u = n
    while u != 1:
        if u % 2 == 0:
            u = u // 2
        else:
            u = 3 * u + 1
        l.append(u)

    return l


def temps_de_vol(l):
    """Retourne le temps de vol d'une suite de Syracuse"""
    # temps de vol = index où la suite atteint 1 = longueur - 1
    return len(l) - 1


def temps_de_vol_en_altitude(l):
    """Retourne le temps de vol en altitude d'une suite de Syracuse"""
    n = l[0]  # altitude de départ

    # on cherche le premier indice k tel que l[k] < n
    for k in range(len(l)):
        if l[k] < n:
            return k
    return 0  # par sécurité, même si cela n'arrive jamais pour n > 1


def altitude_maximale(l):
    """retourne l'altitude maximale d'une suite de Syracuse"""
    return max(l)


#### Fonction principale

def main():

    lsyr = syracuse_l(15)
    syr_plot(lsyr)
    
    print("temps de vol :", temps_de_vol(lsyr))
    print("temps de vol en altitude :", temps_de_vol_en_altitude(lsyr))
    print("altitude maximale :", altitude_maximale(lsyr))


if __name__ == "__main__":
    main()
