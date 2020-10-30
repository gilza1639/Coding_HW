function Plus(num_one, num_two) {
    return num_one + num_two
}

function Minus(num_one, num_two) {
    return num_one - num_two
}

function Diveded(num_one, num_two) {
    return num_one / num_two
}

function Mult(num_one, num_two) {
    return num_one * num_two
}

function mathOperation(arg1, arg2, operation) {
    switch (operation) {
        case '+' || 'Plus':
            return Plus(arg1, arg2)
        
        case '-' || 'Minus':
            return Minus(arg1, arg2)
        
        case '/' || 'Diveded':
            return Diveded(arg1, arg2)
        
        case '*' || 'Mult':
            return Mult(arg1, arg2)
    }
}

while (true) {
    first = Number(prompt('input first num'))
    second = Number(prompt('input second num'))
    command = prompt('input command ((+, -, /, *))')
    alert(mathOperation(first, second, command))
}