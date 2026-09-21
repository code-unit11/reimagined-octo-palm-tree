function loadData() {
  fetch('http://127.0.0.1:5000/api/data')
    .then(response => response.json())
    .then(data => {
      document.getElementById('output').innerText = data.message;
    })
    .catch(error => console.log(error));
}
function typeWriter(element , text ,speed = 15) {
    let i=0 ;
    element.innerHTML = "";

    let timer = setInterval(() =>{  
        if( i < text.length) {
            element.innerHTML = text.substring(0, i+1);
            i++ ;

            //keep the scroll pinned to the bottom during type writer animation
            let box = document.getElementById("chat-box");
            if(box) {
                
                box.scrollTop = box.scrollHeight;

            
        } else{
            clearInterval(timer);
        }
        }

    },speed);
}

function addMessage(text, type) {
    let box = document.getElementById("chat-box");

    let msg = document.createElement("div");
    msg.classList.add("message", type);
    

    box.appendChild(msg);
    if (type === "bot")  {
        typeWriter(msg,text);
    }else{
         msg.innerHTML = text;
         
         box.scrollTop = box.scrollHeight;
         
    }
}

function send() {
    let input = document.getElementById("msg");
    let text = input.value;

    if (!text) return;

    addMessage(text, "user");
    
    input.value = "";

    fetch("/get", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({message: text})
    })
    .then(res => res.json())
    .then(data => {
        addMessage(data.response, "bot");
    });

    

}
```javascript
function quickAsk(question) {
    const input = document.getElementById("msg");

    input.value = question;

    send();
}
```
