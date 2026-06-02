// Создать объект для работы с сокетами
const socket = io()

// Обработать событие connect
socket.on("connect", () => {
    console.log("Ви під'єднались")

})

socket.on("disconnect", () => {
    console.log("Ви ВІД'ЄДНАЛИСЯ")
    
})

// let join_button = document.getElementById("join_button")
// let leave_button = document.getElementById("leave_button")
// let paragraph = document.querySelector("p")

// const linkGroupId = 1

join_button.addEventListener("click", () => {
    // Отправить событие join_room на сервер
    socket.emit('join_room', {groupId: linkGroupId})
})


// Обработать по кнопке leave_button
leave_button.addEventListener("click", () => {
    // Отправить событие leave_room на сервер
    socket.emit("leave_room", {"bebe": "lala"})
})


// // Обработать событие join_room, указать аргумент data
// socket.on("join_room", (data) => {
//     console.log(data.message)
// })



// // Обработать событие leave_room, указать аргумент data
// socket.on("leave_room", (data) => {
//     console.log(data)
// })



// Синтаксис создания JS-объекта
const objectOne = {}


let bear = {
    legsCount: 3,
    "marshall headphones": 2,
    ears: 2,
    flight() {
        console.log("Поднимаемся в воздух");
    }
}

// console.log(bear)

// bear.flight()


// Получение данных
// console.log(bear["legsCount"])

// Денис. Получить значение свойства ears из объект bear
// Вывести значение в консоль
// console.log(bear['ears'])
// 1
// объект.свойство

// 2
// объект["свойство"]


// Запись данных


bear["new"] = 2 

bear.new2 = 10

// объект.новое_свойство = значение
// объект["новое_свойство"] = значение



// Удаление

delete bear.ears

// delete объект.свойство

// console.log(bear);



console.log(typeof bear.new2)


