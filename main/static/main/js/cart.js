console.log('Hello world')

var updateBtns = document.getElementsByClassName('update-cart')
console.log(updateBtns.length)
console.log(updateBtns)

for (var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener("click", function(){
        var itemCode = this.dataset.product
        var action = this.dataset.action
        console.log(itemCode)

        if (user == 'AnonymousUser'){
            console.log('User is not authenticated.')
        }else{
            updateUserOrder(itemCode, action)
        }
    })
}

function updateUserOrder(itemCode, action){
    var url = '/update_item/'

    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'itemCode':itemCode, 'action':action})
    })
    .then((response) =>{
        return response.json();
    })
    .then((data) =>{
        console.log('data', data)
        location.reload()
    })
}


