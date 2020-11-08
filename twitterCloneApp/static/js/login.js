let btn_submit = document.querySelector('.btn_submit');
let user_id = document.getElementsByName('user_id')[0];
const regex = /\s/g; // remove all space
alert('test');
btn_submit.addEventListener('click', function(){
    var inputData = document.getElementsByTagName('input');

    if(!inputData[1].value.replace(regex, '').length > 0
    ||!inputData[2].value.replace(regex, '').length > 0) {
        alert('아이디와 비밀번호를 입력해주세요.');
        return; 
    }
    
    // call view (POST): jquery 사용 (ajax 전송 시)
    console.log('pass validation! ');
    var form = document.querySelector('#login_form');
    var formData = new FormData(form);
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '', true);
    xhr.send(formData); // formData 형태로 보내기 때문에 header에 {"Content-Type": "application/json"} 설정하지 않음 

})