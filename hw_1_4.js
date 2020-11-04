"use strict"

const products = [
    {
        id: 3,
        price: 127,
        photos: [
            "1.jpg",
            "2.jpg",
        ]
    },
    {
        id: 5,
        price: 499,
        photos: []
    },
    {
        id: 10,
        price: 26,
        photos: [
            "3.jpg"
        ]
    },
    {
        id: 8,
        price: 78,
    },
];

let result1 = products.filter(function (elem) {
    return (elem.photos !== undefined)
})



let result2 = result1.filter(function (elem) {
    return (elem.photos[0] !== undefined)
})

console.log(result2)