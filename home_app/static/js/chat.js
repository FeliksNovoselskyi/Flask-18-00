let name = 'Даниелка'

// Условия
// if (1 === '1'){
//     console.log("Значення")
// } else if (1 === "1"){
//     console.log("Типи значень")
// } else {
//     console.log("Kirile Krutoy Super Mega 3000 2012 Pro Max")
// }

// Цикл while
// let count = 0
// while (count < 1000){
//     count++
//     if (count === 100){
//         continue
//     }
//     console.log("Kirile Krutoy Super Mega 3000 2012 Pro Max", count)
// }

// Цикл for
// for (перменная; условие; шаг){}



const socket = io()


socket.on("connect", () => {
    console.log("Вы подключились")
})
