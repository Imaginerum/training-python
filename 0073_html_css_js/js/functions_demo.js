// deklaracja funkcji

// function nazwa_funkcji(parametry){
//     ciało funkcji
// }

// wywolanie funkcji

// nazwa_funkcji(konkretna wartosc parametru)

// ///////// FUNKCJA BEZ PARAMETRU

function hello_wordl(){
    let str1 = "Hello ";
    let str2 = "World! ";
    console.log(str1 + str2);
}

// hello_wordl();

function separator(){
    console.log("//////////////////////////////////NEXT/////////\n///////////////////////////")
}

separator();

// funkcja z parametrem

function add(param_1, param_2){
    console.log("Wynik dodawania: " + String(param_1 + param_2));

}

add(3,5);
separator();

// zwracanie wartosci

function multiplication(param_1, param_2){
    return param_1 * param_2;
}

let score = multiplication(3,4);
console.log(multiplication(3,4));
separator();

// wyrażenia funkcyjne

var result = function(number, power){return number ** power};
console.log(result(5,3));