class BlackList:
    """
    Instruction:
        Il est autorisé de modifier le comportement de cette classe, sauf le nom des attributs
    """

    def __init__(self, wordsFileName) -> None:
        """
        Initialise un set de mots à exclure.
        """
        self.bl = set()
        f = open(wordsFileName, encoding="utf-8")
        self.words = f.read()
        f.close()
        self._make_bl()

    def _make_bl(self) -> None:
        """
        Strip les mots et les ajoute dans l'attribut bl
        """
        words = self.words.split("\n")

        

        for w in words:
            w = w.strip()
            self.bl.add(w)

    def _is_blacklisted(self, word) -> bool:
        return word in self.bl
