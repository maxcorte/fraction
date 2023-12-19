class Fraction:
    """Classe représentant une fraction et ses opérations associées.

    Auteur : Delcorte Maxime
    Date : decembre 2023
    Cette classe permet la manipulation des fractions à travers plusieurs opérations.
    """

    def __init__(self, num=0, den=1):
        """Initialise une fraction avec un numerateur et un denominateur.

        PRÉ :   -num est le numerateur de la fraction, den est le denominateur de la fraction
                -den ne peut pas être nul

        POST :  -La fraction est initialisée avec le numerateur et le denominateur donnés.
                -la fraction doit être simplifiée grâce à la méthode pgcd().
                permet le changement des valeurs de la fraction via des setters
        """
        if den == 0:
            raise ValueError("Le dénominateur ne peut pas être nul.")
        else:
            commun = self._pgcd(num, den)
            self._numerateur = num // commun
            self._denominateur = den // commun

    @property
    def numerateur(self):
        return self._numerateur

    @numerateur.setter
    def numerateur(self, value):
        self._numerateur = value

    @property
    def denominateur(self):
        return self._denominateur

    @denominateur.setter
    def denominateur(self, value):
        if value != 0:
            self._denominateur = value
        else:
            raise ZeroDivisionError("Le dénominateur ne peut pas être nul.")

    def _pgcd(self, a, b):
        """Calcule le plus grand commun diviseur de a et b en utilisant l'algorithme d'Euclide.

        PRÉ : - a est le numérateur de la fraction, b est le dénominateur de la fraction
        POST :- Retourne le plus grand commun diviseur de a et b grâce à l'algorithme d'Euclide.
        """
        if not isinstance(self, Fraction):
            raise ValueError("L'objet n'est pas une fraction.")
        else:
            while b:
                a, b = b, a % b
            return a

    def _ppcm(self, a, b):
        """Calcule le plus petit commun multiple de a et b.

        PRÉ : a est le numérateur de la fraction, b est le dénominateur de la fraction
        POST : Retourne le plus petit commun multiple de a et b.
        """
        return abs(a * b) // self._pgcd(a, b)

    def __str__(self):
        """Retourne une représentation textuelle de la fraction sous sa forme réduite.

        PRÉ :    -une fraction de la classse Fraction
        POST :   -Retourne une chaîne représentant la fraction sous sa forme réduite.
        """
        return f" {self._numerateur}/{self._denominateur}"

    def nombre_mixte(self):
        """Retourne une représentation textuelle de la fraction sous forme de nombre mixte.

        Un nombre mixte est la somme d'un entier et d'une fraction propre.

        PRÉ : self est une fraction
        POST : Retourne une chaîne représentant la fraction sous forme de nombre mixte.
        """
        if not isinstance(self, Fraction):
            raise ValueError("L'objet n'est pas une fraction.")
        else:
            partie_entiere = self._numerateur // self._denominateur
            reste = self._numerateur % self._denominateur
            return f" la partie entière est {partie_entiere} et la partie fraction est {reste}/{self._denominateur}" if partie_entiere != 0 else str(
                self)

    def __add__(self, other):
        """Surcharge de l'opérateur + pour les fractions.

        PRÉ : self et other sont des instances de la classe Fraction
        POST : Retourne une nouvelle fraction représentant la somme de self et other.
        """
        nouveau_num = self._numerateur * other._denominateur + other._numerateur * self._denominateur
        nouveau_den = self._denominateur * other._denominateur
        resultat = Fraction(nouveau_num, nouveau_den)
        return f"le résultat de l'addition est {resultat}"

    def __sub__(self, other):
        """Surcharge de l'opérateur - pour les fractions.

        PRÉ : self et other sont des instances de la classe Fraction
        POST : Retourne une nouvelle fraction représentant la différence entre self et other.
        """
        nouveau_num = self._numerateur * other._denominateur - other._numerateur * self._denominateur
        nouveau_den = self._denominateur * other._denominateur
        resultat = Fraction(nouveau_num, nouveau_den)
        return f"le résultat de la soustraction est {resultat}"

    def __mul__(self, other):
        """Surcharge de l'opérateur * pour les fractions.

        PRÉ : self et other sont des instances de la classe Fraction
        POST : Retourne une nouvelle fraction représentant le produit de self et other.
        """
        nouveau_num = self._numerateur * other._numerateur
        nouveau_den = self._denominateur * other._denominateur
        resultat = Fraction(nouveau_num, nouveau_den)
        return f"le résultat de la multiplication est {resultat}"

    def __truediv__(self, other):
        """Surcharge de l'opérateur / pour les fractions.

        PRÉ : other n'est pas zéro
        POST : Retourne une nouvelle fraction représentant la division de self par other.
        """
        if self.denominateur == 0 or other.denominateur == 0 or other.numerateur == 0:
            raise ZeroDivisionError("Le dénominateur ne peut pas être nul.")
        else:
            nouveau_num = self._numerateur * other._denominateur
            nouveau_den = self._denominateur * other._numerateur
            resultat = Fraction(nouveau_num, nouveau_den)
            return f"le résultat de la division est {resultat}"

    def __pow__(self, exp):
        """Surcharge de l'opérateur ** pour les fractions.

        PRÉ : exp est un entier non négatif
        POST : Retourne une nouvelle fraction représentant self élevé à la puissance exp.
        """
        if not isinstance(exp, int) or exp < 0:
            raise ValueError("L'exposant doit être un entier positif.")
        else:
            nouveau_num = self._numerateur ** exp
            nouveau_den = self._denominateur ** exp
            resultat = Fraction(nouveau_num, nouveau_den)
            return f"le résultat de l'exposant est {resultat}"

    def __eq__(self, other):
        """Surcharge de l'opérateur == pour les fractions.

        PRÉ : self et other sont des fractions
        POST :Retourne les fractions sont égales si le numerateur et le denominateur sont égaux
              Retourne les fractions ne sont pas égales si le numerateur et le denominateur sont différents

        """
        if not isinstance(other, Fraction) or not isinstance(self, Fraction):
            raise ValueError("L'objet n'est pas une fraction.")
        else:
            if self._numerateur == other._numerateur and self._denominateur == other._denominateur:
                return f"Les fractions sont égales."
            else:
                return f"Les fractions ne sont pas égales."

    def __float__(self):
        """Retourne la valeur décimale de la fraction.

        PRÉ : self est une instance de la classe Fraction
              self est une fraction
        POST : Retourne la valeur décimale de la fraction.
        """
        if not isinstance(self, Fraction):
            raise ValueError("L'objet n'est pas une fraction.")
        else:
            resultat = self._numerateur / self._denominateur
            return f"la valeur décimale de la fraction est : {resultat}"

    def est_nulle(self):
        """Vérifie si la valeur de la fraction est 0.

        PRÉ : self est une instance de la classe Fraction
        POST : Retourne la fraction est nulle si le numerateur est égal à 0
               Retourne la fraction n'est pas nulle si le numerateur est différent de 0
        """
        if self._numerateur == 0:
            return f"La fraction est nulle."
        else:
            return f"La fraction n'est pas nulle."

    def est_entiere(self):
        """Vérifie si la fraction est un entier.

        PRÉ :  self est une instance de la classe Fraction
        POST : Retourne la fraction est un entier si le denominateur est égal à 1
               Retourne la fraction n'est pas un entier si le denominateur est différent de 1
        """
        if self._denominateur == 1:
            return f"La fraction est un entier."
        else:
            return f"La fraction n'est pas un entier."

    def est_une_fraction_propre(self):
        """Vérifie si la valeur absolue de la fraction est < 1.

        PRÉ : self est une fraction
        POST : Retourne la fraction est propre si la valeur absolue de la fraction est < 1
               Retourne la fraction n'est pas propre si la valeur absolue de la fraction est > 1
        """
        if not isinstance(self, Fraction):
            raise ValueError("L'objet n'est pas une fraction.")
        else:
            if abs(self._numerateur) < abs(self._denominateur):
                return f"La fraction est propre."
            else:
                return f"La fraction n'est pas propre."

    def est_unitaire(self):
        """Vérifie si le numerateur de la fraction est égal à 1 dans sa forme réduite.

        PRÉ : self est une fraction
        POST : Retourne la fraction est unitaire si le numerateur est égal à 1
               retourne la fraction n'est pas unitaire si le numerateur est différent de 1
        """
        if not isinstance(self, Fraction):
            raise ValueError("L'objet n'est pas une fraction.")
        else:
            if self._numerateur == 1:
                return f"La fraction est unitaire."
            else:
                return f"La fraction n'est pas unitaire."

    def est_adjacente(self, other):
        """
        Deux fractions sont adjacentes si la valeur absolue de leur différence est une fraction unitaire.

        PRÉ :  other est une fraction
        POST : Retourne True si les fractions sont adjacentes, False sinon.
        """
        if not isinstance(other, Fraction):
            raise ValueError("L'objet n'est pas une fraction.")
        else:
            if abs(self._numerateur * other._denominateur - other._numerateur * self._denominateur) == 1:
                return f"Les fractions sont adjacentes."
            else:
                return f"Les fractions ne sont pas adjacentes."

    def simplifier(self):
        """Simplifie la fraction en divisant le numerateur et le denominateur par leur PGCD.

        PRÉ :   -num est le numerateur de la fraction, den est le denominateur de la fraction
                -cette fonction n'est plus très utile car la fraction est simplifiée à l'initialisation
        POST :  -La fraction est simplifiée sur place.
                -la fraction doit être simplifiée grâce à la méthode pgcd().
        """
        commun = self._pgcd(self._numerateur, self._denominateur)
        self._numerateur //= commun
        self._denominateur //= commun


if __name__ == "__main__":
    try:
        Fraction()
        fractions1 = Fraction(4, 2)
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
        print(fractions1 ** 2)
        print(fractions1.est_entiere())
    except ZeroDivisionError as e:
        print("Le dénominateur ne peut pas être nul :", e)
    except ValueError as e:
        print("L'objet n'est pas une fraction :", e)
