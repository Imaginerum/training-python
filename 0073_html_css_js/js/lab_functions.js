// 1. Doplata za koszt naprawy w zależności od marki

function model_car(car){
    if (car == 1){
        return 2000;
    } else if (car == 2){

        return 1500;
    } else if (car == 3){
        return 1000;
    } else {
        return -1;
    }
}

// 2. Doplata za koszt naprawy w zależności od wieku

function client_age(age){
    if (age >=16 && age < 21){
        return 5000;
    } else if (age >= 21){
        return 0;
    } else {
        return -1;
    }
}

function main(){
    
    while (1==1){
        var model_car_input = Number(prompt("Naprawiam auta poniższych marek:\n 1 - BMW\n 2 - AUDI\n 3 - TOYOTA\nWybierz opcje!"));
        var client_age_input = Number(prompt("Kwota naprawy jest uzależniona od wieku. Ile masz lat? "));

        if (client_age(client_age_input) == -1) || model_car(model_car_input) == -1{
            alert("Nie obsługujemy osób poniżej 16 roku życia. Jeśli jesteś starszy, to nie naprawiam takiej marki samochodu.");
        } else {
            
            client_age_price = client_age(client_age_input);
            client_model_car_price = model_car(model_car_input);
            var price = client_age_price + client_model_car_price;

            alert("Kwwota za naprawe wynosi: ", String(price));

        }
    }
}