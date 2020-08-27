const button = document.querySelector('.button');
button.addEventListener('click',()=>{
    textFromForm = getTextFromForm();
    writeOver();
    
    console.log(textFromForm);
});    


function writeOver(){
    const stdout = document.querySelector('.text_out');
    textFromForm = getTextFromForm();
    stdout.innerHTML = textFromForm;
}

function getTextFromForm(){
    const textFromForm = document.getElementById('text_input').value;
    return textFromForm;
}

    


