checkTemperature = (temperature) => {
    if (temperature <=20) {
        console.log("It is Cold Out Here ")
    }
    else if (20 > temperature < 30 ) {
        console.log("Normal Temperature")
    }
    else {
        console.log("Hot")
    }
}
checkTemperature(23)