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

const fileZone=document.querySelector('.file-zone');
const className = 'on';


fileZone.addEventListener('dragover',()=>{
    event.preventDefault();
    fileZone.classList.add(className);
});

fileZone.addEventListener('dragleave',()=>{
    event.preventDefault();
    fileZone.classList.remove(className);
});

fileZone.addEventListener('drop',(event)=>{
    event.preventDefault();
    fileZone.classList.remove(className);

    const transferdFiles = event.dataTransfer.files;
    displayImages(transferdFiles);
});

function displayImages(transferdFiles){
    const imageFileList = [];
    const fileNum = transferdFiles.length;
    
    for (let i =0 ; i<fileNum ; i++){
        if (transferdFiles[i].type.match('image.*') === false){
            return;
        }
        imageFileList.push(transferdFiles[i]);
    }

    //preview image showing area
    const imagePreviewArea = document.querySelector('.image-list');

    for (const imageFile of imageFileList){
        const fileReader = new FileReader();
        fileReader.readAsDataURL(imageFile);
        fileReader.addEventListener('load',(event)=>{
            const image = new Image();
            image.src = event.target.result;
            imagePreviewArea.insertBefore(image,imagePreviewArea.firstChild);
        });
    }
}

