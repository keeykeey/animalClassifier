/*
const uploadedPicture = document.querySelector('.uploaded');

uploadedPicture.addEventListener('dragstart',() =>{
    console.log('dragstart event');
});

uploadedPicture.addEventListener('drag',() => {
    console.log('drag event');
});

uploadedPicture.addEventListener('dragend',() => {
    console.log('dragend event');
});    
*/

/*
const fileZone = document.querySelector('.file-zone');
const className = 'on';

fileZone.addEventListener('dragover', (event) => {                         
    event.preventDefault();                                                  
    fileZone.classList.add(className);                                       
    console.log('oh')
});                                                                        
                                                                            
fileZone.addEventListener('dragleave', (event) => {                             
    event.preventDefault();                                                  
    fileZone.classList.remove(className);                                    
    console.log('aha')
});
*/

const file_zone=document.querySelector('.file-zone');

file_zone.addEventListener('dragenter',()=>{
    console.log('dragenter event');
});

file_zone.addEventListener('dragover',()=>{
    console.log('dragover event');
});

file_zone.addEventListener('dragleave',()=>{
    console.log('dragleave event');
});


