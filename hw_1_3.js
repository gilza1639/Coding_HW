"use strict"

const products = [
    {
        id: 3,
        price: 200,
    },
    {
        id: 4,
        price: 900,
    },
    {
        id: 1,
        price: 1000,
    },
];

products.forEach(function (currentValue, index) {
    products[index] = {
        id: currentValue.id,
        price: currentValue.price*0.85
    }


}) 


console.log(products)



