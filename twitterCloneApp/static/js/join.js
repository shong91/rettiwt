let btn_submit = document.querySelector('.btn_submit');
let join_form = document.querySelector('#join_form');
const regex = /\s/g; // remove all space
const regexId = /^[a-z]\w{4,10}$/; // 4 to 10 lowercase letter
const regexEmail = /\S+@\S+\.\S+/; // anystring@anystring.anystring
const regexPwd = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,20}$/; //  6 to 20 characters which contain at least one numeric digit, one uppercase and one lowercase letter

btn_submit.addEventListener('click', function(){
    var inputData = document.getElementsByTagName('input');

    // validation check
    if(!inputData[1].value.replace(regex, '').length > 0
        ||!inputData[2].value.replace(regex, '').length > 0
        ||!inputData[3].value.replace(regex, '').length > 0
        ||!inputData[4].value.replace(regex, '').length > 0) {
        alert('필수 입력값을 확인해주세요. (필수 입력값: 아이디, 이름, 이메일, 비밀번호)');
        return; 
    } 
    // else if(regexId.test(inputData[1].value)){ // 아이디 ; 길이 4자리 이상 10자리 이하, 중복 검사
    //     return; 
    // } else if(!regexEmail.test(inputData[3].value)){ // 이메일 ; 형식에 맞지 않는 이메일 - use bootstrap validation 
    //     return; 
    // } else if(!regexPwd.test(inputData[4].value)){ // 비밀번호 ;  영문+숫자 조합, 6자리 이상
    //     return; 
    // } 
    
    //call view (POST): 
    console.log('pass validation! ');
    join_form.submit();
    
    // ref) httpRequest 사용
    // var form = document.querySelector('#join_form');
    // var formData = new FormData(form);
    // var xhr = new XMLHttpRequest();
    // xhr.open('POST', '', true);   // 'twc/join/'
    // xhr.send(formData); // formData 형태로 보내기 때문에 header에 {"Content-Type": "application/json"} 설정하지 않음 

    // ref) jquery 사용 (ajax 전송 시)
    // var formData = $('#join_form').serialize();
    // $.ajax({
    //     type: 'POST',
    //     url: '',
    //     data: formData,
    //     success: function (response) {
    //         alert('success');
    //     },
    //     error: function (response) {
    //         alert(response);
    //     }
    // })
    
});

//ref) https://codepen.io/ntpumartin/pen/MWYmypq
function toJSONparse( form ) {
    var obj = {};
    var elements = form.querySelectorAll( "input, select, textarea" );
    for( var i = 0; i < elements.length; ++i ) {
        var element = elements[i];
        var name = element.name;
        var value = element.value;

        if( name ) {
            obj[ name ] = value;
        }
    }

    return obj;
}


