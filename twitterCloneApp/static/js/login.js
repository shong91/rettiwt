let btn_submit = document.querySelector('.btn_submit');
let login_form = document.querySelector('#login_form');
let user_id = document.getElementsByName('user_id')[0];
const regex = /\s/g; // remove all space

btn_submit.addEventListener('click', function(){
    var inputData = document.getElementsByTagName('input');

    if(!inputData[1].value.replace(regex, '').length > 0
    ||!inputData[2].value.replace(regex, '').length > 0) {
        alert('아이디와 비밀번호를 입력해주세요.');
        return; 
    }
    
    // call view (POST): jquery 사용 (ajax 전송 시)
    console.log('pass validation! ');
    login_form.submit();

})