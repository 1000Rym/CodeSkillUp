// Problem1: SleepIn Function:
// when weekday is false or vocation is true sleep.
function sleepIn(weekday, vocation){
  return !weekday || vocation;
}

//Console Log for sleepIn
console.log("Answer for sleepIn:");
console.log(sleepIn(false,false));
console.log(sleepIn(true,false));
console.log(sleepIn(false,true));

// Problem2: Monky Trouble
// If both monkey both smile, or neigther smile print false.
function monkeyTrouble(aSmile, bSmile){
  return aSmile == bSmile &&
         (aSmile === true || aSmile === false);
}

//Coonsolelog for monkeyTrouble
console.log("Answer for monkeyTrouble:");
console.log(monkeyTrouble(true, true));
console.log(monkeyTrouble(false, false));
console.log(monkeyTrouble(false, true));

// Promblem3: string Times
// Multiple n times of string str.
function stringTimes(str, n){
  var my_str = "";
  for (var i = 0 ; i < n ; i ++ ){
    my_str+=str;
  }
  return my_str;
}

console.log("Answer for stringTimes:");
console.log(stringTimes("Hi",2));
console.log(stringTimes("Hi",3));
console.log(stringTimes("Hi",1));

// Problem 4: Lucky Some
// Sum the value of input parameters.
// If the parameter is 13 than not count the following parameters.
function luckySum(a,b,c){
  if (a === 13 ){
    return 0;
  }else if(b === 13){
    return a;
  } else if(c === 13){
    return a + b;
  } else {
    return a + b + c;
  }
}

console.log("Answer for luckySum:");
console.log(luckySum(1,2,3));
console.log(luckySum(1,2,13));
console.log(luckySum(1,13,3));

// Problem 5:
// If the speed is 60 or less -0
// else if the speed is 61~80 -1
// higher than 81 -2
// birthday: can be higher
function caught_speeding(speed, is_birthday){
  if(is_birthday){
    speed -=5;
  }

  if (speed <= 60){
    return 0;
  }else if (speed <=80){
    return 1;
  }else{
    return 2;
  }
}

console.log("Anser for the caught speeding.");
console.log(caught_speeding(60, false));
console.log(caught_speeding(65, false));
console.log(caught_speeding(65, true));

// Problem Bonus
// small - 1 inches each
// big - 5 inches each
// goal - goal to reach
function makeBricks(small, big, goal){
  return goal%5 >=0 &&  goal%5- small <=0 && goal <= small + big * 5;
}

console.log("Anser for the make bricks");
console.log(makeBricks(3,1,8));
console.log(makeBricks(3,1,9));
console.log(makeBricks(3,2,10));
