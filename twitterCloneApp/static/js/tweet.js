let btn_submit = document.querySelector('.btn_submit');
let tw_content = document.querySelector('.tw_content');
btn_submit.addEventListener('click', function(){
    if(tw_content.value == '') {
        alert('필수 입력값 입니다. ');
        return; 
    }

    // call view
    tweet_form.submit();
});