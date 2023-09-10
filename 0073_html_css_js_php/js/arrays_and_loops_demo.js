// deklaracja tablic

//let nazwa_tablicy = [element1, element2];

let jeden_typ_danych = [1,2,3,4,5];

let mix_danych = ["string 1", 2.7,"True"];

let odwolanie_do_elementu = mix_danych[1]; //2.7

var dodanie_elementu = mix_danych[3] = "nowy element tablicy";

var dodanie_elementu_na_koncu_tablicy = mix_danych.push("nowy element z metody push");

var dodanie_elementu_na_poczatku_tablicy = mix_danych.unshift("nowy elemnet dzieki metodzie unshift()");

var usuniecie_elementu_na_koncu_tablicy = mix_danych.pop();

var usuniecie_elementu_na_poczatku_tablicy = mix_danych.shift();

////////////////// PETLE ///////////////////

// petla rosnaco

for (zmienna=1; zmienna<10; zmienna++) {
    console.log(zmienna);
    if (zmienna == 4){
        console.log("Przerwanie akcji po iteracji 4rtej");
        break;
    }
}

//petla malejaco

for (zmienna=10; zmienna>1; zmienna--) {
    console.log(zmienna);
    if (zmienna == 4){
        console.log("Przerwanie akcji po iteracji 7dmej");
        break;
    }
}

// petle przechodzace po tablicach danych

var new_array = [120, "tablica", "kod 200"];

for (var item in new_array){
    console.log(new_array[item]);
}