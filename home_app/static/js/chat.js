// Создать объект для работы с сокетами
const socket = io()

// Обработать событие connect
socket.on("connect", () => {
    console.log("Ви під'єднались")

})

socket.emit("")

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

// Получить кнопку с id messages-tab
const messagesTab = document.getElementById('messages-tab');
// Получить кнопку с id chats-tab

const membersTab = document.getElementById('members-tab');

//divs
const messagesDiv = document.getElementById('messages-div')
const chatsDiv = document.getElementById('chats-div')
const membersTabDiv = document.getElementById('members-tab-div')

// Обработать событие клика по кнопке
membersTab.addEventListener('click', () => {

    console.log('chats-tab clicked!');
    messagesDiv.classList.remove('active');
    membersTabDiv.classList.add('active');

})

// Обработать событие клика по кнопке messagesTab

messagesTab.addEventListener('click', () => {

    console.log('messages-tab clicked!');
    messagesDiv.classList.add('active');
    chatsDiv.classList.remove('active');
    membersTabDiv.classList.remove('active');

})


// Back buttons
const backMessagesTab = document.getElementById('back-messages-tab')
const backChatsTab = document.getElementById('back-chats-tab')



// Обработать клик по кнопке backMessagesTab
backMessagesTab.addEventListener("click", () => {
    messagesDiv.classList.add('active');
    membersTabDiv.classList.remove('active');
})

// Обработать клик по кнопке backChatsTab
backChatsTab.addEventListener("click", () => {
    messagesDiv.classList.remove('active');
    chatsDiv.classList.add('active');
})
