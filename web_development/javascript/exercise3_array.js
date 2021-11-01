
var cond_roster_web = null;
var endMsg = "Thanks for using the Web App! Please refresh the page to start over.";

//check the correct answer
while(cond_roster_web !== `y` && cond_roster_web !== `n`){
  cond_roster_web = prompt("Would you like to start the roster web app? y/n");
}

if (cond_roster_web === 'y'){
  var names = [];

  while(action !== 'quit'){
    var action = prompt("Please select an action: add, remove, display, or quit.");
    if (action === 'add'){
      var name = prompt("What name would you like to add?");
      names.push(name);
    }else if (action === 'remove'){
      var name = prompt("What name would you like to remove?");
      var pos = names.indexOf(name);
      if (pos >=0 ){
        names.splice(pos, 1);
      }
    }else if (action === 'display'){
      console.log(names);
    }
  }
}

alert(endMsg);
