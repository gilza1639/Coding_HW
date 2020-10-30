"use strict"

//пример 1
let a = 1, b = 1, c, d;
c = ++a;
alert(c); // ответ: 2
// Пояснение: к значение А прибавляется 1, итого с = 2


//пример 2
d = b++;
alert(d); //ответ: 1
// Пояснение: к значению b прибавляется один, но возвращается сторое значение b тк ++ стоит после переменной
// Итого b = 2, но d = 1



//пример 3
c = 2 + ++a;
alert(c); //ответ: 5
// Пояснение: после первого примера а = 2, здесь снова происходит прибавление, итого а = 3
// с = 2 + а(3) + 5



//пример 4
d = 2 + b++;
alert(d); //ответ: 4
// Пояснение: после второго примера b=2, затем тут d = 2 + b(2) = 4
alert(a); //3
// Пояснение: в примере 3 переменная а стала равняться 3
alert(b); //3
// Пояснение: b во втором примере стало равно 2, в этом примере снова увеличилось на 1 итого = 3


