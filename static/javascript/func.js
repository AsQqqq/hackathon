document.querySelector('#elastic').oninput = function(){
    let val = this.value.trim();
    let elasticItems = document.querySelectorAll('.elastic li');
    if (val != ''){
        elasticItems.forEach(function(elem){
            if (elem.innerText.search(val) == -1){
                elem.classList.add('hide');
            }
            else {
                elem.classList.remove('hide');
            }
        });
    }
    else {
        elasticItems.forEach(function (elem) {
            elem.classList.remove('hide');
        }
    )};
}

function sendPhoneNumber(phone_number) {
    var elem = document.getElementsByClassName(phone_number);
    var zalupa_plus = document.getElementById(phone_number);
    var zalupa = elem.item(0);
    var class_zalupa = zalupa.className;
    
    if (zalupa_plus.value == "ДОБАВИТЬ" && class_zalupa == phone_number) {
      zalupa_plus.value = "УДАЛИТЬ";
      zalupa_plus.style.backgroundColor = 'red';
    }
    else {
      zalupa_plus.value = "ДОБАВИТЬ";
      zalupa_plus.style.backgroundColor = '#39ace7';
    }
    fetch('/phone-number', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ 'phone_number': phone_number })
    })
    .then(response => {
      if (response.ok) {
        console.log('Номер телефона успешно отправлен на сервер');
      } else {
        console.log('Произошла ошибка при отправке номера телефона');
      }
    })
    .catch(error => {
      console.log('Произошла ошибка при отправке номера телефона:', error);
    });
}
