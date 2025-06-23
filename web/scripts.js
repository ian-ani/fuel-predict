// IMAGEN DE PORTADA

function getImage() {
    const img = document.querySelector("#banner img");

    // En caso de que img no exista (en pai y pvp no existen, por ejemplo)
    if (!img) return;

    const cars = ["lanevo6.jpg", "subaru.jpg"];
    const result = Math.floor(Math.random() * cars.length);

    img.src = `images/${cars[result]}`;
}

getImage();

// CREACION DEL SELECT DE PROVINCIAS

function createProvinces() {
    let select_elem = document.getElementById("get-provinces");

    fetch("data/provincias.json")
        .then(response => response.json())
        .then(result => {
            Object.entries(result).forEach(provincia => {
                let option = document.createElement("option");

                option.textContent = provincia[0]; // nombre (clave)
                option.value = provincia[1]; // valor
                select_elem.appendChild(option);
            });
        })
        .catch(error => console.error("No se ha podido cargar el archivo."));
}

// OBTENER INPUTS

function getInputs() {
    let date = document.getElementById("get-date").value;
    let province = document.getElementById("get-provinces").value;
    let fuel = document.getElementById("get-fuel").value;

    let dateElements = date.split("-");

    let dict = {
        "year": parseInt(dateElements[0]),
        "month": parseInt(dateElements[1]),
        "day": parseInt(dateElements[2]),
        "province": parseInt(province),
        "fuel_type": parseInt(fuel)
    }

    predict(dict);
}

// PREDECIR DATOS

function predict(data) {
    let title = document.title; // asi automaticamente coge si pai o pvp
    let apiUrl = `http://localhost:8080/predict/${title.toLowerCase()}`;

    const headers = new Headers({
        "Content-Type": "application/json"
    })

    let requestOptions = {
        method: "POST",
        headers: headers,
        body: JSON.stringify(data)
    }

    fetch(apiUrl, requestOptions)
        .then(response => response.json())
        .then(result => {
            let predictionResult = document.getElementById("prediction");

            predictionResult.textContent = result.prediction + "€";
        })
        .catch(error => console.error("error", error));
}

