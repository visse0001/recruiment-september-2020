# Zadanie rekrutacyjne

Utworzenie szkieletu aplikacji wraz z mikroserwisem do autoryzacji danych.

## Opis:
1. Utworzenie aplikacji Django wraz z bazą danych Postgres.
2. Utworzenie mikroserwisu mającego na celu autoryzację danych.
    User story:
    1. Użytkownik wprowadza w aplikacji dane imię i nazwisko oraz adres e-mail w celu
    uzyskania autoryzacji.
    2. Dane wysyłane są do zewnętrznego serwisu, które je autoryzuje:
    
        - input: Name, E-mail; <br>
        - output:
        
            ‘PASS’ gdy dane znajdują się w bazie, <br>
            ‘FAIL’ gdy nie ma danych nie ma w bazie,

3. Zapis statusu autoryzacji w bazie aplikacji.
4. Możliwość wyświetlenia zautoryzowanych użytkowników w ramach aplikacji.

## Stack:
1. Python, Django, Postgres.
