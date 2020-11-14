let btn_submit = document.querySelector('.btn_submit');
let tw_content = document.querySelector('.tw_content');

let tweet_form = document.querySelector('#tweet_form');
let update_form = document.querySelector('#update_form');

btn_submit.addEventListener('click', function(){
    if(tw_content.value == '') {
        alert('필수 입력값 입니다. ');
        return; 
    }

    if(btn_submit.innerText == '글쓰기') {
        // call view
        tweet_form.submit();
    } else {
        // call view
        update_form.submit();
    }
    
    
});