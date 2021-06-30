import scipy.stats as stats
import statistics as stat
import pandas as pd
from statsmodels.stats.multicomp import pairwise_tukeyhsd


'''
Nous avons un jeu de données de 5 échantillons dont chacun correspond à un continent et 
reprend différents valeurs de GPD pour ce continent 
'''

Africa = [5288.040382, 2773.287312, 1372.877931, 11003.60508, 1037.645221, 446.4035126, 1934.011449,1156.18186, 1075.811558, 1908.260867, 4754.604414, 7703.4959, 765.3500015, 530.0535319, 12521.71392, 660.5855997, 1111.984578, 945.5835837, 575.7047176, 1287.514732, 1275.184575,531.4823679, 9534.677467, 894.6370822, 665.4231186, 951.4097518, 1579.019543, 9021.815894, 3258.495584,633.6179466, 4072.324751,601.0745012, 1615.286395,785.6537648,1519.635262, 699.489713,882.0818218,7710.946444,1993.398314,4128.116943,899.0742111,886.2205765,5722.,927.7210018,1071.613938,672.0386227]
Americas = [8797.640716, 3413.26269, 8131.212843, 33328.96507, 10778.78385, 5755.259962, 7723.447195, 6340.646683, 5773.044512, 5351.568666, 4858.347495, 1270.364932, 3099.72866, 6994.774861, 10742.44053, 2474.548819, 7356.031934, 3783.674243, 5909.020073, 11460.60023, 39097.09955, 7727.002004, 8605.047831]
Asia = [726.7340548, 23403.55927, 1136.39043, 896.2260153, 3119.280896,  1746.769454, 2873.91287, 9240.761975, 4390.717312, 21905.59514, 28604.5919, 3844.917194, 35110.10566, 9313.93883, 10206.97794, 2140.739323, 1057.206311, 19774.83687, 2092.712441, 2650.921068, 19014.54118, 36023.1054, 3015.378833, 4090.925331, 5913.187529, 1764.456677]
Europe = [4604.211737, 32417.60769, 30485.88375, 6018.975239, 7696.777725, 11628.38895, 32166.50006, 28204.59057, 28926.03234, 30035.80198, 22514.2548, 14843.93556, 31163.20196, 34077.04939, 27968.09817, 33724.75778, 44683.97525, 12002.23908, 19970.90787, 7885.360081, 20660.01936, 24835.47166, 29341.63093, 34480.95771, 6508.085718, 29478.99919]
Oceania = [30687.75473, 23189.80135,26938.77804];



#La fonction comp permet d'évaluer la valeur de la pvalue afin de nous permettre de savoir si 
#L'hypothèse correspondante est valide 
def comp(pvalue):
    if pvalue<0.05:
        print("H0 est a rejeter")
        print("pvalue = ",pvalue )
    else : print("On ne peut pas rejetter l'hypothése avec un niveau de confiance de 95%")


#On vérifie les hypothéses du modèle

print("--------------------------------------")
print("Vérification des hypothèses du modèle")
print("--------------------------------------")
print("Pour le test d'homoscédasticité\n")
y, pvalue = stats.bartlett(Africa,Asia,Americas,Europe,Oceania);
comp(pvalue);

print("\n--------------------------------------")
print("Pour les tests de normalité \n")
print(" \nL'Afrique : ")
n,Pval2 = stats.shapiro(Africa);
comp(Pval2);
print(" \nL'Amérique : ")
n,Pval3 = stats.shapiro(Americas);
comp(Pval3);
print(" \nL'Asie : ")
n,Pval4 = stats.shapiro(Asia);
comp(Pval4);
print("\nL'Océanie : ")
n,Pval5 = stats.shapiro(Oceania);
comp(Pval5);
print(" \nL'Europe :")
n,Pval6 = stats.shapiro(Europe);
comp(Pval6);

#Calcul de l'ANOVA

print("-----------------------------------")
print("ANOVA à un facteur\n")

anova,pAnova=stats.f_oneway(Americas, Asia,Europe,Oceania)
comp(pAnova)



print("-----------------------------------")
print("Etude approfondie grace aux tests à priori - contastes")

#Etant donné que les moyennes ne sont pas identique nous devons faire une étude approfondie

#Test à priori grace aux contrastes

#K est une matrice contenant l'ensemble des observations 
K=[[5288.040382, 2773.287312, 1372.877931, 11003.60508, 1037.645221, 446.4035126, 1934.011449,1156.18186, 1075.811558, 1908.260867, 4754.604414, 7703.4959, 765.3500015, 530.0535319, 12521.71392, 660.5855997, 1111.984578, 945.5835837, 575.7047176, 1287.514732, 1275.184575,531.4823679, 9534.677467, 894.6370822, 665.4231186, 951.4097518, 1579.019543, 9021.815894, 3258.495584,633.6179466, 4072.324751,601.0745012, 1615.286395,785.6537648,1519.635262, 699.489713,882.0818218,7710.946444,1993.398314,4128.116943,899.0742111,886.2205765,5722.,927.7210018,1071.613938,672.0386227],
[8797.640716, 3413.26269, 8131.212843, 33328.96507, 10778.78385, 5755.259962, 7723.447195, 6340.646683, 5773.044512, 5351.568666, 4858.347495, 1270.364932, 3099.72866, 6994.774861, 10742.44053, 2474.548819, 7356.031934, 3783.674243, 5909.020073, 11460.60023, 39097.09955, 7727.002004, 8605.047831],
[726.7340548, 23403.55927, 1136.39043, 896.2260153, 3119.280896,  1746.769454, 2873.91287, 9240.761975, 4390.717312, 21905.59514, 28604.5919, 3844.917194, 35110.10566, 9313.93883, 10206.97794, 2140.739323, 1057.206311, 19774.83687, 2092.712441, 2650.921068, 19014.54118, 36023.1054, 3015.378833, 4090.925331, 5913.187529, 1764.456677],
[4604.211737, 32417.60769, 30485.88375, 6018.975239, 7696.777725, 11628.38895, 32166.50006, 28204.59057, 28926.03234, 30035.80198, 22514.2548, 14843.93556, 31163.20196, 34077.04939, 27968.09817, 33724.75778, 44683.97525, 12002.23908, 19970.90787, 7885.360081, 20660.01936, 24835.47166, 29341.63093, 34480.95771, 6508.085718, 29478.99919],
[30687.75473, 23189.80135,26938.77804]];

#On calcul la moyenne de chaque échantillion

µ = [stat.mean(Africa),
stat.mean(Americas),
stat.mean(Asia),
stat.mean(Europe),
stat.mean(Oceania),
]

#n est un vecteur qui contient la taille de chaque échantillion
n = [len(Africa), len(Americas), len(Asia), len(Europe), len(Oceania)];


#Fonction qui calcul le nombre total des relevés

def tot (n):
   S=0
   for i in range(len(n)):
        S=S+n[i]
   return S

TotalDeRelvés = tot(n);


#Calcul de la somme des carrés
def SCw(c,µ):
    S=0;
    for i in range(len(µ)):
        S=S+ c[i]*µ[i]
    N=S**2
    D=0
    for i in range(len(c)):
        D=D+((c[i]**2)*(1/n[i]));
    SCw=N/D
    return SCw


#Calcul de la statistique F (MCw/MCres)

#Calcul des SCres

def SCres(K,µ):
    SCres=0;
    rows = len(K)    
    columns = n    
    for i in range(rows):
        for j in range(columns[i]) :
            SCres = SCres + (K[i][j]-µ[i])**2;
    return SCres


print("\n-----------------------------------")
print("On oppose l'Afrique aux autres continents \n")
contraste1=[4,-1,-1,-1,-1];

SCw1=SCw(contraste1,µ)
print("\n SCw : ", SCw1, "\n")

SC1 = SCres(K,µ);
print("\n SC : ", SC1, "\n")

MCw1 = SCw1;


MCres1=SC1/(TotalDeRelvés-5);


F=SCw1/MCres1;


p_value = 1 - stats.f.cdf(F, 4 ,TotalDeRelvés-5)

print("p_value : ", p_value, "\n")

comp(p_value)


print("\n-----------------------------------")
print("On oppose l'Amérique et l'Europe à l'Asie et l'Océanie \n")

contraste2=[0,1,-1,1,-1];


SCw2=SCw(contraste2,µ)
print("\n SCw : ", SCw2, "\n")

SC2 = SCres(K,µ);
print("\n SC : ", SC2, "\n")

MCw1 = SCw2;


MCres2=SC2/(TotalDeRelvés-5);


F=SCw2/MCres2;


print("\n F : ", F, "\n")




p_value = 1 - stats.f.cdf(F, 4 ,TotalDeRelvés-5)

print("p_value : ", p_value, "\n")

comp(p_value)

print("-----------------------------------")
print("Etude approfondie grace aux tests à prosteriori - Tucky-Kramer")

all_GDP = Africa + Americas + Asia +Europe + Oceania;

continent = (['Africa']*len(Africa)) + (['Americas']*len(Americas)) + (['Asia']*len(Asia)) + (['Europe']*len(Europe)) + (['Oceania']*len(Oceania))

data = pd.DataFrame({'continent' : continent, 'GDP': all_GDP})

m_comp = pairwise_tukeyhsd(endog=data['GDP'], groups=data['continent'], alpha=0.05)
print(m_comp)


# On utilise le test kruskal qui est un équivalent de l'ANOVA mais ne nécessite pas de
# vérification d'hypothéses



print("\n-----------------------------------")
print("On test l'hypothése d'égalité des médianes de tout les continents \n")

kruskal, pk1 = stats.kruskal(Africa,Americas, Asia,Europe,Oceania);
comp(pk1);

print("\n-----------------------------------")
