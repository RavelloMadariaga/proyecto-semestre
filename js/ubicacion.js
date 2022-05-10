

const cargarApi = async () => {
    try {
        const respuestaIP = await fetch('https://api.ipdata.co/?api-key=28443de0abfe3b4df7f0493fb787176fae3d522ef24be8a59ca72bf5')
        const datosIP = await respuestaIP.json()
        console.log(datosIP)
        const latitude = datosIP.latitude
        const longitude = datosIP.longitude
        const respuestaWeather = await fetch('https://api.openweathermap.org/data/2.5/weather?lat=' + latitude + '&lon=' + longitude + '&lang=sp&appid=8bff2b3c2de034eb2476aa2152464e5d&units=metric')
        const datosWeather = await respuestaWeather.json()
        console.log(datosWeather)
        const datosMaps = await fetch('https://maps.googleapis.com/maps/api/geocode/json?latlng=' + latitude + ',' + longitude + '&key=AIzaSyDQc_ny0KowofSUl7w0df5kV_0JK16_1AM')
        console.log(datosMaps)
        //document.getElementById("columnadatos").innerHTML = "Se recomienda cultivar este tipo de plantas en temperaturas mas calientes que las actuales"
        const icon = 'http://openweathermap.org/img/wn/' + datosWeather.weather[0].icon + '@4x.png'
        date = new Date();
        year = date.getFullYear();
        month = date.getMonth() + 1;
        day = date.getDate();
        document.getElementById("ciudad").innerHTML = "¡Solo hoy "+ day + "/"+ month +"! Despacho gratuito en tu ciudad: " + datosIP.city + " "
        //document.getElementById("temp").innerHTML = "Temperatura: " + Math.round(datosWeather.main.temp) + "°C "
        //document.getElementById("descripcion").innerHTML = "Tiempo actual: " + (datosWeather.weather[0].description).toUpperCase()
        document.getElementById("icon").innerHTML = '<img src="' + datosIP.flag + '" class="border border-3 border-white shadow-sm"> ' + datosIP.currency.symbol
        //document.getElementById("templanta").innerHTML = "<h1>" + "Comuna: " + datosWeather.name + "</h1>"

        //Object.keys(datosWeather.weather[0]).forEach(element => {
        // console.log(element)
        //document.getElementById("div").innerHTML += '<h1>'+element+': '+datosWeather.weather[0][element]+'<h1>'
        //document.getElementById("div").innerHTML ="<h1>"+element+"</h1>"
        //});
    } catch (error) {
        console.log(error)
    }
}

cargarApi();