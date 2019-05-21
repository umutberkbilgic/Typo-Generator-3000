// Copyright (c) 2012 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

var co = `
String.prototype.replaceAt = function(index, replacement){return this.substr(0, index) + replacement + this.substr(index + replacement.length);}  
typos = {
  'a': "qwsz",    'b': "vghn",   'c': "xdfv",
  'd': "serfcx",  'e': "wsdfr",  'f': "dcvgtr",
  'g': "fvbhyt9", 'h': "gbnjuy", 'i': "ujko1",
  'j': "hnmkıu",  'k': "jmloi",  'l': "mkop",
  'm': "njkl",    'n': "bhjm",   'o': "iklp0",
  'p': "ol",      'q': "wa",     'r': "edft",
  's': "wazxde",  't': "rfgy",   'u': "yhji",
  'v': "cfgb",    'w': "qase",   'x': "zsdc",
  'y': "tghu",    'z': "asx",    'ı': "ujklo" , 
  'ğ':"pşiü",     'ü': "ğiş",    'ö': "mklç",
  'ç':"ölşi",     'ş':"çlp"};  
randoms = ["ay", "of", "yha", "ya", "lan" , "wtf", "aq", "abi", "yeter", "amk"];
doc = document.getElementsByClassName("vW7d1");
lastmsg = doc[doc.length - 1];
lastMsg = lastmsg.getElementsByClassName("selectable-text invisible-space copyable-text")[0].innerText;
var textField = document.getElementsByClassName("_2S1VP copyable-text selectable-text")[0];
document.getElementsByClassName("_39LWd")[0].setAttribute("style", "visibility: hidden");
for (var i = 0; i < lastMsg.length; i++) {
  var current = lastMsg.charAt(i).toLowerCase();
  if(current in typos){
    if (Math.random() <= 0.07){
      var typo = typos[current];
      randomLetter = (typo).split('')[Math.floor(Math.random()*typo.length + 1)];
      lastMsg = lastMsg.replaceAt(i, randomLetter); 
    }
  }
  else{
    if(Math.random() <= 0.26){
      var randomWord = randoms[Math.floor(Math.random()*randoms.length + 1)];
      lastMsg = lastMsg.replaceAt(i, " " + randomWord + " ");
    }
  }
}
textField.innerHTML = lastMsg;
textField.dispatchEvent(new InputEvent('input', {bubbles: true}));
var sendButton = document.getElementsByClassName("_35EW6")[0];
sendButton.click();;
`

function click(e) {
  chrome.tabs.executeScript(null, {code: co});
  window.close();
}
document.addEventListener('DOMContentLoaded', function () {
  var divs = document.querySelectorAll('button');
  for (var i = 0; i < divs.length; i++) {
    divs[i].addEventListener('click', click);
  }
});

