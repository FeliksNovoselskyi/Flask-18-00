
// Арсений
// Создать две переменные 
// 1-ая - обычная переменная со строковым типом данных
// 2-ая - константа, значение любое
// let variable = "Hello, World!"
// const PI = 3.14


// Вова
// Проверить совпадают ли эти две переменные (проверить по значению и по типу)
// if (variable === PI){
//     console.log('Yes')
// } else {
//     console.log("No")
// }


// Денис
// Создать переменную счетчика, стартовое значение 0
// let counter = 0

// Создать цикл while с условием, при котором он работает пока counter меньше 100
// while (counter < 100){
//     console.log(counter);
// }


// Создать объект для работы с сокетами
const socket = io()

// Обработать событие connect
socket.on("connect", () => {
    console.log("Ви під'єднались")

})

socket.on("disconnect", () => {
    console.log("Ви ВІД'ЄДНАЛИСЯ")
    
})

socket.on("message", (data) => {
    console.log(data.from, data.message_text)
})
// emit - излючить
socket.emit("message", {messagetext: "Kirusha Malcev"})

