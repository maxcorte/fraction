class Fraction:
    """Classe représentant une fraction et ses opérations associées.

    Auteur : Delcorte Maxime
    Date : decembre 2023
    Cette classe permet la manipulation des fractions à travers plusieurs opérations.
    """

    def __init__(self, num=0, den=1):
        """Initialise une fraction avec un numerateur et un denominateur.

        PRÉ :   -num est le numerateur de la fraction, den est le denominateur de la fraction

        POST :  -La fraction est initialisée avec le numerateur et le denominateur donnés.
                -la fraction doit être simplifiée grâce à la méthode pgcd().
        RAISE:  ZeroDivisionError si le dénominateur est nul
        """
        if den == 0:
            raise ZeroDivisionError("Le dénominateur ne peut pas être nul.")

        abs_num = abs(num)
        if (num < 0 < den) or (num > 0 > den):
            num = -abs_num
        else:
            num = abs_num

        commun = self.pgcd(num, den)
        self._numerateur = num // commun
        self._denominateur = abs(den) // commun

    @property
    def numerateur(self):
        return self._numerateur

    @property
    def denominateur(self):
        return self._denominateur

    @staticmethod
    def other_param(other):
        """
            Convertit le paramètre 'other' en une instance de la classe Fraction si nécessaire.

            PRE :-

            POST :
            - Si 'other' est déjà une instance de Fraction, renvoie 'other' inchangé.
            - Si 'other' est de type int, crée une nouvelle instance de Fraction avec 'other'
            comme numérateur et 1 comme dénominateur.

            RAISE : ValueError si other != int and other != Fraction
            """
        if isinstance(other, int):
            other = Fraction(other)
        if not isinstance(other, Fraction):
            raise ValueError("L'objet n'est pas une fraction.")
        return other

    @staticmethod
    def pgcd(a, b):
        """Calcule le plus grand commun diviseur de a et b en utilisant l'algorithme d'Euclide.

        PRÉ : - a est le numérateur de la fraction, b est le dénominateur de la fraction
        POST :- Retourne le plus grand commun diviseur de a et b grâce à l'algorithme d'Euclide.
        """
        while b:
            a, b = b, a % b
        return abs(a)

    def ppcm(self, a, b):
        """Calcule le plus petit commun multiple de a et b.

        PRÉ : a est le numérateur de la fraction, b est le dénominateur de la fraction
        POST : Retourne le plus petit commun multiple de a et b.
        """
        return abs(a * b) // self.pgcd(a, b)

    def __str__(self):
        """Retourne une représentation textuelle de la fraction sous sa forme réduite.

        PRÉ :    -une fraction de la classse Fraction
        POST :   -Retourne une chaîne représentant la fraction sous sa forme réduite.
        """
        return f"{self._numerateur}/{self._denominateur}"

    def nombre_mixte(self):
        """Retourne une représentation textuelle de la fraction sous forme de nombre mixte.

        Un nombre mixte est la somme d'un entier et d'une fraction propre.

        PRÉ : self est une fraction
        POST : Retourne une chaîne représentant la fraction sous forme de nombre mixte.
        RAISE: ValueError si l'objet n'est pas une fraction
        """
        if self._denominateur == 1 and self._numerateur != 0:
            raise ValueError("L'objet n'est pas une fraction.")
        partie_entiere = self._numerateur // self._denominateur
        reste = self._numerateur % self._denominateur
        if partie_entiere != 0:
            return f"{partie_entiere} + {reste}/{self._denominateur}"
        return self.__str__()

    def __add__(self, other):
        """Surcharge de l'opérateur + pour les fractions.

        PRÉ : self et other sont des instances de la classe Fraction
        POST : Retourne une nouvelle fraction représentant la somme de self et other.
        """
        nouveau_num = self._numerateur * other.denominateur + other.numerateur * self._denominateur
        nouveau_den = self._denominateur * other.denominateur
        resultat = Fraction(nouveau_num, nouveau_den)
        return resultat

    def __sub__(self, other):
        """Surcharge de l'opérateur - pour les fractions.

        PRÉ : self et other sont des instances de la classe Fraction
        POST : Retourne une nouvelle fraction représentant la différence entre self et other.
        """
        nouveau_num = self._numerateur * other.denominateur - other.numerateur * self._denominateur
        nouveau_den = self._denominateur * other.denominateur
        resultat = Fraction(nouveau_num, nouveau_den)
        return resultat

    def __mul__(self, other):
        """Surcharge de l'opérateur * pour les fractions.

        PRÉ : self et other sont des instances de la classe Fraction
        POST : Retourne une nouvelle fraction représentant le produit de self et other.
        """
        nouveau_num = self._numerateur * other.numerateur
        nouveau_den = self._denominateur * other.denominateur
        resultat = Fraction(nouveau_num, nouveau_den)
        return resultat

    def __truediv__(self, other):
        """Surcharge de l'opérateur / pour les fractions.

        PRÉ : self et other sont des instances de la classe Fraction
        POST : Retourne une nouvelle fraction représentant la division de self par other.
        RAISE: ZeroDivisionError si le dividende est nul
        """
        if other.numerateur == 0:
            raise ZeroDivisionError("Le dividende ne peut pas être nul.")
        nouveau_num = self._numerateur * other.denominateur
        nouveau_den = self._denominateur * other.numerateur
        resultat = Fraction(nouveau_num, nouveau_den)
        return resultat

    def __pow__(self, exp):
        """Surcharge de l'opérateur ** pour les fractions.

        PRÉ : exp est un entier non négatif
        POST : Retourne une nouvelle fraction représentant self élevé à la puissance exp.
        RAISE: ValueError si l'exposant n'est pas un entier positif
        """
        if not isinstance(exp, int):
            raise ValueError("L'exposant doit être un entier")
        if exp < 0:
            nouveau_num = self._denominateur ** abs(exp)
            nouveau_den = self._numerateur ** abs(exp)
            resultat = Fraction(nouveau_num, nouveau_den)
            return resultat
        nouveau_num = self._numerateur ** exp
        nouveau_den = self._denominateur ** exp
        resultat = Fraction(nouveau_num, nouveau_den)
        return resultat

    def __eq__(self, other):
        """Surcharge de l'opérateur == pour les fractions.

        PRÉ : self et other sont des fractions
        POST :Retourne True si les fractions sont égales, False sinon.
        """
        other = self.other_param(other)
        return self._numerateur == other._numerateur and self._denominateur == other._denominateur

    def __float__(self):
        """Retourne la valeur décimale de la fraction.

        PRÉ : self est une instance de la classe Fraction
              self est une fraction
        POST : Retourne la valeur décimale de la fraction.
        RAISE : ValueError si l'objet n'est pas une fraction
        """
        if self._numerateur == 0 or self._denominateur == 1:
            raise ValueError("L'objet n'est pas une fraction.")
        resultat = self._numerateur / self._denominateur
        return resultat

    def est_nulle(self):
        """Vérifie si la valeur de la fraction est 0.

        PRÉ : self est une instance de la classe Fraction
        POST : Retourne True si le numerateur de la fraction est égal à 0
               Retourne False si le numerateur de la fraction est différent de 0
        """
        return self._numerateur == 0

    def est_entiere(self):
        """Vérifie si la fraction est un entier.

        PRÉ :  self est une instance de la classe Fraction
        POST : Retourne True si le denominateur de la fraction est égal à 1, False sinon.
        """
        return self._denominateur == 1

    def est_une_fraction_propre(self):
        """Vérifie si la valeur absolue de la fraction est < 1.

        PRÉ : self est une fraction
        POST : Retourne True si la valeur absolue de la fraction est < 1, False sinon.
        RAISE : ValueError si l'objet n'est pas une fraction
        """
        if self._numerateur == 0:
            return False
        return abs(self._numerateur) < abs(self._denominateur)

    def est_unitaire(self):
        """Vérifie si le numerateur de la fraction est égal à 1 dans sa forme réduite.

        PRÉ : self est une fraction
        POST : return True si le numerateur de la fraction
         est égal à 1 dans sa forme réduite, False sinon.
        """
        return self._numerateur == 1

    def est_adjacente(self, other):
        """
        Deux fractions sont adjacentes si la valeur absolue de leur
        différence est une fraction unitaire.

        PRÉ :  other est une fraction
        POST : Retourne True si les fractions sont adjacentes, False sinon.
        """
        other = self.other_param(other)
        return abs(self._numerateur * other._denominateur -
                   other._numerateur * self._denominateur) == 1


if __name__ == "__main__":
    try:
        Fraction()
        fractions1 = Fraction(1, 4)
        fractions2 = Fraction(3, 2)
        multiplation = fractions1 * fractions2
        division = fractions1 / fractions2
        addition = fractions1 + fractions2
        soustraction = fractions1 - fractions2
        print(addition, soustraction, multiplation, division)
        print(Fraction.est_entiere(fractions2))
        print(Fraction.est_adjacente(fractions1, fractions2))
        print(fractions1.__float__())
        print(fractions1.nombre_mixte())
        print(fractions1.est_unitaire())
        print(fractions1.est_une_fraction_propre())
        print(fractions1.est_nulle())
        print(fractions1 == fractions2)
        print(fractions1 ** -2)
        print(fractions1.est_entiere())
        print(fractions1.__str__())
    except ZeroDivisionError as e:
        print("Le dénominateur ne peut pas être nul :", e)
    except ValueError as e:
        print("L'objet n'est pas une fraction :", e)
