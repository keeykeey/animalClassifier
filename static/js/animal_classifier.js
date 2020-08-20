const uploadedPicture = document.querySelector('.uploaded');

uploadedPicture.addEventListener('dragstart',() =>{
    console.log('dragstart event');
});

uploadedPicture.addEventListener('drag',() => {
    console.log('drag event');
});

uploadedPicture.addEventListener('dragged',() => {
    console.log('dragend event');
});    




const fileZone = document.querySelector('.file-zone');
const className = 'on';

fileZone.addEventListener('dragover', (event) => {                         
    event.preventDefault();                                                  
    fileZone.classList.add(className);                                       
});                                                                        
                                                                            
fileZone.addEventListener('dragleave', () => {                             
    event.preventDefault();                                                  
    fileZone.classList.remove(className);                                    
});

