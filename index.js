// Create an array of objects, each representing a person with properties like name, age, and gender. Write a function to filter out all females and then map the remaining people to an array of names. Print the final result.

const females = (fun) => {
  const fm = fun.filter((f) => f.gender !== "female");
  const names = fm.map(nm => nm.name)
  console.log(names);
};

const people = [
  { name: "John", age: 25, gender: "male" },
  { name: "Jane", age: 22, gender: "female" },
  { name: "Alice", age: 30, gender: "female" },
  { name: "Bob", age: 27, gender: "male" },
];

females(people);
