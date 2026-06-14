// Создать объект для работы с сокетами
const socket = io()

// Обработать событие connect
socket.on("connect", () => {
    console.log("Ви під'єднались")

})

socket.on("disconnect", () => {
    console.log("Ви ВІД'ЄДНАЛИСЯ")
    
})
socket.on("display_status", (data) => {
    console.log(data);

    let members = data.members

    const membersDiv = document.getElementById("members-div")
    membersDiv.innerHTML = ''

    members.forEach((member) => {
        console.log(member.status)
        let divUser = document.createElement("div")
        divUser.textContent = `${member.email} ${member.status}`
        
        membersDiv.appendChild(divUser)
    });
})

const chatsButton = document.getElementById("chats-button")

chatsButton.addEventListener('click', () => {
    console.log(123123123123)
    const chatsDiv = document.getElementById('chats-div');
    const messagesDiv = document.getElementById('messages-div');
    
    messagesDiv.classList.add('active');
    chatsDiv.classList.remove('active');


    // chatsDiv.classList - классы которые присвоены элементу
});

document.getElementById("messages-button").addEventListener('click', openMessages);

// function openChat(event){
//     console.log(123123123123)
//     const chatsDiv = document.getElementById('chats-div');
//     const messagesDiv = document.getElementById('messages-div');
    
//     messagesDiv.classList.add('active');
//     chatsDiv.classList.remove('active');


//     // chatsDiv.classList - классы которые присвоены элементу
// }
function openMessages(){
    const messagesDiv = document.getElementById('messages-div');
    
}
