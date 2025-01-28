function getData(){
    let height = prompt("Enter Height");
    let radius = prompt("Enter Radius");
    calculateVolume(radius, height);
}
// Calculates the volume of a cylinder
function calculateVolume(radius, height) {
    const volume = 3.142 * radius * height;
    alert("The volume is: "+ volume);
}
getData();