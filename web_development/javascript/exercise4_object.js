// Given Obejct
// Lenght of the employee's name on the console.

var employee = {
  name : "Benedict Thousand",
  job: "Programmer",
  age: 32,

  nameLenght:function(){
    return this.name.length;
  },

  introAlert:function(){
    var introduction = "Name" + " is " + this.name +
    ", Job is " + this.job +
    ", Age is" + this.age + "."

    alert(introduction);
  },

  lastName:function(){
    var names = this.name.split(' ');
    return names[names.length-1];
  }
};
