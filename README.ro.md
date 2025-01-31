# Joc X și 0 (Tic-Tac-Toe) - Jucător vs Computer

## Descriere

Această aplicație implementează jocul clasic de **X și 0** (Tic-Tac-Toe) într-un mediu în care un jucător joacă împotriva computerului. Jocul se desfășoară pe o tablă de joc 3x3, iar obiectivul este de a plasa trei simboluri pe linie (orizontal, vertical sau pe diagonală).

**Regulile jocului** sunt următoarele:
1. Jucătorul și computerul își aleg alternativ celulele din tabla de joc.
2. Jucătorul joacă cu simbolul **X**, iar computerul joacă cu simbolul **O**.
3. Jucătorul va introduce mutările sub formă de coordonate (de exemplu, A1, B2, C3).
4. Computerul va face mutări aleatorii într-o celulă liberă.
5. Jocul se termină când unul dintre jucători câștigă sau când jocul ajunge într-un egal.

## Tehnologii Folosite

- **Python 3** - Limbajul de programare folosit pentru a implementa aplicația.
- **Algoritm simplu** - Computerul alege o mutare aleatorie din celulele libere.
- **Terminal/Console** - Aplicația rulează într-un terminal sau fereastră de comandă.

## Cum Funcționează Aplicația

Aplicația se bazează pe următoarele funcționalități principale:

- **Tabla de joc**: O matrice 3x3 care reprezintă tabla. Fiecare celulă poate conține un simbol `X` sau `O` (sau poate fi goală).
- **Mutările jucătorului**: Jucătorul introduce coordonatele unde dorește să pună simbolul său (X). Exemple de mutări valabile: `A1`, `B2`, `C3`.
- **Mutările computerului**: Computerul plasează simbolul `O` aleatoriu într-o celulă goală.
- **Verificarea câștigătorului**: După fiecare mutare, aplicația verifică dacă cineva a câștigat sau dacă jocul s-a terminat într-un egal.

## Cum Să Rulezi Aplicația

1. Salvează fișierul cu numele `tic_tac_toe.py`.
2. Deschide un terminal și navighează către directorul unde ai salvat fișierul.
3. Rulează comanda:
   ```bash
   python tic_tac_toe.py
