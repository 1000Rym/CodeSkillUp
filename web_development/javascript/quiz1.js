var firstName = prompt("Please input your First Name:");
var lastName = prompt("Please input your Last Name:");
var age = prompt("Please input your Age:");
var height = prompt("Please input your Height:");
var petName = prompt("Please input your Pet Name:");
alert("Thank you so much for the information.")

if(firstName[0] === lastName[0] &&
  age >= 20 && age <= 30 &&
  height >= 170 &&
  petName.endsWith('y')){
  console.log("You are the spy.");
}else {
  console.log("No extra information.");
}
