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