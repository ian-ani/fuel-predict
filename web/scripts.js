function getInputs() {
    let date = document.getElementById("get-date").value;
    let province = document.getElementById("get-provincias").value; // esto tiene que pasar a valores numericos
    let fuel = document.getElementById("get-combustible").value;

    let dateElements = date.split("-");

    let dict = {
        "year": parseInt(dateElements[0]),
        "month": parseInt(dateElements[1]),
        "day": parseInt(dateElements[2]),
        "province": parseInt(province),
        "fuel": parseInt(fuel)
    }

    // provincia tiene que ser tambien numerico
    
    console.log(dict);

    predict();
}

function predict() {
    console.log("Aqui tendria que hacer la request a la API y devolver el resultado");
    console.log("La request tiene que ser un JSON directamente que es como lo tengo");
    /* 1. mandar json 
    2. coger respuesta
    3. mostrar resultado (aqui o en otra funcion, da igual) */
    /* Tal vez si lo del LabelEncoder lo pido que me lo guarde en un JSON en disco, 
    puedo obtener los valores que luego pasarian a data/provincias.json directamente */
}