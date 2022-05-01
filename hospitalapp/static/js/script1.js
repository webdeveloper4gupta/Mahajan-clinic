let a=document.getElementById('tab-item1');
let e=document.getElementById('tab-item2');
let f=document.getElementById('tab-item3');
let b=document.getElementById('content1');
let c=document.getElementById('content2');
let d=document.getElementById('content3')
a.addEventListener('click',()=>{
   
        b.style.display='block';
        c.style.display='none';
        d.style.display='none';
    
  

});
e.addEventListener('click',()=>{

        c.style.display='block';
        b.style.display='none';
        d.style.display='none';
    
  

});
f.addEventListener('click',()=>{

    d.style.display='block';
    b.style.display='none';
    c.style.display='none';



});