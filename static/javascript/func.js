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