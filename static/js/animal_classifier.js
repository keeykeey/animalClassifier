const fileZone1=document.querySelector('.file-zone1');
const fileZone2=document.querySelector('.file-zone2');
const previewArea = document.querySelector('.file-preview-area');
const uploadByButton = document.getElementById('upload-image-by-button');
const className = 'on';

/* フォームでアップロードした画像ファイルを表示用のエリアに表示するコードを以下に書く*/
fileZone1.addEventListener('change',(event)=>{
    const target = event.target;
    const transferdFiles = target.files;
    displayImages(transferdFiles);
});

fileZone2.addEventListener('dragover',()=>{
    event.preventDefault();
    fileZone2.classList.add(className);
});

fileZone2.addEventListener('dragleave',()=>{
    event.preventDefault();
    fileZone2.classList.remove(className);
});

fileZone2.addEventListener('drop',(event)=>{
    event.preventDefault();
    fileZone2.classList.remove(className);

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





