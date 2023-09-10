// deklaracja zmiennych
// roznica var let to zakres
var nazwa_zmiennej = "wartosc"; //var na cala funkcje
let nazwa_zmiennej_2 = "wartosc 2"; //let na jeden blok komend if, albo for

const nazwa_zmiennej_3 = 3.14;

// wyswietlanie zawartosci zmiennej:

console.log(nazwa_zmiennej,nazwa_zmiennej_2, nazwa_zmiennej_3)

//typy danych:

// int

var liczba_calkowita = 36;

//string

var ciag_znakow_string = "to jest string";

//boolean

var prawda_falsz = true; //albo true albo false jako wdartosc

// float

var zmienno_przecinkowa = 3.14;

// undefined 

var zmienna_undefiined;

// obiekt

var obiekt = new String()

// sprawdzenie jakim typem danych jest dana zmienna

var typ_danych_liczba_calkowita = typeof liczba_calkowita; // number

var typ_danych_ciag_znakow_string = typeof ciag_znakow_string;  // string

var typ_danych_ciag_prawda_falsz = typeof prawda_falsz;  // boolean

var typ_danych_liczba_zmiennoprzecinkowa = typeof liczba_zmiennoprzecinkowa;  // number

var typ_danych_undefined = typeof undefined;  // undefined

var typ_danych_objekt = typeof objekt;  // object

//wpisywanie danych przez usera:

var dlugosc_przerwy = prompt("Jak dluga jest przerwa obiadowa?");

alert("Dziekuje za informacje. Przerwa bedzie trwala " + dlugosc_przerwy);

// type casting:

var wydluzenie_przerwy = dlugosc_przerwy + 15;  // tutaj jest string

//wartosc NaN poniewaz nie zrobilismy type castingu na zmiennej dlugosc_przerwy
var zmiana_typu_na_inta_wydluzenie_przerwy = Number(wydluzenie_przerwy); // typ: NaN

//zmiana kierunku - type casting - dlugosc_przerwy

var zmiana_typu_na_inta_dlugosc_przerwy = Number(dlugosc_przerwy); // typ: number np. 60

var wydluzenie_przerwy_o_15_minut = zmiana_typu_na_inta_dlugosc_przerwy + 15 

alert("Wydluczylismy przrwe o 15 minut. Teraz trwa:  " + wydluzenie_przerwy_o_15_minut)

// SPOSOB II

var dlugosc_przerwy = Number(prompt("jak dluga jest przerwa obiadwa? "));
var dodanie_15_minut = dlugosc_przerwy + 15;

// operacje arytmentyczne

// liczba_1 = a ; liczba_2 = b;
var a = 20;
var b = 10;
var dodawanie = a + b; // 30

// konkatenaacja stringow

var strng_1 = "hello world";
var string_2 = "!!!";
var konkatenacja = strng_1 + string_2;

//manipulacja stringami

var string_3 = "Kod 201 - Created";
var dlugosc_stringa_3 = string_3.length; // 17 bo wliczamy biale znaki

// indeksy od 0

var string_3_pierwszy_znak = string_3[0]; // K

//wyszukiwanie indeksu znaku w stringu

var string_3_indeks_dla_pierwszego_wyszukanego_znaku = string_3.indexOf("e");

// operatory logiczne

// <, >, <=, >=, ==, ===, !=