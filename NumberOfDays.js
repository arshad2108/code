// Use numerics to denote month like 1 for january, 2 february
// question revolves on non-leap year so i used 2019 as year
// As for taking input we can either prompt a input message or get value from a form submit or anythings else and feed it to the function daysInMonth(month)

function nodaysInMonth (month) { 
  return new Date(year, 2019, 0).getDate();
}

console.log("Number of Days in Month: "+nodaysInMonth(2));
