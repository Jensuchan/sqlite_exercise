console.log('imageValidation.js')

document.getElementById('trigger').addEventListener('click', ()=>{
    document.getElementById('files').click();
})

const regExp = new RegExp("\.(exe|sh|bat|dll|jar|msi)$");
const imgRegExp = new RegExp("\.(jpg|jpeg|png|gif)$")
const maxSize = 1024*1024*20; 

function fileValidation(fileName, fileSize){
    if(regExp.test(fileName)){
        return 0;
    }else if(fileSize > maxSize){
        return 0;
    }else{
        return 1;
    }
}


