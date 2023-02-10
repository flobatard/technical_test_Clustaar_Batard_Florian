class BlackList:
    """
    Instruction:
        Il est autorisé de modifier le comportement de cette classe, sauf le nom des attributs
    """

    def __init__(self) -> None:
        """
        Initialise un set de mots à exclure.
        """
        self.bl = set()
        self.words = ""  # TODO load words.txt
        self._make_bl()

    def _make_bl(self) -> None:
        """
        Strip les mots et les ajoute dans l'attribut bl
        """
        words = self.words.split("\n")

        for w in words:
            w = w.strip()

            self.bl.add(w)
