



// Создать объект для работы с сокетами
const socket = io()

// Обработать событие connect
socket.on("connect", () => {
    console.log("Ви під'єднались")

})

socket.on("disconnect", () => {
    console.log("Ви ВІД'ЄДНАЛИСЯ")
    
})


// emit - излючить
socket.emit(
    "message", 
    {
        messagetext: "Kirusha Malcev",

    }
)





// # - id
// . - class


// let join_button = document.getElementById("join_button")
// let leave_button = document.querySelector("#leave_button")
// let currentGroupParagraph = document.querySelector("p")




// // Обрабатываем клик по кнопке join_button
// join_button.addEventListener('click', () => {
//     socket.emit('join_room')
// })


// leave_button.addEventListener('click', () => {
//     socket.emit('leave_room')
// })

// // .addEventListener(событие, функция)

// console.log(join_button, leave_button)


// socket.on("join_room", (data) => {
//     console.log(data.message)

//     currentGroupParagraph.textContent = `Поточна група: ${data.group_title}`
// })

