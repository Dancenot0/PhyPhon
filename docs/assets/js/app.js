
(function(){
  'use strict';
  var root=document.documentElement, key='pyphon-lang';
  function apply(lang){ root.setAttribute('data-lang',lang||'es'); }
  function setLang(lang){
    try{ localStorage.setItem(key,lang); }catch(e){}
    apply(lang);
    var btns=document.querySelectorAll('.lang button');
    for(var i=0;i<btns.length;i++){
      if(btns[i].getAttribute('data-lang')===lang) btns[i].setAttribute('data-on',''); else btns[i].removeAttribute('data-on');
    }
  }
  var stored=null; try{ stored=localStorage.getItem(key); }catch(e){}
  apply(stored||'es');
  document.addEventListener('DOMContentLoaded',function(){
    var btns=document.querySelectorAll('.lang button');
    for(var i=0;i<btns.length;i++){ (function(b){ b.addEventListener('click',function(){ setLang(b.getAttribute('data-lang')); }); })(btns[i]); }
    setLang((stored||(navigator.language||'').toLowerCase().indexOf('en')===0?'en':'es')||'es');
    // copy buttons next to each pre
    var pres=document.querySelectorAll('pre');
    for(var k=0;k<pres.length;k++){
      if(pres[k].getAttribute('data-copy')==='no') continue;
      pres[k].setAttribute('tabindex','0');
    }
  });
})();
