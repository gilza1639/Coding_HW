
// Комментарий оставил спустя час пассивного половоко акта с этим кодом
/*
Мне нужно было выяснить находится ли число в массиве, чтобы на основании этого вывести правильную форму слова
По привычке из питона пишу 6 in [0, 5, 6, 7, 8, 9], и моему удивлению не было предела, когда я узнал
Что конструкция Number in array определяет, есть ли индекс в массиве
*/


// Ниже идет версия 3 из 3 где ничего не работает
// зациклил для дуобства тестирования

while (true) {

    let my_num = prompt('input num pls')
    let almost_last_num = Number(my_num.slice(-2))
    let last_num = Number(my_num.slice(-1))

    let ans
    if ([11, 12, 14, 14].includes(almost_last_num)) {
        ans = 'рублей'
    } else if ([0, 5, 6, 7, 8, 9].includes(last_num)) {
        ans = 'рублей'
    } else if ([2, 3, 4].includes(last_num)) {
        ans = 'рубля'
    } else if ([1].includes(last_num)) {
        ans = 'рубль'
    } else {
        ans = 'Error'
    }



    if (ans == 'Error') {
        alert('Наверняка вы ввели не число')
    } else {
        alert(`Ваша сумма в ${my_num} ${ans} успешно зачислена.`)
    }

}



// Ниже идет версия 2 из 3 где ничего не работает

/* 

while (true) {
    let my_num = prompt('input num pls')
    let last_num = my_num.slice(-2)
    let ans
    if (Number(last_num) in [11, 12, 14, 14]) {
        ans = 'рублей'
    } else if (Number(last_num.slice(-1) in [0, 5, 6, 7, 8, 9])) {
        ans = 'рублей'
    } else if (Number(last_num.slice(-1) in [2, 3, 4])) {
        ans = 'рубля'
    } else if (Number(last_num.slice(-1) in [1])) {
        ans = 'рубль'
    } else {
        ans = 'Error'
    }

    alert(isNaN(ans))

    if (isNaN(ans)) {
        alert('Наверняка вы ввели не число')
    } else {
        alert(`Ваша сумма в ${my_num} ${ans} успешно зачислена.`)
    }

    alert(`Ваша сумма в ${my_num} ${ans} успешно зачислена.`)
}

*/

// Ниже идет версия 1 из 3 где ничего не работает

/* 

function BetterForm(input_num) {
    let last_num = input_num.slice(-2)

    switch (last_num) {
        case '11' || '12' || '13' || '14':
            return 'рублей'
        case last_num.slice(-1) in ['5', "6", "7", "8", "9", "0"]:
            return 'рублей'
        case last_num.slice(-1) in ['2', "3", "4"]:
            return 'рубля'
        case last_num.slice(-1) in ['1']:
            return 'рубль'
    }
}


while (true) {
    let my_num = prompt('input num pls')
    alert(`Ваша сумма в ${my_num} ${BetterForm(my_num)} успешно зачислена.`)
}


*/