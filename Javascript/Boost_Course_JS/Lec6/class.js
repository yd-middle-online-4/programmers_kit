class Person{
    constructor(name, first, second){
        this.name = name;
        this.first = first;
        this.second = second;
    }
    sum(){
    return 'prototype : '+(this.first+this.second);
    }
}

var kim = new Person('kim', 20, 30);
kim.sum = function() {
    return 'this : '+(this.first+this.second-1);
}
console.log('kim', kim);
console.log("kim.sum()", kim.sum());


// var lee = new Person('lee', 10, 10, 10);
// console.log("kim.sum()", kim.sum());
// console.log("kim.sum()", lee.sum());